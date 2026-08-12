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

## 3. June 29th self-review
### Method
- The survey contents are summarized in Table4 として表示されているが、Appendix内のテーブルはAppendix内のテーブルとして番号表示をA.1などとしながらリンク先が表示されるようにしたい。
  - 確認: `chapters/ch3-Method.tex` では `\autoref{table:comfsurvey}` を参照しているため、表示が `Table 4` になるか `Table A.1` になるかは Appendix 側の table counter 設定に依存する。
  - 確認: `Draft_2026-Jan.tex` では `\input{chapters/chap-appendices}` の後に `\setcounter{table}{0}` と `\renewcommand{\thetable}{A.\arabic{table}}` が置かれているため、Appendix 内の既存 table には適用されていない可能性が高い。
  - 修正案: Appendix を読み込む前に table/figure counter と表示形式を切り替える。

```tex
\appendix
\label{appendix:XXX}
\setcounter{table}{0}
\setcounter{figure}{0}
\renewcommand{\thetable}{A.\arabic{table}}
\renewcommand{\thefigure}{A.\arabic{figure}}
\renewcommand{\theHtable}{A.\arabic{table}}
\renewcommand{\theHfigure}{A.\arabic{figure}}

\input{chapters/chap-appendices}
\FloatBarrier
```

  - 補足: `\theHtable` / `\theHfigure` は hyperlink anchor の重複回避用。本文 Table 1 と Appendix Table A.1 のリンクが混ざるリスクを下げる。
  - Method 本文の参照文は番号を直書きせず、現状通り `The survey contents are summarized in \autoref{table:comfsurvey}.` のままでよい。

->OK

- 2.3. Agentic simulationの冒頭、multiple realizationsが何のRealizationかわかるように、 Occupancy compositions and thermal preferenceのcombinationsのRealizationだとわかるようにしてほしい
  - 確認: 現在の `Using the prepared location-log agents and \acp{pcm}, multiple realizations were generated...` は、何を変えた realization なのかが少し抽象的。
  - 方針: `realization` は Monte Carlo 文脈では使えるが、最初に「occupancy composition と thermal-preference assignment の組み合わせ」と定義する。
  - 修正案:

```tex
Using the prepared location-log agents and \acp{pcm}, Monte Carlo trials were generated to represent different combinations of observed occupancy compositions and assigned thermal-preference profiles for each target room.
```

  - 以降は `simulated realization` より `Monte Carlo trial` に寄せると読みやすい。

->OK

- Each simulation trial  first sampled a subgroup...の部分は前後で繰り返しになっているのではないか。
  - 確認: 直前の文で「subgroups are repeatedly sampled」「PCMs are randomly reassigned」と説明した直後に、`Each simulation trial first sampled...` が同じ内容を繰り返している。
  - 方針: 1 文目を目的、2 文目を具体手順にして、同じ動詞を繰り返さない。
  - 修正案: 現行の 2 文を以下のように統合する。

```tex
To preserve room-specific usage patterns while varying the simulated occupant mix, each Monte Carlo trial sampled a subgroup of location-log agents from the regular member pool of room $r$ and randomly assigned \acp{pcm} to the selected location agents.
```

  - この文を入れる場合、後続の `The sampled agents retained...` は「何を保持し、何を入れ替えたか」を補足する役割に絞る。

  ->OK

- For a given trial, K remains fixed over simulation peropd,... の文章がわかりづらい
  - 確認: `K` が subgroup size、`N_{r,t}` が時刻ごとの実在 occupancy count であることは重要だが、現行文は少し数式先行で読みにくい。
  - 方針: まず概念を説明し、その後で記号を置く。
  - 修正案:

```tex
Within a trial, the sampled subgroup size $K$ is fixed for the full simulation period. However, only a subset of those sampled agents is present at any control timestep, so the realized occupancy count varies according to the observed stay logs and is denoted by $N_{r,t}=|S_{r,t}|$.
```

  - これにより、`K` と `N_{r,t}` の違いが Method と Results/Discussion で一貫して使いやすくなる。

->OK

- The sampled agents retained their obsedved stay logs, の部分はin their original roomsなど追記した方が良いか？
  - 判断: 追記した方がよい。今回の simulation は room-specific occupancy pattern を保存することが大事なので、`in their original rooms` を明示すると「場所ログまでシャッフルしているのか」という誤読を避けられる。
  - 修正案:

```tex
The selected location agents retained their observed stay logs in their original rooms, while \acp{pcm} were randomly assigned to those selected location agents in each trial.
```

  - 注意: `sampled agents` より `selected location agents` の方が、PCM と location-log agent の対比が明確。

- while PCMs were randomly assigned to themのThemをthe selected location agentsとする？前の文章とのWhileでの対比がわかりやすくなるように。
  - 判断: `them` は避けて、`the selected location agents` または `those selected location agents` に置き換える。
  - 理由: 直前に subgroup, agents, PCMs が並ぶため、代名詞だと参照先が曖昧になる。
  - 修正案: 上の文とまとめて以下にする。

```tex
The selected location agents retained their observed stay logs in their original rooms, while \acp{pcm} were randomly assigned to those selected location agents in each trial.

->OK
```

- For each simylationd realizationとあるが、Realizationより良い言葉があるか？
  - 判断: `Monte Carlo trial` に統一するのがよい。
  - 理由: `realization` は使えるが、前段で `trial` を使っているため、同じものを指す語が増えて読みにくい。Method では `trial`、必要なら初出で `Monte Carlo trial` とする。
  - 修正案:

```tex
For each Monte Carlo trial, the three \acp{gcm} described above were compared by aggregating the assigned \acp{pcm} at different temporal resolutions.
```

  - ただし、この文自体も次の `Each group comfort representation...` と近いため、下の繰り返し整理と合わせて圧縮する。

->OK

- For all three GCM-based pliciesから始まる文章は繰り返し感がある
  - 確認: `Each group comfort representation was formed...`、`The corresponding setpoint was selected...`、`For all three...` がほぼ同じ setpoint selection rule を説明している。
  - 方針: setpoint selection rule は 1 回だけ説明し、policy differences は group definition の違いに限定して述べる。
  - 修正案: 現行の `For each simulated realization...` から `The difference between policies...` までを以下に差し替える。

```tex
For each Monte Carlo trial, the three \acp{gcm} described above were formed by averaging the assigned individual ``No change'' probability curves at different temporal resolutions.
For each policy, the selected setpoint was the temperature that maximized the corresponding aggregated ``No change'' probability.
Thus, the three policies share the same setpoint-selection rule and differ only in whether the represented group is defined over the full study period, each day, or each control timestep.
```

  - この差し替え後に `Let $p_i(T)=...` の式へ入ると、文章説明から数式定義への流れが自然になる。

->OK

## 4. June 29th self-review 2nd
### Introduction
- In typical OCC frameworksの部分、いきなりSensingなどと言うとよくわからないので、There are three components; the sensing layer... などのように書くことが必要では？繋げながら一文で描きたい。
  - 確認: `ch1-Intro.tex` 21 行目は `sensing collects...; learning develops...; and control translates...` と始まるため、読者が OCC framework の三層構造を先に知らないと少し唐突。
  - 方針: 一文のまま維持しつつ、冒頭で「three components」を明示してから各 layer の説明へ入る。
  - 修正案:

```tex
Typical \ac{occ} frameworks consist of three connected components: the sensing layer collects information such as environmental conditions, comfort feedback, and occupancy; the learning layer develops preference or occupancy models from these data; and the control layer translates the model outputs into \ac{hvac} actions \cite{soleimanijavid_challenges_2024,xie_review_2020}.
```
->ComponentsでなくLayersにしておく

- 1.2Dynamic occupancy andのSubsectionが続けて始まっているが、Meanwhileなど文頭に置くことでThe rise of remote and hybrid workを前の文章に次の段落として繋げられないか？
  - 確認: 直前 subsection は `real-world \ac{occ} applications... remain limited` で終わり、次 subsection が `The rise of remote and hybrid work...` で始まるため、段落間の関係が少し切れて見える。
  - 方針: `Meanwhile,` を置いて、OCC の実装課題と同時に office usage 側も変化している、という接続にする。
  - 修正案:

```tex
Meanwhile, the rise of remote and hybrid work has increased the use of \ac{abw} and other flexible office arrangements \cite{marzban_review_2023}.
```
->OK

- as occupanyts arrive, leave or move between roomsの部分はoccupants move between different spaces throughout the dayに合体
  - 確認: 現在は line 32 で `occupants move between different spaces throughout the day`、line 34 で `as occupants arrive, leave, or move between rooms` と近い内容が重複している。
  - 方針: movement の説明は最初の文に集約し、次の文は「同じ人数でも誰がいるかが違う」点だけに絞る。
  - 修正案:

```tex
In such workplaces, occupants arrive, leave, and move between different spaces throughout the day, causing fluctuations in both occupancy density and occupant composition within a zone \cite{motuziene_office_2022,pan_environmental_2025,huang_space-matching_2025,chang_statistical_2013,levene_problem_2020}.
Dynamic occupancy should therefore be understood not only as a change in the number of people in a room, but also as a change in who is present.
Even when the occupancy count is similar, the thermal preferences represented by the present group may differ.
```
->OK

- Office projectsはof Japanese companiesと明記
  - 確認: `\autoref{table:OccuTrack}` の説明が `office projects` だけだと、対象が一般的な global field studies のようにも読める。
  - 修正案:


```tex
\autoref{table:OccuTrack} provides examples of office projects by Japanese companies that use IoT data for individual-level real-time occupancy tracking.
```
->OK


- Second issueとして次の1.3のSubsectionが始まっているが、そんなに対比できるほどFisrt issueを書けているか？ここまで分離できないのでは？
  - 確認: 現在の `dynamic occupancy raises a second issue` は、前 subsection で明示的に `first issue` として整理していないため、やや強い対比に見える。
  - 方針: `second issue` を避け、前 subsection で説明した dynamic occupancy を受けて「shared-space OCC では aggregation 問題になる」と自然につなぐ。
  - 修正案:

```tex
In shared-space \ac{occ}, these dynamic occupancy patterns make comfort aggregation a central control problem: the controller must decide how individual comfort information should be aggregated for a room-level setpoint.
```
->継続検討。前後の中で両者が最適な導入として書かれているか？

- but such an approach can be data- and compute-intensive にand not all representations are represented.と追記
  - 確認: Lei et al. の方法の限界として、data / compute intensive だけでなく、frequent combinations に基づくため全 occupant combinations をカバーしない点も重要。
  - 方針: `not all representations are represented` はやや不自然なので、`may not cover all possible occupant combinations` と書く。
  - 修正案:

```tex
Lei et al.~\cite{lei_practical_2022} addressed dynamic occupancy using multiple reinforcement-learning models for frequent occupant combinations, but such an approach can be data- and compute-intensive and may not cover all possible occupant combinations.
```
->OK

- Therefore, a simpler practical questionの部分が急すぎる。
  - 確認: 現在は既存研究の限界からすぐに `Therefore, a simpler practical question remains` へ飛ぶため、本研究の static/daily/real-time GCM 比較へ橋渡しが弱い。
  - 方針: 「個別 combination ごとのモデルを大量に持つ代わりに、aggregation の時間解像度を選ぶ問題として整理する」と一文挟む。
  - 修正案:

```tex
Rather than preparing separate control models for many occupant combinations, a more deployable strategy is to vary the temporal resolution at which individual comfort information is aggregated.
This leads to a practical question: when is static, daily, or real-time aggregation sufficient for room-level control?
```
->OK

- Focus of researchの部分、Three GCMs are comparedの部分は論文全体でどこが良いか判断。後のMethodでも同じような説明がされている。
  - 確認: Introduction line 70 と Method `Three-level time-resolution \ac{gcm}s` で、SGCM/DGCM/RTGCM の定義が近い内容で繰り返されている。
  - 方針: Introduction では detailed definition を短くし、「三つの aggregation resolutions を比較する」と研究範囲だけを示す。各 GCM の正式な操作的定義は Method に置く。
  - 修正案:

```tex
The analysis compares three levels of group-comfort aggregation, from fixed room-member aggregation to daily and real-time occupant-composition updates, with the operational definitions provided in the Method section.
```
->OK

- Using field data from real office spaces... の分はコメントアウトし非表示
  - 確認: line 72 の `Using field data from real office spaces...` は research objective の締めとしては情報量が多く、Method の説明とも重なる。
  - 方針: 本文ではコメントアウトし、直前の `Building on prior work...` と次の `Specifically...` を直接つなげる。
  - 修正案:

```tex
% Using field data from real office spaces, the study relates model performance to subgroup size, mean occupancy, occupancy variability, and \ac{utr}.
```
->OK

### Method
- Target building...のSubsectionのうち、The control variable is the zone air temperature setpointの文章は削除
  - 確認: `ch3-Method.tex` line 25 の文は設備説明の直後にあり、後の control policy / setpoint 定義で十分に説明される。
  - 方針: 削除でよい。target building の説明は building / rooms / participants に集中させる。
  - 修正案: 以下の文を削除。

```tex
The controlled variable is the zone air temperature setpoint.
```
->OK

- Suevey answers and location tracking data from...の前にConsidering the sufficience of collected surveysのような文を前置きし、かつこの文章全体を45 office workers who regularlyのあとに置いて流れをよくする
  - 確認: 現在は IRB / consent / anonymization の後に `Survey answers... from 39 participants...` があり、参加者数の流れが分断されている。
  - 方針: `45 invited` の直後に、有効分析対象が 39 名であることを置く。理由は `Considering the sufficiency and completeness...` のように、survey/location data の usable sample として説明する。
  - 修正案:

```tex
\qty{45} office workers who regularly work in the designated target rooms were invited to participate.
Considering the completeness of the collected survey answers and location tracking records, data from \qty{39} participants were used in the analysis.
This study has been approved by the National University of Singapore Institutional Review Board (NUS-IRB Reference Code: NUS-IRB-2025-498).
Informed consent was obtained from all participants prior to the study.
All location and survey data were anonymized by the building administrator before being accessed by the research team to protect privacy.
```

  - 注意: `sufficience` ではなく `sufficiency` だが、この文脈では `completeness` の方が自然。
->OK

- 2.1.3の箇所、BMSのデータは使っていないので、BMSのデータを利用と書いてある部分は削除、compact sensorsだけ残す
  - 確認: line 43 で `obtained from the \ac{bms} and compact sensors` となっているが、実際に BMS data を使っていないなら Method とデータ出所が不一致。
  - 方針: primary measurements は compact sensors 由来に限定し、BMS を削除する。
  - 修正案:

```tex
The primary measurements were \ac{ti} and \ac{rh}, obtained from compact sensors (HIOKI E.E. Corporation, Nagano, Japan) installed in the target rooms.
```
->OK

- 2.1.4の最後の箇所、sucsection.2.となっているが、appendixでの章の表記に。A.1, B.1などのような
  - 確認: `\autoref{app:occupancy_reconstruction}` が `subsection 2` のように出ている可能性がある。Appendix 内で `\subsection` から始まっているため、番号・autoref 名が不自然になりやすい。
  - 方針: Appendix 側の構成を `\section` 単位にするか、本文参照だけ `Appendix~\ref{...}` に変更する。最小修正なら本文側の参照文を変える。
  - 修正案（最小）:

```tex
The detailed procedure for this reconstruction is described in Appendix~\ref{app:occupancy_reconstruction}.
```

  - 修正案（構成を整える場合）: `chapters/chap-appendices.tex` の各 `\subsection` を `\section` に変更し、Appendix A, Appendix B... として出す。さらに table/figure は各 appendix section ごとに A.1, B.1 のようにしたい場合は、section ごとに `\renewcommand{\thetable}{\thesection.\arabic{table}}` などを検討する。
->OK

- 2.2.1 Simulation designの中、最後のAt each control timestep, the location-log agentsの一文は繰り返しになっていないか検討
  - 確認: Simulation Design line 64 の `At each control timestep...` は、後の Agentic simulation line 100 で active set と setpoint selection をより具体的に説明している。
  - 方針: Simulation Design では high-level overview に留め、control timestep の詳細は Agentic simulation subsection に任せる。
  - 修正案: 以下の文を削除またはコメントアウト。

```tex
% At each control timestep, the location-log agents determined the simulated room occupant composition.
```
->コメントアウト

- 2.2.3.のThree-level time-resolution GCMsは論文全体の中でどこが良いか検討。Introductionで触れているなら、ここは圧縮もしくは削除まで考えられる。もしくはIntroductionで定義した上で、次のSubsectionの中で、as describedのように引用して再起させるなど
  - 確認: Introduction で三つの GCM に触れ、Method でも line 79--83 で定義している。完全削除すると数式定義前の読者導線が弱くなるため、Method に短い operational definition は残した方がよい。
  - 方針: subsection として独立させず、`Simulation Design` の終盤または `Agentic simulation` 冒頭で `As introduced above...` と短く再定義する。
  - 修正案:

```tex
As introduced in the research focus, the simulation evaluates three temporal resolutions of \ac{gcm} aggregation: \ac{sgcm}, based on the sampled regular room-member group over the study period; \ac{dgcm}, based on the sampled attendees on each day; and \ac{rtgcm}, based on the sampled occupants present at each control timestep.
```

  - 実装時の選択肢: `\subsubsection{Three-level time-resolution \ac{gcm}s}` を削除し、この一文を `Agentic simulation` の数式前に移すと重複が最も少ない。

->OK


- Thus, the three policies..の文章でdiffer only in whether...と書かれているが、whetherで違いを述べるのはわかりづらい。updating timestep such as...などのように名詞のように書けないか
  - 確認: `differ only in whether...` は文法上は通るが、違いが categorical choice ではなく update timescale なので名詞句の方が明瞭。
  - 修正案:

```tex
Thus, the three policies share the same setpoint-selection rule and differ only in the update timescale of the represented group: the full study period, each day, or each control timestep.
```
->OK


- indexed by i はiが個人IDだと論文の中で分かるように
  - 確認: line 105 の `indexed by $i$` は、$i$ が location-log agent / assigned PCM / individual participant proxy のどれを指すか少し曖昧。
  - 方針: $i$ は selected location-log agent に割り当てられた individual comfort profile の index として明示する。
  - 修正案:

```tex
Let $p_i(T)=P_i(S_{th}=0\mid T)$ denote the ``No change'' probability predicted by the \ac{pcm} assigned to selected location-log agent $i$, where $i$ indexes an individual occupant proxy in the simulation, at \acl{ti} $T$.
```
->OK

- occupancy variabilityは現在は使っていないので、該当箇所をコメントアウト
  - 確認: Method では daily occupancy standard deviation `\sigma_{N,r,d}` を定義しているが、現在の主要 Results が使っていないなら reader に余計な分析軸を期待させる。
  - 方針: `Occupancy variability` paragraph と式 `eq:occ_var` をコメントアウト。Introduction / Focus に残っている `occupancy variability` も削るか、使う場合のみ残す。
  - 修正案:

```tex
% \paragraph{Occupancy variability}
% To capture within-day fluctuations in room load, the daily standard deviation of realized occupancy count is used:
% ...
% \label{eq:occ_var}
```
->OK

- UTRのDaily summariesも現在の分析の中で使っていなければコメントアウト。
  - 確認: Results が timestamp-level `\mathrm{UTR}_{r,t}^{30}` を使い、daily summary `\mathrm{UTR}_{r,d}` を使っていないなら、daily UTR の式は不要。
  - 方針: timestamp-level UTR definition は残し、daily summaries の段落と式だけコメントアウトする。
  - 修正案:

```tex
% For daily summaries, timestamp-level \ac{utr} values are averaged within each room-day:
% ...
% The daily \ac{utr} captures how much the present group composition changes over short horizons, even when the occupancy count is similar.
```
->OK

- 2.4.2 comfort-related outcomesのなか、pを変換するのにqで書くのはわかりにくくないか？
  - 確認: `q_{i,t}^{policy}=p_i(T_set...)` は「PCM probability curve を policy setpoint で評価した score」として数学的には妥当だが、記号が増えて読みにくい。
  - 方針: `q` を廃止し、`p_i(T_{\mathrm{set}}^{policy}(t))` を CP 式に直接入れる。本文では「evaluated no-change probability」と説明する。
  - 修正案:

```tex
For each present member $i\in S_{r,t}$, the setpoint generated by a policy is evaluated by the predicted ``No change'' probability $p_i(T_{\mathrm{set}}^{\mathrm{policy}}(t))$ from the assigned \ac{pcm}.
```

```tex
\mathrm{CP}_{r,d}^{\mathrm{policy}}
=
\frac{
\sum_{t\in\mathcal{T}_{r,d}}
\sum_{i\in S_{r,t}}
p_i\!\left(T_{\mathrm{set}}^{\mathrm{policy}}(t)\right)
}{
\sum_{t\in\mathcal{T}_{r,d}}
|S_{r,t}|
}.
```
->OK

- policy一覧にStatic, Daily, RTとなっているが、これらは\ac{}での略称記号を支えているか
  - 確認: 本文の policy set は mathematical labels として `\mathrm{Static}`, `\mathrm{Daily}`, `\mathrm{RT}` を使っている。一方、本文上のモデル名は `\ac{sgcm}`, `\ac{dgcm}`, `\ac{rtgcm}`。
  - 方針: 数式ラベルは短く保ってよいが、読者が acronym と対応づけられるように一度だけ明記する。
  - 修正案:

```tex
Here, $\mathrm{policy}\in\{\mathrm{Static},\mathrm{Daily},\mathrm{RT}\}$ corresponds to the \ac{sgcm}, \ac{dgcm}, and \ac{rtgcm} policies, respectively.
```
->OK

  - もしくは数式 label 自体を `\mathrm{SGCM}`, `\mathrm{DGCM}`, `\mathrm{RTGCM}` に変える。ただし式が長くなるため、現状の `Static/Daily/RT` に対応説明を足す方が読みやすい。

- 2.4.3 control related outcomes の中で、温度差分の計算式は良いが、式(14)の中に絶対値も再度表現するのはわかりづらい。というか式としてこの前の部分で完結しているので、絶対値表記は不要
  - 確認: `\delta T` の定義式に `\qquad |\delta T|` が並んでおり、1 つの式で二つの量を定義しているように見える。
  - 方針: 式は signed difference の定義だけにし、絶対値は本文で「magnitude is evaluated as...」と説明する。
  - 修正案:

```tex
\begin{equation}
\delta T_{r,t}^{\mathrm{RT}}
=
T_{\mathrm{set}}^{\mathrm{RT}}(t)
-
T_{\mathrm{set}}^{\mathrm{RT}}(t-\Delta t),
\label{eq:rt_setpoint_step}
\end{equation}
```
->OK

```tex
where $\Delta t=\qty{30}{\minute}$ is the control timestep. The adjustment magnitude is evaluated as $|\delta T_{r,t}^{\mathrm{RT}}|$.
```

- C+r,dの部分、イプシロンの設定はしていたか？温度変動のレンジを確かめる上では余計ではないか？
  - 確認: `\varepsilon=\qty{0.05}{\celsius}` は numerical noise 除外としてはあり得るが、本文で根拠を示していないため恣意的に見える。温度変動レンジを見る目的なら全 valid timestep の差分分布で十分。
  - 方針: `\mathcal{C}_{r,d}^{+}` と epsilon threshold を削除し、mean absolute step は全 valid consecutive timesteps で計算する。もし「変更が発生したときのみ」の分析を残すなら、Results figure caption と整合させて threshold の根拠を脚注的に説明する。
  - 修正案（threshold を外す）:

```tex
\begin{equation}
\overline{|\delta T|}_{r,d}^{\mathrm{RT}}
=
\frac{1}{|\mathcal{C}_{r,d}|}
\sum_{t\in\mathcal{C}_{r,d}}
\left|\delta T_{r,t}^{\mathrm{RT}}\right|,
\label{eq:rt_mean_abs_step_daily}
\end{equation}
```

```tex
where $\mathcal{C}_{r,d}$ is the set of timestamps on day $d$ in room $r$ for which both $T_{\mathrm{set}}^{\mathrm{RT}}(t)$ and $T_{\mathrm{set}}^{\mathrm{RT}}(t-\Delta t)$ are defined.
```
->実際のコードを確認してから修正すること。

- 2.5. Analysis outcomeの部分、単独でsubsectionが必要か？目的が分かりやすくなっている？
  - 確認: `Analysis outcomes` は Method の最後にあるが、評価指標の定義後に analysis flow を整理する役割はある。一方で短い subsection なので、独立させるほどの内容かは微妙。
  - 方針: 残すなら名前を `Analysis procedure` または `Outcome comparisons` にして、何を比較するかを簡潔に列挙する。削る場合は `Evaluation Metrics` の最後の段落として統合する。
  - 修正案（統合）:

```tex
The defined metrics are used for three comparisons: mean comfort probability and improvement relative to the fixed \qty{24}{\celsius} baseline across subgroup sizes and \ac{gcm} resolutions; real-time control burden through mean absolute setpoint adjustment; and the relationship between \ac{utr} and the 30-minute action-needed window ratio.
```

  - 実装時は `\subsection{Analysis outcomes}` を削除し、この文を `Control-related outcomes` の後に置くと Method の構造が締まる。

->Evauation metricsの章に合流で良い。

## 5. Selfーreview on June 30th
### Method
- 2.2と2.3で章を分けているが、統合できるのでは？Agentic simulationの大枠の説明は被っているはず
  - 確認: 現在の `ch3-Method.tex` では `Occupancy-log-based agentic comfort simulation` の中に `Simulation Design` と `Personal Comfort Model (PCM)` があり、その直後に別 subsection として `Agentic simulation` が置かれている。
  - 確認: `Simulation Design` は「PCM と location-log agent を分離し、Monte Carlo-style resampling を行う」という大枠、`Agentic simulation` は「subgroup sampling, PCM assignment, GCM aggregation, setpoint selection」を詳述しているため、章の階層としては分けすぎに見える。
  - 方針: `Occupancy-log-based agentic comfort simulation` を大見出しとして残し、その下に `Simulation design`, `Personal comfort model`, `Monte Carlo simulation and GCM policies` を並べる構成にする。つまり現行の `\subsection{Agentic simulation}` は `\subsubsection{Monte Carlo simulation and GCM policies}` に下げる。
  - 修正案:

```tex
\subsection{Occupancy-log-based agentic comfort simulation}
\subsubsection{Simulation design}
...
\subsubsection{Personal comfort model}
...
\subsubsection{Monte Carlo simulation and GCM policies}
As introduced in the research focus, ...
```

  - 追加整理案: `Simulation Design` 末尾の `Based on the simulated occupant compositions...` は、後続の `Monte Carlo simulation and GCM policies` と重複するため削除またはコメントアウトしてよい。
  - 注意: `Agentic simulation` を subsection として残すと、2.2 と 2.3 が並列に見えるが、実際には同じ方法論の内部手順なので、subsubsection 化の方が論理構造に合う。

->重複していた箇所はコメントアウトしつつ、章の構成を調整すること。

### Result
- 3.1 でComfort probabilityと書かれているが、ちゃんと前セクションのEvaluation metricsで定義済みだったか？そのほか指標の定義と実際のResult Section内での利用について矛盾がないか確認
  - 確認: `Comfort probability` は Method の `Comfort-related outcomes` で `\mathrm{CP}_{r,d}^{\mathrm{policy}}` と `\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}` として定義されている。Result 3.1 の `mean comfort probability` はこの `\overline{\mathrm{CP}}` に対応しているため、大枠では矛盾なし。
  - 確認: 一方、Result 3.1 で使う `improvement relative to the fixed \qty{24}{\celsius} baseline` は Method で文章としては触れているが、式として明示されていない。読者には `percentage point difference` なのか `relative percentage increase` なのかが曖昧になり得る。
  - 方針: Method の comfort-related outcomes に baseline improvement の定義を 1 式追加する。Result では `improvement in mean comfort probability relative to the fixed baseline` と書き、必要なら `percentage-point improvement` と明示する。
  - 修正案:

```tex
The improvement relative to the fixed \qty{24}{\celsius} baseline is computed as
\begin{equation}
\Delta \overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
=
\overline{\mathrm{CP}}_{r,K}^{\mathrm{policy}}
-
\overline{\mathrm{CP}}_{r,K}^{24\,^\circ\mathrm{C}} .
\label{eq:comfort_probability_improvement}
\end{equation}
```
->OK

  - 指標対応チェック:
    - 3.1 `mean comfort probability`: Method の `\overline{\mathrm{CP}}_{r,K}^{policy}` に対応。
    - 3.1 `improvement relative to baseline`: 上の式を追加すれば明確。
    - 3.2 `temperature adjustment magnitude`: Method の `|\delta T_{r,t}^{RT}|` と `\overline{|\delta T|}_{r,d,+}^{RT}` に対応。ただし `+` と epsilon threshold は「実際のコード確認後」として保留中。
    - 3.3 `action-needed window ratio`: Method の `\mathrm{AWR}_{r,d}^{30}` に対応。
    - 3.3 `\ac{utr}`: Method の timestamp-level `\mathrm{UTR}_{r,t}^{30}` に対応。daily UTR はコメントアウト済みなので、Result でも daily summary と誤読されないよう `30-minute \ac{utr}` または `timestamp-level \ac{utr}` と書く。

- 3.1.Although both the \ac{dgcm} and \ac{rtgcm} maintain performance improvements over the baseline, the gap between them increases as room size expands. This suggests that, in larger rooms, the \ac{rtgcm} benefits from more dynamic occupant transitions, whereas the \ac{dgcm} cannot fully capture time-varying group comfort as occupancy changes.
ここについては断言できないのでコメントアウト。これを示すことのできる追加グラフは作成可能か検討
  - 確認: 現在の文は「gap が room size とともに増える」だけでなく、「larger rooms では dynamic occupant transitions のため RTGCM が有利」と因果的に読める。現行 Figure だけでは occupant transition の強さを直接示していないため、断言は避けるべき。
  - 方針: 本文ではコメントアウトし、現時点では観察事実に留める。代替文を入れる場合も `may` や `suggests the need to examine` に留める。
  - コメントアウト案:

```tex
% Although both the \ac{dgcm} and \ac{rtgcm} maintain performance improvements over the baseline, the gap between them increases as room size expands.
% This suggests that, in larger rooms, the \ac{rtgcm} benefits from more dynamic occupant transitions, whereas the \ac{dgcm} cannot fully capture time-varying group comfort as occupancy changes.
```

  - 弱めた代替案:

```tex
The difference between the \ac{dgcm} and \ac{rtgcm} should therefore be interpreted together with occupancy-composition dynamics, rather than subgroup size alone.
```

  - 追加グラフ案:
    - `\overline{CP}^{RT} - \overline{CP}^{Daily}` を y 軸、mean \ac{utr} または 30-minute \ac{utr} summary を x 軸にした scatter/contour plot。
    - `\overline{CP}^{RT} - \overline{CP}^{Daily}` を y 軸、subgroup size `K` を x 軸、色を mean \ac{utr} または mean occupancy ratio にした plot。
    - room ごとに `RT-Daily gap` と `UTR` の関係を示す small multiples。
  - 追加グラフで示せること: RTGCM と DGCM の差が「room size」ではなく「occupant-composition turnover」と関係するかを検証できる。これが出せれば、コメントアウトした主張を Discussion で限定的に復活できる。

->追加検討中。保留。

- 3.1. 少しボリュームが足りていない気がする。語りを膨らませられる内容を検討
  - 確認: 現在の 3.1 は Figure の説明、policy ranking、subgroup size による低下、SGCM の baseline 接近、DGCM/RTGCM の positive improvement までで構成されている。主張は通るが、各結果の意味づけが短め。
  - 方針: 新しい因果主張を足すより、Method で定義した `K` と `N_{r,t}` の違い、policy resolution の違い、baseline との差を使って結果の読み方を補強する。
  - 追記候補 1: 3.1 冒頭で Figure の読み方を補足。

```tex
Here, subgroup size $K$ represents the sampled regular-member group size, not the number of occupants present at every timestep. Therefore, the trend across $K$ indicates how the tested policies behave as the potential room-member pool expands.
```
->OK

  - 追記候補 2: SGCM の低下を説明。

```tex
The decline of the \ac{sgcm} improvement indicates that a fixed room-member aggregation becomes less distinct from the fixed-temperature baseline as more heterogeneous comfort profiles are averaged into a single representation.
```
->OK

  - 追記候補 3: DGCM/RTGCM の positive improvement を中立的に説明。

```tex
The positive improvement maintained by the \ac{dgcm} and \ac{rtgcm} indicates that updating the represented occupant group can preserve comfort benefits even when the potential member pool becomes larger.
```
->OK

  - 注意: `RTGCM benefits from dynamic occupant transitions` のような説明は、追加グラフで確認できるまで 3.1 では避ける。

- 3.2のcontrol-adjustment burdenという件、burdenは負担という単語に聞きこえて重い。もう少しNeutralな単語はないか
  - 確認: `burden` は実務負荷の意味として Discussion では有用だが、Results subsection の見出しや説明ではやや評価的に聞こえる。
  - 方針: Results では neutral に `control adjustment`, `setpoint adjustment`, `control-update requirement` などを使い、Discussion で必要に応じて operational burden と解釈する。
  - 候補:
    - `Effect of \ac{rtgcm} on setpoint adjustment`
    - `Setpoint adjustment characteristics under the \ac{rtgcm}`
    - `Control-update requirements under the \ac{rtgcm}`
    - `Temperature setpoint adjustment under the \ac{rtgcm}`
  - 修正案:

```tex
\subsection{Setpoint adjustment characteristics under the \ac{rtgcm}}
...
This subsection investigates the setpoint adjustment characteristics introduced by the \ac{rtgcm}.
```

  - Method 側も `control burden` と言っている箇所があるため、Results だけでなく Method の `To quantify the control burden...` も `To quantify setpoint adjustment requirements...` に変えると全体のトーンがそろう。

->setpoitd adjustment characteristicsでOK

- This analysis intends to visualize the effect of occupancy size from two aspects: subgroup size, which shows sample sizes, and normalizedmean occupancy ratio, which shows the density/sparceness of the target room.
と追記したが、Sample sizeをこの文脈で適切に示す言葉づかいはあるか
  - 確認: ここでの `subgroup size` は statistical sample size ではなく、simulation condition として sampled regular-member pool の大きさを示す `K`。`sample size` と書くと統計的なサンプル数や trial 数に見える。
  - 方針: `sample size` は避け、`sampled regular-member group size`, `potential room-member group size`, `simulated room-member pool size` のいずれかにする。
  - `normalizedmean occupancy ratio` は typo があり、`normalized mean occupancy ratio` または `mean occupancy normalized by subgroup size` とする。
  - 修正案:

```tex
This analysis visualizes occupancy scale from two complementary perspectives: subgroup size $K$, which represents the sampled regular-member group size in each simulation condition, and the normalized mean occupancy ratio, which represents how densely that sampled group is occupied during operation.
```

->OK

  - さらに簡潔にする案:

```tex
Here, subgroup size $K$ represents the simulated regular-member pool, whereas the normalized mean occupancy ratio represents realized occupancy density within that pool.
```
->一つ上のもので採用

  - `density/sparseness of the target room` は room 自体の密度というより sampled group に対する realized occupancy の疎密なので、`realized occupancy density within the sampled group` がより正確。


- 3.3. adjustment events of at least 0.5degreeは表現として違和感。適切な言葉に。
  - 確認: Method では `action-needed window ratio` を「30-minute window 内に rounded real-time setpoint update が \qty{0.5}{\celsius} 以上ある場合」と定義している。したがって `temperature adjustment events of at least 0.5 degree` は少し粗く、window-based metric であることが伝わりにくい。
  - 方針: `event` ではなく `30-minute windows requiring an actionable setpoint change` と書く。
  - 修正案:

```tex
\autoref{fig:CtrlWindowRatio} shows the 30-minute action-needed window ratio across different \ac{utr} levels, where an action-needed window is defined as a window containing at least one rounded \ac{rtgcm} setpoint change of \qty{0.5}{\celsius} or larger.
```
->OK

  - 短い案:

```tex
\autoref{fig:CtrlWindowRatio} shows the relationship between \ac{utr} and the share of 30-minute windows requiring an actionable setpoint change of at least \qty{0.5}{\celsius}.
```

  - 併せて直後の `probability of required temperature adjustment` は `action-needed window ratio` に統一する。
->一つ上のもので採用

## Potential references
jung energy 2020: in a responsive and adaptive building system, the dynamic diversity of pcm in thermal zones provides opportunities for dynamic setpoint adjustment
jung energy 2020: it comes to the improvement in thermal comfort, the thermal comfort sensitivity based approach had the best
jung energy 2020(discussion ): long-term acclimatation to  the climate... 
jung energy 2020(conclusion):as number of occupants per multioccupancy zone increases, the opportunities
jung energy 2020(conclusion): by having more than six occupants per zone, the benefit of using pao dininishes
jung energy 2020(conclusion): the performance from the integration of personal comfort model converges to that of conventional generalized models
jung comparative 2019thermal preferences were distributed across a range from 20 to 27, which is an acceptable range according to the field study

## 6. Discussion reinforcement from potential references and RefPaper notes

Discussion はすでに `Effect of occupancy parameters on comfort performance`, `Effect of occupancy parameters on control`, `Limitations` の3部構成になっている。
RefPaper の Result/Discussion から補強できる論点は、単に「先行研究と一致した」ではなく、本研究の貢献である occupancy dynamics / time resolution / practical control relevance をより明確にする方向で使うのがよい。
以下では、それぞれ「参照できる先行研究の論点」「本研究結果との接続」「追記案」を近くにまとめる。

### 6.1 Group size effect は既存Discussionにあるが、SGCMだけでなく DGCM/RTGCM との差分を新規性として強調する

- 参照できる論点:
  - \mycite{jung_energy_2020}\cite{jung_energy_2020} は、multi-occupancy zone で人数が増えると personal comfort integration の便益が小さくなり、一定人数以上では conventional/generalized model に近づくことを示している。
  - \mycite{jung_comparative_2019}\cite{jung_comparative_2019} でも、occupants の人数が増えるほど collective comfort probability が下がり、複数戦略の性能差が収束する傾向が示されている。

- 本研究との接続:
  - SGCM の改善率が subgroup size とともに小さくなり、K=5--7 付近で fixed baseline に近づく点は先行研究と整合する。
  - ただし、本研究の新規性は「人数が増えると個人差が平均化される」だけでなく、DGCM/RTGCM が subgroup size 増加後も positive improvement を維持する点にある。
  - これは「人数」だけでなく、「その日に誰が来たか」「時刻ごとに誰に入れ替わったか」という occupancy dynamics が comfort aggregation の有効性を左右する、という解釈につなげられる。

- 追記候補:

```tex
This agreement with previous studies should be interpreted mainly for the \ac{sgcm}, which represents a relatively static aggregation of the potential room-member group.
The more distinctive finding of the present study is that the \ac{dgcm} and \ac{rtgcm} maintain positive improvement even when the subgroup size becomes larger.
This suggests that the diminishing return of personal-comfort integration with increasing group size can be partly offset when the represented group is updated according to realized attendance or real-time occupant composition.
Thus, the effective aggregation scale in shared offices is not determined only by the number of potential users assigned to a room, but also by how frequently the actually present occupants differ from that static membership.
```

- 挿入先:
  - `Effect of occupancy parameters on comfort performance` の第1段落後、既存の `At the same time, the \ac{dgcm} and \ac{rtgcm} maintain positive improvement...` の周辺に入れる。
  - 既存文と重複するため、入れる場合は現在の2段落目を置き換えるのがよい。

- 注意:
  - `room size` と言い切るより `subgroup size`, `potential room-member group`, `realized attendance` の語を使う。
  - 「人数が6人を超えると必ず無効」とは書かず、先行研究と本研究条件での傾向として扱う。

### 6.2 Dynamic diversity を RTGCM の価値説明に使う

- 参照できる論点:
  - \mycite{jung_energy_2020}\cite{jung_energy_2020} は、responsive/adaptive building system では thermal zone 内の personal comfort models の dynamic diversity が dynamic setpoint adjustment の機会になる、という方向の議論をしている。

- 本研究との接続:
  - 本研究はこの dynamic diversity を、実測の location log と \ac{utr} によってより具体的に扱っている。
  - \ac{utr} は人数の多寡ではなく「誰が置き換わったか」を表すため、RTGCM が DGCM より意味を持つ条件を説明する指標になる。
  - Discussion では `mean occupancy` と `\ac{utr}` の違いをもう一段はっきり書くと、Results の control window ratio とつながる。

- 追記候補:

```tex
The role of \ac{utr} also extends the notion of dynamic diversity discussed in prior comfort-driven control studies.
While mean occupancy indicates how many occupants are present, \ac{utr} indicates whether the comfort profiles represented by the present group are being replaced over time.
Therefore, a room with the same occupancy count can require different \ac{rtgcm} setpoints when occupant composition changes, whereas a room with stable membership may not benefit substantially from real-time aggregation.
This distinction helps explain why real-time tracking is most relevant when occupant turnover changes the represented comfort distribution, rather than merely when the room is sparsely occupied.
```

- 挿入先:
  - `Effect of occupancy parameters on control` の \ac{utr} 説明段落、現在の `Mean occupancy and occupancy variability describe...` の直後。

- 注意:
  - Results 側で RTGCM/DGCM の差を動的遷移だけに過度に帰属させない。
  - Discussion では「結果の解釈」として、\ac{utr} が real-time aggregation の operational relevance を示す、と書くのが安全。

### 6.3 Comfort model resolution と HVAC/control resolution のミスマッチを、RTGCM導入条件の議論に拡張する

- 参照できる論点:
  - \mycite{ono_effects_2022}\cite{ono_effects_2022} は、thermal comfort model の occupancy resolution と HVAC control の occupancy/control resolution が合わないと、comfort improvement や energy saving の便益が失われることを示している。
  - lower control resolution に対して high-resolution comfort model を使っても、実際に好ましい条件へ調整できない場合がある。

- 本研究との接続:
  - 現Discussionにはすでに `resolution-mismatch argument` があるが、さらに「RTGCMを使うべきかどうかは、tracking availability だけでなく actuator/control interval/resolution に依存する」と明確にできる。
  - 本研究では \qty{0.1}{\celsius} の制御解像度を仮定し、\qty{0.5}{\celsius} 以上の action-needed window を確認しているため、実務的な制御分解能との接続を議論しやすい。

- 追記候補:

```tex
This also means that \ac{rtgcm}-level information is not automatically useful unless the control system can act on the resulting setpoint differences.
The present simulation assumed a fine setpoint resolution of \qty{0.1}{\celsius}, but the action-needed-window analysis separately examined whether the difference would exceed a more common \qty{0.5}{\celsius} control step.
In this sense, the proposed metrics help distinguish latent comfort-model differences from actionable control differences.
Such a distinction is important for avoiding a resolution mismatch in which real-time comfort information is available but the HVAC system cannot respond at the same practical resolution.
```

- 挿入先:
  - `Effect of occupancy parameters on control` の Ono paragraph の後。
  - 既存の `The present results show this trade-off...` と一部重複するため、置き換えまたは後半を統合する。

- 注意:
  - \qty{0.1}{\celsius} は実装上やや仮想的な細かさとして扱う。
  - \qty{0.5}{\celsius} は「一般的な thermostat step」として operational threshold に使う、という説明がよい。

### 6.4 Collective comfort と fairness の限界を、平均CPだけに依存する本研究の制約として書ける

- 参照できる論点:
  - \mycite{jung_comparative_2019}\cite{jung_comparative_2019} は、multi-occupant conditioning では majority / mean / median のような単一集約が、特定occupantの継続的不満足を生む可能性を議論している。
  - \mycite{topak_collective_2023}\cite{topak_collective_2023} は collective comfort probability を扱いつつ、occupant locations や micro-thermal conditions を利用することで、平均的な室温だけでは見えない快適性改善を示している。

- 本研究との接続:
  - 本研究の \ac{gcm} 評価は mean comfort probability を主指標としており、誰かが繰り返し不利になる fairness は直接評価していない。
  - Discussion の Limitations に、平均CPの改善が occupant-level fairness を保証しない点を追加すると強い。
  - 特に RTGCM は occupant composition に応じて setpoint を変えるため、短期的な平均改善だけでなく、occupantごとの累積不快や公平性を将来的に見る必要がある。

- 追記候補:

```tex
Another limitation is that the present analysis evaluates group performance primarily through mean comfort probability.
Although this metric is useful for comparing aggregation levels, it does not show whether the same occupants repeatedly receive lower comfort probability under a group-optimal setpoint.
Prior discussions on collective conditioning have noted that majority- or mean-based setpoint selection may improve average comfort while raising fairness concerns for minority preference groups.
Future work should therefore evaluate occupant-level cumulative discomfort or fairness-aware objectives together with the mean \ac{cp}, especially when real-time aggregation is used to update setpoints throughout the day.
```

- 挿入先:
  - `Limitations` の `Third, comfort evaluation is based on predicted...` の後。

- 注意:
  - 本研究では actual person-specific PCM と movement が対応していないため、fairness を定量評価したとは書かない。
  - 「将来課題」として置くのがよい。

### 6.5 Non-uniform thermal conditions / spatial matching は本研究の範囲外だが、ABWとの接続を強められる

- 参照できる論点:
  - \mycite{topak_collective_2023}\cite{topak_collective_2023} は、shared open office では occupant location ごとの micro-thermal condition が異なり、personal comfort profiles と空間配置を組み合わせることで collective comfort を改善できることを示している。
  - 同論文は、uniform room-average temperature を前提にする OCC 研究の限界も示唆している。

- 本研究との接続:
  - 本研究は room-level setpoint と location log に基づく occupancy dynamics を対象としており、室内位置ごとの温熱差や seating assignment optimization は扱っていない。
  - ただし、ABW/free-address office では「誰が部屋にいるか」だけでなく「どこに座るか」も重要になるため、Discussion の future work として自然につなげられる。
  - 本研究の \ac{utr} は room-level の入れ替わりを捉える指標だが、将来的には seat-level/micro-zone occupancy と組み合わせられる。

- 追記候補:

```tex
The present study focuses on room-level setpoint selection and does not model non-uniform thermal conditions within each office room.
However, studies on collective comfort in shared offices have shown that occupants at different locations can experience different micro-thermal conditions even under the same room-average operation.
For activity-based or free-address offices, this implies that occupancy dynamics may interact with seat choice and spatial thermal heterogeneity.
Combining \ac{utr}-based temporal dynamics with seat-level or micro-zone comfort modeling would be a natural extension for evaluating whether real-time comfort information should be used for setpoint control, seat recommendation, or both.
```

- 挿入先:
  - `Limitations` の energy/HVAC response の制約の後、または Discussion 末尾に future work として追加。

- 注意:
  - 現在の結果は room-level simulation なので、Topak の non-uniform thermal field を直接比較しすぎない。
  - ABW の文脈とつなげると Introduction/Discussion の一貫性が上がる。

### 6.6 Thermal preference diversity と sensitivity を、PCM assignment の妥当性/限界として補足できる

- 参照できる論点:
  - \mycite{jung_comparative_2019}\cite{jung_comparative_2019} は、thermal preferences が広い温度範囲に分布し、thermal comfort sensitivity が collective conditioning の setpoint 選択に影響することを示している。
  - \mycite{jung_energy_2020}\cite{jung_energy_2020} でも、occupants' thermal comfort characteristics のばらつきが comfort-driven control の重要因子として扱われている。

- 本研究との接続:
  - 本研究では PCM profiles を observed location-log agents に再割当てしているため、個人ごとの移動パターンと快適性嗜好の対応は直接保持していない。
  - 一方で、複数PCMを組み合わせた Monte Carlo design によって、thermal preference diversity が occupancy dynamics と相互作用する状況を評価している、と説明できる。
  - Discussion では妥当性と限界の両方を書くとよい。

- 追記候補:

```tex
The Monte Carlo assignment of \ac{pcm} profiles should also be interpreted in relation to the diversity of thermal preference and comfort sensitivity reported in previous multi-occupant comfort studies.
By repeatedly assigning different comfort profiles to observed location-log agents, the simulation explores how preference diversity can interact with the same occupancy dynamics.
At the same time, because the assigned \ac{pcm} profiles are not linked to the actual occupants who generated the movement logs, the results do not capture possible correlations between a person's attendance pattern, seat choice, and thermal preference.
```

- 挿入先:
  - `Limitations` の `Second, the agentic simulation reassigns \ac{pcm} profiles...` の周辺。

- 注意:
  - これは Method の Monte Carlo design の補足にもなる。
  - 「本研究の弱点」だけでなく「なぜ再割当てに意味があるか」も明確にできる。

### 6.7 Energy implications は今回の主結果ではないが、RTGCMの実装判断には必要と書ける

- 参照できる論点:
  - \mycite{jung_energy_2020}\cite{jung_energy_2020} は、comfort-driven control の energy implication が条件によって正にも負にもなり得ることを示している。
  - \mycite{topak_collective_2023}\cite{topak_collective_2023} は、airflow direction の変更など、快適性改善とエネルギー影響が制御手段に依存することを示している。
  - \mycite{ono_effects_2022}\cite{ono_effects_2022} は、適切な comfort/control resolution の組み合わせが energy saving にも影響することを示している。

- 本研究との接続:
  - 本研究は comfort probability と setpoint adjustment characteristics に焦点があり、energy consumption は直接評価していない。
  - RTGCM は comfort improvement を増やせるが、setpoint変更頻度や制御応答が増える可能性があるため、energy/HVAC dynamics を今後評価すべきという議論につなげられる。

- 追記候補:

```tex
Finally, the present results should not be interpreted as direct evidence of energy savings.
Prior comfort-driven control studies have shown that the energy implication of personal comfort integration depends on occupancy level, comfort-profile diversity, control strategy, and available actuation.
In the present study, \ac{rtgcm} improved comfort probability under some occupancy conditions, but the associated setpoint-update frequency may also affect equipment operation, response delay, and energy use.
Evaluating this comfort-control trade-off with a dynamic HVAC or building-energy model is therefore necessary before translating the proposed aggregation levels into an operational control strategy.
```

- 挿入先:
  - `Limitations` の `Energy consumption, \ac{hvac} response delay...` を置き換え/拡張。

- 注意:
  - Energy saving を主張しない。
  - 「comfort benefit と operational/energy cost の trade-off」を評価課題として書く。

### 6.8 Discussion全体の構成案

- 現在の構成は保ったままでよい。
- ただし、各 subsection の役割を少し明確にすると読みやすい。

1. `Effect of occupancy parameters on comfort performance`
   - Jung energy / Jung comparative と接続。
   - group size による diminishing return。
   - その上で DGCM/RTGCM の positive improvement を本研究の新規性として提示。

2. `Effect of occupancy parameters on control`
   - Ono mismatch と接続。
   - RTGCM の setpoint difference が actionable かどうか。
   - \ac{utr} による dynamic diversity / real-time relevance の説明。

3. `Limitations and future work`
   - mean CP は fairness を保証しない。
   - PCM reassignment は preference diversity を探索するが、実個人との対応はない。
   - non-uniform thermal conditions / seat-level control は未評価。
   - energy and HVAC dynamics は未評価。

- Discussionに本文反映する際の優先順位:
  - 優先度高: 6.1, 6.2, 6.3, 6.6, 6.7
  - 余裕があれば: 6.4, 6.5
  - 特に 6.4 fairness と 6.5 spatial heterogeneity は、本文が長くなりすぎる場合は Limitations/Future work に短く入れる程度でよい。

## 7. ASIM 2026 Conference稿の未解決コメントと追加内容の反映計画（2026-08-12）

### 7.1 対象、扱い、結論

- 参照元:
  - `IBPSA ASIM 2026_OccupancySimulation/overleaf_comments_unresolved.csv`
  - ASIM Conference稿の実コンパイル対象である `ASIM2026-fullpaper.tex` と `sections/1.introduction.tex` ～ `sections/5.conclusion.tex`
  - ASIM側の `HANDOVER.md` と `content-selection-notes.md`
- ASIM Conference側は**参照のみ**とし、ファイル変更は行わない。
- CSVは旧ファイル名 `sections/method.tex` 等を参照しているが、実コンパイル対象は番号付きの `sections/2.method.tex` 等である。番号付き稿では、建物名の匿名化、対象4室の表、追跡方式、occupancy-density図、定量的Conclusionなど、コメントの一部がすでに反映されている。
- CSVのコメント本文のうち No. 1, 5, 14, 15 は末尾が `...` で切れている。以下は取得できた範囲と、番号付きASIM稿で実際に行われた修正から判断した。最終回答前に、必要ならOverleaf上の完全なthreadを確認する。
- 現行journal稿には、ASIM側で図・コード準拠に直された重要なerrataが残る。特に**15分／30分、改善幅、UTRとactionable率、低在室時のsetpoint step**は、文章追加より先に直す必要がある。
- この章では、conference固有の体裁コメントと、同じデータ・解析に関わるjournal稿の科学的修正を分離する。

### 7.2 優先順位

#### P0: 投稿前に必ず直す

1. **comfort outcomeとpolicy algorithmの整合を解決する。** 現行journal図はbinary comfort coverageであり、Methodのperson-time ``No change'' probabilityと一致しない。さらに現行workerではSGCMとDGCM/RT-GCMのsetpoint ruleが異なるため、aggregation resolutionの効果とalgorithm差が交絡している。
2. ASIM採用comfort図のprovenanceと生成コードを確認する。軸はperson-time comfort probabilityだが、同じpipelineでSGCM/DGCM/RT-GCMが同一ruleから生成されたかは画像だけでは分からない。
3. `chapters/ch3-Method.tex` の30-minute control timestep / UTR / action-needed-window定義を、実際に採用する生成pipelineと図に合わせて整理する。
4. `chapters/ch4-Results.tex` のRT-GCM/DGCM改善幅を、採用が確定したprobability-based出力に合わせて修正し、`%` と percentage point を区別する。
5. `chapters/ch4-Results.tex` の「UTR 0.7--0.8で90\%」を、採用するaction-frequency pipelineのbin別値へ修正する。
6. `chapters/ch4-Results.tex` の低在室時setpoint adjustmentを、生成元データ確認後、約1.3°Cから始まる傾向として記載する。
7. 15-minute transition metricと30-minute action window / rolling UTRを別指標として定義し、本文・式・図キャプションの時間幅を一致させる。
8. room名の対応を確定する。現行稿の `R\&D Office / Admin Office C / Shared Office 2` とASIM稿の `Office 5A / Office 5B / Shared Office 5A / Shared Office 5B` の対応には不整合の可能性があるため、推測で置換しない。
9. raw predicted probabilityと、各PCMのpeakでnormalizeしたscoreを区別する。normalized scoreを使う場合は`comfort probability`と呼ばない。
10. 39 PCM participants、eligible location-log user pool、sampled subgroup $K$を別母集団として記述し、PCM samplingのwith/without replacementを実runから確定する。
11. comfort estimandが全期間person-time poolingか、room-day内person-time平均をday間で等重みした値かを確定する。
12. uncertainty band / CIの観測単位、resampling単位、含まれない不確実性を明記する。
13. ASIM新図filenameの`raw2000`とMethodの1,000 trialsの不一致を解消し、figure source tableと本文のtrial数を一致させる。
14. action metricの分母、empty set、欠測gap、日境界、rounding、bin edgeを生成コードから確定する。

#### P0-1の詳細: comfort metricとpolicy rule

- 現行journal Resultsが参照する `analysis21_a6_style_comfort_rates_expanded_pool_selected_k_adopted_...png` とimprovement図は、`static_ratio`, `dynamic_ratio`, `daily_fixed_ratio`を描いている。
- `ref/a6_worker.py`では、これらは各PCMの`RangeMin <= setpoint <= RangeMax`を数える**binary comfort coverage**であり、Methodの「予測``No change'' probabilityのperson-time average」ではない。
- 同workerでは、SGCM setpointは`sampled["PeakSET"].mean()`、DGCM/RT-GCMは`calculate_optimal_setpoint_from_curves(...)`で求める。したがって現行実装は、represented groupの時間解像度だけでなくsetpoint-selection algorithmも異なる。
- `run_a7_prob_daily`はprobability-based評価を出すが、確認できた版ではSGCM setpointが依然としてmean PeakSETであり、DGCM列もない。これだけではMethodに書かれた「3 policyが同じmerged-curve argmax rule」を再現していない。
- ASIM採用稿は別図 `fig1_analysis23nr_with_fixed24_raw2000_64_100_all_solid_small_markers_paper.png` を使い、軸を`Mean person-time comfort probability (%)`としている。しかしASIMフォルダ内に生成script/notebookがなく、journal側notebookにも同filenameの生成セルが見つからないため、provenanceが未確認である。
- さらに、ASIM採用図では$K=2$のRT-GCMが目視で約92--93\%である一方、ASIM Results本文は96--97\%と記載しており、**ASIM採用稿の図と本文にも不一致が残る**。96--97\%は同フォルダ内の旧図 `fig1_comfort_probability_64_100_paper.png` に近い。新旧の数値を混在させない。

推奨する解決策はAである。

- **A（推奨）: probability-basedで再生成し、全policyのruleを統一する。** SGCM/DGCM/RT-GCMすべてについて、対応するrepresented groupのprobability curvesを平均し、同一candidate grid上のargmaxでsetpointを選ぶ。そのsetpointをpresent occupantsのPCMへ戻してperson-time mean probabilityを計算する。この設計なら、比較対象をaggregation resolutionに限定できる。
- **B（非推奨）: 現行実装を正直に記述する。** binary coverageをoutcomeとし、SGCMはmean PeakSET、DGCM/RT-GCMはmerged-curve argmaxとMethodに書く。この場合、結果はaggregation resolution単独の効果ではなくalgorithm差を含むため、研究目的・title・causal languageを再定義する必要がある。

Aを採用する場合の完了条件:

1. SGCM、DGCM、RT-GCMが同じgroup-to-setpoint map、$g(G)=\arg\max_T |G|^{-1}\sum_{i\in G}p_i(T)$を通る。違うのは$G=R_r,A_{r,d},S_{r,t}$だけとする。
2. 最適化とscoringの両方で、同じ$p_i(T)$定義を使う。raw/calibrated predicted probabilityを使うか、各PCM peakでnormalizeしたscoreを使うかを固定する。後者は`normalized comfort score`等と呼び、calibrated comfort probabilityと同一視しない。
3. fixed 24°Cはgroup-to-setpoint ruleではなく外部baselineとし、present occupantsについて他policyと同じmetricでscoreする。
4. PCM poolとlocation-agent poolを区別し、実runのpool size、eligible user条件、sampling replacement、random pairing、expanded poolの有無、$K$上限をsource tableへ保存する。
5. estimandを固定する。全期間person-time poolingと、room-day内person-time平均をday間で等重みする集計は同じでないため、生成コード、Method式、本文表現を一致させる。
6. room × $K$ × trial × dayの集計順、day/trial/roomの重み、欠測dayの扱いを明示する。
7. probability-basedのcomfort本図、baseline improvement図、RT-GCM minus DGCM図を同じrunから再生成する。
8. figure source table/CSV、seed、trial数、candidate grid、tie-breakingを保存する。ASIM新図filenameの`raw2000`がtrial数を意味するか確認し、Methodの1,000 trialsと不一致のまま使わない。
9. error bar / bandについて、trial、room-day、transition binのどれを観測単位としたか、percentileかbootstrap CIかを記載する。Monte Carlo assignmentのspreadをpopulation CIと呼ばず、PCM推定誤差と同一occupancy log再利用が通常は含まれないことをLimitationsで明示する。
10. Results、Abstract、Discussion、Conclusionの全数値を新しいsource tableから再抽出する。
11. binary図とprobability図、異なるtrial数またはpolicy ruleの図を同じ本文で併用しない。

Analysis manifestに必ず残す項目:

- data snapshot/date、roomsと対応表、$K$ range、largest tested $K$、trial数、seed、script/version hash。
- location-user eligibility、PCM eligibility、with/without replacement、location IDとPCMのrandom pairing。同じtrial内では全policyが同じpairingを共有する。
- $R_r$, $A_{r,d}$, $S_{r,t}$の構築規則、empty $A/S$、raw detectionからanalysis gridへの変換、gapとday boundaryの扱い。
- common optimizerの関数、raw/normalized curve、setpoint grid bounds/step、interpolation、missing curve、argmax tie-breaking。
- scoring probability/scoreのrangeとNaN処理、person-time分母、day equal-weight / pooled、room/K/trialの要約順。
- contrastは同じtrial内のpaired differenceをpercentage pointsで保存する。別々に集計した平均の差だけに依存しない。
- action burdenのrounding tie、threshold、consecutive transition、empty-union UTR、bin edges、各binのsample size。
- comfort本図、baseline差、RT-GCM minus DGCM、source CSVを同一manifestから生成し、ASIM画像だけを単独でコピーしない。

#### P1: 再現性と主張の根拠のために追加する

1. 4つのsimulation target roomsの一覧表をMethodに追加し、7つのdata-collection roomsとの違いを明記する。
2. location trackingがroom entranceとcorridorに設置されたface-recognition system由来であることを、匿名化・IRBの説明とセットで明記する。
3. candidate setpoint gridが0.1°C resolutionであることをMethodに追加する。
4. setpoint-change図の帯が25--75 percentileと10--90 percentileであることをcaptionに明記する。
5. partial attendanceがRT-GCM/DGCMの便益を残すという説明には、decision-time occupancy densityの結果または図を直接対応させる。
6. AbstractとConclusionに、評価対象が`predicted person-time comfort probability`と`setpoint-update burden`であること、および主要な定量結果を追加する。

#### P2: 追加分析または著者判断が必要

1. 15分または30分を選んだ科学的・運用的理由を明記する。ASIM採用図と引継ぎメモは15-minute transitionを示す一方、journal workerは30-minute action windowを生成する。センサー分解能、stay-log再構成単位、HVAC運用周期のどれが各時間幅の根拠かは未確認である。
2. UTRとactionable率の関係について、$K$だけでなく実在室人数 $N_{r,t}$ で層別した結果を確認する。現図の$K$ bandの近接だけでは「actual occupancyよりturnoverがdominant」とは断定できない。
3. high-UTR binのtransition数を確認する。95\% date-cluster bootstrap CIは既存captionにあるが、端のbinのsample sizeが不明である。PCM推定誤差や別occupancy-log sampleへの一般化を表すCIではない。
4. occupancy-density figureをjournal稿へ移植する場合、元集計、room label、confidence intervalとsimulation intervalの定義を確認する。
5. 15-minute transitionを主解析にするなら、可能な範囲で30-minute definitionとのsensitivityを示す。入力gridが15分であるだけなら、HVAC control intervalと同一視しない。実施できなければLimitationsにtime-step dependenceを加える。

### 7.3 現行journal稿への具体的修正指示

#### 7.3.1 30分と15分の混在を解消する

- 対象: `chapters/ch3-Method.tex`
- 現時点では全記述を15分へ一括置換しない。journal側には、raw timestamp間のstep、30-minute window内にactionが一度でもあったwindow ratio、30-minute rolling UTRが共存している。ASIM側は別の15-minute actionable-step figureを採用しているが、その生成コードは確認できていない。
- まず一般形を定義する。

```tex
For a lag $\Delta t$, occupant-composition turnover was quantified using the Jaccard distance between consecutive occupant sets:
\begin{equation}
\mathrm{UTR}_{r,t}^{\Delta t}
=
1-
\frac{|S_{r,t}\cap S_{r,t-\Delta t}|}
{|S_{r,t}\cup S_{r,t-\Delta t}|}.
\end{equation}
UTR equals zero when the two sets are identical and one when they have no members in common.
```

- そのうえで、採用するfigure pipelineに応じて次のどちらか一方を主指標にする。

**A. ASIMの15-minute transition figureを採用する場合**

```tex
The RT-GCM setpoint was rounded to the nearest 0.5$^\circ$C. A 15-minute transition was classified as actionable when the absolute difference between consecutive rounded setpoints was at least 0.5$^\circ$C. The actionable-update rate was the number of actionable transitions divided by the number of valid occupied transitions in each UTR bin.
```

- この場合、`analysis25_final_15min_action_step_rate_by_15min_utr_member_size`のsource tableと生成codeを確保し、Methodの30-minute AWR式は削除またはauxiliary analysisへ移す。

**B. journal workerの30-minute window metricを採用する場合**

- `ref/a6_worker.py`の`dynamic_action_window_ratio_30m`に合わせ、現行の`\mathrm{AWR}_{r,d}^{30}`式を維持する。
- この場合、ASIMの15-minute actionable率（37\%～89--93\%）とfigureは転用せず、30-minute window outputから本文数値と図を再生成する。

- `analysis25_utr30_rolling_...` を使うweekday profileは、どちらの場合も主action-frequency metricとは別の**30-minute rolling diagnostic**として定義する。
- ASIM番号付き稿でもFig. 4(b)は本文が30-minute、captionが15-minute、filenameが`utr30`となっており不一致が残る。codeまたはsource tableを確認するまでcaptionを確定しない。
- 15分を選ぶ理由、または30-minute windowへ集約する理由を、sensor/stay-log resolutionとHVAC decision intervalのどちらに基づくか明記する。

#### 7.3.2 comfort performanceの数値を図準拠にする

- 対象: `chapters/ch4-Results.tex`
- 現在の問題文:

```tex
... with \ac{rtgcm} improvement remaining approximately \qtyrange{15}{20}{\percent} and \ac{dgcm} improvement approximately \qtyrange{5}{20}{\percent}.
```

- まずP0-1のA案を完了し、同じprobability-based source tableから数値を再抽出する。現時点ではASIM本文の数値を「検証済み」と扱わない。
- 特にASIM本文の$K=2$におけるRT-GCM 96--97\%は、実コンパイル対象の新図（目視約92--93\%）と一致しないため、journal稿へ転記しない。
- 新pipeline確定後の文章形式は次とする。角括弧はsource tableから埋める。

```tex
At $K=2$, mean person-time comfort probability ranged from [xx--xx]\% under the \ac{rtgcm}, [xx--xx]\% under the \ac{dgcm}, and [xx--xx]\% under the \ac{sgcm}. At the largest tested subgroup sizes, the corresponding ranges were [xx--xx]\%, [xx--xx]\%, and [xx--xx]\%, respectively. Relative to the fixed \qty{24}{\celsius} baseline, the \ac{rtgcm} improvement at the largest tested subgroup sizes was [xx--xx] percentage points, and its additional improvement over the \ac{dgcm} was [xx--xx] percentage points.
```

- ASIM Abstract/Discussionには、最大KでRT-GCMのbaseline比12--15 points、DGCM比6--8 pointsと書かれており、実コンパイル対象の図とも概ね整合する。ただしprovenanceとpolicy ruleの確認後にのみ採用する。
- `6--8 percentage points`はRT-GCMの**DGCMに対する追加便益**である。DGCMのbaseline差ではない。DGCMのbaseline差を併記する場合はsource tableから別に計算する。
- `improvement ratio` ではなく、baselineとの差を引き算している限り `percentage-point improvement` とする。
- `The previous subsection showed that the RTGCM maintained a 15--30 percent higher...` も、relative percentかpercentage-point differenceかを図から再確認してから修正する。

#### 7.3.3 setpoint adjustmentの値と帯の定義を直す

- 対象: `chapters/ch4-Results.tex`
- 現在のアンカー:

```tex
However, the mean value remains approximately around 1.0°C around mean occupancy(1--5) ...
```

- `analysis23_mean_occupancy_moving_quantile...` のsource tableと集計対象（changed stepsのみ）を再確認した後、次へ置換する。

```tex
The central trend decreased from about \qty{1.3}{\celsius} near a daily mean occupancy of one to roughly \qty{1.0}{\celsius} near four and \qty{0.8}{\celsius} at the upper end of the observed daily mean-occupancy range. The spread was widest at low occupancy, while the typical changed step remained above the common \qty{0.5}{\celsius} thermostat resolution.
```

- `fig:DynSpStepHist` のcaption末尾に追加する。

```tex
Bands denote the 25th--75th and 10th--90th percentiles of the plotted simulation outcomes.
```

- `error band`とは書かない。trial、room-day、changed-step observationのどれをpercentile対象にしたかは生成code確認後にcaptionへ追加する。

#### 7.3.4 UTRとactionable updateの結果を直す

- 対象: `chapters/ch4-Results.tex`
- 現在の誤記:

```tex
... when \ac{utr} reaches approximately 0.7--0.8, the action-needed window ratio reaches 90\%.
```

- 7.3.1でA（ASIMの15-minute transition metric）を採用し、source tableから再確認できた場合に限り次へ置換する。B（30-minute window metric）を採用する場合は、この数値を使わない。

```tex
The actionable-update rate increased monotonically from approximately 37\% at a 15-minute UTR near 0.05 to 63--69\% at 0.4, 77--78\% at 0.65, and 89--93\% at 0.9--1.0.
```

- その後の因果的に強い文は弱める。

```tex
The similar trends across the plotted $K$ strata indicate that the association between UTR and actionable-update frequency was not strongly modified by sampled subgroup size in this analysis. The independent contribution of instantaneous occupancy $N_{r,t}$ should be evaluated separately.
```

- `occupant replacement, rather than group size, was the dominant driver` は、$N_{r,t}$を含む比較分析を行うまでは使わない。
- Figure captionの `user turnover rate` は `occupant turnover rate` に変更する。95\% date-cluster bootstrap intervals with 1,000 resamplesの記載はASIM引継ぎメモで検証済みとされているが、採用するsource tableとresampling codeが対応することを再確認して維持する。

#### 7.3.5 対象室の説明を追加し、名称対応を固定する

- 対象: `chapters/ch3-Method.tex` の `Target Building...` subsection、現在のtarget-room列挙の直後。
- data collectionは7室、simulation resultsは4室である。本文で同じ「target rooms」と呼ぶと混乱するため、`data-collection rooms` と `simulation target rooms` を分ける。
- ASIM稿で追加された4室表の内容:

| Room ID | Job function | Seating | Floor area (m²) | Capacity |
|---|---|---:|---:|---:|
| Office 5A | Real estate development | Assigned | 221.40 | 15 |
| Office 5B | Research & development | Assigned | 163.56 | 18 |
| Shared Office 5A | Real estate development | Shared | 221.40 | 14 |
| Shared Office 5B | Building construction | Shared | 213.73 | 20 |

- この表はjournal稿にも有用だが、現行のroom名との対応を先に確定する。特に「MondayにUTR≈1.0」の室が現行稿では`R\&D Office`、ASIM稿では`Office 5A`と読めるため、表だけを先に移植しない。
- 対応確定後、Resultsの各room名、figure内label、caption、Discussionを同じIDへ一括統一する。

#### 7.3.6 location trackingの再現性を上げる

- 対象: `chapters/ch3-Method.tex` の `Individual-level location tracking log`
- 現在の冒頭文:

```tex
Individual-level location data were obtained from anonymized, timestamped records provided through the \ac{bms}.
```

- ASIM稿で開示された取得方式を反映する候補:

```tex
Anonymized individual-level location records were obtained from a face-recognition system installed at room entrances and in corridors. The timestamped zone-level records were reconstructed into continuous room-stay intervals with anonymized IDs and inferred start and end times.
```

- face recognitionというセンシティブな方式なので、直後のIRB、informed consent、administratorによる事前匿名化の説明を削らない。
- detection accuracy、missed detections、重複・overlap解消規則がAppendixにある場合は相互参照する。精度が未評価なら、その点をLimitationsに短く追加する。

#### 7.3.7 0.1°C gridと0.5°C actionable thresholdを区別する

- 対象: `chapters/ch3-Method.tex` の `where $\mathcal{T}_{\mathrm{set}}$ is the temperature grid...` の後。
- 追記候補:

```tex
The candidate setpoint grid had a resolution of \qty{0.1}{\celsius}. This fine grid was used to estimate the comfort-optimal setpoint, whereas the separate actionable-update analysis rounded setpoints to \qty{0.5}{\celsius} to test whether the predicted difference would remain relevant at a coarser thermostat resolution.
```

- 0.1°Cを実建物で実現したとは書かず、simulation assumptionとして扱う。

#### 7.3.8 occupancy densityを根拠として追加する

- コメントで問題になった説明は「large member poolでもpartial attendanceならpresent groupがregular membersやdaily attendeesと異なるため、高解像度aggregationの便益が残る」である。ただし$N_{r,t}/K$だけで示せるのはregular-member poolよりinstantaneous setが小さいことまでであり、daily attendee setとの差やcomposition mechanismは直接示せない。
- 現行journal稿はこの説明をResultsで断定しているが、対応するoccupancy-density図を本文に出していない。
- ASIMで新規追加された `occupancy_density_timeofday_k12_paper.png` をjournal側へコピーして使う場合、Conference側を変更せず、journal側のfigure directoryへ複製する。
- 挿入先: `fig:ComfAgentic` の直後、comfort performance paragraphの前。
- 本文候補:

```tex
Decision-time occupancy density, $N_{r,t}/K$, was generally below one and varied by room and time of day, indicating that the instantaneous occupant set was often smaller than the sampled regular-member pool.
```

- Discussionでのみ次のように解釈する。

```tex
This pattern is consistent with partial attendance as one reason why attendance-aware aggregation can remain beneficial at larger $K$; however, $N_{r,t}/K$ alone does not isolate changes in occupant composition or establish the mechanism.
```

- RT-GCMとDGCMの差を説明するなら、$|S_t\triangle A_d|$、Jaccard distance、またはwithin-day composition turnoverの直接分析を追加する。図を追加しない場合はResultsでは観測事実だけを書く。

#### 7.3.9 Abstractを評価対象と定量結果が分かる形へ直す

- 実際にコンパイルされるAbstractは `chapters/abstract.tex` ではなく `Draft_2026-Jan.tex` 内の直書き部分である。片方だけ修正すると反映されないため、`\input{chapters/abstract.tex}`へ一本化するか、両方を同期する。
- `room-level setpoint` はoccupant-centric control全体の定義ではなく、本研究が扱うzone-level actuatorとして書く。
- `mean occupancy approaches four to five occupantsでbenefit becomes limited` は、現稿に対応図がなくASIMでは撤回されたため、図を復活させない限りAbstractから削除する。
- Abstractに最低限入れる内容:
  - 評価対象: raw predicted person-time comfort probabilityまたは明示的に命名したnormalized score、baselineに対するpercentage-point difference、RT-GCM setpoint-change magnitude、採用した15-minute transitionまたは30-minute window metric
  - データ: 39 PCM participants、responses retained for PCM fitting/analysis、four weeks、four simulation rooms。2,608がraw収集数か20-minute除外後の保持数かを確認する。
  - 主結果: P0-1と7.3.1で確定したsource tableから、policy ranking、最大Kのbaseline/DGCM差、setpoint step、UTR-actionable rateを記載する。ASIM記載の12--15 points、6--8 points、約0.8°C、約37\%から約90\%は確認候補値であり、そのまま固定しない。
  - 限定: predicted comfort / simulationであり、field-delivered comfortやenergy savingではない

#### 7.3.10 DiscussionとConclusionを結果に対応させる

- `chapters/ch5-Discussion.tex` 冒頭は、`value of temporal resolution`だけでなく、実在室・動的occupancyとの関係を明示する。ただしinteraction / multivariable effectを示したように書かない。A案完了後の候補:

```tex
Using observed occupancy logs and field-derived PCMs under a common group-to-setpoint rule, predicted comfort performance varied across subgroup-size and occupancy conditions, while actionable-update frequency increased with occupant-composition turnover.
```

- 先行研究との接続は現稿のJungとOnoだけで終わらせず、Introductionで使う実装障壁、dynamic occupancy、trackingの文献もDiscussionの該当主張に再接続する。ただし、引用数を増やすこと自体を目的にせず、本研究の結果をsupport/contrastする位置に置く。
- ASIMで新規導入された `wang_enhancing_2026` は、large-group preference diversityとmaximum satisfactionの方向性を示す背景に使える。ただし対象は主に10人と50--500人の比較で、本研究の$K$ range、PCM、outcomeとは尺度も指標も異なる。直接的な数値支持や同一現象の再現とは書かない。journalの`references.bib`には現時点で同keyがないため、採用時にASIM側のBibTeX entryをコピーする。
- `chapters/ch6-Conclusion.tex` は現在定量値がない。P0-1と7.3.1の検証後、以下の順で追記する。
  1. 新しいsource tableの全room/Kセルで確認できた場合に限り、RT-GCMがhighest predicted mean CPだったと記載する。
  2. 最大Kのbaseline差とDGCM差（ASIM記載候補は12--15 points、6--8 points）。
  3. changed-stepのhigh mean occupancy側の値（ASIM記載候補は約0.8°C）。
  4. 採用した15-minute transitionまたは30-minute window metricの低UTRから高UTRへの変化。異なる時間定義の数値を混在させない。
  5. 以上はcomfort-only simulationの結果であり、energy/HVAC dynamics/privacy/costを未評価。

### 7.4 CSV 17件のjournal稿への適用判定

| No. | 指摘の要点 | journal稿への判定 | 対応 |
|---:|---|---|---|
| 1 | OCCをsetpoint変更と同一視していないか | 必須 | Abstract/Introで、setpoint selectionは本研究で扱うOCC actuationの一形態と限定する。 |
| 2 | titleにある語をkeywordで重複させない | 要対応 | journal稿はtitle/highlights/keywordsが`XXX`。投稿先guideに従い、title確定後に非重複語を選ぶ。 |
| 3 | affiliationのpostcode不要では | venue依存 | Elsevier CASのaffiliation fieldなのでASIM判断を転用せず、target journalのguide確認後に決める。 |
| 4 | simulationで何を評価したか不明 | 必須 | Abstractにpredicted comfort performanceとcontrol-update burdenを明記する。 |
| 5 | presence/absence detectionが曖昧 | 必須 | face-recognition system、設置位置、stay reconstruction、匿名化をMethodに記載する。 |
| 6 | 建物名・会社名は不要 | venue・匿名化方針依存 | double-blind/author policyを確認し、必要ならproper nounを外す。Singapore office building、用途、HVAC、room typologyは科学的文脈として残す。funding/conflict disclosureとは分ける。 |
| 7 | four roomsの一覧が必要 | 必須 | simulation 4室表を追加し、data collection 7室と区別する。 |
| 8 | partial-attendance解釈の根拠がない | 必須 | density図はpartial attendanceの根拠に限る。composition-difference analysisを追加するか、便益機序の主張をDiscussionで弱める。 |
| 9 | どのFigureが根拠か明記 | 必須 | occupancy-density figure番号を明記する。ただしRT-vs-DGの機序には別のcomposition指標が必要。 |
| 10 | 15-minuteを選んだ理由 | 科学的理由・感度分析が必要 | data/control上の理由を確認し、可能なら15/30-minute sensitivityを示す。できなければLimitationsへ。 |
| 11 | setpoint trendにerror bandsがあるか | 必須 | 25--75\%、10--90\% percentile rangesと定義し、集計単位を確認する。error / population CIと呼ばない。 |
| 12 | shared/assigned roomがFigureで識別不能 | 必須 | room table、figure legend/caption、本文room IDを一致させる。 |
| 13 | $K$ではなくactual occupancyの影響は | 追加分析推奨 | $N_{r,t}$またはoccupancy densityで層別。未実施ならdominant-driver主張を弱める。 |
| 14 | 大きい$K$でもRT-GCMが10 points超改善 | 必須 | probability-based同一ruleの再解析で再確認後、最大Kのbaseline差をResults/Discussion/Conclusionに明記する。ASIM記載値は12--15 points。 |
| 15 | Discussionで先行研究を十分再訪していない | 推奨 | Jung/Onoに加え、dynamic occupancy、tracking、implementation barrierの文献を該当結果へ接続する。 |
| 16 | temporal resolutionよりreal/dynamic occupancyでは | 必須 | independent variableはaggregation resolution、適用条件はrealized/dynamic occupancyと書き分ける。 |
| 17 | Conclusionに定量結果が必要 | 必須 | comfort、RT-vs-DGCM、setpoint step、UTR-action rateの代表値を追加する。 |

### 7.5 ASIM稿から移植できる新規情報・データ

#### provenance確認なしで移植できる記述情報

- 39 participants、2,608 valid survey responses、four-week record、four simulation rooms。
- face-recognition systemの設置位置、4室のfloor area / seating capacity / seating type。ただしroom mappingを確定してから使う。
- limitationsとして、predicted comfort、one building/four weeks、random PCM assignment、energy/HVAC response/integration cost未評価、mean CPはfairnessを保証しないこと。

#### 生成元を確認した後にのみ移植する定量結果

- 各policyのpredicted mean comfort probability range。特に$K=2$はASIM新図と本文が不一致なので再抽出必須。
- ASIM記載の、最大tested $K$でのRT-GCM baseline比12--15 percentage points、RT-GCMのDGCM比6--8 percentage points。
- daily mean occupancyが約1、4、観測上限側のときのchanged-step central trend: 約1.3、1.0、0.8°C。
- 15-minute transition metricを採用する場合のUTR bin別actionable rate: 約37\%、63--69\%、77--78\%、89--93\%。
- 0.1°C candidate setpoint gridと0.5°C actionable thresholdの役割分担。
- setpoint-change bandの定義: 25--75\%と10--90\% percentile ranges。

#### ファイルを複製して追加する候補

- `figures/occupancy_density_timeofday_k12_paper.png`: partial attendanceの根拠図。元集計とinterval定義確認後にjournal側へcopyする。
- `figures/TargetRooms.tex`: 4室表。journalのtable styleへ変換し、room mapping確定後にcopyする。
- `wang_enhancing_2026` BibTeX entry: large-group preference diversityのDiscussion用。原指標との差を説明して使う。

#### 解釈としてのみ使い、結果のように書かない

- SGCM / DGCM / RT-GCMをdeployment hierarchyとして使う提案。
- UTRでreal-time updateをgateし、deadband/minimum hold timeでcyclingを抑える提案。
- sensing reliability、latency、privacy、costを含む実装条件。

### 7.6 現時点では移植しない内容

- 現行journalのbinary comfort図と、その図から読んだ改善値。Methodのprobability outcomeと一致しない。
- ASIMのprobability-labeled comfort図および本文数値。全policyのsetpoint ruleと生成pipelineが確認できるまでは、移植候補に留める。
- `SGCM improvement crosses/approaches zero around K≈6--8`: 採用するprobability-based同一rule runで再確認するまで移植しない。
- `mean occupancy 4--5でRT-GCM benefitがlimited/zeroに近づく`: 対応するcontour図を本文に出していないため、Abstractへ戻さない。
- `occupant replacement was the dominant driver`: actual occupancyを含む比較がないため断定しない。
- room-name置換: ASIM表、ASIM Results、現行journal Resultsの間でMonday peakのroom対応が未確定。
- `15-minute interval was selected because ...`: 理由がsource filesに記載されていないため、推測で補わない。
- postcode削除: conference format固有の可能性がある。
- energy savings、field-delivered comfort、cost effectiveness: 本研究では直接評価していない。

### 7.7 反映順

1. P0-1のA案を実装・確認し、probability-basedかつ全policy同一ruleのsource tableと図を確定する。
2. notebook/codeと最終figureから15-minute/30-minuteの各指標の役割とroom mappingを確認する。
3. Methodのcomfort metric、policy rule、time grid、UTR、actionable metricを確定した実装に合わせて修正する。
4. Resultsの数値、percentage point、band定義、room/captionをsource tableから修正する。
5. occupancy-density図と4室表の採否を決める。
6. Abstract、Discussion、Conclusionを修正済みResultsに合わせる。
7. `Draft_2026-Jan.tex`のtitle/highlights/keywordsとAbstract入力方式を整理する。
8. 全文で `user turnover rate` を `occupant turnover rate` に統一する。
9. コンパイル後、本文・caption・式・図内labelのmetric、時間幅、room ID、単位、割合表現を目視確認する。

### 7.8 独立レビュアーエージェントの判定

- 独立レビュアーはASIM Conference側とjournal側を参照のみで確認し、ファイル編集は行っていない。
- 総合判定: 第7章の方向性とA案は妥当。ただし、単なるconference文章の移植ではなく、comfort metric、policy rule、sampling population、estimand、uncertainty、time-step provenanceの監査を先に行う必要がある。
- CSV 17件の分類:
  - 必須: No. 1, 4, 5, 7, 8, 9, 11, 12, 14, 16, 17
  - 追加分析推奨: No. 13, 15
  - 投稿先・匿名化方針依存: No. 2, 3, 6
  - 科学的理由または感度分析が必要: No. 10
- A案を推奨する決定的な理由: 現在の実装ではaggregation resolutionとsetpoint-selection algorithmが交絡している。全policyへ同じ `group curves -> common-grid argmax -> present occupantsでscore` を適用して初めて、主な比較をrepresented groupの時間解像度へ限定できる。
- Reviewer convergence criteria: 共通ruleの再生成、同一manifest/source tableからの全図作成、数値監査、Method確定、Results更新の後に、Abstract / Discussion / Conclusionを更新する。

### 7.9 journal側へコピー済みの移植候補

- 保存先: `ref/asim2026_import_candidates/`
- ASIM Conference側は変更せず、次をjournal repository内へコピーした。
  - occupancy-density図
  - probability-labelled comfort図（provenance確認前の保留候補）
  - setpoint adjustmentのcompact 2図
  - UTR/actionのcompact 2図
  - compact simulation workflow
  - 4室表 `TargetRooms.tex`
  - 実コンパイル対象のmain TeXと番号付き5 section、および未コンパイルの補足`appendix-draft.tex`のsnapshot
  - `wang_enhancing_2026`の単独BibTeX entry
  - unresolved-comment CSV、content-selection ledger、ASIM handover noteのsource snapshot
- 各ファイルの移植目的、検証条件、既存journal図とのSHA-256重複、copy時点のhashは同フォルダの`README.md`に記録した。
- active manuscriptからはまだ参照していない。room mapping、metric、policy rule、trial数、time resolutionを確定後、必要なファイルだけ`pic/`または本文tableへ昇格する。
