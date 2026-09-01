# Introduction / Discussion 文献拡充案

## このファイルの位置づけ

- 本ファイルは提案書であり、本文への変更は一切適用していない。
- chapters/ch1-Intro.tex、chapters/ch5-Discussion.tex、references.bib は作業開始前の状態へ戻している。
- 以下の英文は、そのまま採用するための確定稿ではなく、挿入位置と論旨を確認するための候補文である。
- 文献候補は Zotero の添付本文または索引済み全文まで確認した。抄録だけで採用した文献はない。
- Chapter 8 の修正結果を前提とし、旧 SGCM の「K=5--8 でゼロに近づく／固定ベースラインに収束する」という解釈は採用しない。
- Figure 1 の指標が comfort probability か binary comfort-range coverage かは未確定であるため、指標名に依存する文は保留する。

## Introduction の Expansion 案

### I-1. Thermal comfort と productivity の関係を、因果ではなくエビデンスの種類に沿って補足する

**挿入位置**  
冒頭段落の末尾、現在の “...a significant relationship between indoor environmental conditions and occupant productivity.” の後。

**目的**  
現状は thermal comfort が productivity と health を直接改善するようにも読める。レビューと実オフィス研究を追加し、関連は示される一方、研究デザインや自己申告指標により解釈が異なることを明示する。

**根拠文献**  
bueno_evaluating_2021（systematic review）、lipczynska_thermal_2018（6週間の実オフィス研究）。

**追加英文案**

~~~latex
The evidence should nevertheless be interpreted with care because the reported relationship varies with study design, exposure range, and the productivity measure used \cite{bueno_evaluating_2021}. In a six-week tropical-office field study, self-reported concentration, alertness, and productivity remained high across the tested acceptable conditions and were more closely related to individual thermal satisfaction than to room temperature alone \cite{lipczynska_thermal_2018}. These findings support treating thermal comfort as an important occupant outcome without assuming that a particular setpoint will directly improve productivity.
~~~

**注意**  
health まで残す場合は kaushik_effect_2022 がその主張を直接支えるか再確認する。十分でなければ、冒頭の health は削るか、健康アウトカムを直接扱う別レビューを追加する。

### I-2. PMV の限界から PCM への論理的な橋渡しを加える

**挿入位置**  
“This one-size-fits-all approach is inherently limited in achieving widespread occupant satisfaction.” の後。

**目的**  
PMV が集団平均モデルであることと、本研究が個人別モデルを用いる理由をつなぐ。

**根拠文献**  
wang_individual_2018、cheung_analysis_2019、kim_personal_2018-1。

**追加英文案**

~~~latex
This limitation reflects a difference in prediction target: the \ac{pmv} model represents the mean response of a population, whereas a personal comfort model aims to predict the response of a specific individual. Reviews and field-data analyses have documented substantial between-person variation and reduced predictive accuracy when population models are applied to individuals \cite{wang_individual_2018,cheung_analysis_2019,kim_personal_2018-1}. Personal comfort models address this limitation by learning an individual's response from personal feedback and contextual data, although their data requirements, updating procedures, and integration with building controls remain application-dependent \cite{kim_personal_2018-1}.
~~~

### I-3. OCC の定義に「どの occupant information を、どの解像度で使うか」を加える

**挿入位置**  
IEA EBC Annex 79 の OCC 定義文の後。

**目的**  
後半の static / daily / real-time aggregation を、OCC 一般の情報解像度の議論へ接続する。

**根拠文献**  
nagy_ten_2023、wagner_international_2024。

**追加英文案**

~~~latex
In this context, occupant information can range from presence and count to activity and identity, and its usefulness depends on both spatial and temporal resolution \cite{nagy_ten_2023}. Higher information resolution can enable more individualized control, but it also increases sensing, data-management, integration, and privacy requirements.
~~~

### I-4. sensing--learning--control chain が実装上どこで失敗し得るかを補足する

**挿入位置**  
“...translates the model outputs into \ac{hvac} actions” と説明する段落の末尾。

**目的**  
OCC の概念説明だけでなく、field deployment が限定的な理由を複数のレビューで裏付ける。

**根拠文献**  
obrien_key_2020、nagy_ten_2023、soleimanijavid_challenges_2024、zhang_impact_2023。

**追加英文案**

~~~latex
The performance of this chain depends not only on model accuracy but also on sensing quality, communication with the building automation system, controller design, and local operating conditions \cite{zhang_impact_2023}. Reported barriers to broader deployment include data availability and management, interoperability with existing systems, operator capacity, scalability, privacy, and validation across buildings and climates \cite{obrien_key_2020,nagy_ten_2023,soleimanijavid_challenges_2024}.
~~~

### I-5. shared space で group representation が必要になる根拠を追加する

**挿入位置**  
“...a single room-level \ac{hvac} setpoint must represent multiple occupants at the same time.” の後。

**目的**  
単一 occupant の feedback をそのまま room control に使えない理由と、collective objective の必要性を先行研究で示す。

**根拠文献**  
schumann_predicting_2010、topak_collective_2023。

**追加英文案**

~~~latex
Earlier work on shared offices noted that responding directly to one person's feedback implicitly assumes either single occupancy or identical preferences among occupants \cite{schumann_predicting_2010}. More recent collective-comfort studies likewise frame shared-zone control as a problem of combining heterogeneous preferences under a common environmental decision \cite{topak_collective_2023}.
~~~

### I-6. ABW の利点を前提化せず、mixed evidence と実際の利用変動を加える

**挿入位置**  
“Meanwhile, the rise of remote and hybrid work...” で始まる段落の後半。remote/hybrid work の普及文と、occupants arrive, leave, and move の文の間が自然。

**目的**  
ABW の効果は一様ではないことを示したうえで、研究上重要な事実である時空間的な workstation use の変化を実測研究で支える。

**根拠文献**  
engelen_is_2019、gocer_overlaps_2022。

**追加英文案**

~~~latex
Evidence on activity-based working is mixed: systematic-review findings include benefits for some interaction, control, and satisfaction outcomes, but disadvantages for concentration and privacy and equivocal findings for health \cite{engelen_is_2019}. A twelve-month case study of an \ac{abw}-supportive office documented time-varying workstation use and movement among zones, with utilisation patterns differing by season and by spatial markers associated with expected indoor environmental conditions \cite{gocer_overlaps_2022}.
~~~

**注意**  
Gocer et al. は IEQ を縦断測定して movement の原因を同定した研究ではないため、「thermal conditions caused movement」とは書かない。

### I-7. occupancy count と occupant identity/composition の違いを分類体系で支える

**挿入位置**  
“Dynamic occupancy should therefore be understood not only as a change in the number of people in a room, but also as a change in who is present.” の後。

**目的**  
本研究の中心である「人数が同じでも、誰がいるかが違う」という区別を OCC のデータ解像度へ位置づける。

**根拠文献**  
nagy_ten_2023。

**追加英文案**

~~~latex
This distinction corresponds to different grades of occupant information: occupancy count describes how many people are present, whereas identity-level information is needed to associate the present group with person-specific comfort profiles \cite{nagy_ten_2023}. Count data alone therefore cannot determine whether the group comfort representation should change when one occupant replaces another.
~~~

### I-8. occupancy sensing の選択肢に、精度・遅延・privacy の trade-off を加える

**挿入位置**  
“Recent IoT and building-management technologies...” で列挙している PIR、CO2、Wi-Fi の文の後。

**目的**  
real-time composition tracking が技術的に利用可能というだけでなく、各方式が異なる情報粒度と制約を持つことを示す。

**根拠文献**  
yang_review_2016、zafari_survey_2019、brambilla_potential_2021、wang_modeling_2017、obrien_key_2020。

**追加英文案**

~~~latex
These modalities do not provide equivalent information. Reviews identify trade-offs among counting capability, spatial resolution, latency, cost, and privacy for PIR, CO$_2$, camera, WLAN, and related approaches \cite{yang_review_2016,zafari_survey_2019,brambilla_potential_2021}. For example, CO$_2$-based inference can respond slowly to changes, while Wi-Fi-based inference can be affected by unstable signals and device-to-occupant behaviour \cite{wang_modeling_2017}. Identity-level tracking introduces an additional privacy and data-governance burden \cite{obrien_key_2020,nagy_ten_2023}.
~~~

### I-9. group size だけでなく preference heterogeneity が aggregation に影響することを加える

**挿入位置**  
Shared-space GCM resolution subsection の “...simply averaging preferences or applying a single \ac{pcm} may fail to represent the group.” の後。

**目的**  
K の大きさだけでなく、内部の preference diversity が collective comfort を左右することを示す。

**根拠文献**  
schumann_predicting_2010、topak_collective_2023、jung_energy_2020、wang_enhancing_2026。

**追加英文案**

~~~latex
The difficulty is shaped by both group size and preference heterogeneity. Shared-space studies have shown that collective comfort depends on how conflicting individual preferences are represented and combined, rather than on occupancy count alone \cite{schumann_predicting_2010,topak_collective_2023}. Simulation studies further suggest that the combined energy-and-comfort benefit of integrating personal models can diminish as more occupants share a thermal zone \cite{jung_energy_2020}, while the potential maximum satisfaction rate may also decrease for larger groups \cite{wang_enhancing_2026}.
~~~

**注意**  
Jung et al. は comfort だけを独立に評価した根拠としてではなく、energy-and-comfort の統合結果として記述する。

### I-10. research gap を「誰を、いつ GCM に含めるか」と明文化する

**挿入位置**  
field studies の表を導入する段落で、静的 attendance assumption を説明した後。

**目的**  
既往研究の不足と本研究の three aggregation levels を一文でつなぐ。

**根拠文献**  
nagy_ten_2023、schumann_predicting_2010、topak_collective_2023。

**追加英文案**

~~~latex
The unresolved design question is therefore not only how several \acp{pcm} should be aggregated, but which occupants should enter that aggregation at each control decision. Static membership, daily attendance, and real-time presence represent progressively finer temporal resolutions of the same group-representation problem, with corresponding increases in sensing and integration burden \cite{nagy_ten_2023}.
~~~

### I-11. Focus subsection の outcome 記述を、未確定の Figure 1 指標から独立させる

**対象位置**  
“Specifically, the analysis compares...” の箇条書き (1) と、最後の relationship に関する記述。

**提案**  
Figure 1 の指標確定前は、本文の “mean comfort probability” を増補しない。必要なら暫定的に “predicted comfort outcome” とし、UTR は causal effect ではなく association と記述する。

**指標確定後の候補**

~~~latex
Specifically, the analysis compares \ac{sgcm}, \ac{dgcm}, and \ac{rtgcm} policies in terms of: (1) the selected predicted-comfort metric and its improvement relative to a fixed \qty{24}{\celsius} baseline; (2) the setpoint adjustment magnitude required by the \ac{rtgcm}; and (3) the association between occupancy dynamics, especially \ac{utr}, and the frequency of actionable control updates.
~~~

## Discussion の Expansion / 修正案

### D-1. Jung et al. と Wang et al. の比較を、過度に数値一致させず方向性として述べる

**対象位置**  
最初の subsection の冒頭段落。現在の “converging to nearly two percent...” を含む部分。

**目的**  
異なるモデル、評価指標、条件を用いた先行研究との比較は、同じ数値に収束したとするより方向性の一致として示す。

**根拠文献**  
jung_energy_2020、wang_enhancing_2026。

**置換英文案**

~~~latex
Simulation studies indicate that the combined energy-and-comfort benefit of integrating personal models can diminish as more occupants share a thermal zone \cite{jung_energy_2020}. A separate stochastic simulation likewise reported lower potential maximum satisfaction rates for larger groups \cite{wang_enhancing_2026}. These studies support a directional expectation that aggregation can dilute the influence of individual preferences, although their numerical results are not directly comparable with the present analysis because the control strategies, populations, and outcome definitions differ.
~~~

### D-2. corrected SGCM と矛盾する旧記述を、Chapter 8 の結果に沿って修正する

**対象位置**  
次の二つの active sentence/block。

1. “...decreases as subgroup size increases and approaches zero around subgroup sizes of five to seven.”
2. “The SGCM here follows the same directional pattern, crossing zero at K approximately 6--8.”

**目的**  
corrected composite-curve argmax の結果では、largest K でも SGCM は fixed baseline より 5.1--5.5 percentage points 高い。したがって zero crossing / convergence は使用できない。

**置換英文案（指標名に依存しない暫定版）**

~~~latex
The corrected \ac{sgcm} results show a decline in improvement as subgroup size increases, but they do not converge to or cross the fixed baseline within the tested range. The higher-resolution policies retain the ordering \ac{rtgcm}, \ac{dgcm}, \ac{sgcm}, and fixed baseline at larger subgroup sizes. The present analysis therefore supports the same broad dilution mechanism reported in earlier group-size studies, while showing that the static group representation still retains a positive advantage under the corrected setpoint-selection rule.
~~~

**重要**  
これは参考文献の expansion ではなく、Chapter 8 と本文の整合性を保つための必須修正候補。ユーザー承認なしには TeX へ反映しない。

### D-3. largest K の差を示す文は、Figure 1 の metric 決定後だけ追加する

**挿入位置**  
D-2 の修正文の後。

**追加英文案**

~~~latex
At the largest tested subgroup size in each room, \ac{rtgcm} remained 5.5--6.3 percentage points above \ac{dgcm}, whereas \ac{sgcm} remained 5.1--5.5 percentage points above the fixed \qty{24}{\celsius} baseline.
~~~

**保留条件**  
percentage points が何の差かを、comfort probability または comfort-range coverage のどちらかに確定してから、文中に明記する。

### D-4. Ono et al. の resolution mismatch と、本研究の 0.5 degree C threshold を分離する

**対象位置**  
“This finding also relates to the resolution-mismatch argument...” の段落。

**目的**  
Ono et al. が検証したのは occupant-resolution と control-resolution の対応であり、0.1 degree C と 0.5 degree C の thermostat step の比較そのものではない。

**根拠文献**  
ono_effects_2022。

**置換・追加英文案**

~~~latex
The \qty{0.5}{\celsius} threshold is an operational analysis choice in the present study and should not be interpreted as a threshold established by prior work. At a different dimension of resolution, Ono et al.~\cite{ono_effects_2022} showed through simulation that the occupant resolution of a comfort model should be commensurate with that of the HVAC control it informs. Together, these points distinguish model-information resolution from numerical setpoint resolution and from the physical ability of an HVAC system to realise a requested change.
~~~

### D-5. actionable setpoint difference と field deployability の間に実装エビデンスを加える

**挿入位置**  
0.5 degree C actionable threshold を説明した段落の後。

**目的**  
simulation 上で差があることと、実設備で comfort / energy benefit が得られることを区別する。

**根拠文献**  
jiang_occupied_2023、kong_hvac_2022、zhang_impact_2023。

**追加英文案**

~~~latex
An actionable setpoint difference in simulation does not by itself establish field deployability. Long-term and side-by-side field studies show that realised outcomes can depend on occupancy-sensor accuracy, communication with the building automation system, damper or actuator cycling, outdoor conditions, controller design, and local operating constraints \cite{jiang_occupied_2023,kong_hvac_2022,zhang_impact_2023}. Closed-loop evaluation is therefore required to determine whether the predicted comfort advantage persists after sensing delay and HVAC dynamics are introduced.
~~~

### D-6. occupant adaptation の遅れを limitation として補足する

**挿入位置**  
D-5 の直後、または Limitations の HVAC response delay の文の後。

**目的**  
モデルが直ちに最適 setpoint を選んでも、人の行動や知覚が即時に変化するとは限らないことを明示する。

**根拠文献**  
li_study_2022。

**追加英文案**

~~~latex
Occupant responses may also lag changes in environmental stimuli. Field observations of shading behaviour, although not a direct test of temperature-setpoint response, demonstrate that adaptive actions can occur with temporal delay \cite{li_study_2022}. Future closed-loop evaluation should therefore represent both HVAC response time and occupant adaptation rather than assuming an instantaneous response.
~~~

### D-7. UTR を count では捉えられない composition replacement の指標として位置づける

**挿入位置**  
“Mean occupancy and occupancy variability describe how many people are present...” の後。

**目的**  
UTR の新規性を説明しつつ、因果効果や普遍的優位性までは主張しない。

**根拠文献**  
nagy_ten_2023、wang_modeling_2017。

**追加英文案**

~~~latex
Occupant-data taxonomies distinguish count from identity because the same count can correspond to different sets of people and therefore different personal comfort profiles \cite{nagy_ten_2023}. Common count-oriented sensing approaches can estimate occupancy patterns but do not necessarily identify which profiles have been replaced \cite{wang_modeling_2017}. In the present simulation, \ac{utr} is consequently interpreted as an indicator associated with composition replacement and control-update frequency, not as a causal determinant of comfort improvement.
~~~

### D-8. SGCM / DGCM / RT-GCM の deployment hierarchy を「検証すべき仮説」として弱める

**対象位置**  
“The three aggregation levels can consequently be treated as a deployment hierarchy...” で始まる段落。

**目的**  
one-building simulation から普遍的な実装 recommendation や UTR threshold を導かない。

**根拠文献**  
gocer_overlaps_2022、nagy_ten_2023、obrien_key_2020、zafari_survey_2019。

**置換英文案**

~~~latex
The three aggregation levels suggest a deployment hypothesis rather than a universal hierarchy. A static representation may be adequate in zones with stable membership, daily updating may offer a lower-complexity response to attendance variation, and real-time updating may be most useful when within-day composition changes frequently. Longitudinal utilisation research shows that movement and workstation use vary by season and spatial context \cite{gocer_overlaps_2022}, while occupant-information reviews emphasise that higher resolution brings additional infrastructure, privacy, and data-management requirements \cite{nagy_ten_2023,obrien_key_2020,zafari_survey_2019}. The observed \ac{utr} ranges should therefore be validated locally rather than treated as transferable thresholds.
~~~

### D-9. control-update gating を提案する場合は、deadband と hold time を future work として扱う

**挿入位置**  
“\ac{utr} can gate real-time updates...” の文の後。

**追加英文案**

~~~latex
Such gating remains a control-design hypothesis in the present study. Future experiments should test alternative deadbands, minimum hold times, and update intervals to quantify the trade-off among predicted comfort, actuator cycling, energy use, and responsiveness.
~~~

### D-10. Limitations を simulation validity、fairness、field validation の三点で拡張する

**挿入位置**  
Limitations subsection の末尾。

**目的**  
現状の one-building、random PCM reassignment、closed-loop 未検証に加えて、aggregate mean では個人間の不公平を評価できない点と simulation-to-field gap を明示する。

**根拠文献**  
hobson_workflow_2021、jiang_occupied_2023、zhang_impact_2023。

**追加英文案**

~~~latex
In addition, the group-level mean objective does not reveal whether an improvement is shared across occupants or achieved at the expense of a consistently disadvantaged minority. Individual-level distributions, worst-case comfort, and fairness-oriented objectives should therefore be examined alongside the mean. Simulation enables controlled comparison of OCC strategies, but its conclusions remain conditional on model inputs and cannot establish occupant acceptance or field performance by itself \cite{hobson_workflow_2021}. A stronger validation design would pair each person's observed movement with that person's comfort model and then evaluate the selected policy in closed-loop operation, including sensing error, communication failures, HVAC dynamics, energy use, and occupant feedback \cite{jiang_occupied_2023,zhang_impact_2023}.
~~~

## 文献候補一覧と採用理由

| BibTeX key | Evidence type | Introduction で支える内容 | Discussion で支える内容 | 推奨 |
|---|---|---|---|---|
| lipczynska_thermal_2018 | 6-week office field study | thermal satisfaction と self-reported performance の関係 | -- | I-1 |
| kim_personal_2018-1 | review / PCM framework | PMV と PCM の prediction target の違い | -- | I-2 |
| nagy_ten_2023 | Annex 79 synthesis | OCC 定義、presence/count/activity/identity、情報解像度 | count と identity、deployment burden | I-3, I-4, I-7, I-10; D-7, D-8 |
| zhang_impact_2023 | private-office field implementation | sensing--model--control chain | controller・weather・field constraints | I-4; D-5, D-10 |
| schumann_predicting_2010 | shared-office method / evaluation | single feedback と shared-zone representation | preference aggregation | I-5, I-9 |
| topak_collective_2023 | CFD / PCM simulation | heterogeneous collective comfort | preference diversity | I-5, I-9 |
| obrien_key_2020 | Annex 79 position / review | scalability、standards、privacy | identity-level sensing burden | I-4, I-8; D-8 |
| engelen_is_2019 | systematic review | ABW の mixed outcomes | -- | I-6 |
| gocer_overlaps_2022 | 12-month utilisation case study | time-varying movement and workstation use | context dependence of deployment | I-6; D-8 |
| yang_review_2016 | sensing review | modality-specific limitations | sensing burden | I-8 |
| wang_modeling_2017 | Wi-Fi field experiment / model | unstable signal と device behaviour | count data の限界 | I-8; D-7 |
| jiang_occupied_2023 | 2-year field experiment | -- | sensing error、BACnet、cycling、privacy | D-5, D-10 |
| kong_hvac_2022 | side-by-side field experiment | -- | sensor accuracy と outdoor conditions | D-5 |
| li_study_2022 | field observation / behaviour model | -- | adaptive behaviour の時間遅れ（shading の研究として限定） | D-6 |
| hobson_workflow_2021 | building simulation workflow | -- | simulation-to-field limitation | D-10 |

## BibTeX について

- 上記 15 文献はすべて現在の references.bib に既存のため、今回 BibTeX entry は追加・修正していない。
- Kim, Schiavon, and Brager (2018) の review は、この repository では kim_personal_2018-1 を使う。kim_personal_2018 は別の Kim et al. 論文に割り当てられている。
- lipczynska_thermal_2018 と schumann_predicting_2010 には補完可能な publication metadata があるが、本文を元に戻す依頼に合わせ、今回は references.bib に反映していない。必要なら別途、書誌情報だけの変更として提案・確認する。
- references.bib には本提案と無関係な既存の duplicate-key group が 17 組ある。今回の範囲では変更しない。

## 推奨する反映順序

1. Figure 1 の指標を comfort probability / comfort-range coverage のどちらにするか確定する。
2. Discussion の旧 SGCM zero-crossing / convergence 記述について、D-2 と D-3 の修正内容を確定する。
3. Introduction は I-1、I-2、I-5、I-7、I-10 を優先し、研究動機の論理線を先に強化する。
4. Discussion は D-1、D-4、D-5、D-7、D-10 を優先し、先行研究との比較と simulation-to-field limitation を強化する。
5. 追加量が多すぎる場合は、sensing の詳細（I-8）と deployment hierarchy（D-8）を短縮する。
6. 採用する案が決まった後にのみ、TeX と BibTeX を編集し、Undefined citation、重複キー、図表指標、Abstract / Results / Conclusion との整合性を確認する。

## 未解決事項

1. Figure 1 が raw “No change” probability と binary comfort-range coverage のどちらを示すか。
2. Method と code で normalized PCM curve と raw PCM curve のどちらを用いるか。
3. 15-minute と 30-minute の turnover / actionable-control metric をどう統一するか。
4. four-room name mapping が正しいか。
5. trial counts と Figure 1 error-bar definition をどの記述に統一するか。
6. Abstract、Results、Conclusion に残る旧 SGCM 数値・zero-convergence 解釈をどのタイミングで修正するか。
