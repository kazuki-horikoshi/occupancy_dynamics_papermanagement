# Introduction / Discussion 文献拡充案

## このファイルの位置づけ

- 本ファイルは提案書であり、本文への変更は一切適用していない。
- chapters/ch1-Intro.tex、chapters/ch5-Discussion.tex、references.bib は作業開始前の状態へ戻している。
- 以下の英文は、そのまま採用するための確定稿ではなく、挿入位置と論旨を確認するための候補文である。
- 文献候補は Zotero の添付本文または索引済み全文まで確認した。抄録だけで採用した文献はない。
- Chapter 8 の修正結果を前提とし、旧 SGCM の「K=5--8 でゼロに近づく／固定ベースラインに収束する」という解釈は採用しない。
- Figure 1 の指標が comfort probability か binary comfort-range coverage かは未確定であるため、指標名に依存する文は保留する。

## Introduction の Expansion 案

### Introduction 全体の推奨論理順序

個別の文献を順に差し込むだけでは、定義前の用語使用や、指示語の参照先が曖昧になる可能性がある。Introduction では、次の順序で概念を一段ずつ導入するのが自然である。

| 順序 | 説明する概念 | 次の概念への役割 |
|---|---|---|
| 1 | Thermal comfort と occupant outcomes | 研究対象の重要性を示す |
| 2 | 従来の \ac{pmv} と population-average prediction の限界 | 個人差を扱う必要性を示す |
| 3 | \ac{pcm} の定義 | individual-level comfort information を初めて導入する |
| 4 | \ac{occ} の定義 | 個人情報を building operation に利用する枠組みを導入する |
| 5 | sensing--learning--control の three-layer chain | occupant information が制御へ届く仕組みを示す |
| 6 | occupant information の種類と解像度 | presence/count と identity/composition の違いを予告する |
| 7 | shared space と \ac{gcm} | 複数の \acp{pcm} を一つの room-level decision にまとめる問題を示す |
| 8 | \ac{abw} と dynamic occupancy | なぜ group membership が時間変化するかを示す |
| 9 | occupancy count と occupant composition | 人数だけでは \ac{gcm} の構成員を決められないことを示す |
| 10 | real-time sensing の可能性と負担 | higher-resolution aggregation の実装条件を示す |
| 11 | static / daily / real-time aggregation の研究ギャップ | 本研究の比較対象へ接続する |
| 12 | research focus と evaluation outcomes | Method へ接続する |

**前後関係の確認結果**

- I-2 では、\ac{pcm} を \ac{pmv} との比較対象として突然置くのではなく、最初の文でモデルとして明示的に定義する。
- occupant-information resolution は Annex 79 の定義直後には置かず、three-layer chain を説明した後に置く。これにより、occupant information がどこで使われる情報なのかが先に分かる。
- chain の performance と deployment barriers は分ける。前者は three-layer sentence の直後、後者は “real-world applications remain limited” の直後に置く。
- 指示語だけで開始せず、“The end-to-end performance of this sensing--learning--control chain” や “This limited uptake” のように参照対象を同じ文で明示する。
- I-9 は既存の Jung / Ono の二文と内容が重なるため、単純挿入ではなく、その二文を含む小段落の再構成案とする。

### I-1. Thermal comfort と productivity の関係を、因果ではなくエビデンスの種類に沿って補足する

**対象位置**
冒頭段落全体。現在の二文目と三文目は Bueno et al. のレビュー内容を繰り返しているため、末尾への単純挿入ではなく、段落を一つの論理にまとめる方が自然。

**目的**
現状は thermal comfort が productivity と health を直接改善するようにも読める。レビューと実オフィス研究を追加し、関連は示される一方、研究デザインや自己申告指標により解釈が異なることを明示する。

**根拠文献**
bueno_evaluating_2021（systematic review）、lipczynska_thermal_2018（6週間の実オフィス研究）。

**統合英文案**

~~~latex
Thermal comfort is an important component of indoor environmental quality because it is associated with occupant satisfaction and work-related outcomes \cite{bueno_evaluating_2021}. The reported relationship with productivity should nevertheless be interpreted with care because it varies with study design, exposure range, and the outcome measure used \cite{bueno_evaluating_2021}. In a six-week tropical-office field study, self-reported concentration, alertness, and productivity remained high across the tested acceptable conditions and were more closely related to individual thermal satisfaction than to room temperature alone \cite{lipczynska_thermal_2018}. These findings motivate attention to thermal comfort without assuming that a particular setpoint will directly improve productivity.
~~~

**注意**
health まで残す場合は kaushik_effect_2022 がその主張を直接支えるか再確認する。十分でなければ、冒頭の health は削るか、健康アウトカムを直接扱う別レビューを追加する。

**前後の接続**
この段落は importance と evidence limitation までで閉じる。次段落の “Traditional \ac{hvac} systems...” が、重要な thermal comfort を従来どのように制御してきたかへ自然に移る。

### I-2. PMV の限界から PCM への論理的な橋渡しを加える

**挿入位置**
“This one-size-fits-all approach is inherently limited in achieving widespread occupant satisfaction.” の後。

**目的**
\ac{pmv} の限界を述べた直後に、\ac{pcm} が何を入力として何を予測するモデルなのかを明示的に定義する。その後で両者の prediction target を比較し、次の subsection で individual-level comfort information を building control に利用する \ac{occ} を導入できるようにする。

**根拠文献**
wang_individual_2018、cheung_analysis_2019、kim_personal_2018-1。

**追加英文案**

~~~latex
To address this limitation, a \ac{pcm} learns the relationship between an individual's thermal response and personal or contextual variables from that individual's feedback \cite{kim_personal_2018-1}. Unlike the \ac{pmv} model, which represents the mean response of a population, a \ac{pcm} targets the response of a specific person. Reviews and field-data analyses have documented substantial between-person variation and reduced predictive accuracy when population models are applied to individuals \cite{wang_individual_2018,cheung_analysis_2019,kim_personal_2018-1}. The next question is how this individual-level comfort information can be incorporated into building operation.
~~~

**前後の接続**
直前の “This one-size-fits-all approach...” に対して “To address this limitation” が応答し、最後の “incorporated into building operation” が次の \ac{occ} subsection の冒頭へ接続する。この時点では \ac{occ} をまだ用語として出さない。

### I-3. three-layer chain の後に occupant-information resolution を導入する

**挿入位置**
Annex 79 の \ac{occ} 定義直後ではなく、現在の “Typical \ac{occ} frameworks consist of three connected layers...” という一文の直後。

**目的**
先に sensing--learning--control の全体像を示し、その後で occupant information が sensing / learning layers への入力であると位置づける。これにより、presence、count、identity を突然列挙せずに済む。また、chain performance の主語を省略せず、どの chain を指すかを同じ文で明示する。

**根拠文献**
nagy_ten_2023、zhang_impact_2023。

**追加英文案**

~~~latex
The end-to-end performance of this sensing--learning--control chain depends not only on model accuracy but also on sensing quality, communication with the \ac{bms}, controller design, and local operating conditions \cite{zhang_impact_2023}. Within this architecture, occupant information provides an input to the sensing and learning layers and can range from presence and count to activity and identity \cite{nagy_ten_2023}. The useful spatial and temporal resolution of that information depends on the control decision it is intended to support.
~~~

**既存の次文に対する最小限の接続修正案**
追加文の後に現在の “Among these functions...” をそのまま置くと、functions が layers を指すのか processing steps を指すのか少し曖昧になる。採用時には、次の一文へ置き換えると shared-space paragraph へ自然につながる。

~~~latex
For comfort-oriented control, a particularly important link in this chain is the connection between individual comfort information and the final control decision, because it determines how personal preferences affect the room-level setpoint.
~~~

**前後の接続**
直前は three layers の定義、追加文は chain の性能条件と情報入力、次文は comfort information から setpoint への link を説明する。その次の “In shared office spaces, however...” が、一人分の情報から複数人を代表する setpoint へ論点を狭める。

### I-4. deployment barriers は limited adoption の直後にまとめる

**挿入位置**
three-layer paragraph の途中ではなく、同 subsection 末尾の “Despite growing recognition ... real-world \ac{occ} applications in buildings remain limited...” の直後。

**目的**
chain の仕組みを説明している途中で実装障壁へ脱線しないようにする。limited adoption という観察を先に述べ、その原因候補を次文で説明する。

**根拠文献**
obrien_key_2020、nagy_ten_2023、soleimanijavid_challenges_2024。

**追加英文案**

~~~latex
This limited uptake has been attributed to data availability and management, interoperability with existing systems, operator capacity, scalability, privacy, and the need for validation across buildings and climates \cite{obrien_key_2020,nagy_ten_2023,soleimanijavid_challenges_2024}.
~~~

**前後の接続**
“This limited uptake” は直前の “real-world applications ... remain limited” のみを受けるため、指示対象が明確である。この文で subsection を閉じると、次の dynamic-occupancy subsection は一般的な deployment barrier から、本研究が扱う具体的な情報課題へ移れる。

### I-5. shared space で group representation が必要になる根拠を追加する

**挿入位置**
“...a single room-level \ac{hvac} setpoint must represent multiple occupants at the same time.” の後。

**目的**
単一 occupant の feedback をそのまま room control に使えない理由と、collective objective の必要性を先行研究で示す。

**根拠文献**
schumann_predicting_2010。

**追加英文案**

~~~latex
Earlier work on shared offices noted that responding directly to one person's feedback implicitly assumes either single occupancy or identical preferences among occupants \cite{schumann_predicting_2010}.
~~~

**前後の接続**
直前の文が shared space では複数人を一つの setpoint で代表する必要性を述べ、追加文が single-user feedback を適用できない理由を先行研究で裏づける。その後の “This makes the construction of a \ac{gcm}...” の “This” は、この shared-zone representation problem 全体を受けるため自然につながる。preference heterogeneity の詳細は I-9 に置き、ここでは先取りしない。I-2 で \ac{pcm} を既に定義しているため、ここで \acp{pcm} が初出になる問題もない。

### I-6. ABW の利点を前提化せず、mixed evidence と実際の利用変動を加える

**挿入位置**
“Meanwhile, the rise of remote and hybrid work...” の一文の後、現在の “In such workplaces, occupants arrive, leave, and move...” の前。

**目的**
ABW の効果は一様ではないことを示したうえで、研究上重要な事実である時空間的な workstation use の変化を実測研究で支える。

**根拠文献**
engelen_is_2019、gocer_overlaps_2022。

**追加英文案**

~~~latex
The broader outcomes of \ac{abw} are mixed: systematic-review findings include benefits for some interaction, control, and satisfaction outcomes, but disadvantages for concentration and privacy and equivocal findings for health \cite{engelen_is_2019}. For the present study, the relevant characteristic is not a presumed general benefit of \ac{abw}, but the time-varying use of work settings. A twelve-month case study of an \ac{abw}-supportive office documented variation in workstation use and movement among zones, with utilisation patterns differing by season and by spatial markers associated with expected indoor environmental conditions \cite{gocer_overlaps_2022}.
~~~

**注意**
Gocer et al. は IEQ を縦断測定して movement の原因を同定した研究ではないため、「thermal conditions caused movement」とは書かない。

**前後の接続**
直前が \ac{abw} の普及、追加文が broader outcomes と本研究に関係する space-use variability、直後の “In such workplaces...” が arrive / leave / move による occupancy density と composition の変化を具体化する。追加文では movement の存在を一度だけ根拠づけ、直後の文に動的 occupancy の定義を担わせる。

### I-7. occupancy count と occupant identity/composition の違いを分類体系で支える

**挿入位置**
“Dynamic occupancy should therefore...” の直後ではなく、その次の “Even when the occupancy count is similar, the thermal preferences represented by the present group may differ.” の後。

**目的**
本研究の中心である「人数が同じでも、誰がいるかが違う」という区別を OCC のデータ解像度へ位置づける。

**根拠文献**
nagy_ten_2023。

**追加英文案**

~~~latex
Occupant-information taxonomies formalize this distinction: occupancy count describes how many people are present, whereas identity-level information is needed to associate the present group with person-specific comfort profiles \cite{nagy_ten_2023}. Count data alone therefore cannot determine whether the group comfort representation should change when one occupant replaces another.
~~~

**前後の接続**
先に本文の二文で count と “who is present” の違いを平易に説明し、その後で taxonomy と identity-level information を導入する。追加文の後に現在の “This makes static temperature control less reliable...” を置けば、“This” は count と composition の不一致全体を受ける。

### I-8. occupancy sensing の選択肢に、精度・遅延・privacy の trade-off を加える

**挿入位置**
“Recent IoT and building-management technologies...” で列挙している PIR、CO2、Wi-Fi の文の後。

**目的**
real-time composition tracking が技術的に利用可能というだけでなく、各方式が異なる情報粒度と制約を持つことを示す。

**根拠文献**
yang_review_2016、zafari_survey_2019、brambilla_potential_2021、wang_modeling_2017、obrien_key_2020。

**追加英文案**

~~~latex
However, these modalities do not provide equivalent information. Reviews identify trade-offs among counting capability, spatial resolution, latency, cost, and privacy for PIR, CO$_2$, camera, WLAN, and related approaches \cite{yang_review_2016,zafari_survey_2019,brambilla_potential_2021}. For example, CO$_2$-based inference can respond slowly to changes, while Wi-Fi-based inference can be affected by unstable signals and device-to-occupant behaviour \cite{wang_modeling_2017}. Identity-level tracking introduces an additional privacy and data-governance burden \cite{obrien_key_2020,nagy_ten_2023}.
~~~

**前後の接続**
“However” が直前の “more accessible” を限定し、利用可能性と実用上の等価性を区別する。その後の \autoref{table:OccuTrack} は、一般的な modality trade-off から実際の individual-level tracking examples へ移る具体例として機能する。

### I-9. group size だけでなく preference heterogeneity が aggregation に影響することを加える

**対象位置**
“...simply averaging preferences or applying a single \ac{pcm} may fail to represent the group.” は保持する。その直後にある既存の Jung et al. と Ono et al. の二文を、以下の小段落に置き換える。

**目的**
この位置へ元の追加案をそのまま挿入すると、直後の既存 Jung sentence と同じ group-size claim が重複する。そこで、(1) preference conflict、(2) group-size effect、(3) model/control resolution の順に一つの小段落として再構成する。

**根拠文献**
topak_collective_2023、jung_energy_2020、wang_enhancing_2026、ono_effects_2022。

**小段落の統合英文案**

~~~latex
This aggregation problem is shaped by both group size and preference heterogeneity. Collective-comfort studies show that shared-zone control must combine heterogeneous individual preferences under a common environmental decision \cite{topak_collective_2023}. Simulation studies indicate that the combined energy-and-comfort benefit of integrating \acp{pcm} can diminish as more occupants share a thermal zone \cite{jung_energy_2020}; a separate stochastic simulation likewise reported lower potential maximum satisfaction rates for larger groups \cite{wang_enhancing_2026}. At a different dimension of resolution, Ono et al.~\cite{ono_effects_2022} showed that the occupant resolution of a comfort model should be commensurate with that of the control it informs.
~~~

**注意**
Jung et al. は comfort だけを独立に評価した根拠としてではなく、energy-and-comfort の統合結果として記述する。

**前後の接続**
“This aggregation problem” は直前の “averaging preferences ... may fail” を受ける。段落内では preference heterogeneity から group size、さらに resolution alignment へ進み、その後の既存 “These findings indicate...” が三つの論点をまとめられる。

### I-10. research gap を「誰を、いつ GCM に含めるか」と明文化する

**挿入位置**
Lei et al. の dynamic-occupancy approach と、その data / compute / combination-coverage limitations を説明する一文の直後。現在の “Rather than preparing separate control models...” の前。

**目的**
既往研究の不足と本研究の three aggregation levels を一文でつなぐ。

**根拠文献**
nagy_ten_2023、schumann_predicting_2010、topak_collective_2023。

**追加英文案**

~~~latex
Taken together, these studies leave unresolved not only how several \acp{pcm} should be aggregated, but which occupants should enter that aggregation at each control decision. Static membership, daily attendance, and real-time presence represent progressively finer temporal resolutions of the same group-representation problem, with corresponding increases in sensing and integration burden \cite{nagy_ten_2023}.
~~~

**前後の接続**
“Taken together” は直前までの static-attendance studies と Lei et al. の dynamic approach の双方を受ける。次の “Rather than preparing separate control models...” が、この未解決問題に対する本研究の temporal-resolution strategy を提示し、その次の practical question と Focus subsection へ続く。

### I-11. Focus subsection の outcome 記述を、未確定の Figure 1 指標から独立させる

**対象位置**
“Specifically, the analysis compares...” の箇条書き (1) と、最後の relationship に関する記述。

**提案**
Figure 1 の指標確定前は、本文の “mean comfort probability” を増補しない。必要なら暫定的に “predicted comfort outcome” とし、UTR は causal effect ではなく association と記述する。

**指標確定後の候補**

~~~latex
Specifically, the analysis compares \ac{sgcm}, \ac{dgcm}, and \ac{rtgcm} policies in terms of: (1) the selected predicted-comfort metric and its improvement relative to a fixed \qty{24}{\celsius} baseline; (2) the setpoint adjustment magnitude required by the \ac{rtgcm}; and (3) the association between occupancy dynamics, especially \ac{utr}, and the frequency of actionable control updates.
~~~

**前後の接続**
直前の review subsection は static / daily / real-time aggregation の practical question で終わり、Focus subsection は “Based on this background” でその問いに応答する。ここでは新しい概念や文献を増やさず、三つの aggregation policy と評価項目を Method へ引き渡すことに限定する。

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
Simulation studies indicate that the combined energy-and-comfort benefit of integrating \acp{pcm} can diminish as more occupants share a thermal zone \cite{jung_energy_2020}. A separate stochastic simulation likewise reported lower potential maximum satisfaction rates for larger groups \cite{wang_enhancing_2026}. These studies support a directional expectation that aggregation can dilute the influence of individual preferences, although their numerical results are not directly comparable with the present analysis because the control strategies, populations, and outcome definitions differ.
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
The \qty{0.5}{\celsius} threshold is an operational analysis choice in the present study and should not be interpreted as a threshold established by prior work. At a different dimension of resolution, Ono et al.~\cite{ono_effects_2022} showed through simulation that the occupant resolution of a comfort model should be commensurate with that of the \ac{hvac} control it informs. Together, these points distinguish model-information resolution from numerical setpoint resolution and from the physical ability of an \ac{hvac} system to realise a requested change.
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
An actionable setpoint difference in simulation does not by itself establish field deployability. Long-term and side-by-side field studies show that realised outcomes can depend on occupancy-sensor accuracy, communication with the \ac{bms}, damper or actuator cycling, outdoor conditions, controller design, and local operating constraints \cite{jiang_occupied_2023,kong_hvac_2022,zhang_impact_2023}. Closed-loop evaluation is therefore required to determine whether the predicted comfort advantage persists after sensing delay and \ac{hvac} dynamics are introduced.
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
Occupant responses may also lag changes in environmental stimuli. Field observations of shading behaviour, although not a direct test of temperature-setpoint response, demonstrate that adaptive actions can occur with temporal delay \cite{li_study_2022}. Future closed-loop evaluation should therefore represent both \ac{hvac} response time and occupant adaptation rather than assuming an instantaneous response.
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
In addition, the group-level mean objective does not reveal whether an improvement is shared across occupants or achieved at the expense of a consistently disadvantaged minority. Individual-level distributions, worst-case comfort, and fairness-oriented objectives should therefore be examined alongside the mean. Simulation enables controlled comparison of \ac{occ} strategies, but its conclusions remain conditional on model inputs and cannot establish occupant acceptance or field performance by itself \cite{hobson_workflow_2021}. A stronger validation design would pair each person's observed movement with that person's \ac{pcm} and then evaluate the selected policy in closed-loop operation, including sensing error, communication failures, \ac{hvac} dynamics, energy use, and occupant feedback \cite{jiang_occupied_2023,zhang_impact_2023}.
~~~

## 文献候補一覧と採用理由

| BibTeX key | Evidence type | Introduction で支える内容 | Discussion で支える内容 | 推奨 |
|---|---|---|---|---|
| lipczynska_thermal_2018 | 6-week office field study | thermal satisfaction と self-reported performance の関係 | -- | I-1 |
| kim_personal_2018-1 | review / PCM framework | PMV と PCM の prediction target の違い | -- | I-2 |
| nagy_ten_2023 | Annex 79 synthesis | OCC 定義、presence/count/activity/identity、情報解像度 | count と identity、deployment burden | I-3, I-4, I-7, I-10; D-7, D-8 |
| zhang_impact_2023 | private-office field implementation | sensing--model--control chain | controller・weather・field constraints | I-4; D-5, D-10 |
| schumann_predicting_2010 | shared-office method / evaluation | single feedback と shared-zone representation | preference aggregation | I-5 |
| topak_collective_2023 | CFD / PCM simulation | heterogeneous collective comfort | preference diversity | I-9 |
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

## 追加調査: Ono et al. / Jung et al. の引用連鎖と新規 Journal

以下は Discussion を中心とした追加候補である。Introduction は追加しない。本文と references.bib はこの調査では変更せず、採用時に Expansion 案から反映する。

### D-11. Jung et al. の先行研究を用いて、group-size 効果を thermal sensitivity まで分解する

**挿入位置**

Discussion 最初の subsection で jung_energy_2020 と wang_enhancing_2026 を比較した冒頭段落の直後。本研究の Figure 1 の結果説明へ入る前。

**目的**

人数増加に伴う性能低下を preferred temperature の平均化だけで説明せず、各 \ac{pcm} の曲線幅・傾きに対応する thermal comfort sensitivity も集団 setpoint に影響し得ることを示す。

**根拠文献**

jung_comparative_2019。この論文は jung_energy_2020 が直接参照している先行研究であり、2--10 人の multi-occupancy simulation で personal thermal comfort sensitivity を考慮すると setpoint が 86\% のケースで変わり、collective comfort probability が改善したと報告している。

**追加英文案**

~~~latex
One mechanism underlying this group-size effect is variation not only in occupants' preferred temperatures but also in their thermal comfort sensitivities. In an earlier multi-occupancy simulation, incorporating personal thermal comfort sensitivity changed the selected setpoint in 86\% of the tested cases and increased the probability of collective comfort \cite{jung_comparative_2019}. Because the present \acp{gcm} average complete \ac{pcm} probability curves rather than point estimates of preferred temperature, both the location and the breadth of the individual curves can influence the merged optimum. The present analysis does not separately quantify these two contributions.
~~~

**前後の接続**

直前の段落は group size が大きくなると individual preference の影響が薄まるという方向性を示している。この追加は、その方向性を preferred temperature と sensitivity の二要素へ分解する。その後に本研究の結果を置くことで、先行研究の機序候補から Figure 1 の解釈へ自然に移れる。ここでは本研究が sensitivity の因果効果を検証したとは述べない。

### D-12. Jung et al. が参照した field study から、simulation-to-field gap を補強する

**挿入位置**

From comfort information to actionable control subsection の “Closed-loop evaluation is therefore required ...” で終わる段落の直後。\ac{utr} の説明へ移る前。

**目的**

simulation 上の actionable setpoint と field performance の間に差が生じ得る理由として、occupancy event の時間的・空間的配置と zone 間の熱的相互作用を追加する。

**根拠文献**

pritoni_field_2016。この論文は jung_energy_2020 が fairness-oriented setpoint switching の energy implication を論じる際に参照した field study である。3 棟の university residence hall を対象とした controlled field evaluation では、通常の academic period に standard-practice simulation が省エネ量を 2--10 倍過大評価し、短く分散した vacancy event と隣接 zone 間の熱的相互作用が重要だったと報告している。

**追加英文案**

~~~latex
Field evidence also cautions against treating each occupancy-responsive setpoint change as an independent source of benefit. In a controlled evaluation of learning thermostats in three university residence halls, a standard-practice simulation overestimated academic-period energy savings by a factor of two to ten because the temporal and spatial distribution of vacancy events and thermal interactions among adjacent zones affected the realised outcome \cite{pritoni_field_2016}. Although residence halls differ from the shared offices studied here and that evaluation addressed energy rather than \ac{gcm}-based comfort, it supports validating the timing and spatial coincidence of occupancy changes at the whole-building level.
~~~

**前後の接続**

直前は sensing delay と \ac{hvac} dynamics を含む closed-loop evaluation の必要性を述べる。この追加はその一般論へ具体的な field evidence を与える。次の段落は mean occupancy と \ac{utr} の違いを説明するため、最後を timing and spatial coincidence of occupancy changes とすることで occupancy composition の時間変化へ接続できる。

### D-13. setpoint 変更後の occupant response を、thermostat interaction の直接的 evidence で補強する

**挿入位置**

Limitations の “Occupant responses may also lag changes in environmental stimuli.” の後。現在の li_study_2022 による shading behaviour の説明の前、またはその段落を短縮する場合は li_study_2022 の文の代替候補。

**目的**

shading behaviour からの間接的類推に加え、comfort survey と thermostat interaction を同期した field study を用いて、steady-state assumption と instantaneous response assumption の限界を直接補強する。

**根拠文献**

kang_longitudinal_2026。41 人・20 住宅・6 か月の longitudinal field study であり、app-based comfort survey、thermostat interaction、building time series を同期している。standard steady-state comfort model の誤差が spatiotemporal temperature variation 下で増える場合があり、manual setpoint change に household / occupant-specific temporal pattern が観察された。

**追加英文案**

~~~latex
More direct evidence from thermostat interactions also indicates that comfort and control responses can be time-dependent. A six-month field study involving 41 occupants in 20 homes found that standard steady-state comfort models became less reliable under substantial spatiotemporal temperature variation and that manual setpoint changes exhibited occupant- and household-specific temporal patterns \cite{kang_longitudinal_2026}. Although the residential demand-response setting differs from the present shared offices, the findings reinforce the need for future closed-loop tests to represent dynamic occupant response and \ac{hvac} response rather than evaluating each selected setpoint as an instantaneous steady state.
~~~

**前後の接続**

Limitations は直前まで energy、\ac{hvac} response delay、actuator constraints、occupant adaptive behavior が未評価であることを列挙しているため、この位置で dynamic response の evidence を示すのが自然である。住宅の demand-response study であることを同じ段落内で明示し、office \ac{gcm} に数値を直接転用しない。

### 後方引用探索の判断

| Candidate | 参照元 | Discussion への価値 | 判断 |
|---|---|---|---|
| jung_comparative_2019 | Jung et al. (2020) | preferred temperature だけでなく thermal sensitivity が collective setpoint に影響することを示す直接的な先行 simulation | D-11 として推奨。Zotero と PDF は既存 |
| pritoni_field_2016 | Jung et al. (2020) | occupancy-responsive control の simulation-to-field gap と、vacancy の時間・空間配置の重要性を controlled field evaluation で示す | D-12 として推奨。公開 PDF を Zotero に保存 |
| jayathissa_humans-as--sensor_2020 | Ono et al. (2022) | longitudinal subjective feedback と preference group の形成を支える | 既に Zotero / BibTeX にあり、Discussion では D-11 と内容が重なるため保留 |
| chong_occupancy_2021 | Ono et al. (2022) | occupancy data の高い空間解像度が常に energy-model calibration を改善するとは限らないことを示す | outcome が \ac{occ} control ではなく building-energy model calibration で、信頼できる OA PDF も確保できなかったため保留・未登録 |
| Shin et al. (2017), Exploring fairness in participatory thermal comfort control in smart buildings | Jung et al. (2020) | mean / majority aggregation が同じ occupant を継続的に不利にする可能性を扱う | 内容は有用だが conference paper。Journal 中心という条件と、既に wang_enhancing_2026 が fairness-oriented evaluation を提供することから今回は保留 |

kang_longitudinal_2026 は Ono / Jung の参考文献ではないが、2026 年の open-access Journal field study として D-13 の dynamic-response limitation を直接補強するため採用候補に含めた。

### Zotero / BibTeX の状態

- 本文と references.bib は変更していない。採用時は Zotero から pritoni_field_2016 と kang_longitudinal_2026 の2エントリだけを同期する。
- Zotero には pritoni_field_2016（item GF349DRW、PDF attachment 8VDW6WYH）と kang_longitudinal_2026（item BQS25N5C、PDF attachment DTLFRAMX）を追加した。
- Pritoni et al. (2016) は最初の Connector 保存時に PDF なしの重複項目 KBV2GHKT も作成された。Zotero Desktop の Duplicate Items で GF349DRW 側を主項目として統合する。本文では PDF 付き項目の固定 citation key pritoni_field_2016 を使う。

## 追加調査第2回: social interaction と sensing uncertainty

今回も Introduction は追加せず、Discussion の既存論理を補う候補だけを選んだ。本文と references.bib は変更していない。

### D-14. 独立な \ac{pcm} 出力の集約と、実際の社会的な妥協を区別する

**挿入位置**

Discussion 最初の subsection の末尾付近。\ac{rtgcm} と \ac{dgcm} の差を occupant composition dynamics で説明した後、現在の “These predicted gains assume immediate setpoint selection ...” の直前。

**目的**

本研究の \acp{gcm} が予測された個人選好を共通目的へ集約するモデルであり、共有空間で occupants が選好を表明・抑制・交渉する過程そのものはモデル化していないことを明示する。group size と thermal sensitivity を扱う D-11 の後に置き、数理的な aggregation の説明から未評価の social interaction へ論点を一段進める。

**根拠文献**

ding_reconciling_2026。20 人を対象とした controlled chamber study で、physiological、psychological、social needs を統合した evolutionary-game model を構築している。ablation study では social-feedback module を除くと temperature drift と step-change の両条件で intention-prediction error が増加した。一方、同論文の reward--punishment mechanism は参加者の social status が等しいと仮定し、実際の office hierarchy と interpersonal relationships を今後の課題としている。

**追加英文案**

~~~latex
The present \acp{gcm} aggregate individual \ac{pcm} outputs as independent inputs to a common objective and therefore represent predicted thermal preferences rather than the social process through which occupants express, suppress, or negotiate those preferences in a shared office. In a controlled chamber study with 20 adults, an intrinsic-needs evolutionary-game model produced larger temperature-adjustment intention errors when its social-feedback module was removed under both temperature-drift and step-change conditions \cite{ding_reconciling_2026}. That model itself assumed equal social status among participants, and its authors identified workplace hierarchy and interpersonal relationships as remaining limitations. These results do not establish that game-theoretic control would outperform the present \acp{gcm}; instead, they identify social interaction as a separate dimension for future shared-office validation.
~~~

**前後の接続**

直前では subgroup size、thermal sensitivity、realized composition が aggregation result に影響することを説明する。この追加は、それらをすべて個人 \ac{pcm} の属性として集約する本研究の範囲を明確にし、次の “These predicted gains assume ...” にある field conditions の限定へ接続する。\ac{pcm} を先に定義済みの Discussion であるため、ここで略称を新規導入する必要はない。

### D-15. \ac{rtgcm} の sensing layer を不確実な入力として評価する

**挿入位置**

From comfort information to actionable control subsection の closed-loop evaluation 段落と D-12 の field evidence の後、\ac{utr} と occupant identity の説明へ移る前。

**目的**

real-time tracking を「利用可能／利用不可能」の二値条件として扱わず、sensing error が membership selection と selected setpoint にどう伝播するかを将来検証項目として具体化する。

**根拠文献**

bae_sensor_2021。building / \ac{hvac} control に対する sensor impact を扱った129報のレビューと expert interviews を統合し、sensor type、location、accuracy、reliability、cost、data delivery、control strategy を相互依存の設計要因として整理している。同レビューは、sensor accuracy や fault が control performance に与える影響を定量化した研究と、統一的な impact-evaluation framework が不足していると結論づけている。

**追加英文案**

~~~latex
The sensing layer should also be evaluated as part of the control method rather than as a binary implementation prerequisite. A review of 129 studies, augmented by expert interviews, identified sensor type, location, accuracy, reliability, cost, and data delivery as coupled design factors and found limited quantitative analysis of how sensor accuracy or faults propagate to building-control performance \cite{bae_sensor_2021}. Because the \ac{rtgcm} selects a changing set of \acp{pcm}, future tests should perturb missed detections, false occupant assignments, identity uncertainty, and latency, and then quantify their effects on both group membership and the selected setpoint. The identity-specific error cases are proposed extensions for this method rather than effects directly quantified by Bae et al.
~~~

**前後の接続**

直前の D-12 は occupancy events の時間・空間配置が realised field performance を変えることを示す。D-15 は、その events 自体が完全には観測されない場合へ議論を進める。直後の本文は count と identity を区別して \ac{utr} を説明するため、最後を group membership と selected setpoint への error propagation とすることで自然に接続する。

### 第2回探索の判断

| Candidate | 由来 | Discussion への価値 | 判断 |
|---|---|---|---|
| ding_reconciling_2026 | Jung et al. (2019) を直接参照する新規 Journal | independent preference aggregation では表現しない social feedback と compromise を、ablation study を含む実験で示す | D-14 として推奨。UCL の CC BY accepted manuscript PDF を Zotero に保存 |
| bae_sensor_2021 | 追加の Journal 探索 | sensing を control と分離せず、accuracy / fault / location / cost を含む impact evaluation の不足を整理 | D-15 として推奨。DOE OSTI の公開 PDF を Zotero に保存 |
| Azimi and O'Brien (2022), *Fit-for-purpose: Measuring occupancy to support commercial building operations: A review* | Ono et al. (2022) の直接引用 | application ごとに必要な occupancy resolution と sensing technology を対応づける | 有用だが購読版のみで信頼できる公開 PDF を確保できず、既存の resolution discussion とも重なるため保留・未登録 |
| An et al. (2026), *A hierarchical thermal preference structure for understanding satisfaction in multi-occupant offices under cooling season conditions* | 最新 Journal 探索 | real office complaint data から、狭い comfort range を持つ少数 group が maximum collective satisfaction を制約する | fairness の根拠として非常に有力だが closed access で公開 PDF がなく、今回は保留・未登録 |
| Alamirah and Tabet Aoul (2026), *Toward socially-aware Personal Comfort Models* | 最新 Journal 探索 | conformity、social roles、unequal control access を整理した socially-aware \ac{pcm} framework | CC BY 記録は確認したが直接取得可能な PDF URLを確保できず、field-validated model ではない。D-14 の Ding et al. を優先して保留・未登録 |
| Lu et al. (2022), *Sensor impact evaluation in commercial buildings* | sensing-error 探索 | occupancy count / presence sensor の bias、latency、noise、misdetection を control outcome に結びつける | 内容は D-15 に直接的だが、OSTI と publisher は accepted-manuscript landing page のみで PDF を取得できなかった。公開 PDF を確認できる bae_sensor_2021 を採用し、未登録 |

### Zotero / BibTeX の状態（第2回）

- Zotero に ding_reconciling_2026（item FFBR7Q22、PDF attachment WLPGMIDJ）を追加した。PDF は UCL Discovery の CC BY accepted manuscript で、Zotero の全文索引を確認済み。
- Zotero に bae_sensor_2021（item DFX9E43G、PDF attachment 9M5YWI48）を追加した。PDF は DOE OSTI で公開された Journal pre-proof で、Zotero の全文索引を確認済み。
- 本文と references.bib は変更していない。D-14 / D-15 の採用時にのみ、上記2エントリを Zotero から references.bib へ同期する。
