# ch3 Method 修正方針メモ

対象: `chapters/ch3-Method.tex` の `Agentic simulation`、`Evaluation Metrics: Comfort-Related`、`Evaluation Metrics: Occupancy Related`

参照した実装:

- `ref/GEARoccupancyComfortSimulation.ipynb`
- `ref/a6_worker.py`
- `C:/Users/horik/Documents/gear_simulation/src/a6_worker.py`
- `C:/Users/horik/Documents/gear_simulation/src/setpoint.py`

## 1. 現状本文との差分

現在の本文では comfort 評価が「個人 comfort zone に setpoint が入るかどうか」の binary indicator として書かれている。しかし現在の解析では、主指標は binary comfort coverage ではなく、選ばれた setpoint を各個人 PCM に戻し、その setpoint における `No change` 確率を person-time 平均している。

修正方針:

- `C_{i,t}^{policy}` の binary 式は本文から外す。
- `No change` probability score を主指標として定義する。
- setpoint は個人最適温度の単純平均ではなく、個人 PCM の `No change` 確率曲線を merge した group comfort model の最大点として書く。
- OTR / DTR は使わず、30分前との Jaccard turnover を時系列で定義し、その daily average を日次 UTR として定義する。

## 2. Group comfort model と setpoint 選択

個人 PCM の `No change` 確率を次のように書く。

```tex
p_i(T) = P_i(S_{th}=0 \mid T)
```

ここでの `T` は Standard Effective Temperature ではなく、PCM と setpoint 選択で用いる温度軸である。

Group `G` の merged group comfort model:

```tex
\bar{p}_G(T)
=
\frac{1}{|G|}
\sum_{i\in G} p_i(T).
```

Group-level optimal setpoint:

```tex
T_G^{*}
=
\operatorname*{arg\,max}_{T\in\mathcal{T}_{\mathrm{set}}}
\bar{p}_G(T).
```

where:

- `G` is the set of PCM profiles aggregated for a given policy.
- `\mathcal{T}_{\mathrm{set}}` is the common setpoint-temperature grid used in the probability curves.
- `p_i(T)` is the `No change` probability of occupant `i`.

Policy-specific groups:

```tex
G_r^{\mathrm{Static}} = R_r,
\qquad
G_{r,d}^{\mathrm{Daily}} = A_{r,d},
\qquad
G_{r,t}^{\mathrm{RT}} = S_{r,t}.
```

対応する setpoint:

```tex
T_{\mathrm{set}}^{\mathrm{Static}}(t) = T_{G_r^{\mathrm{Static}}}^{*},
\qquad
T_{\mathrm{set}}^{\mathrm{Daily}}(t) = T_{G_{r,d(t)}^{\mathrm{Daily}}}^{*},
\qquad
T_{\mathrm{set}}^{\mathrm{RT}}(t) = T_{G_{r,t}^{\mathrm{RT}}}^{*}.
```

where:

- `R_r` is the sampled room member group for room `r`.
- `A_{r,d}` is the set of sampled agents who appear in room `r` on day `d`.
- `S_{r,t}` is the set of sampled agents present in room `r` at timestamp `t`.
- `d(t)` is the calendar day containing timestamp `t`.

## 3. Agentic simulation の流れ

本文では以下の流れで書く。

1. Stay log から room-time snapshot を作る。各 timestamp `t` について、room `r` にいる occupant IDs を保持する。
2. 各 room `r` と subgroup size `K` について、room member pool から `K` 人の agent を抽出する。
3. 抽出された agent に PCM をランダムに割り当てる。
4. 各 timestamp で、選ばれた agent のうち実際に room に存在する集合を `S_{r,t}` とする。
5. Static, Daily, Real-time の各 policy について、対応する group `G` の merged `No change` probability curve から setpoint `T_G^*` を選ぶ。
6. 選ばれた setpoint を、現在在室している各個人 `i \in S_{r,t}` の PCM に戻し、`p_i(T_{\mathrm{set}}^{policy}(t))` を記録する。
7. この person-time probability score を日次、room、subgroup size、trial ごとに平均する。

注意:

- `observed_set_range` はMethod本文には出さない。
- PCM pool が subgroup size より小さい場合の replacement sampling は別箇所で述べるため、ここでは書かない。

## 4. Comfort-related evaluation metrics

主指標は binary coverage ではなく、setpoint における個人 PCM の `No change` 確率である。

```tex
q_{i,t}^{\mathrm{policy}}
=
p_i\left(T_{\mathrm{set}}^{\mathrm{policy}}(t)\right),
\qquad i\in S_{r,t}.
```

日次 room-level score:

```tex
\mathrm{CP}_{r,d}^{\mathrm{policy}}
=
\frac{
\sum_{t\in\mathcal{T}_{r,d}}
\sum_{i\in S_{r,t}}
q_{i,t}^{\mathrm{policy}}
}{
\sum_{t\in\mathcal{T}_{r,d}}
|S_{r,t}|
}.
```

where:

- `\mathrm{CP}_{r,d}^{policy}` is the daily mean comfort probability score for room `r`, day `d`, and policy `policy`.
- `\mathcal{T}_{r,d}` is the ordered set of analysis timestamps for room `r` on day `d`.
- Empty timestamps are excluded from the denominator because no person-time comfort score exists when `|S_{r,t}|=0`.
- `q_{i,t}^{policy}` is the `No change` probability of present occupant `i` under the policy setpoint.

Gain metrics は Results の本文内で説明する想定なので、Method では定義しない。

## 5. Occupancy-related metrics

冒頭で以下を定義する。

```tex
Let \mathcal{T}_{r,d} denote the ordered set of analysis timestamps for room r on day d.
Let S_{r,t} be the set of selected agents present in room r at timestamp t, and let N_{r,t}=|S_{r,t}|.
```

`K` と `N_{r,t}` は分ける。`K` は simulation condition の subgroup size、`N_{r,t}` はその subgroup のうち実際に timestamp `t` に在室している人数。

### Mean occupancy

```tex
\bar{N}_{r,d}
=
\frac{1}{|\mathcal{T}_{r,d}|}
\sum_{t\in\mathcal{T}_{r,d}} N_{r,t}.
```

### Occupancy count variability

```tex
\sigma_{N,r,d}
=
\sqrt{
\frac{1}{|\mathcal{T}_{r,d}|-1}
\sum_{t\in\mathcal{T}_{r,d}}
\left(N_{r,t}-\bar{N}_{r,d}\right)^2
}.
```

### UTR

UTR はまず daily に均す前の時系列指標として定義する。現在の解析では、現在の occupant set と30分前の occupant set の Jaccard distance を用いる。

```tex
\mathrm{UTR}_{r,t}^{30}
=
1
-
\frac{
|S_{r,t}\cap S_{r,t-30}|
}{
|S_{r,t}\cup S_{r,t-30}|
}.
```

where:

- `S_{r,t-30}` is the occupant set in room `r` 30 minutes before timestamp `t`.
- If both current and lagged sets are empty, the timestamp-level turnover is undefined.
- A higher value indicates stronger short-horizon replacement of attendees.

Daily UTR は時系列 UTR の平均として別段落で定義する。

```tex
\mathrm{UTR}_{r,d}
=
\frac{1}{|\mathcal{V}_{r,d}|}
\sum_{t\in\mathcal{V}_{r,d}}
\mathrm{UTR}_{r,t}^{30}.
```

where `\mathcal{V}_{r,d}` is the set of timestamps on day `d` for which the 30-minute turnover is defined.

## 6. 本文でコメントアウトして残すもの

`chapters/ch3-Method.tex` では、以下をコメントアウトして残す。

- 旧 `theta_i` 平均による setpoint 定義
- 旧 binary comfort coverage 式
- 旧 windowed `\sigma^{(W)}_{N,t}` と `UTR^{(W)}_t`
- 旧 `\mu_t` ベースの control deviation
- 旧 `N_{\text{avg}}, V_{\text{occ}}, \mathrm{UTR}^{(W)}_t` の outcome wording

## 2026-05-07 追記: Method 追加修正方針

対象: `chapters/ch3-Method.tex` の `Agentic simulation` と `Evaluation Metrics`。主な意図は、simulation condition と outcome を明確化し、Results で使っている集計指標と Method の定義をそろえること。

参照した実装:

- `ref/a6_worker.py`
  - `run_a7_prob_daily`: probability-based comfort outcome
  - `run_a8_daily`: control burden / actionable 30-min metrics
- `ref/GEARoccupancyComfortSimulation.ipynb`
  - `a6p_static_realtime_daily_by_subgroup.png`
  - `a6p_improvement_vs24_by_subgroup.png`

### 7. Agentic simulation に追記する内容

`subgroup size` は Method 内で明示的に定義する。`K` は simulation condition として固定される sampled location-log agents の人数であり、時刻ごとの実在室人数 `N_{r,t}` とは別物として説明する。

差し込み位置メモ:

- 対象は `chapters/ch3-Method.tex` の `\subsection{Agentic simulation}`。
- `K` の説明は、`Each simulation trial first sampled a subgroup of location-log agents from the room's regular member pool.` の直後、`The sampled agents retained their observed stay logs...` の前に差し込む。
- Control timestep の説明は、`At each timestamp $t$, the subset of sampled location-log agents who are present in room $r$ is denoted by $S_{r,t}$.` の直後、`For each simulated realization, the three \acp{gcm} described above...` の前に差し込む。
- 本文化するときは、`At each timestamp $t$` と `At each control timestep` が重複しやすいため、必要なら `timestamp` を `30-minute control timestep` に寄せて 1 文に統合する。
- Figure caption の `control timestep` も同じ 30 分 timestep を指すように、必要なら caption 側にも `at each 30-minute control timestep` を補う。

追記方針:

```tex
The subgroup size $K$ denotes the number of location-log agents sampled from the regular member pool of room $r$ in a simulation condition.
For a given trial, $K$ remains fixed over the simulation period, whereas the realized occupancy count $N_{r,t}=|S_{r,t}|$ varies over time according to the observed stay logs.
```

Control timestep についても Agentic simulation に入れる。本文上は、setpoint を更新・評価する制御時間分解能を 30 分として明示する。

追記方針:

```tex
The control timestep was set to 30 minutes.
At each control timestep, the location-log agents present in room $r$ defined the active set $S_{r,t}$, and each policy selected the corresponding temperature setpoint from its group comfort model.
```

注意:

- 実装では `run_a8_daily` の docstring 上、`30-minute windows are used as a decision-resolution layer, while 15-minute timestamps remain the estimation-resolution layer` とされている。
- Method で「30分ごとに操作」と書く場合、本文では「control decision timestep」として 30 分を強調する。
- もし raw timestamp grid が 15 分のままなら、`dynamic_sp_mean_abs_step_when_changed` が 15 分差分、`dynamic_action_window_ratio_30m` が 30 分 window 指標になっている点を本文内で混同しない。

### 8. Evaluation Metrics の章構成を入れ替える

現在の `Evaluation Metrics` は `Comfort-Related` の後に `Occupancy Related`、最後に `Control Related` が置かれている。今回の整理では、Occupancy parameter は outcome ではなく評価・説明のための explanatory metrics なので、Comfort / Control outcome より前に置く。

差し込み位置メモ:

- 対象は `chapters/ch3-Method.tex` の `\subsection{Evaluation Metrics}`。
- 現在の `\subsubsection{Occupancy Related Parameters}` から `The daily \ac{utr} captures how much the present group composition changes over short horizons, even when the occupancy count is similar.` までのブロックを、`\subsection{Evaluation Metrics}` の直後へ移動する。
- 移動後、`Occupancy Related Parameters` の見出しは `Occupancy-related evaluation parameters` に変更する。
- 現在の `\subsubsection{Comfort-Related}` は Occupancy-related evaluation parameters の後に置き、見出しを `Comfort-related outcomes` に変更する。
- 現在の `\subsubsection{Control Related}` は Comfort-related outcomes の後に置き、見出しを `Control-related outcomes` に変更する。
- Occupancy-related evaluation parameters 冒頭の `K` 説明は、Agentic simulation で `K` を定義した後なので、`As defined in the simulation design, $K$ is the fixed subgroup size of sampled location-log agents, whereas $N_{r,t}$ is the realized occupancy count at timestamp $t$.` のように短くする。

推奨構成:

```tex
\subsection{Evaluation Metrics}

\subsubsection{Occupancy-related evaluation parameters}
% mean occupancy, occupancy variability, UTR

\subsubsection{Comfort-related outcomes}
% comfort probability by policy

\subsubsection{Control-related outcomes}
% setpoint adjustment magnitude and action-needed ratio
```

本文の説明方針:

- Occupancy-related metrics: `K`, `N_{r,t}`, `\bar{N}_{r,d}`, `\sigma_{N,r,d}`, `UTR_{r,d}`。これらは comfort/control の結果を説明するための evaluation parameters として書く。
- Comfort-related outcomes: policy ごとの comfort probability。これは outcome として書く。
- Control-related outcomes: required setpoint movement / operation frequency。これも outcome として書く。

### 9. Comfort-related outcomes に期間中の policy 比較を追加する

実装の `run_a7_prob_daily` では、各 present person-time について policy setpoint を個人 PCM に戻し、`get_normalized_prob_at_setpoint` による `No change` probability を蓄積している。日次 outcome として以下の列が出る。

- `static_prob_daily`
- `dynamic_prob_daily`
- `baseline24_prob_daily`
- `gain_static_prob_vs_24_daily`
- `gain_dynamic_prob_vs_24_daily`
- `gain_dynamic_prob_vs_static_daily`

Method では、すでに定義している room-day comfort probability `\mathrm{CP}_{r,d}^{policy}` に加えて、Results の最初の節で示す「期間中の policy ごとの平均比較」を定義する。

差し込み位置メモ:

- 対象は `Comfort-related outcomes` の日次 comfort probability 定義の直後。
- 具体的には、`\mathrm{CP}_{r,d}^{\mathrm{policy}}` の式、`Here, $\mathcal{T}_{r,d}$ is ...`、`Timestamps with no present location-log agents ...` の説明が終わった直後に差し込む。
- その後に `Control-related outcomes` が続く構成にする。
- 追加する内容は、Monte Carlo trial を表す `m` を添えた `\mathrm{CP}_{r,d,m}^{\mathrm{policy}}`、期間・trial 平均の `\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}`、fixed 24 ℃ baseline との差 `\Delta \overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}`。
- 現本文の `Dynamic` 表記は、GCM 名と合わせるなら `RT` または `Real\mbox{-}time` に寄せる。

追記方針:

```tex
For comparison across the simulation period, daily room-level comfort probabilities were averaged over the analysis days and Monte Carlo trials for each room, subgroup size, and policy:

\begin{equation}
\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
=
\frac{1}{|\mathcal{M}_{r,K}|}
\sum_{m\in\mathcal{M}_{r,K}}
\frac{1}{|\mathcal{D}_{r,m}|}
\sum_{d\in\mathcal{D}_{r,m}}
\mathrm{CP}_{r,d,m}^{\mathrm{policy}} .
\end{equation}
```

変数説明文案:

```tex
where $m$ is the Monte Carlo trial index, $\mathcal{M}_{r,K}$ is the set of Monte Carlo trials for room $r$ and subgroup size $K$, $\mathcal{D}_{r,m}$ is the set of valid analysis days for room $r$ in trial $m$, and $\mathrm{policy}\in\{\mathrm{Static},\mathrm{Daily},\mathrm{RT},24\,^\circ\mathrm{C}\}$ denotes the evaluated control policy.
```

Baseline improvement も Results の最初の節と対応するように、Method で短く定義してよい。

```tex
\Delta \overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
=
\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
-
\overline{\mathrm{CP}}_{r,K}^{24^\circ\mathrm{C}} .
```

注意:

- Results の `Comfort achievement ratio` は、現在の probability-based 解析に合わせるなら `comfort probability` または `mean comfort probability` と呼ぶほうが安全。
- `achievement ratio` という語を残す場合、binary coverage ではなく probability average であることを Method で明記する。
- `Daily` policy の probability outcome は、必要なら `daily_fixed_prob_daily` と対応させる。Static / RT / 24C は `run_a7_prob_daily` の列と直接対応する。

### 10. Control-related outcomes に追加する指標

Results の Control 後半では、前 control step からの操作温度差の絶対値と、0.5 ℃以上の操作が必要とされた割合を扱っている。Method の `Control Related` に以下を追加する。

差し込み位置メモ:

- 対象は `Control-related outcomes`。
- 既存の `RT` と `Static/Daily` の setpoint deviation 定義がある場合は、`Unless stated otherwise, the magnitudes of $|\Delta T^{\mathrm{Static}}_t|$ and $|\Delta T^{\mathrm{Daily}}_t|$ will be analyzed.` の直後に差し込む。
- 差し込み順は、まず `\paragraph{Setpoint adjustment magnitude.}` で前 control step からの changed-step adjustment を定義し、その後に `\paragraph{Action-needed ratio.}` と `\paragraph{Action-needed window ratio.}` を置く。
- 既存の `\Delta T^{Static}` / `\Delta T^{Daily}` は policy 間の deviation、追加する `\delta T^{RT}` は前 control step からの adjustment なので、記号を大文字 `\Delta` と小文字 `\delta` で分ける。
- `dynamic_sp_mean_abs_step_when_changed` を Results で使うため、10.1 では changed-step only の定義を本文の主定義にする。
- `dynamic_action_window_ratio_30m` を Results で使う場合は、10.2 の 30 分 window 指標 `\mathrm{AWR}_{r,d}^{30}` を主定義として置く。

#### 10.1 前 control step からの操作温度差

本文追記文案:

```tex
\paragraph{Setpoint adjustment magnitude.}
To quantify the control burden of the real-time policy, the setpoint adjustment from the previous control timestep is defined as
\begin{equation}
\delta T_{r,t}^{\mathrm{RT}}
=
T_{\mathrm{set}}^{\mathrm{RT}}(t)
-
T_{\mathrm{set}}^{\mathrm{RT}}(t-\Delta t),
\qquad
\left|\delta T_{r,t}^{\mathrm{RT}}\right|,
\label{eq:rt_setpoint_step}
\end{equation}
where $\Delta t=\qty{30}{\minute}$ is the control timestep, $\delta T_{r,t}^{\mathrm{RT}}$ is the setpoint change required by the real-time policy from the previous control timestep, and $|\delta T_{r,t}^{\mathrm{RT}}|$ is its absolute adjustment magnitude.
Because this analysis focuses on actual setpoint adjustments, the daily mean adjustment magnitude is computed only over timesteps with a non-negligible setpoint change.
\begin{equation}
\mathcal{C}_{r,d}^{+}
=
\left\{
t\in\mathcal{C}_{r,d}
\;:\;
\left|\delta T_{r,t}^{\mathrm{RT}}\right| \geq \varepsilon
\right\},
\qquad
\varepsilon=\qty{0.05}{\celsius}.
\label{eq:changed_step_set}
\end{equation}
\begin{equation}
\overline{|\delta T|}_{r,d,+}^{\mathrm{RT}}
=
\frac{1}{|\mathcal{C}_{r,d}^{+}|}
\sum_{t\in\mathcal{C}_{r,d}^{+}}
\left|\delta T_{r,t}^{\mathrm{RT}}\right|,
\label{eq:rt_mean_abs_step_when_changed_daily}
\end{equation}
where $\mathcal{C}_{r,d}$ is the set of timestamps on day $d$ in room $r$ for which both $T_{\mathrm{set}}^{\mathrm{RT}}(t)$ and $T_{\mathrm{set}}^{\mathrm{RT}}(t-\Delta t)$ are defined, $\mathcal{C}_{r,d}^{+}$ is the subset of valid control timesteps with a non-negligible setpoint change, and $\overline{|\delta T|}_{r,d,+}^{\mathrm{RT}}$ is the mean absolute adjustment magnitude when the setpoint changes.
% For each room-day, the mean absolute adjustment magnitude over all valid setpoint-update timestamps would be computed as follows:
% \begin{equation}
% \overline{|\delta T|}_{r,d}^{\mathrm{RT}}
% =
% \frac{1}{|\mathcal{C}_{r,d}|}
% \sum_{t\in\mathcal{C}_{r,d}}
% \left|\delta T_{r,t}^{\mathrm{RT}}\right|,
% \label{eq:rt_mean_abs_step_daily}
% \end{equation}
% where $\mathcal{C}_{r,d}$ is the set of timestamps on day $d$ in room $r$ for which both $T_{\mathrm{set}}^{\mathrm{RT}}(t)$ and $T_{\mathrm{set}}^{\mathrm{RT}}(t-\Delta t)$ are defined.
```

実装対応:

- `dynamic_sp_mean_abs_step`: all consecutive step の平均絶対値。
- `dynamic_sp_mean_abs_step_when_changed`: `CHANGE_EPS = 0.05` 以上変化した step だけの平均絶対値。
- Results の `analysis23...mean_abs_step_when_changed...` 図を説明するなら、Method では後者を主に定義する。

#### 10.2 0.5 ℃以上の操作が必要とされた割合

確認結果:

- Result 本文の `fig:CtrlWindowRatio` には `analysis25_utr30_endpoint_k_scaling_step_rate_full_confirm_rng_k16_trial1_1000_combined_20260416_073500.png` が差し込まれている。
- Result 本文ではこの図を「\qty{0.5}{\celsius} 以上の temperature adjustment event の probability」と説明している。
- 解析コードでは、この action frequency 系の図は `dynamic_action_window_ratio_30m` を使っており、notebook 内でも `paper_action_col = 'dynamic_action_window_ratio_30m'`、y-axis label は `Action-needed ratio` とされている。
- `ref/a6_worker.py` では、`dynamic_action_window_ratio_30m` は 30分 window ごとに rounded dynamic setpoint の \qty{0.5}{\celsius} 以上の update が少なくとも一度あるかを判定し、その window の割合として計算されている。
- したがって本編で主に使うべき定義は `\mathrm{AWR}_{r,d}^{30}` の 30分 window ratio。
- `\mathrm{AR}_{r,d}^{0.5}` は consecutive timestep ごとの割合なので、今回は本文には出さず、必要なら参考またはコメントアウトで残す。

本文追記文案:

```tex
\paragraph{Action-needed window ratio.}
For the 30-minute decision-window analysis, the real-time setpoint is first rounded to the nearest \qty{0.5}{\celsius}, denoted by $T_{\mathrm{set},0.5}^{\mathrm{RT}}(t)$.
A 30-minute window is counted as requiring action when at least one rounded real-time setpoint update within the window is \qty{0.5}{\celsius} or larger:
\begin{equation}
\mathrm{AWR}_{r,d}^{30}
=
\frac{1}{|\mathcal{W}_{r,d}^{30}|}
\sum_{w\in\mathcal{W}_{r,d}^{30}}
\mathbb{1}
\left(
\max_{t\in\mathcal{C}_{r,d,w}}
\left|
T_{\mathrm{set},0.5}^{\mathrm{RT}}(t)
-
T_{\mathrm{set},0.5}^{\mathrm{RT}}(t-\Delta t)
\right|
\geq \qty{0.5}{\celsius}
\right),
\label{eq:action_needed_window_ratio}
\end{equation}
where $\mathbb{1}(\cdot)$ is the indicator function, $\mathcal{W}_{r,d}^{30}$ is the set of 30-minute decision windows for room $r$ on day $d$, $\mathcal{C}_{r,d,w}$ is the set of valid within-window consecutive setpoint-update timestamps in window $w$, and $\mathrm{AWR}_{r,d}^{30}$ is the share of 30-minute windows requiring at least one actionable real-time setpoint update.
```

参考としてコメントアウトして残す timestep-level ratio:

```tex
% \paragraph{Timestep-level action-needed ratio.}
% For each valid control timestep, the action-needed indicator can be defined as
% \begin{equation}
% I_{r,t}^{0.5}
% =
% \mathbb{1}
% \left(
% \left|\delta T_{r,t}^{\mathrm{RT}}\right|
% \geq \qty{0.5}{\celsius}
% \right),
% \label{eq:action_needed_indicator}
% \end{equation}
% and the daily timestep-level action-needed ratio can be computed as
% \begin{equation}
% \mathrm{AR}_{r,d}^{0.5}
% =
% \frac{1}{|\mathcal{C}_{r,d}|}
% \sum_{t\in\mathcal{C}_{r,d}}
% I_{r,t}^{0.5}.
% \label{eq:action_needed_ratio_daily}
% \end{equation}
```

注意:

- `dynamic_sp_large_change_ratio` は consecutive setpoint steps のうち `0.5 ℃` 以上の割合。
- `dynamic_action_window_ratio_30m` は 30 分 window 内で少なくとも一度 `0.5 ℃` 以上の rounded dynamic update が必要だった window の割合であり、`fig:CtrlWindowRatio` に対応する。
- Results の `Control action frequency` で使っている図が `analysis25_utr30...step_rate...` なら、Method では `dynamic_action_window_ratio_30m` / `AWR_{r,d}^{30}` を優先して定義する。

### 11. 本文修正の作業順

1. `Agentic simulation` に `K` と 30 分 control timestep の説明を追加する。
2. `Evaluation Metrics` の順番を `Occupancy parameters` -> `Comfort outcomes` -> `Control outcomes` に変更する。
3. `Comfort outcomes` に、日次 `CP` だけでなく、期間中・policy ごとの平均 `\overline{CP}` と baseline improvement を追加する。
4. `Control outcomes` に、前 step からの `|\delta T|` と `0.5 ℃` 以上操作割合を追加する。
5. Results 側の用語を、必要に応じて `comfort achievement ratio` から `mean comfort probability` に寄せる。
6. `Analysis outcomes` 側には、必要に応じて `The comfort- and control-related outcomes defined above are analyzed against the occupancy-related evaluation parameters to identify the occupancy conditions under which high-resolution group comfort modeling is beneficial and operationally demanding.` を `\subsection{Analysis outcomes}` の直後、`\paragraph{Mapping Occupancy Conditions}` の前に追加する。

## 2026-05-07 Ver2: 反映確認と追加修正方針

対象: `chapters/ch3-Method.tex` と `chapters/ch4-Results.tex` を見比べ、これまでの revision 案が反映されているかと、Method の再現可能性をさらに上げるために必要な追加修正を確認した。

参照した実装と図:

- `ref/a6_worker.py`
  - `run_a7_prob_daily`: `static_prob_daily`, `dynamic_prob_daily`, `baseline24_prob_daily` を出す probability-based comfort outcome。
  - `run_a8_daily`: `dynamic_sp_mean_abs_step_when_changed` と `dynamic_action_window_ratio_30m` を出す control-burden outcome。
  - `run_a8_daily` の docstring では、15-minute timestamps を estimation-resolution layer、30-minute windows を decision-resolution layer として扱うと説明されている。
- `chapters/ch4-Results.tex`
  - `a6p_static_realtime_daily_by_subgroup.png`: Static / Realtime / Daily / Baseline の comfort result 図。
  - `a6p_improvement_vs24_by_subgroup.png`: 24 ℃ baseline からの improvement 図。
  - `analysis23_mean_occupancy_moving_quantile_dynamic_sp_mean_abs_step_when_changed...png`: changed-step の mean absolute setpoint adjustment 図。
  - `analysis25_utr30_endpoint_k_scaling_step_rate...png`: `dynamic_action_window_ratio_30m` に対応する action-needed window ratio 図。

### 12. これまでの revision 案の反映状況

- `location-log agents` への表記統一は `chapters/ch3-Method.tex` 側に概ね反映済み。
- `Agentic simulation` における subgroup size $K$ の定義は反映済み。
- $K$ と時刻ごとの realized occupancy count $N_{r,t}$ を分ける説明は反映済み。
- Evaluation Metrics の章順は `Occupancy-related evaluation parameters` -> `Comfort-related outcomes` -> `Control-related outcomes` に反映済み。
- Comfort-related outcomes に room-day comfort probability と Monte Carlo / analysis-day 平均の式は反映済み。
- Baseline improvement の式 `\Delta \overline{\mathrm{CP}}` はまだ本文に明示されていない。
- Control-related outcomes に changed-step mean absolute adjustment magnitude は反映済み。
- Action-needed window ratio `\mathrm{AWR}_{r,d}^{30}` は反映済み。
- ただし timestep-level の `Action-needed ratio` と window-level の `Action-needed window ratio` が両方本文に残っており、Results の `fig:CtrlWindowRatio` には window-level の方だけを主指標として対応させる方がよい。
- `Analysis outcomes` はまだ `Based on the function above` という曖昧な表現が残っており、Method 内で定義した occupancy parameters と comfort/control outcomes をどう対応づけるかを明示するとよい。

### 13. Ver2 で優先して直すべき点

#### 13.1 real-time 評価は30分 decision window として扱う

確認結果:

- 現在の Method では `At each 30-minute control timestep $t$` と書かれている。
- `ref/a6_worker.py` の `run_a8_daily` では、連続 setpoint step には15分 timestamp に由来する中間計算が残っている。
- ただし Results の control action frequency 図で使っている指標は `dynamic_action_window_ratio_30m` である。
- `dynamic_action_window_ratio_30m` は `obs_df["ts"].dt.floor("30min")` で30分 window を作り、その window 内に丸め後の real-time setpoint が \qty{0.5}{\celsius} 以上変化した箇所が少なくとも一度あるかを数えている。
- したがって最終的な real-time control action frequency の評価は30分 decision window として説明してよい。
- Method 本文にすでに `At each 30-minute control timestep $t$` とあるため、完全に記載が抜けている箇所以外では、15分 timestamp や resampling の詳細は追記しない。

差し込み位置:

- `chapters/ch3-Method.tex` の `Agentic simulation` にある `At each 30-minute control timestep $t$, ...` は基本的に維持する。
- 30分評価であることが抜けている箇所があれば、`Control-related outcomes` の action-needed window ratio 定義の直前に最小限の1文だけを追加する。

必要な場合の最小追記文案:

```tex
The real-time policy was evaluated using 30-minute control decision windows.
```

既存文を置き換える場合の文案:

```tex
At each 30-minute control decision window $t$, the sampled location-log agents present in room $r$ defined the active set $S_{r,t}$, and each policy selected the corresponding temperature setpoint from its \ac{gcm}.
```

注意:

- `dynamic_sp_mean_abs_step_when_changed` は setpoint adjustment magnitude の補助的な制御負荷指標として扱う。
- Results で主に使う control action frequency は `dynamic_action_window_ratio_30m` / `\mathrm{AWR}_{r,d}^{30}` に統一する。
- 15分 timestamp や resampling の詳細は、完全に再現不能になる場合を除き本文には入れない。

#### 13.2 Comfort outcome は probability で統一する

方針:

- Comfort outcome は binary coverage ではなく、\ac{pcm} の ``No change'' probability を person-time average した `mean comfort probability` として統一する。
- Results の最初の comfort 図も、この方針に合わせて probability-based の集計値に差し替える。
- Method 本文では `\mathrm{CP}_{r,d}^{\mathrm{policy}}` と `\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}` を主指標として残す。
- `comfort achievement ratio` や `comfort probability ratio` は、本文では `mean comfort probability` に寄せる。
- Improvement 図は fixed \qty{24}{\celsius} baseline からの mean comfort probability の差として定義する。

確認結果:

- 現在の `chapters/ch3-Method.tex` は probability-based の `q_{i,t}^{\mathrm{policy}}` と `\mathrm{CP}_{r,d}^{\mathrm{policy}}` をすでに定義している。
- したがって Method 側は binary coverage を追加せず、baseline improvement の式だけ補えばよい。
- Results 側は、図と本文で使う集計列が `static_prob_daily`, `daily_prob_daily` または対応する Daily probability column, `dynamic_prob_daily`, `baseline24_prob_daily` に基づくことを確認する。
- Daily probability column の最終名称は解析コード側で確認し、Method の policy 表記と揃える。

差し込み位置:

- `chapters/ch3-Method.tex` の `Comfort-related outcomes` で、`\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}` の式と where 文の直後に追加する。

本文追記文案:

```tex
The improvement relative to the fixed \qty{24}{\celsius} baseline is defined as
\begin{equation}
\Delta \overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
=
\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
-
\overline{\mathrm{CP}}_{r,K}^{24\,^\circ\mathrm{C}} .
\label{eq:comfort_probability_gain_vs24}
\end{equation}
```

Results 側の修正文案:

```tex
Figure~\ref{fig:ComfAgentic}\subref{fig:ComfAchi} shows the mean comfort probability under the \ac{sgcm}, \ac{dgcm}, \ac{rtgcm}, and fixed \qty{24}{\celsius} baseline policies for different subgroup sizes across the four office rooms.
Figure~\ref{fig:ComfAgentic}\subref{fig:ComfImp} shows the improvement in mean comfort probability relative to the fixed \qty{24}{\celsius} baseline.
Across all rooms, the fixed \qty{24}{\celsius} baseline remained nearly constant across subgroup sizes.
The \ac{rtgcm} produced the highest mean comfort probability for every room and subgroup size, followed by the \ac{dgcm} and then the \ac{sgcm}.
```

注意:

- 現在の Results 図ファイルが binary coverage に基づく場合は、図を probability-based 集計で作り直してから本文を上記表現へ寄せる。
- `comfort achievement ratio` を残すと binary coverage と混同しやすいため、Probability 統一版では使わない。

#### 13.3 policy setpoint の定義を comfort probability curve 平均に揃える

現時点の方針:

- Static も Daily / RT と同様に、対象 group の comfort probability curves を平均し、その merged curve を最大化する setpoint として定義したい。
- この方針にする場合、Method の現在の式は概ね自然だが、実装側で Static が `PeakSET` 平均になっていないか確認する。
- 後ほど本文修正時に、Static / Daily / RT のすべてが同じ `\bar{p}_G(T)` と `T_G^{*}` の定義から出ていることを明確にする。

差し込み位置:

- `chapters/ch3-Method.tex` の `The policy-specific groups are` から `The resulting policy setpoints are` の周辺を見直す。
- Static を `PeakSET` 平均として書く案は採用しない。
- Static / Daily / RT を同じ comfort probability curve aggregation のルールで記述する。

本文確認・追記文案:

```tex
For all three \ac{gcm}-based policies, the policy setpoint is selected by maximizing the merged ``No change'' probability curve of the corresponding group.
The difference between policies is therefore not the setpoint-selection rule itself, but the temporal resolution at which the group $G$ is defined.
```

追加で明記したい文案:

```tex
The fixed baseline policy is defined as $T_{\mathrm{set}}^{24\,^\circ\mathrm{C}}(t)=\qty{24}{\celsius}$ during the analysis period.
```

#### 13.4 Sampling procedure と candidate setpoint grid の詳細は今回は追加しない

方針:

- Sampling procedure の replacement setting や random-seed rule は、現段階の本文追記としては細かすぎるため追加しない。
- Candidate setpoint grid の範囲、刻み、tie-breaking も、現段階では Method 本文への追記対象から外す。
- 必要になった場合は Appendix または reproducibility note として別途整理する。

#### 13.5 Control-related outcomes の重複整理は反映済み

確認結果:

- 現在の `Control-related outcomes` には `Action-needed ratio` と `Action-needed window ratio` が両方ある。
- `chapters/ch4-Results.tex` の `fig:CtrlWindowRatio` は `dynamic_action_window_ratio_30m` に対応する。
- `dynamic_sp_large_change_ratio` に対応する timestep-level ratio は、現在差し込んでいる Results 図の主指標ではない。
- ただしこの点はすでに統合・整理済みとして扱い、新規の追記対象にはしない。

差し込み位置:

- `chapters/ch3-Method.tex` の `\paragraph{Action-needed ratio.}` から `\mathrm{AR}_{r,d}^{0.5}` の式までをコメントアウトするか、Appendix 用の auxiliary definition に移す。
- `\paragraph{Action-needed window ratio.}` を Control-related outcomes の主定義として残す。

本文に残す文案:

```tex
\paragraph{Action-needed window ratio.}
For the Results analysis of control action frequency, the main actionable metric is the 30-minute action-needed window ratio.
```

コメントアウトする場合のメモ:

```tex
% The timestep-level action-needed ratio $\mathrm{AR}_{r,d}^{0.5}$ was considered as an auxiliary diagnostic, but the Results figures use the 30-minute window-level metric $\mathrm{AWR}_{r,d}^{30}$.
```

#### 13.6 Results の内容を踏まえて Analysis outcomes を修正する

確認結果:

- 現在の `Analysis outcomes` は `Based on the function above` から始まっており、どの metrics をどう使うかが曖昧。
- Method の構成上、occupancy-related evaluation parameters は explanatory metrics、comfort/control は outcomes として整理したので、その対応を明示すると章の筋が通る。
- Results では、まず subgroup size $K$ ごとの mean comfort probability と fixed \qty{24}{\celsius} baseline からの improvement を比較する。
- Results では、次に \ac{rtgcm} の setpoint adjustment magnitude を daily mean occupancy や subgroup-size-normalized occupancy と対応させる。
- Results では、最後に \ac{utr} と action-needed window ratio の関係、および部屋・曜日別の \ac{utr} transition を示す。

差し込み位置:

- `chapters/ch3-Method.tex` の `\subsection{Analysis outcomes}` の直後に入れる。
- 現在の `Based on the function above...` の文は置き換える。

本文置き換え文案:

```tex
The analysis links the occupancy-related evaluation parameters to the comfort- and control-related outcomes defined above.
First, mean comfort probability and its improvement relative to the fixed \qty{24}{\celsius} baseline are compared across subgroup sizes and \ac{gcm} resolutions.
Second, the real-time control burden is evaluated by relating the mean absolute setpoint adjustment magnitude to daily mean occupancy and subgroup-size-normalized occupancy.
Third, the operational frequency of actionable control is evaluated by relating \ac{utr} to the 30-minute action-needed window ratio.
Representative \ac{utr} transitions by room and weekday are then used to interpret the occupancy-dynamics patterns associated with higher action-needed ratios.
```

注意:

- `equivalence-effective` という表現は定義済みの統計的 equivalence test がない限り避ける。
- Results で threshold を示すなら、どの outcome をどの occupancy parameter に対して mapping したかを Method に対応させる。

### 14. Results 側と Method 側の整合性メモ

- `chapters/ch4-Results.tex` の comfort 節では `comfort probability ratio` と `comfort achievement ratio` が混在している。
- Probability 統一方針では、Results 側は `mean comfort probability` に寄せる。
- 現在の `a6p...` 図が binary coverage ベースなら、probability-based figure に差し替える。
- `chapters/ch4-Results.tex` の `The \ac{rtgcm} shows the highest ... followed by \ac{dgcm} and then \ac{dgcm}.` は最後が `\ac{sgcm}` の誤記と思われる。
- `fig:CtrlWindowRatio` の本文は \ac{utr} と action-needed ratio の関係を説明しているが、caption は `daily occupancy-count standard deviation` と書かれている。
- `fig:CtrlWindowRatio` の caption は、図の x-axis が \ac{utr} なら `Relationship between user turnover rate and action-needed window ratio` のように直す。
- `fig:UTRexamples` の caption は UTR transition 図なのに `Distribution of temperature adjustment magnitudes under dynamic group control` と書かれている。
- `fig:UTRexamples` の caption は `Representative 30-minute user turnover rate transitions by room and weekday` のように直す。

### 15. Ver2 作業順

1. 13.1 は real-time control action frequency を30分 decision-window 評価として扱い、15分 timestamp や resampling の詳細は本文に追記しない方針で確認する。
2. Comfort outcome は probability-based に統一し、Method には `\Delta \overline{\mathrm{CP}}` の式を追加する。
3. Results の comfort 図を probability-based figure に差し替え、本文用語を `mean comfort probability` に統一する。
4. Static / Daily / RT の setpoint selection は、すべて comfort probability curve の平均を最大化する方針で確認する。
5. Sampling procedure と candidate setpoint grid の詳細追記は今回は見送る。
6. Control-related outcomes は window-level `\mathrm{AWR}_{r,d}^{30}` を主定義として整理済みとして扱う。
7. `Analysis outcomes` の導入文を、Results の comfort comparison、setpoint adjustment magnitude、action-needed window ratio、UTR transition に対応する形へ置き換える。
8. Results captions と本文中の用語を Method の定義に合わせて修正する。
