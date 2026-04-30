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
Let \mathcal{T}_{r,d} denote the ordered set of analysis timestamps
for room r on day d. Let S_{r,t} be the set of selected agents present
in room r at timestamp t, and let N_{r,t}=|S_{r,t}|.
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
