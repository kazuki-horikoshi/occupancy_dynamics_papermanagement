# OccupancyDynamics chapter update memo

作成日: 2026-06-17  
更新日: 2026-06-22

## 前提

- 参照稿と現在の OccupancyDynamics 論文は別論文として扱う。
- 参照稿側の別テーマ固有の分析枠組みや結果は現在稿へ移植しない。
- Review は今回の本文追記対象外とする。
- 参照稿から使うのは、Dynamic Occupancy、shared-space OCC、GCM resolution、対象建物・調査条件・survey 項目など、現在稿と共通する情報に限定する。

## 全体方針

1. Introduction は、Dynamic Occupancy と Group Comfort Model Resolution の必要性が自然に立ち上がる構成へ整理する。
2. Method は、現在稿の occupancy-log-based agentic simulation を主軸に残し、参照稿から field-data detail と SGCM/DGCM/RT-GCM の説明を補強する。
3. Appendix は、thermal comfort survey items と clo-value calculation など、現在稿でもそのまま使える調査情報だけを追記する。
4. Results/Discussion/Conclusion は、現在稿の simulation results の解釈を補強する範囲で既存研究との接続を加える。
5. 参照稿側の別テーマ専用の図表・表は移植対象外。

## Chapter 1: Introduction

### 確認結果

現在稿には、OCC、ABW、real-time occupancy sensing、shared-space OCC、Jung/Ono/Lei への接続、SGCM/DGCM/RT-GCM の研究目的が既に入っている。

追加・修正が必要なのは、内容の新規追加というより、以下の整理。

- OCC から GCM への接続を早めに明示する。
- Dynamic Occupancy を「人数変化」だけでなく「occupant composition の変化」として強調する。
- Real-time tracking は利用可能になっているが、常に導入すべきとは限らない、という実務的問題を明確にする。
- 現在稿 Results に基づき、研究目的を「具体の効果を見る」形に寄せる。

### 追記・整理案

#### 1. OCC から GCM への接続

現在稿で不足しているのは、shared-space control では PCM を room-level decision に集約する必要がある、という一文の明確さ。

追記候補:

```tex
In shared office spaces, however, \ac{occ} cannot rely only on isolated \acp{pcm}, because a single room-level \ac{hvac} setpoint must represent multiple occupants at the same time. This makes the construction of a \ac{gcm}, which aggregates individual comfort information into a room-level representation, a central design issue for shared-space \ac{occ}.
```
->追記

続けて、GCM resolution の問題を入れる。

```tex
The key question is not only how accurately individual \acp{pcm} predict comfort, but also which occupant set should be represented when the room-level control decision is made.
```
->追記

#### 2. Dynamic Occupancy の背景

現在稿には ABW と dynamic occupancy の説明はあるが、occupant composition の変化をより明確にする。

追記候補:

```tex
In such spaces, dynamic occupancy should be understood not only as a change in the number of occupants, but also as a change in who is present. Even when the occupancy count is similar, the thermal preferences represented by the present group may differ as occupants arrive, leave, or move between rooms.
```
->追記

これにより、UTR を後段で扱う理由が自然になる。

#### 3. Real-time occupancy tracking の実務的背景

現在稿には IoT/BMS による real-time sensing の説明がある。Result に接続するなら、以下のように「高解像度 tracking の価値と負荷を同時に評価する」書き方にする。

追記候補:

```tex
Although real-time occupancy data are increasingly available, their practical value depends on whether the additional occupant-composition information produces enough comfort benefit to justify the sensing, integration, and control burden. Therefore, this study evaluates both the comfort improvement and the operational implications of using higher-resolution \acp{gcm}.
```
->追記

#### 4. Research gap / objective

現在稿の Results は、RT-GCM/DGCM が fixed 24 C baseline より高い mean comfort probability を維持する一方、RT-GCM は setpoint adjustment magnitude と action-needed window ratio で運用負荷を生む、という構成。

Introduction の research question は以下に寄せる。

```tex
This study asks when higher-resolution aggregation of individual comfort information improves predicted comfort in shared office spaces, and what operational burden is introduced by real-time occupant-composition updates.
```
->追記

具体的な目的は以下の 3 点で整理する。

```tex
Specifically, the analysis compares \ac{sgcm}, \ac{dgcm}, and \ac{rtgcm} policies in terms of:
(1) mean comfort probability and improvement relative to a fixed \qty{24}{\celsius} baseline;
(2) the setpoint adjustment magnitude required by the \ac{rtgcm}; and
(3) the relationship between occupancy dynamics, especially \ac{utr}, and the frequency of actionable control updates.
```
->追記

## Chapter 3: Method

### 確認結果

多くの field-data detail は現在稿に既に記載済み。

既に記載済み:

- The GEAR が Singapore の R&D and administrative office building であること。
- 2025-09-29 から 2025-10-24 の 4 週間。
- 3rd to 6th floors が対象であること。
- shared-office and static seating work styles が混在すること。
- central air conditioning system, air handling units, dedicated outdoor air handling units, VAV, zone air temperature setpoint。
- ANSI/ASHRAE Standard 55:2023 Appendix L。
- 20 minutes after room entry exclusion。
- six prompts per workday。
- 2608 responses。
- \(\ac{ti}\), \(\ac{rh}\), BMS and compact sensors。
- \(\qtyrange{22}{27}{\celsius}\), \(\qty{1}{\celsius}\) steps, randomized order, morning/afternoon setpoint differences。
- 45 invited participants, NUS-IRB-2025-498, informed consent, anonymization, 39 participants used。
- SGCM/DGCM/RT-GCM の基本定義。
- subgroup size \(K\) と realized occupancy count \(N_{r,t}\) の区別。
- merged "No change" probability curve を最大化する setpoint selection。

### 追記・修正が必要な内容

#### Target building and spaces

追加する内容:

- Kajima Corporation が The GEAR を運営していること。
- room names を anonymized names に統一すること。
->追記

修正方針:

- 現在稿の room names はコメントアウトし、本文は参照稿側の anonymized names に統一する。
- ただし、Results/Discussion で `Katris`, `KD`, `ILYA` が残っている場合は、同じ anonymized names に合わせて修正する。

置換候補:

```tex
The data collection was conducted at The GEAR, an R\&D and administrative office building located in Singapore and operated by Kajima Corporation, from 29 September to 24 October 2025 (4 weeks).
The 3rd to 6th floors, which accommodate a mix of shared-office and static seating work styles depending on departmental roles, were the target areas for data collection.
Data collection was limited to the following rooms: 3F: Admin Office A, Admin Office B; 5F: R\&D Office, Admin Office C, Shared Office 1, Shared Office 2; 6F: Design Office.
% Data collection was limited to the following rooms: 3F: Office 3A, Office 3B; 5F: Katris Office, KD Office, Shared Office 1, Shared Office 2; 6F: ILYA Office.
```
->追記修正してOK

#### HVAC system

現在稿にほぼ記載済み。必要なのは表記調整のみ。

修正候補:

```tex
The target zones are served by a central air-conditioning system consisting of air-handling units and dedicated outdoor air-handling units, using variable air volume units capable of individual zone temperature and ventilation control.
The controlled variable is the zone air temperature setpoint.
```
->表記調整OK

#### Thermal comfort survey

現在稿に主要内容は記載済み。追記不要。

必要なら、以下の文を `Indoor Environmental Measurements` ではなく `Thermal Comfort Survey` 側に移動すると構成が自然。

- setpoint cycling between 22 and 27 C
- randomized order
- morning/afternoon setpoint differences

理由: これは environmental measurement というより、survey response variability を確保する experimental protocol であるため。

#### Environmental measurements

追加する内容:

- compact sensor model。

追記候補:

```tex
The compact sensors were LR8514 units (HIOKI E.E. Corporation, Nagano, Japan).
```
->表記調整OK

#### Participant recruitment and ethics

内容は記載済み。英語表現だけ修正する。

修正候補:

```tex
Informed consent was obtained from all participants prior to the study.
```

```tex
Survey answers and location tracking data from 39 participants were used in the final analysis.
```
->表記調整OK

#### Three-level time-resolution GCMs

現在稿に定義は記載済み。補強として「simulation case ごとに固定」という点を SGCM に加える。

追記候補:

```tex
Within each simulation trial, the \ac{sgcm} remains fixed for the sampled room-member group over the simulation period.
```
->不要

#### Agentic simulation

現在稿には数式レベルで既に入っているが、読み手向けの要約文を追加するとよい。

追記候補:

```tex
For all three \ac{gcm}-based policies, the policy setpoint is selected by maximizing the merged ``No change'' probability curve of the corresponding group. The difference between policies is therefore not the setpoint-selection rule itself, but the temporal resolution at which the group is defined.
```
->追記

#### Policy naming

現在稿 Method では `Dynamic` と `RT` が混在している。

修正対象:

- `\mathrm{policy}\in\{\mathrm{Static},\mathrm{Daily},\mathrm{Dynamic}\}` は `RT` に統一。
- 本文では `real-time policy` または `\ac{rtgcm}` と書く。
- `Dynamic` は GCM 名として使わない。
->統一

## Chapter 4: Results

### 参照稿から直接移植する結果はない

現在稿 Results は simulation results に集中する。

### 修正必要な内容

以下は実際に現在稿で確認されたため修正する。

#### Comfort section

修正対象:

```tex
The \ac{rtgcm} produced the highest mean comfort probability for every room and subgroup size,followed by \ac{dgcm} and then \ac{dgcm}.
```

修正候補:

```tex
The \ac{rtgcm} produced the highest mean comfort probability for every room and subgroup size, followed by the \ac{dgcm} and then the \ac{sgcm}.
```
->修正

修正対象:

```tex
The mean comfort achievement ratio across rooms ranged ...
```

修正候補:

```tex
The mean comfort probability across rooms ranged approximately ...
```
->修正

Figure caption 修正:

```tex
\caption{Mean comfort probability under different comfort-representation controls}
```
->修正

#### Control adjustment section

修正対象:

- `Effect of \ac{rtgcm} to Control Adjustment`
- `effect of \ac{rtgcm} to control adjustment`
- `Since {sgcm} and {dgcm} assumes`
- `comtrol`
- `maginitude`
- `\qty{1.0}{\celsius}even`

修正候補:

```tex
\subsection{Effect of \ac{rtgcm} on control adjustment}
```

```tex
This subsection investigates the control-adjustment burden introduced by the \ac{rtgcm}.
Because the \ac{sgcm} and \ac{dgcm} use coarser occupant-composition representations, frequent setpoint updates are primarily required under \ac{rtgcm}-based control.
```
->修正

#### UTR / action frequency section

修正対象:

```tex
\caption{Relationship between daily occupancy-count standard deviation and the ratio of required control actions}
```

修正候補:

```tex
\caption{Relationship between 30-minute user turnover rate and action-needed window ratio}
```
->修正

修正対象:

```tex
\caption{Distribution of temperature adjustment magnitudes under dynamic group control}
```

修正候補:

```tex
\caption{Representative 30-minute user turnover rate transitions by room and weekday}
```
->修正不要。そのまま

本文修正候補:

```tex
\autoref{fig:CtrlWindowRatio} shows the relationship between \ac{utr} and the probability that a 30-minute decision window requires a temperature adjustment of at least \qty{0.5}{\celsius}.
As \ac{utr} increases, the action-needed window ratio also increases; when \ac{utr} reaches approximately 0.7--0.8, the ratio approaches \qty{90}{\percent}.
```

```tex
\autoref{fig:UTRexamples} shows representative mean \ac{utr} transitions by time of day and weekday for the four offices.
```
->修正不要。そのまま

## Chapter 5: Discussion

### 確認結果

現在稿には Jung et al. との接続はあるが、文章が粗く、Ono et al. との接続、dynamic occupancy metrics の意味、practical implication、limitations が不足している。

Discussion は小修正より、以下の 4 要素で再構成するのがよい。

### 追記・修正案

#### 1. Group size and preference averaging

現在稿の内容を以下の方向で整理する。

- Jung et al. は occupant number が増えるほど PCM integration の利点が収束することを示した。
- 現在稿でも、SGCM の fixed 24 C baseline に対する improvement は subgroup size 5--7 程度で小さくなる。
- RT-GCM/DGCM は larger subgroup size でも positive improvement を維持するが、subgroup size や mean occupancy が大きくなるほど individual preference differences は averaged out される。
- したがって、RT-GCM の価値は単なる room size ではなく、realized occupancy と occupant composition dynamics に依存する。

追記候補:

```tex
These results are consistent with prior multi-occupant comfort-control studies showing that the benefit of integrating personal comfort information tends to diminish as more occupants are aggregated within a single thermal zone. As the realized group becomes larger, individual thermal preferences are averaged within the group representation, reducing the difference among alternative aggregation resolutions.
```
->追記

#### 2. GCM resolution and HVAC control resolution

Ono et al. との接続を追加する。

追記候補:

```tex
This finding also relates to the resolution-mismatch argument reported by \mycite{ono_effects_2022}\cite{ono_effects_2022}. A high-resolution comfort representation can only be useful in practice when the available \ac{hvac} control resolution can respond to the corresponding setpoint differences. The present results show this trade-off from the operational side: the \ac{rtgcm} can improve mean comfort probability, but it also introduces larger and more frequent setpoint adjustments.
```
->追記

#### 3. Dynamic occupancy metrics の意味

UTR の実務的意味を追加する。

追記候補:

```tex
Mean occupancy and occupancy variability describe how many people are present and how strongly the count fluctuates, whereas \ac{utr} captures who is replaced over short time intervals. This distinction is important for \ac{gcm}-based control because the preferred group setpoint can change even when the occupancy count remains similar, if the occupant composition changes.
```
->追記

#### 4. Practical implication

追記候補:

```tex
These findings suggest that \ac{rtgcm}-level control should not be adopted solely because real-time tracking is available. It is most valuable in sparse or highly variable shared-office conditions where occupant composition changes frequently. In contrast, a \ac{dgcm} may provide a practical compromise when daily attendance differs from regular membership but within-day turnover is moderate, while a \ac{sgcm} may be sufficient when occupancy is stable or group size is large enough for individual differences to average out.
```
->追記

### Limitations

現在稿には明示的な limitations subsection がないため追加する。

追記候補:

```tex
\subsection{Limitations}
Several limitations should be noted. First, the data come from one office building and one observation period, so the numerical thresholds for subgroup size, mean occupancy, and \ac{utr} may depend on building use, occupant population, room size, and survey protocol. Second, the agentic simulation reassigns \ac{pcm} profiles to observed location-log agents. This increases scenario coverage but does not represent the actual person-specific coupling between movement patterns and comfort preferences. Third, comfort evaluation is based on predicted ``No change'' probability rather than direct closed-loop field operation. Energy consumption, \ac{hvac} response delay, actuator constraints, and occupant adaptive behavior were not fully evaluated. Finally, real-time tracking availability does not automatically imply deployability; privacy, sensing reliability, and integration cost remain practical constraints.
```
->追記

## Chapter 6: Conclusion

### 確認結果

現在の `ch6-Conclusion.tex` は generic contribution 文のみで、現在稿の結果を反映できていない。

### 追記候補

```tex
This study investigated how the temporal resolution of \ac{gcm} aggregation affects predicted comfort and control burden in dynamically occupied shared offices. Three \acp{gcm} were compared: a \ac{sgcm} based on regular room members, a \ac{dgcm} based on daily attendees, and a \ac{rtgcm} based on occupants present at each control decision window.

Using field survey data and reconstructed location logs, the agentic simulation showed that higher-resolution \acp{gcm} can improve mean comfort probability relative to a fixed \qty{24}{\celsius} baseline and the \ac{sgcm}. The advantage of the \ac{rtgcm} was strongest under sparse or dynamically changing occupancy conditions. At the same time, the \ac{rtgcm} introduced operational demands, reflected in setpoint adjustment magnitude and the action-needed window ratio.

These findings indicate that high-resolution occupancy tracking should be deployed selectively, based on occupancy metrics such as mean occupancy, subgroup size, occupancy variability, and \ac{utr}. Future work should include closed-loop field tests, energy analysis, \ac{hvac} dynamics, privacy-aware sensing implementation, and longer deployments across different office types.
```
->追記

## Appendix

### Thermal comfort survey items

現在稿 Appendix には table はあるが、clo-value calculation はないため追記する。

追記候補:

```tex
The following clothing insulation values were used for clo-value calculation based on the selected clothing option: short-sleeve shirt and trousers, 0.57 clo; long-sleeve shirt and trousers, 0.61 clo; and long-sleeve shirt, jacket and trousers, 0.96 clo.
```
->追記

Caption 修正候補:

```tex
\caption{Items in the thermal comfort survey}
```
->修正

### Tracking adoption cases

重要な確認点:

- `chapters/chap-appendices.tex` では `\autoref{table:OccuTrack}` を参照しているが、該当 table はコメントアウトされている。
- `ch1-Intro.tex` でも `\autoref{table:OccuTrack}` を参照している。

したがって、以下のどちらかを行う。

1. `OccuTrack` table を Appendix で有効化する。
2. 本文と Appendix の `\autoref{table:OccuTrack}` 参照を削除または一般表現に変える。

現在稿の real-time tracking 背景を支えるなら、1 の table 有効化がよい。

## 図表・ファイル

移植・利用候補:

- `pic/chap-appe/ThermalComfort.tex`: 既に使用中。
- `pic/chap-appe/TrackingEx.tex`: table を有効化するなら使用。
- `pic/chap-appe/ExOccuStudy.tex`: 既に使用中。

移植しないもの:

- 参照稿側の別テーマ専用 method figures。
- 参照稿側の別テーマ専用 result figures/tables。
- 参照稿側の別テーマ専用 appendix tables。

## 表記・整合性メモ

### 統一するもの

- `RTGCM`, `RT-GCM`, `Real-time`, `Dynamic` が混在している。本文では `\ac{rtgcm}`、説明文では `real-time GCM` に統一する。
- `Dynamic` policy と書く箇所は、GCM 名としては `RT-GCM` に寄せる。
- `comfort achievement ratio` は `mean comfort probability` に統一する。
- 現在稿では `subgroup size K` に統一し、参照稿側の別テーマ用 `target session size k` は持ち込まない。
- Room names は anonymized names に統一する。

### 要検討

- `subgroup size K` と realized occupancy count `N_{r,t}` は現在稿 Method で既に区別されている。Results/Discussion でも同じ区別を維持する。
- `RPP` と `DPP` は acronym を増やしすぎるより、本文では `regular room members` と `daily attendees` と書くほうが読みやすい。数式内だけ \(R_r\), \(A_{r,d}\), \(S_{r,t}\) を使う。

## 優先作業順

1. `ch1-Intro.tex` の構成整理。
2. Introduction に Dynamic Occupancy と GCM resolution の research gap を追加。
3. `ch3-Method.tex` の room names を anonymized names に統一し、Kajima Corporation と LR8514 情報を追加。
4. `Three-level time-resolution GCMs` と `Agentic simulation` に、三つの GCM policy は group definition が異なるだけで setpoint-selection rule は共通であることを追記。
5. Method/Results の `Dynamic` policy 表記を `RT` / `\ac{rtgcm}` に統一。
6. Results の typo/caption/outcome wording を修正。
7. `chap-appendices.tex` に clo-value calculation を追記し、ThermalComfort caption を修正。
8. `OccuTrack` table を有効化するか、参照を削除する。
9. Discussion に group size, preference averaging, GCM-control resolution trade-off, UTR の実務的意味、limitations を追加。
10. Conclusion に dynamic occupancy 条件に応じた SGCM/DGCM/RT-GCM の使い分けを反映。


## 2. June 21st self-review
### Introduction
- 1.2と1.4は内容が近いため、現在の1.3→1.2と1.4を合体したSubsectionとし、合体したセクション内での重複は削除。まずは重複しているものをリストアップ。
- 1.1は一般論としての3Layerの話が長い。現在の説明文はコメントアウトして、圧縮した文章を作成。
- Depite growing recognition- の文章はOCCの一般論の近くに置いて、前後の文章の流れをよくしたい。
- (e.g., through technologies such as-)の文章は長いので簡潔に。
- Dynamic-occupancy-based controlのsubsectionの中のHistorically, tracking personal-level の文章も以前にあったはず。重複はなくす。前の文章の箇所に動かし統合する。
- 同じsubsectionで、This section focuses onは長いレヴュー論文のような書き方。簡潔に前後の文章を繋げて導入する。
- その他、Repetitiveな内容はやめて簡潔かつこの論文での目的説明の流れをスムーズに繋がるように、それぞれの文章や段落間での流れが自然になるように。
- 基本的にはOK。Refは論文の足元を固めるものとして残しておきたいので、Refが入っている文章からはその部分の内容を残す。

### 追加コメント反映後の前提

- `ch2-Review.tex` は現在使っていないため、重複確認の比較対象から外す。Introduction 内部での重複だけを整理対象にする。
- 引用付きの文は、単に削除せず、引用が支えている主張を圧縮して残す。特に ABW/dynamic occupancy、real-time sensing、multi-occupant OCC、Jung/Ono/Lei への接続は Introduction の根拠として残す。
- ただし、同じ引用・同じ主張が Introduction 内で複数回出る場合は、最も流れが自然な subsection に集約する。

### Introduction の subsection 別修正案

修正後の推奨構成:

1. `Occupant-centric control and shared-space comfort aggregation`
2. `Dynamic occupancy and real-time tracking in activity-based working environments`
3. `Shared-space GCM resolution under dynamic occupancy`
4. `Focus of the research`

#### 1.1 `Occupant-centric control`

コメント反映方針:

- 3-layer 説明は短くするが、Sensing / Learning / Control の概要は残す。
- `Despite growing recognition...` は OCC の一般論の最後に置き、次の ABW / tracking 技術の話へつなげる。
- shared-space では isolated \acp{pcm} だけでは足りず、room-level \ac{gcm} が必要になる、という導入までをここに置く。

圧縮元の文章:

```tex
In recent years, \ac{occ} has emerged as a promising alternative \ac{hvac} strategy that decides control actions by considering individual thermal preferences \cite{soleimanijavid_challenges_2024}. 
In definition, \ac{occ} leverages sensor data and \acp{pcm} to adjust \ac{hvac} operation, potentially improving both thermal comfort and energy efficiency as examined by existing studies \cite{xie_review_2020}.
In this context, IEA EBC Annex 79 defines \ac{occ} as an "occupant-in-the-loop" approach that seeks to provide optimal and personalized conditions rather than imposing fixed settings\cite{wagner_international_2024}.

As some existing research has exhibited, the general \ac{occ} framework is composed of a combination of three components, namely “Sensing,” “Learning,” and “Control” layers \cite{soleimanijavid_challenges_2024,xie_review_2020}.
In the sensing layer, information is gathered from various sources, such as environmental data, occupants’ comfort sensation, or occupants’ attendance. 
In the learning layer, prediction models on environmental preference or occupancy are developed.
In the control layer, considering these occupancy and preference information, control actions are decided based on tailored algorithms.
Among these components, the thermal preference model and its integration into the control layer have a significant impact on occupant comfort, hence they should be carefully considered as a framework.

In shared office spaces, however, \ac{occ} cannot rely only on isolated \acp{pcm}, because a single room-level \ac{hvac} setpoint must represent multiple occupants at the same time.
This makes the construction of a \ac{gcm}, which aggregates individual comfort information into a room-level representation, a central design issue for shared-space \ac{occ}.
The key question is not only how accurately individual \acp{pcm} predict comfort, but also which occupant set should be represented when the room-level control decision is made.
Despite growing recognition in the industry and active framework development in simulations, the number of real-world \ac{occ} applications in buildings remains limited \cite{soleimanijavid_challenges_2024}. 
```

修正案:

```tex
\subsection{Occupant-centric control and shared-space comfort aggregation}

In recent years, \ac{occ} has emerged as a promising \ac{hvac} strategy that uses occupant information to support more individualized building operation \cite{soleimanijavid_challenges_2024}.
IEA EBC Annex 79 defines \ac{occ} as an ``occupant-in-the-loop'' approach that seeks to provide optimal and personalized conditions rather than imposing fixed settings \cite{wagner_international_2024}.
In typical \ac{occ} frameworks, sensing collects information such as environmental conditions, comfort feedback, and occupancy; learning develops preference or occupancy models from these data; and control translates the model outputs into \ac{hvac} actions \cite{soleimanijavid_challenges_2024,xie_review_2020}.
Among these functions, the connection between personal comfort information and the control decision is especially important because it determines how individual preferences affect the final setpoint.

In shared office spaces, however, \ac{occ} cannot rely only on isolated \acp{pcm}, because a single room-level \ac{hvac} setpoint must represent multiple occupants at the same time.
This makes the construction of a \ac{gcm}, which aggregates individual comfort information into a room-level representation, a central design issue for shared-space \ac{occ}.
The key question is therefore not only how accurately individual \acp{pcm} predict comfort, but also which occupants should be represented when a room-level control decision is made.
Despite growing recognition in the industry and active framework development in simulations, real-world \ac{occ} applications in buildings remain limited \cite{soleimanijavid_challenges_2024}.
```

接続確認:

- 前段の PMV / one-size-fits-all 批判から、OCC の定義へ入れる。
- 最後の `real-world applications remain limited` は、次の subsection で「では、近年の ABW と tracking 技術により何が変わったか」へつながる。
- 以前の圧縮案より長いが、Sensing/Learning/Control の概要を残すため、一般論から shared-space GCM への橋渡しが読みやすい。

#### 1.2 `Thermal comfort consideration with rising trend of Activity-based working` + 1.3 `Treating dynamic occupancy information`

コメント反映方針:

- 1.2 と 1.3 は統合し、ABW / hybrid work、occupant composition、real-time tracking、OCC への応用機会、実務負荷の順に説明する。
- 1.4 冒頭にあった flexible work / static setpoint の説明はここへ集約し、同じ背景説明を後段で繰り返さない。
- Occupancy fluctuation の引用は削除せず、ABW による occupancy density / distribution 変化の根拠として残す。
- Occupancy prediction の段落は今回の主題から外れるため、本文ではコメントアウト候補にする。
- Real-time tracking 技術の列挙だけで終わらせず、OCC への応用機会が生まれていることを 1 文でつなぐ。

統合元の文章:

```tex
\subsection{Thermal comfort consideration with rising trend of Activity-based working}
The rise of remote work and \ac{abw} following the COVID-19 pandemic has further complicated thermal comfort control \cite{marzban_review_2023}. 
Dynamic working environments are characterized by dynamic occupancy patterns. 
Individuals move between different workspaces throughout the day, leading to significant fluctuations in occupancy density and distribution within a single zone\cite{motuziene_office_2022,pan_environmental_2025,huang_space-matching_2025,chang_statistical_2013,levene_problem_2020}.
In such spaces, dynamic occupancy should be understood not only as a change in the number of occupants, but also as a change in who is present.
Even when the occupancy count is similar, the thermal preferences represented by the present group may differ as occupants arrive, leave, or move between rooms.
When considering such dynamic occupancy, it becomes extremely challenging to maintain consistent thermal conditions that satisfy all occupants using traditional, static control methods.
A static approach, optimized for a specific occupancy scenario, will inevitably lead to discomfort for some individuals when the actual occupancy deviates from that scenario.
This can result in reduced occupant satisfaction and potentially increased energy consumption as occupants attempt to individually adjust their local environment.

\subsection{Treating dynamic occupancy information}
To incorporate occupancy information in \ac{occ} frameworks, two main approaches can be identified: prediction-based methods and real-time sensing. 
Many studies have attempted to predict occupancy patterns using historical data and machine learning techniques. 
However, as noted in prior research \cite{goyal_occupancy-based_2013}, such prediction methods often entail high computational costs, may be more expensive than real-time sensing, and may not offer sufficient accuracy or reliability.

On the other hand, recent advances in IoT and sensor technologies have made it increasingly feasible to obtain real-time occupancy data with relatively low cost and high granularity (e.g., through technologies such as passive infrared sensors, CO$_2$ sensors, and Wi-Fi-based tracking systems) \cite{soleimanijavid_challenges_2024, zafari_survey_2019, brambilla_potential_2021}.
Real-time sensing may enable adaptive control strategies that respond immediately to the presence and number of occupants, which is particularly valuable in shared and flexible workspaces. 
The availability of real-time data fundamentally shifts the design paradigm of occupant-centric systems from predictive to responsive, thereby enhancing both energy efficiency and thermal comfort performance.

Especially after the COVID-19 and raise of hybrid working, the need of real-time tracking of employee became highly focused.
\autoref{table:OccuTrack} in appendix exhibits examples of Japanese office projects that implement real-time tracking using IoT data.
As such examples show, recent technology enables office management dealing with detailed individual tracking data.

\subsection{Complex occupancy in multi-shared spaces}
Modern flexible work arrangements have led to highly dynamic and variable occupancy patterns in office environments. 
Conventional \ac{hvac} systems, which often rely on fixed, static temperature setpoints (e.g., based on the \ac{pmv} model), frequently fail to respond effectively to these fluctuations. 
This mismatch can result in both occupant discomfort and unnecessary energy consumption\cite{ono_effects_2022}.
```

修正案:

```tex
\subsection{Dynamic occupancy and real-time tracking in activity-based working environments}

The rise of remote and hybrid work has increased the use of \ac{abw} and other flexible office arrangements \cite{marzban_review_2023}.
In such workplaces, occupants move between different spaces throughout the day, causing fluctuations in occupancy density and distribution within a zone \cite{motuziene_office_2022,pan_environmental_2025,huang_space-matching_2025,chang_statistical_2013,levene_problem_2020}.
Dynamic occupancy should therefore be understood not only as a change in the number of people in a room, but also as a change in who is present.
Even when the occupancy count is similar, the thermal preferences represented by the present group may differ as occupants arrive, leave, or move between rooms.
This makes static temperature control less reliable, because a condition optimized for one attendance pattern may not represent another.

Recent IoT and building-management technologies have made room- or occupant-level occupancy data more accessible through sources such as PIR, CO$_2$, and Wi-Fi-based sensing \cite{soleimanijavid_challenges_2024,zafari_survey_2019,brambilla_potential_2021}.
\autoref{table:OccuTrack} provides examples of office projects that use IoT data for individual-level real-time occupancy tracking.
Therefore, opportunities are emerging to use such data in \ac{occ} systems that respond to changes in the occupants currently present.
At the same time, the practical value of real-time occupant-composition data depends on whether the comfort benefit justifies the sensing, integration, privacy, and control burden.
```

コメントアウト候補:

```tex
% To incorporate occupancy information in \ac{occ} frameworks, two main approaches can be identified: prediction-based methods and real-time sensing.
% Many studies have attempted to predict occupancy patterns using historical data and machine learning techniques.
% However, as noted in prior research \cite{goyal_occupancy-based_2013}, such prediction methods often entail high computational costs, may be more expensive than real-time sensing, and may not offer sufficient accuracy or reliability.
```

接続確認:

- 1 段落目は ABW -> dynamic occupancy -> static control の限界までを扱う。
- 2 段落目は sensing 技術 -> OCC への応用機会 -> burden の評価必要性へ進む。
- `Therefore, opportunities are emerging...` を追加することで、tracking 技術の列挙から研究目的へ急に飛ばない。
- Prediction-based methods は今回の主題から外れるため本文からは外し、必要ならコメントアウトで保持する。

#### 1.4 `Complex occupancy in multi-shared spaces` + 1.5 `Dynamic-occupancy-based control`

コメント反映方針:

- 1.4 と 1.5 は統合し、dynamic occupancy の一般説明ではなく、shared-space \ac{gcm} / control-resolution 問題に集中する。
- `This section focuses on...` はレビュー章の導入のように見えるため削除する。
- Jung / Ono / Lei への接続は、Introduction の根拠として残す。
- `table:OccuIntegration` は `ch2-Review.tex` ではなく Introduction 側の根拠表として残す。ただし、本文中の table description は短くする。
- `Occupancy Adaptation` column の細かい読み方説明は Introduction では重いため削る。

統合元の文章:

```tex
For actual building operation scenarios, both occupancy resolution and comfort model resolution must be considered.

Effective \ac{occ} systems require determining proper control resolution and comfort model resolution depending on the room/building usage.
Existing \ac{occ} research has largely focused on developing and validating \acp{pcm} and control algorithms in single-occupancy settings \cite{park_critical_2019, jung_human---loop_2019}.
While these studies demonstrate the potential of \ac{occ}, few have tried to address the complexities of shared spaces.
Shared workspaces present a significant challenge for \ac{occ}, as multiple occupants with potentially conflicting thermal preferences must be accommodated simultaneously \cite{xie_review_2020}.
Simply averaging preferences or applying a single \ac{pcm} is unlikely to satisfy everyone, and may even exacerbate discomfort for some individuals.
\mycite{jung_energy_2020} investigated how the number of occupants in a zone affects \ac{hvac} system performance, considering both comfort and energy consumption.
They found that both performances could decrease as the number of occupants increases, and results could differ depending on the methods used to integrate individual comfort models \cite{jung_energy_2020}.
\mycite{ono_effects_2022} investigated how the resolution of thermal comfort models and \ac{hvac} control settings should match.
They found that mismatches between comfort model resolution and control resolution, especially when using detailed comfort models with simpler \ac{hvac} systems, may reduce effectiveness and decrease occupant satisfaction \cite{ono_effects_2022}.

\subsection{Dynamic–occupancy–based control}
As noted in reviews \cite{xie_review_2020}, integrating diverse preferences across multiple occupants remains underexplored.
This section focuses on how comfort models are incorporated into control.
In some studies on the effectiveness of \ac{occ}, such as \cite{jung_energy_2020}, occupancy is often assumed to be static.  
However, in today’s dynamic working environments—where hybrid working, combining remote and office-based work, has become commonplace\cite{redmond_rise_nodate} —this static assumption may underestimate the impact of occupancy characteristics.
\autoref{table:OccuIntegration} compares field studies that integrate multiple \acp{pcm} within the same control zone.
The “Occupancy Adaptation” column indicates each framework’s ability to handle different occupancy patterns; “dynamic” adjusts to real–time combinations, while “static” assumes fixed configurations. 
Only \cite{lei_practical_2022} considers transitions among combinations by pre–training multiple RL models for frequent patterns—data–and compute–intensive.

\begin{table}[pos=!htbp]
  \centering
  \input{pic/ch2-Review/ModelIntegration.tex}
  \caption{Field OCC studies integrating multiple personal comfort models}
  \label{table:OccuIntegration}
\end{table}

While these studies have investigated multi-occupancy scenarios, a significant limitation is that most assume a static occupant attendance configuration, meaning they do not account for occupants arriving and leaving dynamically \cite{lee_implementation_2019,li_indoor_2019,li_personalized_2017,li_indoor_2023,aguilera_thermal_2019,li_experimental_2021}.

A notable exception is the work by Lei et al.~(2022), which addressed dynamic occupancy in a shared-lab office \cite{lei_practical_2022}. 
They employed multiple reinforcement learning models tailored to the most common combinations of occupants.
However, this approach is computationally demanding as it requires maintaining and training numerous models.

Historically, tracking personal–level occupancy was difficult in typical \ac{bms}; this has changed with IoT systems enabling occupancy/location tracking \cite{soleimanijavid_challenges_2024}.
Thus, \autoref{table:OccuIntegration} underlines the potential of real–time occupancy for \ac{occ} frameworks as an underexplored domain.
Although real-time occupancy data are increasingly available, their practical value depends on whether the additional occupant-composition information produces enough comfort benefit to justify the sensing, integration, and control burden.
Therefore, this study evaluates both the comfort improvement and the operational implications of using higher-resolution \acp{gcm}.
```

修正案:

```tex
\subsection{Shared-space GCM resolution under dynamic occupancy}

For shared-space \ac{occ}, dynamic occupancy raises a second issue: the controller must decide how individual comfort information should be aggregated for a room-level setpoint.
Existing \ac{occ} research has largely focused on developing and validating \acp{pcm} and control algorithms in single-occupant settings, while shared spaces with multiple occupants remain less explored \cite{park_critical_2019,jung_human---loop_2019,xie_review_2020}.
In shared workspaces, multiple occupants with potentially conflicting thermal preferences must be accommodated simultaneously, and simply averaging preferences or applying a single \ac{pcm} may fail to represent the group.
\mycite{jung_energy_2020} showed that the number of occupants in a zone can affect both comfort and energy performance, and that results depend on how individual comfort models are integrated.
\mycite{ono_effects_2022} further showed that mismatches between comfort-model resolution and control resolution may reduce control effectiveness and occupant satisfaction.
These findings indicate that shared-space \ac{occ} requires attention to both comfort aggregation and room-level control resolution.

\autoref{table:OccuIntegration} compares field studies that integrate multiple \acp{pcm} within the same control zone.
Most existing multi-occupant studies assume static occupant attendance configurations and do not account for occupants arriving and leaving dynamically \cite{lee_implementation_2019,li_indoor_2019,li_personalized_2017,li_indoor_2023,aguilera_thermal_2019,li_experimental_2021}.
Lei et al.~\cite{lei_practical_2022} addressed dynamic occupancy using multiple reinforcement-learning models for frequent occupant combinations, but such an approach can be data- and compute-intensive.
Therefore, a simpler practical question remains: when is static, daily, or real-time aggregation of individual comfort information sufficient for room-level control?

\begin{table}[pos=!htbp]
  \centering
  \input{pic/ch2-Review/ModelIntegration.tex}
  \caption{Field OCC studies integrating multiple personal comfort models}
  \label{table:OccuIntegration}
\end{table}
```

接続確認:

- 1.2 が「occupant composition が変わる」と説明しているため、ここでは dynamic occupancy の一般説明を繰り返さず、「その結果、GCM aggregation が問題になる」と受ける。
- Jung/Ono は control/comfort resolution の根拠、Lei は dynamic occupancy を扱った例外として残る。
- `table:OccuIntegration` は削除せず、field studies の根拠として残す。
- Table の説明は短くし、`Occupancy Adaptation` column の読み方説明は本文からは外す。

#### 1.6 `Focus of the research`

コメント反映方針:

- 直前 subsection の `static, daily, or real-time aggregation` の practical question を受けて、研究目的へ入る。
- Gap の再説明は避け、目的、3 種の \acp{gcm}、評価対象に絞る。
- Jung / Ono の引用は、group size と control granularity に基づく研究の足元として残す。
- 既存の `Specifically, the analysis compares...` 以下はそのまま続ける。

圧縮元の文章:

```tex
\subsection{Focus of the research}
As highlighted in the background, the practical application of \ac{occ} in shared office spaces is still limited by the common assumption of static occupancy.
However, occupant composition in a room can change across longer-term, daily, and real-time timescales.
This raises a practical question: at what occupancy conditions does higher-resolution aggregation of individual comfort information become worthwhile for room-level control?
This study asks when higher-resolution aggregation of individual comfort information improves predicted comfort in shared office spaces, and what operational burden is introduced by real-time occupant-composition updates.

To address this question, this study focuses on three group comfort models that differ in the timescale at which individual \acp{pcm} are aggregated: a static model based on regular room members, a daily model based on a day's attendees, and a real-time model based on the occupants currently present.
Building on prior work that investigated the impact of group size and control granularity \cite{ono_effects_2022,jung_energy_2020}, this study introduces temporal occupancy variability as a key dimension of analysis.
Using field data from real office spaces, the study investigates how the relative benefit of these models changes with occupancy conditions such as group size, occupancy variability, and user turnover.
```

修正案:

```tex
\subsection{Focus of the research}

Based on this background, this study evaluates when higher-resolution aggregation of individual comfort information improves predicted comfort in shared offices, and what operational burden is introduced by real-time occupant-composition updates.
Three \acp{gcm} are compared: a \ac{sgcm} based on regular room members, a \ac{dgcm} based on daily attendees, and a \ac{rtgcm} based on occupants present at each control decision window.
Building on prior work on group size and control granularity \cite{ono_effects_2022,jung_energy_2020}, the analysis introduces temporal occupancy variability as a key dimension of shared-space \ac{occ}.
Using field data from real office spaces, the study relates model performance to subgroup size, mean occupancy, occupancy variability, and \ac{utr}.
```

既存の以下はそのまま続ける:

```tex
Specifically, the analysis compares \ac{sgcm}, \ac{dgcm}, and \ac{rtgcm} policies in terms of:
(1) mean comfort probability and improvement relative to a fixed \qty{24}{\celsius} baseline;
(2) the setpoint adjustment magnitude required by the \ac{rtgcm}; and
(3) the relationship between occupancy dynamics, especially \ac{utr}, and the frequency of actionable control updates.
```

接続確認:

- 直前 subsection の `static, daily, or real-time aggregation` を受けて、SGCM/DGCM/RT-GCM の説明に入る。
- `Based on this background` で前段との接続を明示するが、gap を再度長く説明しない。
- `Building on prior work...` は Jung/Ono の引用を保持し、Introduction 全体の論理的な足元を残す。

### Introduction の優先修正順

1. 1.1 を上記の再修正案に置換し、Sensing/Learning/Control の概要を残す。
2. 1.2 と 1.3 を統合し、prediction-based methods の段落はコメントアウトする。
3. 1.4 と 1.5 を統合し、`table:OccuIntegration` は Introduction 側に残す。
4. `This section focuses on...` は削除し、shared-space aggregation の問題文に置換する。
5. Focus of the research は目的・3 種の GCM・評価指標に絞り、既存の `Specifically...` は維持する。

### その他の Repetitive / 整合性問題

#### 1. `table:OccuIntegration` が Introduction と Review で重複

- `ch1-Intro.tex` 91--95 と `ch2-Review.tex` 136--140 で同じ table と label を使用している。
- ただし `ch2-Review.tex` は現在使っていないため、これは現時点ではコンパイル上の優先問題ではない。
- `table:OccuIntegration` は Introduction の論旨を支える根拠として Introduction 側に残す。
- table の前後説明は短くし、`Occupancy Adaptation` column の細かい読み方説明は削る。
- Jung/Ono/Lei と static/dynamic adaptation の論点は、table だけに頼らず本文でも引用付きで短く残す。

#### 2. `fig:Upd-Field` label が複数箇所で重複

- `ch2-Review.tex` 143--147: dynamic occupancy schematic。
- `ch2-Review.tex` 173--177: model update figure。
- `ch1-Intro.tex` 98--102 はコメントアウトされているが、復活させるとさらに重複する。

修正案:

- `ch2-Review.tex` は使っていないため、現時点では Introduction 内で復活させる図だけ注意する。
- Introduction のコメントアウト図を復活させる場合は `fig:dynamic_occupancy_schematic_intro` などに変更する。
- 図を使わないならコメントアウトブロックごと削除してよい。

#### 3. Introduction 内の dynamic-occupancy review がやや重い

- `ch2-Review.tex` は前提にしないため、Introduction 内に必要な引用と根拠は残す。
- ただし、table description や `The "Occupancy Adaptation" column...` のような表の読み方説明は Introduction では長い。
- Introduction は「既存研究は static multi-occupant assumption が多い」「Jung/Ono は group size や control/comfort resolution の根拠になる」「Lei et al. は動的 occupancy を扱う例外だが重い」「本研究は simple GCM resolution comparison に絞る」の 4 点を残す。

#### 4. Method の simulation 説明に局所的な繰り返し

- `ch3-Method.tex` 94--101 は sampling / random assignment / active set の説明。
- `ch3-Method.tex` 103--107 は GCM aggregation / setpoint selection の説明。
- 内容は必要だが、`setpoint was selected...` と `policy setpoint is selected...` が連続している。

修正候補:

```tex
For each simulated realization, the three \acp{gcm} were formed by averaging the individual ``No change'' probability curves of the assigned \acp{pcm}. The same setpoint-selection rule was then applied to all policies: the selected setpoint maximized the merged ``No change'' probability curve. Thus, the policies differ only in the temporal resolution at which the occupant group is defined.
```

#### 5. Results の UTR 説明で `marks` が反復

- `ch4-Results.tex` 85--90 で `\ac{utr} marks...` が複数回続く。

修正候補:

```tex
\autoref{fig:UTRexamples} shows weekday mean \ac{utr} transitions by time of day for four offices. The highest values generally appear during arrival and departure periods, around \DTMtime{08:00:00}--\DTMtime{08:30:00} and \DTMtime{17:30:00}--\DTMtime{18:00:00}. Shared offices and the R\&D Office also show elevated turnover around lunchtime. During office hours, Shared Office 1 and Shared Office 2 vary more dynamically than Admin Office C, while most non-peak periods remain around 0.2--0.5.
```

#### 6. Results figure caption に `dynamic group control` が残っている

- `ch4-Results.tex` 69: RT-GCM の図なので `dynamic group control` より `\ac{rtgcm}` がよい。
- `ch4-Results.tex` 102: `UTRexamples` の caption が temperature adjustment magnitude になっており内容と不一致。

修正候補:

```tex
\caption{Distribution of temperature adjustment magnitudes under \ac{rtgcm}-based control}
```

```tex
\caption{Representative 30-minute user turnover rate transitions by room and weekday}
```

#### 7. Discussion の Jung et al. 接続が二重

- `ch5-Discussion.tex` 5--8 で Jung et al. と現在結果の対応を説明。
- `ch5-Discussion.tex` 10--13 でほぼ同じ解釈をもう一度述べている。

修正案:

- 5--13 を 1 段落に統合し、Jung との接続、SGCM の収束、DGCM/RTGCM の残存 benefit をまとめる。

置換候補:

```tex
\mycite{jung_energy_2020}\cite{jung_energy_2020} showed that the comfort benefit of integrating personal comfort information tends to diminish as more occupants share the same thermal zone. The present simulation shows a similar tendency: the \ac{sgcm} improvement relative to the fixed \qty{24}{\celsius} baseline decreases with subgroup size and approaches zero around subgroup sizes of five to seven. However, the \ac{dgcm} and \ac{rtgcm} maintain positive improvement even at larger subgroup sizes, indicating that the value of higher-resolution \acp{gcm} depends not only on room-member size but also on realized occupancy and occupant-composition dynamics.
```

#### 8. Conclusion は現在よくまとまっているが、Intro と同じ表現が出やすい

- `higher-resolution \acp{gcm}`, `control burden`, `occupancy metrics` は必要語だが、Introduction と同じ文型にしない。
- Conclusion では research gap の再説明ではなく、findings と design implication に限定する。

修正方針:

- 現在の Conclusion は大きく直さなくてよい。
- もし短くするなら、最後の future work 文だけを `Future work should test these selection rules in closed-loop field operation...` のように具体化する。

### 全体の優先修正順

1. `ch2-Review.tex` は無視し、Introduction 単体で必要な引用・根拠を残す方針に切り替える。
2. 1.1 の 3-layer 説明を圧縮。
3. 1.2 + 1.3 を統合して ABW/dynamic occupancy/real-time sensing を 2 段落に整理。
4. 1.4 + 1.5 を統合して shared-space GCM resolution の gap に集中。
5. `table:OccuIntegration` は Introduction の根拠として残し、table description だけを短くする。
6. 1.6 を research objective と evaluated policies/metrics だけに圧縮。
7. Results/Discussion の局所的な反復と caption 不一致を修正。
