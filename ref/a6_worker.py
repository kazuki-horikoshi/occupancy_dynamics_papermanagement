"""
src/a6_worker.py
================
Worker function for Analysis 6 parallel execution.

This module is intentionally kept free of notebook-level state so that
it can be imported and executed in child processes via
``concurrent.futures.ProcessPoolExecutor``.

All data required by the worker is passed as serialisable arguments;
no global notebook variables are referenced.
"""

import random

import numpy as np
import pandas as pd

from src.setpoint import (
    calculate_optimal_setpoint_from_curves,
    get_normalized_prob_at_setpoint,
)


def run_a6_for_room_and_subgroup(args: tuple) -> list:
    """Execute all trials for one (room, subgroup_size) condition.

    Parameters
    ----------
    args : tuple
        ``(room, k, n_trials, seed, full_members,
           room_snaps, model_pool_records, mc_replace, fixed_sp_values)``

        room              – room name string (original_room label)
        k                 – subgroup size (int, >= 2)
        n_trials          – number of trials for this condition
        seed              – integer seed for this task (reproducible)
        full_members      – list[str]  full member IDs of the room
        room_snaps        – dict[str, list[str]]  {ts_str: [AI_Camera_IDs]}
        model_pool_records– list[dict]  rows from model_pool_df as dicts
        mc_replace        – bool  whether to sample with replacement
        fixed_sp_values   – list[float]  fixed setpoints to evaluate in the
                            same trial (e.g. [24.0, 24.5]). Each produces a
                            column ``fixed{sp}_ratio`` (dot → underscore).

    Returns
    -------
    list[dict]
        One dict per trial with keys:
        ``original_room``, ``subgroup_size``, ``trial``,
        ``selected_members``, ``static_ratio``, ``dynamic_ratio``,
        ``daily_fixed_ratio``, and one ``fixed{sp}_ratio`` column per entry
        in fixed_sp_values.
    """
    (
        room,
        k,
        n_trials,
        seed,
        full_members,
        room_snaps,
        model_pool_records,
        mc_replace,
        fixed_sp_values,
    ) = args

    # ------------------------------------------------------------------
    # Deterministic seeding (both stdlib random and NumPy)
    # ------------------------------------------------------------------
    random.seed(seed)
    np.random.seed(seed)

    # ------------------------------------------------------------------
    # Reconstruct model pool DataFrame from serialised records
    # ------------------------------------------------------------------
    model_pool_df = pd.DataFrame(model_pool_records)

    # Pre-compute column names for fixed baselines
    fixed_col_names = {
        sp: f"fixed{str(sp).replace('.', '_')}_ratio"
        for sp in fixed_sp_values
    }

    # ------------------------------------------------------------------
    # Pre-filter: keep only members observed in at least one snapshot.
    # Members registered for a room but absent during the analysis period
    # (e.g. zero stays) would always yield NaN — exclude them up-front so
    # that every possible subgroup selection produces valid data.
    # ------------------------------------------------------------------
    all_snapshot_members: set = set()
    for occupants in room_snaps.values():
        all_snapshot_members.update(occupants)
    eligible_members = [m for m in full_members if m in all_snapshot_members]
    if len(eligible_members) < k:
        # Safety fallback: should not occur when OCT_ACTUAL_MEMBERS is in sync
        eligible_members = full_members

    results: list[dict] = []

    for trial_idx in range(n_trials):

        # --------------------------------------------------------------
        # Step 1: Randomly select k members from the eligible member list
        #   (pre-filtered to members present in ≥1 snapshot)
        # --------------------------------------------------------------
        selected = sorted(random.sample(eligible_members, k))

        # --------------------------------------------------------------
        # Step 2: Assign comfort models randomly (same as serial A6)
        # --------------------------------------------------------------
        sampled = model_pool_df.sample(
            n=k, replace=mc_replace, random_state=None
        ).reset_index(drop=True)

        # person_id → row index in `sampled`
        person_to_row = {pid: i for i, pid in enumerate(selected)}

        # --------------------------------------------------------------
        # Step 3: Static setpoint = mean PeakSET of assigned models
        # --------------------------------------------------------------
        trial_fixed_sp = float(sampled["PeakSET"].mean())

        # --------------------------------------------------------------
        # Step 4: Per-timestamp comfort judgment — single pass over timestamps
        #   Computes static, dynamic, and all fixed baselines together.
        #   Only members who are BOTH in room_snaps AND in `selected`.
        # --------------------------------------------------------------
        trial_dynamic_cache: dict = {}
        static_in = 0
        static_total = 0
        dynamic_in = 0
        dynamic_total = 0
        fixed_ins   = {sp: 0 for sp in fixed_sp_values}
        fixed_totals = {sp: 0 for sp in fixed_sp_values}
        daily_accum: dict[str, dict] = {}

        for ts_str, occupants in room_snaps.items():
            date_str = ts_str[:10]

            # Occupied members that belong to the selected subgroup
            present_selected = [p for p in occupants if p in person_to_row]

            if date_str not in daily_accum:
                daily_accum[date_str] = {
                    "all_present_rows": set(),
                    "daily_in": 0,
                    "daily_total": 0,
                }

            if not present_selected:
                continue

            present_rows = [person_to_row[p] for p in present_selected]
            present_profiles = sampled.loc[present_rows]
            daily_accum[date_str]["all_present_rows"].update(present_rows)

            # --- Static ---
            for _, prof in present_profiles.iterrows():
                static_total += 1
                if prof["RangeMin"] <= trial_fixed_sp <= prof["RangeMax"]:
                    static_in += 1

            # --- Dynamic (memoised by unique profile combination) ---
            combo_key = tuple(sorted(present_rows))
            if combo_key in trial_dynamic_cache:
                dyn_sp = trial_dynamic_cache[combo_key]
            else:
                dyn_sp = calculate_optimal_setpoint_from_curves(present_profiles)
                trial_dynamic_cache[combo_key] = dyn_sp

            if dyn_sp is not None:
                for _, prof in present_profiles.iterrows():
                    dynamic_total += 1
                    if prof["RangeMin"] <= dyn_sp <= prof["RangeMax"]:
                        dynamic_in += 1

            # --- Fixed baselines (one pass per profile, one counter per sp) ---
            for sp in fixed_sp_values:
                for _, prof in present_profiles.iterrows():
                    fixed_totals[sp] += 1
                    if prof["RangeMin"] <= sp <= prof["RangeMax"]:
                        fixed_ins[sp] += 1

        daily_fixed_sps: dict[str, float] = {}
        for date_str, acc in daily_accum.items():
            if not acc["all_present_rows"]:
                daily_fixed_sps[date_str] = float("nan")
                continue

            all_day_profiles = sampled.loc[sorted(acc["all_present_rows"])]
            daily_sp = calculate_optimal_setpoint_from_curves(all_day_profiles)
            daily_fixed_sps[date_str] = (
                daily_sp if daily_sp is not None else float("nan")
            )

        for ts_str, occupants in room_snaps.items():
            date_str = ts_str[:10]
            present_selected = [p for p in occupants if p in person_to_row]
            if not present_selected:
                continue

            daily_sp = daily_fixed_sps.get(date_str, float("nan"))
            if daily_sp != daily_sp:
                continue

            present_rows = [person_to_row[p] for p in present_selected]
            present_profiles = sampled.loc[present_rows]
            for _, prof in present_profiles.iterrows():
                daily_accum[date_str]["daily_total"] += 1
                if prof["RangeMin"] <= daily_sp <= prof["RangeMax"]:
                    daily_accum[date_str]["daily_in"] += 1

        daily_in = sum(acc["daily_in"] for acc in daily_accum.values())
        daily_total = sum(acc["daily_total"] for acc in daily_accum.values())

        # --------------------------------------------------------------
        # Step 5: Store result — existing schema preserved, fixed cols appended
        # --------------------------------------------------------------
        rec = {
            "original_room": room,
            "subgroup_size": k,
            "trial": trial_idx + 1,
            "selected_members": tuple(selected),
            "static_ratio": (
                static_in / static_total if static_total > 0 else float("nan")
            ),
            "dynamic_ratio": (
                dynamic_in / dynamic_total
                if dynamic_total > 0
                else float("nan")
            ),
            "daily_fixed_ratio": (
                daily_in / daily_total if daily_total > 0 else float("nan")
            ),
        }
        for sp in fixed_sp_values:
            tot = fixed_totals[sp]
            rec[fixed_col_names[sp]] = (
                fixed_ins[sp] / tot if tot > 0 else float("nan")
            )
        results.append(rec)

    return results


# ---------------------------------------------------------------------------
# Analysis 7 — Daily-resolution worker
# ---------------------------------------------------------------------------

def _utr_t(s_curr: frozenset, s_prev: frozenset) -> float | None:
    """Compute UTR for a single timestamp pair.

    UTR_t = 1 - |S_t ∩ S_{t-1}| / |S_t ∪ S_{t-1}|

    Returns None when both sets are empty (undefined turnover).
    Returns 1.0 when one set is non-empty and intersection is zero.
    """
    union_size = len(s_curr | s_prev)
    if union_size == 0:
        return None  # Both empty — undefined
    return 1.0 - len(s_curr & s_prev) / union_size


def _get_raw_prob_at_setpoint(user_profile, target_setpoint: float) -> float:
    """Return the unnormalized no-change probability at a target setpoint."""
    prob_curve_data = user_profile.get("probability_curve")
    if not prob_curve_data:
        return np.nan

    try:
        set_axis = np.array(prob_curve_data["set_values"], dtype=float)
        full_probs = np.array(prob_curve_data["probabilities"], dtype=float)
        if len(set_axis) == 0 or len(full_probs) == 0:
            return np.nan
        return float(np.interp(target_setpoint, set_axis, full_probs))
    except (TypeError, ValueError, KeyError):
        return np.nan


def run_a7_daily(args: tuple) -> list:
    """Daily-resolution comfort and occupancy worker for Analysis 7.

    Uses the **same seeding and member/model sampling** as
    ``run_a6_for_room_and_subgroup`` so results are reproducible and
    directly comparable to Analysis 6 when the same task list is used.

    Parameters
    ----------
    args : tuple
        ``(room, k, n_trials, seed, full_members,
           room_snaps, model_pool_records, mc_replace)``

        Identical signature to ``run_a6_for_room_and_subgroup``.
        The fixed 24.0 °C baseline is always computed internally.

    Returns
    -------
    list[dict]
        One dict per (trial, date).  Required columns:

        ``original_room``, ``subgroup_size``, ``trial``, ``date``,
        ``selected_members``,
        ``static_ratio_daily``, ``dynamic_ratio_daily``,
        ``baseline24_ratio_daily``,
        ``gain_static_vs_24_daily``,  ``gain_dynamic_vs_24_daily``,
        ``gain_dynamic_vs_static_daily``,
        ``mean_occupancy_daily``,  ``max_occupancy_daily``,
        ``sd_occupancy_daily``,   ``occupancy_presence_ratio_daily``,
        ``utr_daily``,            ``unique_user_count_daily``,
        ``n_timestamps_daily``,   ``n_valid_turnover_points_daily``
    """
    (
        room,
        k,
        n_trials,
        seed,
        full_members,
        room_snaps,
        model_pool_records,
        mc_replace,
    ) = args

    BASELINE_SP: float = 24.0  # fixed reference temperature (°C)

    random.seed(seed)
    np.random.seed(seed)

    model_pool_df = pd.DataFrame(model_pool_records)

    results: list[dict] = []

    for trial_idx in range(n_trials):

        # ------------------------------------------------------------------
        # Reproduce identical member/model selection as run_a6_for_room_and_subgroup
        # ------------------------------------------------------------------
        selected = sorted(random.sample(full_members, k))

        sampled = model_pool_df.sample(
            n=k, replace=mc_replace, random_state=None
        ).reset_index(drop=True)

        person_to_row: dict = {pid: i for i, pid in enumerate(selected)}

        # Static setpoint: mean PeakSET of the assigned comfort models
        trial_static_sp = float(sampled["PeakSET"].mean())

        # ------------------------------------------------------------------
        # Accumulate per-day statistics
        #   daily_accum[date_str] holds running counters for every metric.
        #   Keys are calendar dates (first 10 chars of ts_str "YYYY-MM-DD").
        # ------------------------------------------------------------------
        daily_accum: dict = {}

        # Cache for dynamic setpoints: combo_key → float | None
        trial_dynamic_cache: dict = {}

        # We need timestamps in a stable order for UTR lag computation.
        # room_snaps is a plain dict; insertion order is preserved in Python
        # 3.7+, which matches the time-grid insertion order used in Cell 65.
        for ts_str, occupants in room_snaps.items():

            date_str = ts_str[:10]  # "YYYY-MM-DD"

            # Subgroup members present at this timestamp
            present_selected = [p for p in occupants if p in person_to_row]
            N_t = len(present_selected)
            S_t = frozenset(present_selected)  # used for UTR

            # Initialise date bucket on first encounter
            if date_str not in daily_accum:
                daily_accum[date_str] = {
                    # Occupancy time-series (one entry per timestamp in day)
                    "N_t_list":    [],   # list[int]       → N_t values
                    "S_t_list":    [],   # list[frozenset] → S_t sets (ordered)
                    "all_users":   set(),
                    # Comfort counters
                    "static_in":    0, "static_total":    0,
                    "dynamic_in":   0, "dynamic_total":   0,
                    "baseline_in":  0, "baseline_total":  0,
                    "n_timestamps": 0,
                }

            acc = daily_accum[date_str]
            acc["N_t_list"].append(N_t)
            acc["S_t_list"].append(S_t)
            acc["all_users"].update(present_selected)
            acc["n_timestamps"] += 1

            # No one present → skip comfort counting for this timestamp
            if not present_selected:
                continue

            present_rows = [person_to_row[p] for p in present_selected]
            present_profiles = sampled.loc[present_rows]

            # ── Static ──────────────────────────────────────────────────
            for _, prof in present_profiles.iterrows():
                acc["static_total"] += 1
                if prof["RangeMin"] <= trial_static_sp <= prof["RangeMax"]:
                    acc["static_in"] += 1

            # ── Dynamic (memoised) ───────────────────────────────────────
            combo_key = tuple(sorted(present_rows))
            if combo_key not in trial_dynamic_cache:
                trial_dynamic_cache[combo_key] = (
                    calculate_optimal_setpoint_from_curves(present_profiles)
                )
            dyn_sp = trial_dynamic_cache[combo_key]

            if dyn_sp is not None:
                for _, prof in present_profiles.iterrows():
                    acc["dynamic_total"] += 1
                    if prof["RangeMin"] <= dyn_sp <= prof["RangeMax"]:
                        acc["dynamic_in"] += 1

            # ── Fixed baseline 24.0 °C ───────────────────────────────────
            for _, prof in present_profiles.iterrows():
                acc["baseline_total"] += 1
                if prof["RangeMin"] <= BASELINE_SP <= prof["RangeMax"]:
                    acc["baseline_in"] += 1

        # ------------------------------------------------------------------
        # Collapse each day's accumulators into a single output row
        # ------------------------------------------------------------------
        for date_str, acc in sorted(daily_accum.items()):

            N_list = acc["N_t_list"]
            S_list = acc["S_t_list"]

            # ── Comfort ratios ───────────────────────────────────────────
            def _safe_ratio(num: int, den: int) -> float:
                return num / den if den > 0 else float("nan")

            srd = _safe_ratio(acc["static_in"],   acc["static_total"])
            drd = _safe_ratio(acc["dynamic_in"],  acc["dynamic_total"])
            brd = _safe_ratio(acc["baseline_in"], acc["baseline_total"])

            def _gain(a: float, b: float) -> float:
                if a != a or b != b:   # NaN check without math import
                    return float("nan")
                return a - b

            # ── Occupancy metrics ────────────────────────────────────────
            N_arr = np.array(N_list, dtype=float)
            n_ts  = len(N_arr)

            mean_occ  = float(np.nanmean(N_arr))        if n_ts > 0   else float("nan")
            max_occ   = float(np.nanmax(N_arr))         if n_ts > 0   else float("nan")
            sd_occ    = float(np.nanstd(N_arr, ddof=1)) if n_ts > 1   else float("nan")
            pres_ratio = float(np.mean(N_arr > 0))      if n_ts > 0   else float("nan")
            unique_cnt = len(acc["all_users"])

            # ── UTR (lag-1 Jaccard turnover) ─────────────────────────────
            utr_vals: list[float] = []
            for t in range(1, len(S_list)):
                utr_val = _utr_t(S_list[t], S_list[t - 1])
                if utr_val is not None:
                    utr_vals.append(utr_val)

            n_valid_utr = len(utr_vals)
            utr_daily   = float(np.mean(utr_vals)) if utr_vals else float("nan")

            # ── Assemble row ─────────────────────────────────────────────
            results.append(
                {
                    "original_room":   room,
                    "subgroup_size":   k,
                    "trial":           trial_idx + 1,
                    "date":            date_str,
                    "selected_members": tuple(selected),
                    # Comfort ratios
                    "static_ratio_daily":           srd,
                    "dynamic_ratio_daily":          drd,
                    "baseline24_ratio_daily":       brd,
                    # Gain columns
                    "gain_static_vs_24_daily":      _gain(srd, brd),
                    "gain_dynamic_vs_24_daily":     _gain(drd, brd),
                    "gain_dynamic_vs_static_daily": _gain(drd, srd),
                    # Occupancy metrics
                    "mean_occupancy_daily":         mean_occ,
                    "max_occupancy_daily":          max_occ,
                    "sd_occupancy_daily":           sd_occ,
                    "occupancy_presence_ratio_daily": pres_ratio,
                    "utr_daily":                    utr_daily,
                    "unique_user_count_daily":      unique_cnt,
                    # Counts
                    "n_timestamps_daily":           acc["n_timestamps"],
                    "n_valid_turnover_points_daily": n_valid_utr,
                }
            )

    return results


def run_a7_prob_daily(args: tuple) -> list:
    """Daily-resolution probability-based comfort worker for Analysis 7-2.

    This worker mirrors ``run_a7_daily`` in:

    - subgroup sampling
    - comfort-profile sampling
    - dynamic setpoint calculation
    - occupancy metric construction

    but replaces binary in-range comfort counting with per-user probability
    averaging based on the personal comfort model.

    Output columns intentionally mirror Analysis 7 naming where possible:

    - ``static_prob_daily``          ↔ ``static_ratio_daily``
    - ``dynamic_prob_daily``         ↔ ``dynamic_ratio_daily``
    - ``baseline24_prob_daily``      ↔ ``baseline24_ratio_daily``
    - ``gain_dynamic_prob_vs_static_daily`` ↔
      ``gain_dynamic_vs_static_daily``

    Raw probabilities are also stored for secondary inspection, but are not
    intended to be the primary first-pass analysis target.
    """
    (
        room,
        k,
        n_trials,
        seed,
        full_members,
        room_snaps,
        model_pool_records,
        mc_replace,
    ) = args

    BASELINE_SP: float = 24.0

    random.seed(seed)
    np.random.seed(seed)

    model_pool_df = pd.DataFrame(model_pool_records)
    results: list[dict] = []

    for trial_idx in range(n_trials):
        selected = sorted(random.sample(full_members, k))
        sampled = model_pool_df.sample(
            n=k, replace=mc_replace, random_state=None
        ).reset_index(drop=True)

        person_to_row: dict = {pid: i for i, pid in enumerate(selected)}
        trial_static_sp = float(sampled["PeakSET"].mean())

        daily_accum: dict = {}
        trial_dynamic_cache: dict = {}

        def _init_day_bucket():
            return {
                "N_t_list": [],
                "S_t_list": [],
                "all_users": set(),
                "n_timestamps": 0,
                "static_prob_sum": 0.0,
                "static_prob_n": 0,
                "dynamic_prob_sum": 0.0,
                "dynamic_prob_n": 0,
                "baseline_prob_sum": 0.0,
                "baseline_prob_n": 0,
                "static_rawprob_sum": 0.0,
                "static_rawprob_n": 0,
                "dynamic_rawprob_sum": 0.0,
                "dynamic_rawprob_n": 0,
                "baseline_rawprob_sum": 0.0,
                "baseline_rawprob_n": 0,
            }

        for ts_str, occupants in room_snaps.items():
            date_str = ts_str[:10]
            present_selected = [p for p in occupants if p in person_to_row]
            N_t = len(present_selected)
            S_t = frozenset(present_selected)

            if date_str not in daily_accum:
                daily_accum[date_str] = _init_day_bucket()

            acc = daily_accum[date_str]
            acc["N_t_list"].append(N_t)
            acc["S_t_list"].append(S_t)
            acc["all_users"].update(present_selected)
            acc["n_timestamps"] += 1

            if not present_selected:
                continue

            present_rows = [person_to_row[p] for p in present_selected]
            present_profiles = sampled.loc[present_rows]

            combo_key = tuple(sorted(present_rows))
            if combo_key not in trial_dynamic_cache:
                trial_dynamic_cache[combo_key] = (
                    calculate_optimal_setpoint_from_curves(present_profiles)
                )
            dyn_sp = trial_dynamic_cache[combo_key]

            for _, prof in present_profiles.iterrows():
                static_prob = get_normalized_prob_at_setpoint(
                    prof, trial_static_sp
                )
                if pd.notna(static_prob):
                    acc["static_prob_sum"] += float(static_prob)
                    acc["static_prob_n"] += 1

                static_rawprob = _get_raw_prob_at_setpoint(prof, trial_static_sp)
                if pd.notna(static_rawprob):
                    acc["static_rawprob_sum"] += float(static_rawprob)
                    acc["static_rawprob_n"] += 1

                baseline_prob = get_normalized_prob_at_setpoint(
                    prof, BASELINE_SP
                )
                if pd.notna(baseline_prob):
                    acc["baseline_prob_sum"] += float(baseline_prob)
                    acc["baseline_prob_n"] += 1

                baseline_rawprob = _get_raw_prob_at_setpoint(prof, BASELINE_SP)
                if pd.notna(baseline_rawprob):
                    acc["baseline_rawprob_sum"] += float(baseline_rawprob)
                    acc["baseline_rawprob_n"] += 1

                if dyn_sp is None:
                    continue

                dynamic_prob = get_normalized_prob_at_setpoint(prof, dyn_sp)
                if pd.notna(dynamic_prob):
                    acc["dynamic_prob_sum"] += float(dynamic_prob)
                    acc["dynamic_prob_n"] += 1

                dynamic_rawprob = _get_raw_prob_at_setpoint(prof, dyn_sp)
                if pd.notna(dynamic_rawprob):
                    acc["dynamic_rawprob_sum"] += float(dynamic_rawprob)
                    acc["dynamic_rawprob_n"] += 1

        for date_str, acc in sorted(daily_accum.items()):
            def _safe_mean(total: float, count: int) -> float:
                return total / count if count > 0 else float("nan")

            def _gain(a: float, b: float) -> float:
                if a != a or b != b:
                    return float("nan")
                return a - b

            static_prob_daily = _safe_mean(
                acc["static_prob_sum"], acc["static_prob_n"]
            )
            dynamic_prob_daily = _safe_mean(
                acc["dynamic_prob_sum"], acc["dynamic_prob_n"]
            )
            baseline24_prob_daily = _safe_mean(
                acc["baseline_prob_sum"], acc["baseline_prob_n"]
            )

            static_rawprob_daily = _safe_mean(
                acc["static_rawprob_sum"], acc["static_rawprob_n"]
            )
            dynamic_rawprob_daily = _safe_mean(
                acc["dynamic_rawprob_sum"], acc["dynamic_rawprob_n"]
            )
            baseline24_rawprob_daily = _safe_mean(
                acc["baseline_rawprob_sum"], acc["baseline_rawprob_n"]
            )

            N_arr = np.array(acc["N_t_list"], dtype=float)
            S_list = acc["S_t_list"]
            n_ts = len(N_arr)

            mean_occ = float(np.nanmean(N_arr)) if n_ts > 0 else float("nan")
            max_occ = float(np.nanmax(N_arr)) if n_ts > 0 else float("nan")
            sd_occ = (
                float(np.nanstd(N_arr, ddof=1)) if n_ts > 1 else float("nan")
            )
            pres_ratio = float(np.mean(N_arr > 0)) if n_ts > 0 else float("nan")
            unique_cnt = len(acc["all_users"])

            utr_vals: list[float] = []
            for t in range(1, len(S_list)):
                utr_val = _utr_t(S_list[t], S_list[t - 1])
                if utr_val is not None:
                    utr_vals.append(utr_val)

            n_valid_utr = len(utr_vals)
            utr_daily = float(np.mean(utr_vals)) if utr_vals else float("nan")

            results.append(
                {
                    "original_room": room,
                    "subgroup_size": k,
                    "trial": trial_idx + 1,
                    "date": date_str,
                    "selected_members": tuple(selected),
                    "static_prob_daily": static_prob_daily,
                    "dynamic_prob_daily": dynamic_prob_daily,
                    "baseline24_prob_daily": baseline24_prob_daily,
                    "static_rawprob_daily": static_rawprob_daily,
                    "dynamic_rawprob_daily": dynamic_rawprob_daily,
                    "baseline24_rawprob_daily": baseline24_rawprob_daily,
                    "gain_static_prob_vs_24_daily": _gain(
                        static_prob_daily, baseline24_prob_daily
                    ),
                    "gain_dynamic_prob_vs_24_daily": _gain(
                        dynamic_prob_daily, baseline24_prob_daily
                    ),
                    "gain_dynamic_prob_vs_static_daily": _gain(
                        dynamic_prob_daily, static_prob_daily
                    ),
                    "mean_occupancy_daily": mean_occ,
                    "max_occupancy_daily": max_occ,
                    "sd_occupancy_daily": sd_occ,
                    "occupancy_presence_ratio_daily": pres_ratio,
                    "utr_daily": utr_daily,
                    "unique_user_count_daily": unique_cnt,
                    "n_timestamps_daily": acc["n_timestamps"],
                    "n_valid_turnover_points_daily": n_valid_utr,
                }
            )

    return results


# ---------------------------------------------------------------------------
# Analysis 8 & 9 — Extended daily worker
# ---------------------------------------------------------------------------

def run_a8_daily(args: tuple) -> list:
    """Extended daily-resolution worker for Analysis 8/9.

    This worker expands ``run_a7_daily`` by computing both:
    (i) continuous setpoint-burden metrics, and
    (ii) actionable control metrics based on 0.5 °C rounded setpoints
         and 30-minute decision windows.

    Computes all columns produced by ``run_a7_daily`` plus:

    Analysis 8 — Continuous Dynamic setpoint burden:
        ``dynamic_sp_day_mean``          – mean dynamic setpoint within the day
        ``dynamic_sp_day_sd``            – SD of dynamic setpoint within the day
        ``dynamic_sp_day_range``         – max - min dynamic setpoint
        ``dynamic_sp_mean_abs_step``     – mean absolute 15-min setpoint step
        ``dynamic_sp_sum_abs_step``      – sum of absolute 15-min steps
        ``dynamic_sp_n_changes``         – count of steps >= CHANGE_EPS
        ``dynamic_sp_change_ratio``      – share of steps >= CHANGE_EPS
        ``dynamic_sp_n_large_changes``   – count of steps >= ACTION_STEP
        ``dynamic_sp_large_change_ratio``– share of steps >= ACTION_STEP
        ``dynamic_sp_max_abs_step``      – maximum absolute 15-min step

    Analysis 9 — Continuous Daily-fixed vs Dynamic comparison:
        ``daily_fixed_sp``               – daily fixed setpoint from all attendees appearing that day
        ``daily_fixed_ratio_daily``      – comfort coverage at daily fixed setpoint
        ``gain_dynamic_vs_daily_daily``  – dynamic_ratio_daily - daily_fixed_ratio_daily
        ``gap_dyn_vs_daily_day_mean_abs``– mean |T_dyn - T_daily|
        ``gap_dyn_vs_daily_day_max_abs`` – max  |T_dyn - T_daily|
        ``gap_dyn_vs_daily_day_sd``      – SD of (T_dyn - T_daily)
        ``daily_not_followable_ratio``   – share of timestamps with |T_dyn - T_daily| >= ACTION_STEP

    Rounded / actionable control metrics:
        ``daily_fixed_sp05``                  – daily fixed setpoint rounded to 0.5 °C
        ``dynamic05_ratio_daily``             – comfort coverage using rounded dynamic setpoint
        ``daily_fixed05_ratio_daily``         – comfort coverage using rounded daily fixed setpoint
        ``gain_dynamic05_vs_daily05_daily``  – rounded dynamic coverage gain vs rounded daily fixed

        ``dynamic_action_window_count_30m``   – number of 30-min windows with
                                                at least one 0.5 °C dynamic update
        ``dynamic_action_window_ratio_30m``   – share of 30-min windows requiring
                                                at least one 0.5 °C dynamic update
        ``dyn_daily_mismatch_window_count_30m`` – number of 30-min windows where
                                                  rounded Dynamic and rounded Daily differ
        ``dyn_daily_mismatch_window_ratio_30m`` – share of 30-min windows where
                                                  rounded Dynamic and rounded Daily differ

    Notes
    -----
    - Continuous metrics describe latent mismatch / theoretical burden.
    - Rounded 0.5 °C metrics describe actionable control differences under
      thermostat-like resolution.
    - 30-minute windows are used as a decision-resolution layer, while
      15-minute timestamps remain the estimation-resolution layer.
    """
    (
        room,
        k,
        n_trials,
        seed,
        full_members,
        room_snaps,
        model_pool_records,
        mc_replace,
    ) = args

    BASELINE_SP: float = 24.0
    ACTION_STEP: float = 0.5
    CHANGE_EPS: float = 0.05

    def _round_to_step(x: float, step: float = ACTION_STEP) -> float:
        return round(x / step) * step

    def _window30_label(ts_str: str):
        return pd.Timestamp(ts_str).floor("30min")

    random.seed(seed)
    np.random.seed(seed)

    model_pool_df = pd.DataFrame(model_pool_records)
    results: list[dict] = []

    for trial_idx in range(n_trials):
        selected = sorted(random.sample(full_members, k))
        sampled = model_pool_df.sample(
            n=k, replace=mc_replace, random_state=None
        ).reset_index(drop=True)

        person_to_row = {pid: i for i, pid in enumerate(selected)}
        trial_static_sp = float(sampled["PeakSET"].mean())

        daily_accum = {}
        trial_dynamic_cache = {}

        for ts_str, occupants in room_snaps.items():
            date_str = ts_str[:10]
            present_selected = [p for p in occupants if p in person_to_row]
            N_t = len(present_selected)
            S_t = frozenset(present_selected)

            if date_str not in daily_accum:
                daily_accum[date_str] = {
                    "N_t_list": [],
                    "S_t_list": [],
                    "all_users": set(),
                    "static_in": 0, "static_total": 0,
                    "dynamic_in": 0, "dynamic_total": 0,
                    "baseline_in": 0, "baseline_total": 0,
                    "daily_in": 0, "daily_total": 0,
                    "dynamic05_in": 0, "dynamic05_total": 0,
                    "daily05_in": 0, "daily05_total": 0,
                    "n_timestamps": 0,
                    "dyn_sp_series": [],
                    "dyn_obs": [],              # <-- new
                    "all_present_rows": set(),
                }

            acc = daily_accum[date_str]
            acc["N_t_list"].append(N_t)
            acc["S_t_list"].append(S_t)
            acc["all_users"].update(present_selected)
            acc["n_timestamps"] += 1

            if not present_selected:
                continue

            present_rows = [person_to_row[p] for p in present_selected]
            acc["all_present_rows"].update(present_rows)
            present_profiles = sampled.loc[present_rows]

            for _, prof in present_profiles.iterrows():
                acc["static_total"] += 1
                if prof["RangeMin"] <= trial_static_sp <= prof["RangeMax"]:
                    acc["static_in"] += 1

            combo_key = tuple(sorted(present_rows))
            if combo_key not in trial_dynamic_cache:
                trial_dynamic_cache[combo_key] = (
                    calculate_optimal_setpoint_from_curves(present_profiles)
                )
            dyn_sp = trial_dynamic_cache[combo_key]

            if dyn_sp is not None:
                dyn_sp05 = _round_to_step(dyn_sp)

                acc["dyn_sp_series"].append(dyn_sp)
                acc["dyn_obs"].append((ts_str, dyn_sp, dyn_sp05, tuple(present_rows)))

                for _, prof in present_profiles.iterrows():
                    acc["dynamic_total"] += 1
                    if prof["RangeMin"] <= dyn_sp <= prof["RangeMax"]:
                        acc["dynamic_in"] += 1

                    acc["dynamic05_total"] += 1
                    if prof["RangeMin"] <= dyn_sp05 <= prof["RangeMax"]:
                        acc["dynamic05_in"] += 1

            for _, prof in present_profiles.iterrows():
                acc["baseline_total"] += 1
                if prof["RangeMin"] <= BASELINE_SP <= prof["RangeMax"]:
                    acc["baseline_in"] += 1

        daily_fixed_sps = {}
        for date_str, acc in daily_accum.items():
            if not acc["all_present_rows"]:
                daily_fixed_sps[date_str] = float("nan")
            else:
                all_day_profiles = sampled.loc[sorted(acc["all_present_rows"])]
                sp = calculate_optimal_setpoint_from_curves(all_day_profiles)
                daily_fixed_sps[date_str] = sp if sp is not None else float("nan")

        for ts_str, occupants in room_snaps.items():
            date_str = ts_str[:10]
            present_selected = [p for p in occupants if p in person_to_row]
            if not present_selected:
                continue

            daily_sp = daily_fixed_sps.get(date_str, float("nan"))
            if daily_sp != daily_sp:
                continue

            daily_sp05 = _round_to_step(daily_sp)
            present_rows = [person_to_row[p] for p in present_selected]
            present_profiles = sampled.loc[present_rows]

            for _, prof in present_profiles.iterrows():
                daily_accum[date_str]["daily_total"] += 1
                if prof["RangeMin"] <= daily_sp <= prof["RangeMax"]:
                    daily_accum[date_str]["daily_in"] += 1

                daily_accum[date_str]["daily05_total"] += 1
                if prof["RangeMin"] <= daily_sp05 <= prof["RangeMax"]:
                    daily_accum[date_str]["daily05_in"] += 1

        for date_str, acc in sorted(daily_accum.items()):
            def _safe_ratio(num, den):
                return num / den if den > 0 else float("nan")

            def _gain(a, b):
                if a != a or b != b:
                    return float("nan")
                return a - b

            srd  = _safe_ratio(acc["static_in"], acc["static_total"])
            drd  = _safe_ratio(acc["dynamic_in"], acc["dynamic_total"])
            brd  = _safe_ratio(acc["baseline_in"], acc["baseline_total"])
            dfrd = _safe_ratio(acc["daily_in"], acc["daily_total"])

            drd05  = _safe_ratio(acc["dynamic05_in"], acc["dynamic05_total"])
            dfrd05 = _safe_ratio(acc["daily05_in"], acc["daily05_total"])

            daily_sp = daily_fixed_sps[date_str]
            daily_sp05 = _round_to_step(daily_sp) if daily_sp == daily_sp else float("nan")

            N_arr = np.array(acc["N_t_list"], dtype=float)
            S_list = acc["S_t_list"]
            n_ts = len(N_arr)

            mean_occ = float(np.nanmean(N_arr)) if n_ts > 0 else float("nan")
            max_occ = float(np.nanmax(N_arr)) if n_ts > 0 else float("nan")
            sd_occ = float(np.nanstd(N_arr, ddof=1)) if n_ts > 1 else float("nan")
            pres_ratio = float(np.mean(N_arr > 0)) if n_ts > 0 else float("nan")
            unique_cnt = len(acc["all_users"])

            utr_vals = []
            for t in range(1, len(S_list)):
                utr_val = _utr_t(S_list[t], S_list[t - 1])
                if utr_val is not None:
                    utr_vals.append(utr_val)
            n_valid_utr = len(utr_vals)
            utr_daily = float(np.mean(utr_vals)) if utr_vals else float("nan")

            dyn_series = np.array(acc["dyn_sp_series"], dtype=float)
            n_dyn = len(dyn_series)

            if n_dyn > 0:
                dynamic_sp_day_mean = float(np.mean(dyn_series))
                dynamic_sp_day_sd = float(np.std(dyn_series, ddof=1)) if n_dyn > 1 else float("nan")
                dynamic_sp_day_range = float(np.nanmax(dyn_series) - np.nanmin(dyn_series))
            else:
                dynamic_sp_day_mean = float("nan")
                dynamic_sp_day_sd = float("nan")
                dynamic_sp_day_range = float("nan")

            if n_dyn > 1:
                steps = np.abs(np.diff(dyn_series))
                dynamic_sp_mean_abs_step = float(np.mean(steps))
                dynamic_sp_sum_abs_step = float(np.sum(steps))
                dynamic_sp_n_changes = int(np.sum(steps >= CHANGE_EPS))
                dynamic_sp_change_ratio = float(np.mean(steps >= CHANGE_EPS))
                dynamic_sp_n_large_changes = int(np.sum(steps >= ACTION_STEP))
                dynamic_sp_large_change_ratio = float(np.mean(steps >= ACTION_STEP))
                dynamic_sp_max_abs_step = float(np.max(steps))

                changed_steps = steps[steps >= CHANGE_EPS]
                large_steps = steps[steps >= ACTION_STEP]
                dynamic_sp_mean_abs_step_when_changed = (
                    float(np.mean(changed_steps)) if len(changed_steps) > 0 else float("nan")
                )
                dynamic_sp_mean_abs_step_large_only = (
                    float(np.mean(large_steps)) if len(large_steps) > 0 else float("nan")
                )
            else:
                dynamic_sp_mean_abs_step = float("nan")
                dynamic_sp_sum_abs_step = float("nan")
                dynamic_sp_n_changes = 0
                dynamic_sp_change_ratio = float("nan")
                dynamic_sp_n_large_changes = 0
                dynamic_sp_large_change_ratio = float("nan")
                dynamic_sp_max_abs_step = float("nan")
                dynamic_sp_mean_abs_step_when_changed = float("nan")
                dynamic_sp_mean_abs_step_large_only = float("nan")

            if n_dyn > 0 and daily_sp == daily_sp:
                abs_gaps = np.abs(dyn_series - daily_sp)
                gap_mean = float(np.mean(abs_gaps))
                gap_max = float(np.max(abs_gaps))
                gap_sd = float(np.std(dyn_series - daily_sp, ddof=1)) if n_dyn > 1 else float("nan")
                gap_nf_ratio = float(np.mean(abs_gaps >= ACTION_STEP))
            else:
                gap_mean = gap_max = gap_sd = gap_nf_ratio = float("nan")

            # ---- New actionable 30-min metrics ----
            if len(acc["dyn_obs"]) > 0 and daily_sp05 == daily_sp05:
                obs_df = pd.DataFrame(
                    acc["dyn_obs"],
                    columns=["ts_str", "dyn_sp", "dyn_sp05", "present_rows"]
                )
                obs_df["ts"] = pd.to_datetime(obs_df["ts_str"])
                obs_df = obs_df.sort_values("ts").reset_index(drop=True)
                obs_df["window30"] = obs_df["ts"].dt.floor("30min")
                obs_df["daily_sp05"] = daily_sp05
                obs_df["dyn_daily_mismatch"] = obs_df["dyn_sp05"] != obs_df["daily_sp05"]

                win_rows = []
                for _, g in obs_df.groupby("window30"):
                    g = g.sort_values("ts")
                    if len(g) >= 2:
                        has_action = bool(np.any(np.abs(np.diff(g["dyn_sp05"].to_numpy())) >= ACTION_STEP))
                    else:
                        has_action = False

                    has_mismatch = bool(g["dyn_daily_mismatch"].any())
                    win_rows.append((has_action, has_mismatch))

                n_win = len(win_rows)
                if n_win > 0:
                    dynamic_action_window_count_30m = int(sum(x[0] for x in win_rows))
                    dynamic_action_window_ratio_30m = dynamic_action_window_count_30m / n_win
                    dyn_daily_mismatch_window_count_30m = int(sum(x[1] for x in win_rows))
                    dyn_daily_mismatch_window_ratio_30m = dyn_daily_mismatch_window_count_30m / n_win
                else:
                    dynamic_action_window_count_30m = 0
                    dynamic_action_window_ratio_30m = float("nan")
                    dyn_daily_mismatch_window_count_30m = 0
                    dyn_daily_mismatch_window_ratio_30m = float("nan")
            else:
                dynamic_action_window_count_30m = 0
                dynamic_action_window_ratio_30m = float("nan")
                dyn_daily_mismatch_window_count_30m = 0
                dyn_daily_mismatch_window_ratio_30m = float("nan")

            results.append({
                "original_room": room,
                "subgroup_size": k,
                "trial": trial_idx + 1,
                "date": date_str,
                "selected_members": tuple(selected),

                "static_ratio_daily": srd,
                "dynamic_ratio_daily": drd,
                "baseline24_ratio_daily": brd,
                "daily_fixed_ratio_daily": dfrd,
                "dynamic05_ratio_daily": drd05,
                "daily_fixed05_ratio_daily": dfrd05,

                "gain_static_vs_24_daily": _gain(srd, brd),
                "gain_dynamic_vs_24_daily": _gain(drd, brd),
                "gain_dynamic_vs_static_daily": _gain(drd, srd),
                "gain_dynamic_vs_daily_daily": _gain(drd, dfrd),
                "gain_dynamic05_vs_daily05_daily": _gain(drd05, dfrd05),

                "mean_occupancy_daily": mean_occ,
                "max_occupancy_daily": max_occ,
                "sd_occupancy_daily": sd_occ,
                "occupancy_presence_ratio_daily": pres_ratio,
                "utr_daily": utr_daily,
                "unique_user_count_daily": unique_cnt,
                "n_timestamps_daily": acc["n_timestamps"],
                "n_valid_turnover_points_daily": n_valid_utr,

                "daily_fixed_sp": daily_sp,
                "daily_fixed_sp05": daily_sp05,
                "dynamic_sp_day_mean": dynamic_sp_day_mean,
                "dynamic_sp_day_sd": dynamic_sp_day_sd,
                "dynamic_sp_day_range": dynamic_sp_day_range,
                "dynamic_sp_mean_abs_step": dynamic_sp_mean_abs_step,
                "dynamic_sp_sum_abs_step": dynamic_sp_sum_abs_step,
                "dynamic_sp_n_changes": dynamic_sp_n_changes,
                "dynamic_sp_change_ratio": dynamic_sp_change_ratio,
                "dynamic_sp_n_large_changes": dynamic_sp_n_large_changes,
                "dynamic_sp_large_change_ratio": dynamic_sp_large_change_ratio,
                "dynamic_sp_max_abs_step": dynamic_sp_max_abs_step,
                "dynamic_sp_mean_abs_step_when_changed": dynamic_sp_mean_abs_step_when_changed,
                "dynamic_sp_mean_abs_step_large_only": dynamic_sp_mean_abs_step_large_only,

                "gap_dyn_vs_daily_day_mean_abs": gap_mean,
                "gap_dyn_vs_daily_day_max_abs": gap_max,
                "gap_dyn_vs_daily_day_sd": gap_sd,
                "daily_not_followable_ratio": gap_nf_ratio,

                "dynamic_action_window_count_30m": dynamic_action_window_count_30m,
                "dynamic_action_window_ratio_30m": dynamic_action_window_ratio_30m,
                "dyn_daily_mismatch_window_count_30m": dyn_daily_mismatch_window_count_30m,
                "dyn_daily_mismatch_window_ratio_30m": dyn_daily_mismatch_window_ratio_30m,
            })

    return results
