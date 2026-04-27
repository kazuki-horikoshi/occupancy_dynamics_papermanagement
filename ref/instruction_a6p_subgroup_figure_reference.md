# Reference: Analysis 6P Subgroup Figures

## Scope

This note explains the two Analysis 6P figures below so another agent can read the source CSV and understand exactly what was plotted without reopening the whole notebook narrative.

- Target figure 1:
  [a6p_static_realtime_daily_by_subgroup.png](/workspaces/gear_occupancysimulation/outputs/61.ComOccu_Analysis/analysis6p_subgroup_simulation/a6p_static_realtime_daily_by_subgroup.png)
- Target figure 2:
  [a6p_improvement_vs24_by_subgroup.png](/workspaces/gear_occupancysimulation/outputs/61.ComOccu_Analysis/analysis6p_subgroup_simulation/a6p_improvement_vs24_by_subgroup.png)

The plotting logic is in
[notebooks/GEARoccupancyComfortSimulation.ipynb](/workspaces/gear_occupancysimulation/notebooks/GEARoccupancyComfortSimulation.ipynb:9477)
under the `Analysis 6P 可視化 & 保存（revised）` cell.

## Best Source Files

For understanding the current saved PNGs, the most direct backing CSV is:

- [a6p_results_20260326_092448.csv](/workspaces/gear_occupancysimulation/outputs/61.ComOccu_Analysis/analysis6p_subgroup_simulation/a6p_results_20260326_092448.csv)

Why this file is the best source:

- The visualization cell starts from `a6_results_df` loaded by the saved-result loader.
- It then creates `a6_plot_df` by adding the derived columns used in the improvement figure.
- The same visualization cell saves that derived dataframe with `save_df_timestamped(..., 'a6p_results')`.
- The current PNG timestamps are a few minutes later than this CSV, so this CSV is the closest saved tabular representation of the plotted data.

Related files:

- Saved-result loader:
  [notebooks/GEARoccupancyComfortSimulation.ipynb](/workspaces/gear_occupancysimulation/notebooks/GEARoccupancyComfortSimulation.ipynb:8977)
- 95% CI helper:
  [src/data_helpers.py](/workspaces/gear_occupancysimulation/src/data_helpers.py:17)

## What Each Figure Plots

### Figure 1: `a6p_static_realtime_daily_by_subgroup`

For each room panel, the x-axis is `subgroup_size (k)`.

The plotted series are:

- `static_ratio`
- `dynamic_ratio`
- `daily_fixed_ratio`
- `fixed24_0_ratio`

Plot labels in the notebook:

- `Static`
- `Realtime`
- `Daily`
- `Baseline (24°C)`

### Figure 2: `a6p_improvement_vs24_by_subgroup`

This figure uses derived columns created in the visualization cell:

```python
imp_static_vs_24   = static_ratio - fixed24_0_ratio
imp_realtime_vs_24 = dynamic_ratio - fixed24_0_ratio
imp_daily_vs_24    = daily_fixed_ratio - fixed24_0_ratio
```

Plot labels in the notebook:

- `Static - baseline`
- `Realtime - baseline`
- `Daily - baseline`

The horizontal red dashed line is `y = 0`, meaning "no improvement over the 24.0C baseline".

## Aggregation Logic

The notebook uses this helper:

```python
def aggregate_metric(df, col):
    return (
        df.groupby(['original_room', 'subgroup_size'])[col]
          .apply(ci95)
          .unstack()
    )
```

`ci95()` returns:

- `mean`
- `ci_lo`
- `ci_hi`
- `std`

Implementation:

- Drop NaN
- Compute mean
- Compute standard error with `scipy.stats.sem`
- Compute a two-sided 95% t-interval with `stats.t.interval`

So the line position is the mean across trials for each `(room, k)` pair, and the error bar is the 95% CI.

## Data Coverage

Source CSV used for this note:

- [a6p_results_20260326_092448.csv](/workspaces/gear_occupancysimulation/outputs/61.ComOccu_Analysis/analysis6p_subgroup_simulation/a6p_results_20260326_092448.csv)

Coverage in that CSV:

- Total rows: `50,000`
- Trials per `(room, k)`: `2,000`
- Rooms in plot order:
  `L5 - Katris Office`, `L5 - KD Office`, `L5 - Shared Office 1`, `L5 - Shared Office 2`

Observed `k` ranges:

- `L5 - Katris Office`: `k = 2..10`
- `L5 - KD Office`: `k = 2..6`
- `L5 - Shared Office 1`: `k = 2..6`
- `L5 - Shared Office 2`: `k = 2..7`

Columns in the saved derived CSV:

- `original_room`
- `subgroup_size`
- `trial`
- `selected_members`
- `static_ratio`
- `dynamic_ratio`
- `daily_fixed_ratio`
- `fixed24_0_ratio`
- `fixed24_5_ratio`
- `imp_static_vs_24`
- `imp_realtime_vs_24`
- `imp_daily_vs_24`
- `diff_realtime_vs_daily`

For the two target figures, `fixed24_5_ratio` and `diff_realtime_vs_daily` are not used.

## Mean Values Used by Figure 1

These are the mean values by `(room, k)` from the saved derived CSV.

| original_room | subgroup_size | static_ratio | dynamic_ratio | daily_fixed_ratio | fixed24_0_ratio |
|---|---|---|---|---|---|
| L5 - Katris Office | 2 | 0.7262 | 0.9579 | 0.9216 | 0.6668 |
| L5 - Katris Office | 3 | 0.7185 | 0.9286 | 0.8790 | 0.6762 |
| L5 - Katris Office | 4 | 0.7023 | 0.9021 | 0.8437 | 0.6677 |
| L5 - Katris Office | 5 | 0.6818 | 0.8778 | 0.8134 | 0.6689 |
| L5 - Katris Office | 6 | 0.6752 | 0.8593 | 0.7936 | 0.6755 |
| L5 - Katris Office | 7 | 0.6641 | 0.8439 | 0.7774 | 0.6677 |
| L5 - Katris Office | 8 | 0.6571 | 0.8283 | 0.7615 | 0.6661 |
| L5 - Katris Office | 9 | 0.6569 | 0.8165 | 0.7511 | 0.6673 |
| L5 - Katris Office | 10 | 0.6474 | 0.8062 | 0.7413 | 0.6645 |
| L5 - KD Office | 2 | 0.7259 | 0.9387 | 0.8963 | 0.6628 |
| L5 - KD Office | 3 | 0.7165 | 0.8968 | 0.8480 | 0.6774 |
| L5 - KD Office | 4 | 0.6919 | 0.8617 | 0.8081 | 0.6647 |
| L5 - KD Office | 5 | 0.6790 | 0.8335 | 0.7809 | 0.6673 |
| L5 - KD Office | 6 | 0.6763 | 0.8171 | 0.7674 | 0.6647 |
| L5 - Shared Office 1 | 2 | 0.7210 | 0.9589 | 0.9103 | 0.6747 |
| L5 - Shared Office 1 | 3 | 0.7051 | 0.9253 | 0.8623 | 0.6725 |
| L5 - Shared Office 1 | 4 | 0.6971 | 0.8998 | 0.8307 | 0.6794 |
| L5 - Shared Office 1 | 5 | 0.6750 | 0.8735 | 0.7973 | 0.6648 |
| L5 - Shared Office 1 | 6 | 0.6632 | 0.8545 | 0.7782 | 0.6595 |
| L5 - Shared Office 2 | 2 | 0.7046 | 0.9798 | 0.9584 | 0.6712 |
| L5 - Shared Office 2 | 3 | 0.6928 | 0.9530 | 0.9172 | 0.6643 |
| L5 - Shared Office 2 | 4 | 0.7016 | 0.9355 | 0.8926 | 0.6654 |
| L5 - Shared Office 2 | 5 | 0.6791 | 0.9099 | 0.8582 | 0.6624 |
| L5 - Shared Office 2 | 6 | 0.6722 | 0.8895 | 0.8347 | 0.6682 |
| L5 - Shared Office 2 | 7 | 0.6709 | 0.8768 | 0.8233 | 0.6735 |

## Mean Values Used by Figure 2

These are the mean values by `(room, k)` from the saved derived CSV.

| original_room | subgroup_size | imp_static_vs_24 | imp_realtime_vs_24 | imp_daily_vs_24 |
|---|---|---|---|---|
| L5 - Katris Office | 2 | 0.0594 | 0.2911 | 0.2548 |
| L5 - Katris Office | 3 | 0.0423 | 0.2524 | 0.2028 |
| L5 - Katris Office | 4 | 0.0346 | 0.2344 | 0.1760 |
| L5 - Katris Office | 5 | 0.0129 | 0.2089 | 0.1446 |
| L5 - Katris Office | 6 | -0.0003 | 0.1838 | 0.1182 |
| L5 - Katris Office | 7 | -0.0035 | 0.1762 | 0.1097 |
| L5 - Katris Office | 8 | -0.0091 | 0.1621 | 0.0953 |
| L5 - Katris Office | 9 | -0.0104 | 0.1492 | 0.0838 |
| L5 - Katris Office | 10 | -0.0172 | 0.1417 | 0.0767 |
| L5 - KD Office | 2 | 0.0631 | 0.2759 | 0.2335 |
| L5 - KD Office | 3 | 0.0390 | 0.2194 | 0.1706 |
| L5 - KD Office | 4 | 0.0272 | 0.1970 | 0.1434 |
| L5 - KD Office | 5 | 0.0117 | 0.1662 | 0.1137 |
| L5 - KD Office | 6 | 0.0116 | 0.1524 | 0.1027 |
| L5 - Shared Office 1 | 2 | 0.0463 | 0.2842 | 0.2356 |
| L5 - Shared Office 1 | 3 | 0.0326 | 0.2528 | 0.1898 |
| L5 - Shared Office 1 | 4 | 0.0177 | 0.2204 | 0.1513 |
| L5 - Shared Office 1 | 5 | 0.0102 | 0.2087 | 0.1325 |
| L5 - Shared Office 1 | 6 | 0.0037 | 0.1950 | 0.1187 |
| L5 - Shared Office 2 | 2 | 0.0334 | 0.3086 | 0.2873 |
| L5 - Shared Office 2 | 3 | 0.0285 | 0.2887 | 0.2529 |
| L5 - Shared Office 2 | 4 | 0.0362 | 0.2701 | 0.2272 |
| L5 - Shared Office 2 | 5 | 0.0168 | 0.2475 | 0.1959 |
| L5 - Shared Office 2 | 6 | 0.0040 | 0.2213 | 0.1665 |
| L5 - Shared Office 2 | 7 | -0.0026 | 0.2032 | 0.1497 |

## Quick Read for Another Agent

If another agent only needs the essentials:

1. Open the saved derived CSV:
   [a6p_results_20260326_092448.csv](/workspaces/gear_occupancysimulation/outputs/61.ComOccu_Analysis/analysis6p_subgroup_simulation/a6p_results_20260326_092448.csv)
2. Treat each row as one simulation trial for one `(room, subgroup_size, trial)`.
3. For Figure 1, average `static_ratio`, `dynamic_ratio`, `daily_fixed_ratio`, `fixed24_0_ratio` by `(original_room, subgroup_size)`.
4. For Figure 2, average `imp_static_vs_24`, `imp_realtime_vs_24`, `imp_daily_vs_24` by `(original_room, subgroup_size)`.
5. If exact plot replication is needed, compute 95% CI with `src.data_helpers.ci95()` and plot error bars using the notebook cell referenced above.
