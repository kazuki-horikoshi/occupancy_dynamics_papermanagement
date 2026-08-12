# ASIM 2026 import candidates

Copied on 2026-08-12 from the read-only conference-paper folder:

`/Users/kazukihorikoshi/Overleaf/IBPSA ASIM 2026_OccupancySimulation`

These files are staging copies for the OccupancyDynamics journal manuscript. They are not referenced by the active manuscript yet. The source conference folder was not modified.

## Candidates that can be integrated after local checks

| File | Intended journal use | Required check before activation |
|---|---|---|
| `figures/occupancy_density_timeofday_k12_paper.png` | Evidence that decision-time occupancy density was often below one | Confirm source table, interval definitions, room mapping, and the meanings of the plotted intervals. Do not use this figure alone to claim an RT-GCM versus DGCM mechanism. |
| `tex/TargetRooms.tex` | Four-room simulation-target table | Confirm mapping between Office 5A/5B labels and the current journal room names; adapt ASIM-specific table macros. |
| `figures/SimulationFlow_small.png` | Compact Method workflow | Check terminology against the final common policy rule and journal figure style. |
| `figures/fig3a_setpoint_adjustment_by_occupancy_compact_paper.png` | Compact setpoint-adjustment panel | Confirm generator, changed-step denominator, and percentile unit. |
| `figures/fig3b_setpoint_adjustment_by_group_size_and_occupancy_density_compact_paper.png` | Compact subgroup-size/occupancy-density panel | Confirm generator, bin definitions, and blank-cell threshold. |
| `figures/fig4a_action_rate_by_turnover_compact_paper.png` | Compact 15-minute UTR/action panel | Confirm transition denominator, empty intervals, day boundaries, rounding, bin edges, and source table. Do not combine with the journal 30-minute AWR definition without reconciliation. |
| `figures/fig4b_weekly_30min_utr_selected_compact_paper.png` | Compact weekday UTR panel | Resolve the 15-minute caption versus 30-minute filename/text inconsistency and room mapping. |
| `figures/fig1_analysis23nr_with_fixed24_raw2000_64_100_all_solid_small_markers_paper.png` | Probability-labelled comfort comparison | Hold until the common optimizer, raw versus normalized probability, trial count, and source table are verified. The ASIM text and this figure disagree at small K. |
| `bib/wang_enhancing_2026.bib` | Optional Discussion reference | Use only as directional background; its group scale and outcome differ from this study. |

## TeX snapshot

`tex/ASIM2026-fullpaper.tex` and `tex/sections/1.introduction.tex` through `5.conclusion.tex` are snapshots of the compiled ASIM manuscript. `tex/appendix-draft.tex` retains supplementary Method and Results candidates that were excluded from the eight-page conference paper. They are retained so that candidate sentences, captions, and quantitative claims can be audited without editing or depending on the conference folder.

They should not be copied wholesale into the journal manuscript. The metric, policy rule, trial count, time resolution, and room labels must first satisfy the checks in `Update.md`, Chapter 7.

`source_notes/` contains exact snapshots of the unresolved-comment CSV, the ASIM content-selection ledger, and the handover notes used to determine provenance and unresolved checks.

## Files already present byte-for-byte in the journal repository

The following ASIM assets were not copied again as separate candidates because identical SHA-256 content already exists under `pic/ch4-Results/agentic/Result_Agentic/`:

| ASIM asset | Existing journal asset |
|---|---|
| `comfort_probability_by_subgroup.png` | `analysis21_a6_style_comfort_rates_expanded_pool_selected_k_adopted_20260630_083849.png` |
| `rt_minus_daily_by_subgroup.png` | `analysis21_a6_style_rt_minus_dgcm_expanded_pool_selected_k_adopted_20260630_090131.png` |
| `comfort_improvement_by_subgroup.png` | `analysis21_a6_style_improvement_vs24_expanded_pool_selected_k_adopted_20260630_083849.png` |
| `setpoint_adjustment_by_occupancy.png` | `analysis23_mean_occupancy_moving_quantile_dynamic_sp_mean_abs_step_when_changed_expanded_pool_overlap_dense_only.png` |
| `setpoint_adjustment_heatmap.png` | `analysis23_k_normalized_mean_occupancy_mean_abs_step_when_changed_heatmap_regime_style_expanded_pool_overlap_dense_ybins05pct_kle16_minn20.png` |
| `action_rate_by_turnover.png` | `analysis25_final_15min_action_step_rate_by_15min_utr_member_size.png` |
| `turnover_profiles_by_room.png` | `analysis25_utr30_rolling_representative_k_separate_room_panels_30min_full_confirm_rng_k16_trial1_1000_combined_20260416_073500.png` |

Byte identity does not establish analytical provenance. These files remain subject to the common-rule and source-table audit.

## Copied-file SHA-256 values

```text
32a7b6b899117fc159da3d35c0bd0e7f3bbce7997ef2c819c55963be9a58bc5f  source_notes/HANDOVER.md
42553f2cc381b1238129f8333214b219003f5e4a11b504021d02f9923d2a9bfa  source_notes/overleaf_comments_unresolved.csv
14c1e11cb16170efcac5ec93201b9a949422f566b12f79ddde627e98000ec4c1  tex/sections/1.introduction.tex
17c294ca25cae839b4acb7c9915f1198e49d3ba82f19fe82d48f3de31974e4bf  tex/appendix-draft.tex
1e8238a37cf03bcb00d7b052ca3f7adf5bcf34a3099ab172a465404b0deda4de  figures/fig4b_weekly_30min_utr_selected_compact_paper.png
2c1a4142c8caa9f1e7a79e644dc33209457b513945eafa0f2f2caab21c5c189b  figures/fig3b_setpoint_adjustment_by_group_size_and_occupancy_density_compact_paper.png
2eaba113f6495428fa29ede8f25439f3f814a744e43ef64beba416392c00b1d5  tex/ASIM2026-fullpaper.tex
3191b014d8c7b68122cf30ebb3249f644b5a31691b2e41a70d1834b598856903  figures/fig4a_action_rate_by_turnover_compact_paper.png
3350459b1f50616a54cfd694eaf642799cc17b3a2b5788e20d561be82ba962d0  tex/TargetRooms.tex
4402125239322032c2c1109059a929f2bfeaa718702bc61fe31def6f90bf9961  tex/sections/5.conclusion.tex
5e71a622bd6b425e3b53db9ebc81981b048d3ba80796b6cd24754537e181af2c  bib/wang_enhancing_2026.bib
70fb26609287af2fc90dd345d90dd7f78c2fad43baa15e98142af5a532344e12  figures/occupancy_density_timeofday_k12_paper.png
9335c3bd6e60bb9a8579e857f5b59a4f4167f8257cb809d74e279905df5d30d1  tex/sections/2.method.tex
947b485ce8c1da595d9f3becd48da7124c1dbe6f9689b334b775624a2d030da3  figures/fig1_analysis23nr_with_fixed24_raw2000_64_100_all_solid_small_markers_paper.png
9a594a35cb93b4a7d88fd28cf34088b3705af4934b3d7a4b8fcc6cd40357b7b9  figures/SimulationFlow_small.png
b0aa6c6552f50cb634149c48d364b7c2e0b1eb7ee80fbc05e385aa7a9feee89c  tex/sections/3.results.tex
e9ce95bd347c196f0cea98dfdb81ac86130c8f9df70c9fb6a86c4618fdf7a6ba  tex/sections/4.discussion.tex
e5bb14a38e832e43c1b580f501a778fbb56108e9cada2a861f4869601ee1d2b7  source_notes/content-selection-notes.md
ed06fb693a9804775c6a1991dcb89e1c555e0d381a206ddaed29fd362742a1e1  figures/fig3a_setpoint_adjustment_by_occupancy_compact_paper.png
```
