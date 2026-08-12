# ReviewPerspectives適用レビュー + 追記案 + 再帰レビュー (2026-07-18)

対象: `chapters/ch4-Results.tex`, `ch5-Discussion.tex`, `ch6-Conclusion.tex`, `abstract.tex`(整合確認のみ)
基準: `ref/ReviewPerspectives_SimulationPaper.md` の11観点
このファイルはレビューと提案のみで、`.tex`は変更していない。

---

## Part 1. 観点別評価(現状どこまで価値が出ているか)

凡例: ◎=十分 / ○=概ね良いが改善余地 / △=不足 / ✗=欠落・不整合

### 1. 主張とフレーミング — ○
- ◎ 「Xがいつ価値を持つか」型の主張は成立している(Intro末尾の3比較軸、Discussion 5.2末尾の使い分け提案)。coarse・staticをデフォルトとする論理も成立。
- △ 閾値の条件依存性: 「5--7人でstatic改善がゼロ」「mean occupancy 4--5で頭打ち」がAbstract/Discussionでuniversal thresholdに読める書き方。Limitationsには書いてあるが、**結論文と同じ場所**での併記(観点3.6)がない。
- △ Abstract末尾 "identify when high-resolution occupancy tracking is justified for practical HVAC control" は、シミュレーションというevidence typeを超えてdeployment効果として読める(観点1.2)。"simulation-based screening guidance" 程度に弱める必要。
- ✗ **Abstractの「mean occupancy 4--5で改善が頭打ち」の根拠図(analysis72 contour)がResultsからコメントアウトされている。** 本文に存在しない結果をAbstract/Conclusionが主張している状態(観点1.2, 5.7, 10.1)。最重要の不整合。

### 2. 構成と役割分担 — △
- △ Resultsにメカニズム説明が残存: L54 "indicates that a fixed room-member aggregation becomes less distinct...", L59 "due to the more dynamic occupant transitions", L103 "can be practical in actual HVAC operation"(実務含意)。`review_a6p`の指摘が未反映。
- △ Discussion 5.1でL7とL10がほぼ同一の主張("consistent with prior studies...")を2回述べている(観点2.5)。
- ○ DiscussionによるResults数値の再掲は許容範囲。

### 3. Resultsの読者ガイド(Mihara観点) — △
- ✗ Results冒頭のorientation(何をどの順で見るか)がない。
- ○ K vs N_{r,t}の取り違え防止(L9--10)は良い。ただしcomfort probabilityが「予測 "No change" 確率のperson-time平均」であることのリマインドがResultsにない。
- △ 差の大きさの定量化は概ね良いが、減衰の速さ・どの条件に集中するかの言語化が弱い(例: staticが負になる部屋の明示)。
- ✗ 弱い条件の併記なし: UTR 0.7--0.8のサンプル薄さ、最大Kが部屋により異なること等。

### 4. DiscussionとPrior work(Ono観点) — △
- ✗ Discussion冒頭のkey contributions段落(方法論/シミュレーション的発見/設計含意の3分類)がない(観点4.1)。
- ✗ 5.1の第1文の主語がJung et al.(文献要約が主語)。本稿が何を加えるかのtopic sentenceで始まっていない(観点4.2)。
- △ Jungの「2%に収束 @6人」と本稿の「5--7人でゼロ」を直接対応させ気味。"same broad tendency"接続に留めるべき(観点4.6)。※jung_energy_2020はシミュレーション研究なので「実測に先立つ」等の不成立軸は現状使っておらずOK。ただし引用時にevidence type(simulation)を一言明示すると安全。
- ✗ **Causality論文(companion paper)との役割分担の記述が皆無**(観点9.4)。
- △ 実務的含意(センシングコスト・privacy)はLimitationsのみ。設計含意段落で「本研究で未評価」と明示した上でqualitativeに述べる形(観点4.8)になっていない。特に**エネルギー未評価のまま採用ガイダンスを出している**点は、ガイダンス文と同じ場所でcomfort-only scopeを明示すべき。

### 5. AbstractとConclusion — △
- ✗ Abstract「mean occupancy 4--5」がResults本文に不在(上述)。
- △ Abstract "room size approaches six occupants" — room size / group size / subgroup size が混在。用語統一が必要(観点6.1)。
- △ Conclusionに数値elaborationがほぼない(観点5.4)。改善幅15--20%、調整幅~1.0°C vs 制御刻み0.5°C、UTR 0.7--0.8で90%等の直感的数値を入れられる。
- △ Conclusion "advantage strongest under sparse or dynamically changing occupancy" — sparse側の根拠が現Resultsに不在。UTRの結果は「制御頻度」の話でcomfortの優位ではない。主張と根拠種別の対応ズレ。
- ○ intensive field dataの成立条件強調は「Using field survey data and reconstructed location logs」で最低限あり。1棟・39名・1ヶ月・2608回答という強度をConclusionで一言添えると良い(validityの根拠としてではなく)。

### 6. 用語・記法・略語 — ○
- △ subgroup size / room member size / room size / group size の揺れ(Abstract, Results 4.2冒頭 "room member sizes")。分析用語はsubgroup size $K$に統一し、設計文脈では "the number of occupants sharing the zone" 等に言い換える。
- ✗ 図キャプションの "dynamic group control"(fig:DynSpStepHist, fig:UTRexamples)は**RTGCMを指しているのにDGCM(daily)と衝突**する旧称。pool改名の教訓と同型(観点6.3, 7.4)。

### 7. 図表 — ✗
- ✗ **同一画像の重複掲載**: L33--38(fig:MeanOccuConf)とL40--45(fig:ImpGCDMvsRTGCM)が同じpng。前者は削除。
- ✗ fig:UTRexamplesのキャプションがコピペ誤り("Distribution of temperature adjustment magnitudes..."だが実際はUTRの時刻推移)。
- △ キャプション誤植: "probability probability"(fig:ComfAchi)、"between\ac{rtgcm}"のスペース欠落。
- △ 複数パネル図(fig:ComfAgentic)のパネル・系列・軸の対応の言語化が本文に薄い(観点7.5)。
- △ fig:ComfAgenticキャプションはcaption単独で読めない(系列=4政策、x軸=K、パネル=部屋、の説明なし)。

### 8. 数値と統計 — △
- ✗ 1000 Monte Carlo trialsを回しているのに、comfort結果にSD/CI等の変動幅表示がない(観点8.2)。CIがあるのはfig:CtrlWindowRatioのみ。
- △ 数値の追跡可能性: Results "RT improvement 15--20%, DGCM 5--20%" vs `review_a6p`の元データ "RT 0.14--0.20, Daily 0.08--0.15"。DGCM下限5%は要確認。4.2冒頭の "15--30% higher than SGCM" も4.1の数値(RT 80--98 vs SGCM 65--73)と整合するか要確認。**[TODO: 結果ファイルと突合。本文執筆時の新規再集計はしない]**
- ✗ **fig:ImpGCDMvsRTGCMの解釈文が内部矛盾**: 「K<6で増加し大きいKで収束」→「RTは*小さい部屋*でより有効」は逆向き。増加して収束するなら優位はKとともに拡大して飽和。データを確認して主張の向きを確定する必要(観点10.2の宙に浮いた論理)。

### 9. シミュレーション論文固有 — ○
- ◎ PCM出自(1棟・39名・ordered logit・Ti単変量)、occupancyが実測ログ由来であること、PCM再割当の限界、はMethod/Limitationsに明示済み。
- ✗ Causality論文との役割分担(あちら=representationのadded informativenessのfield検証 / こちら=closed-loop outcomeのシミュレーション評価)が未記載。
- △ 24°C固定baselineの選定理由が未記載(公平性の観点9.7)。「調査建物の従来運用に近い」等の根拠を一文。
- ○ comfort-onlyでenergy未評価はLimitationsに明示済み。ただし上記の通りガイダンス文側にも併記が必要。

### 10. 整合性 — ✗
- 上記の図重複、キャプション誤り、Abstract/Conclusion vs Results不整合、fig:ImpGCDMvsRTGCM論理矛盾。
- 文法: "This may because that"(L95)、"controlable"(L103)、"for each target rooms"(L56)。
- Methodの図ラベル `fig:ComChara` がOverallFlow図に付いている(名称ねじれ、コメントアウト旧図の遺物)。

---

## Part 2. Result / Discussion / Conclusion への追記・修正案

方針: (a) Resultsは観察に限定し、orientation・不確かさ・弱条件併記を追加、(b) Discussionはkey contributions段落を新設し、topic-sentence-first・メカニズム説明受け入れ・companion paper役割分担・comfort-only明示、(c) Conclusionは数値elaboration+hedge。

### R1. Results冒頭にorientation段落(新規)
```tex
This section reports three sets of results.
Section~\ref{subsec:ComfPerf} compares the mean comfort probability of the three \ac{gcm} policies and the fixed \qty{24}{\celsius} baseline across subgroup sizes, where the comfort probability is the person-time average of the predicted ``No change'' probability defined in \autoref{subsec:comfMetrics}.
Section~\ref{subsec:controleffect} then quantifies the setpoint adjustment magnitude required when the \ac{rtgcm} is adopted, and Section~4.3 relates occupant-composition turnover, measured by \ac{utr}, to the frequency of actionable setpoint changes.
Throughout, improvement denotes the difference in mean comfort probability from the fixed \qty{24}{\celsius} baseline, not a relative ratio.
```

### R2. 4.1の観察の定量補強+不確かさ+弱条件(追記)
```tex
Static-model improvement approached zero around subgroup sizes of five to seven and became slightly negative in some rooms at the largest tested sizes.
% [TODO: 負になる部屋名とKを結果ファイルから確認して明記 (ref: R&D OfficeでK>=6, Shared Office 2でK=7)]
Across the 1,000 Monte Carlo trials per room and subgroup size, the between-trial variability of the mean comfort probability was [TODO: SD or 95% interval を結果ファイルから記載].
Note that the largest tested subgroup size differs across rooms according to each room's regular-member pool, so cross-room comparisons at large $K$ rest on fewer rooms.
```

### R3. メカニズム文の削除(→D3へ移動)
- L54 "The decline ... indicates that a fixed room-member aggregation becomes less distinct ..." → 観察文に置換:
```tex
The static-model improvement thus became close to the fixed-temperature baseline at larger subgroup sizes, while the ranking among the three policies remained unchanged.
```
- L58--59のfig:ImpGCDMvsRTGCM解釈文 → **まずデータで向きを確認**した上で観察のみ記述:
```tex
The improvement difference between the \ac{rtgcm} and \ac{dgcm} increased with subgroup size below approximately $K=6$ and then stabilized at larger subgroup sizes.
% [TODO: 図の実挙動と一致するか確認。現行文の「小さい部屋で有効」との向き矛盾を解消]
```
- L103の実務解釈文("can be practical in actual HVAC operation")→ 削除し観察のみ:
```tex
For most conditions, the mean adjustment magnitude remained at or above \qty{0.5}{\celsius}, which corresponds to a common thermostat setpoint step.
```

### R4. sparse-occupancy根拠の復活(Abstract整合のため必須)
コメントアウトされているanalysis72(mean occupancy contour)段落と図を、観察のみの形で復活:
```tex
\autoref{fig:MeanOccuConf} shows the improvement relative to the \qty{24}{\celsius} baseline as a function of daily mean occupancy for the \ac{rtgcm} and \ac{sgcm}.
The \ac{rtgcm} improvement was largest under sparse occupancy and decreased as daily mean occupancy increased; as mean occupancy approached four to five occupants, the improvement approached the level of the \ac{sgcm}.
% [TODO: 図の系列構成(k4/k6/k8, contour+回帰線)の読み方を1文追加。数値は図・結果ファイルから確認]
```
(代替案: Abstract/Conclusionから当該主張を削る。ただし「sparse occupancyでこそ価値」という本稿の中心的メッセージを失うため非推奨。)

### R5. 図の修正(観点7)
- 重複図(L33--38)削除。
- fig:UTRexamplesキャプション → `Mean \ac{utr} transition by time of day (weekday mean across the four office rooms)`。
- "dynamic group control" → "\ac{rtgcm}-based control" に統一(fig:DynSpStepHist)。
- fig:ComfAchiの "probability probability" 修正、`between\ac{rtgcm}` のスペース。
- fig:ComfAgenticキャプションを自立化: `Mean comfort probability (a) and improvement over the fixed \qty{24}{\celsius} baseline (b) for the four control policies. Each panel corresponds to one office room; the horizontal axis is subgroup size $K$.`

### D1. Discussion冒頭にkey contributions段落(新規、観点4.1)
```tex
The key contributions of this study are threefold.
Methodologically, it provides an occupancy-log-based agentic simulation framework that treats the temporal resolution of group-comfort aggregation -- static, daily, and real-time -- as an explicit design parameter, by recombining observed movement records with independently assigned \acp{pcm}.
As simulation-based findings, it shows that the benefit of higher-resolution aggregation depends jointly on subgroup size, realized occupancy, and occupant-composition turnover, rather than on room-member size alone.
As a design implication, it suggests that occupancy metrics readily available from building systems, such as mean occupancy and \ac{utr}, can serve as screening indicators for deciding whether real-time occupancy tracking is worth its operational burden -- a decision that this simulation can inform but not settle, since energy use and field deployment were not evaluated.
```

### D2. 5.1のtopic-sentence-first化+broad tendency接続(改稿)
```tex
The present results add a temporal-resolution axis to prior findings on group size in multi-occupant comfort control.
\mycite{jung_energy_2020}\cite{jung_energy_2020}, in a simulation study of personal-comfort-model integration, reported that the comfort benefit diminishes as more occupants share a zone, with only marginal improvement remaining at around six occupants.
The present \ac{sgcm} results show the same broad tendency: its improvement over the fixed \qty{24}{\celsius} baseline approached zero around subgroup sizes of five to seven in the studied rooms, although the specific sizes at which this occurs should be read as building-specific rather than universal.
What the prior work could not address is whether this saturation is inherent to group size itself; the present comparison shows that it is not, because the \ac{dgcm} and \ac{rtgcm}, which update the represented group, maintained positive improvement at the same subgroup sizes.
```
(現行L7とL10の重複主張はこの改稿で1回に統合。)

### D3. メカニズム段落(Resultsから移動、新規)
```tex
These contrasts can be explained by which occupants each aggregation represents.
The \ac{sgcm} averages the preferences of all sampled regular members, so as the member pool grows, its setpoint converges toward a population-average temperature that differs little from a fixed setpoint.
The \ac{dgcm} restricts the represented group to each day's attendees, and the \ac{rtgcm} further restricts it to the occupants present at each control timestep.
The consistently higher performance of the \ac{rtgcm} therefore indicates that within-day occupancy transitions carry comfort-relevant information even at larger subgroup sizes.
```

### D4. 設計含意にcomfort-only scopeを併記(5.2末尾の改稿)
```tex
These findings suggest that \ac{rtgcm}-level control should not be adopted solely because real-time tracking is available.
Within the comfort-only scope of this simulation, it is most valuable in sparse or highly variable shared-office conditions where occupant composition changes frequently, whereas a \ac{dgcm} may be a practical compromise when daily attendance differs from regular membership but within-day turnover is moderate, and a \ac{sgcm} is likely to suffice when occupancy is stable or the group is large enough for individual differences to average out -- subject to verification in the target building and use pattern.
Because energy use, \ac{hvac} response dynamics, and sensing costs were not evaluated, these are qualitative screening suggestions rather than deployment prescriptions.
```

### D5. Companion(causality)論文との役割分担(新規、観点9.4)
```tex
This study is complementary to our companion field analysis \cite{[TODO: causality paper key]}, which examined whether real-time occupant-composition representations add predictive information about group comfort in observational field data.
The companion study addresses the informativeness of the representation itself, whereas the present study evaluates the closed-loop consequence of acting on that representation through setpoint control, using simulation to cover occupancy and membership conditions beyond those observed.
Together, they separate the question of whether finer occupancy information is informative from whether using it improves control outcomes.
```
**[TODO: causality論文のDiscussionでの差分軸の書き方と矛盾しないか、あちらの原稿と突合(観点9.5)]**

### D6. Limitationsへの追記(baseline公平性)
```tex
In addition, the fixed \qty{24}{\celsius} baseline follows common practice in the target building's climate, but alternative baselines (e.g., a well-tuned static schedule) could narrow the reported improvements.
```

### C1. Conclusion改稿(数値elaboration+hedge+根拠種別対応)
Part 3の更新版参照。

### A1. Abstract(最小修正)
- "room size approaches six occupants" → "as the subgroup size approaches six occupants in the studied rooms"(用語統一+条件依存)。
- "identify when ... is justified for practical HVAC control" → "provide simulation-based guidance on when high-resolution occupancy tracking is likely to be worthwhile"。
- R4を採用しない場合はmean occupancy 4--5の文を削除(採用する場合はそのまま)。

---

## Part 3. 更新版シミュレーション(Results抜粋 / Discussion / Conclusion)

以下はR1--R5, D1--D6, C1を反映した場合の姿。数値の[TODO]は結果ファイル突合が前提。

### Results(構成のみ、変更点はPart 2の通り)
1. Orientation段落(R1)
2. 4.1 Comfort performance: 観察+定量+不確かさ+弱条件、メカニズム文なし、sparse-occupancy図復活(R4)
3. 4.2 Setpoint adjustment: 観察のみ、0.5°C対応の事実記述まで
4. 4.3 Action frequency & UTR: 現状維持+高UTR域のサンプル薄さ併記

### Discussion(全文シミュレーション)
```
5.0 Key contributions (D1)
5.1 Effect of occupancy parameters on comfort performance
    - topic sentence: 本稿が加えるのはtemporal-resolution軸 (D2)
    - Jung: simulation研究としての要約 + same broad tendency + 閾値は building-specific
    - メカニズム説明 (D3)
5.2 Effect of occupancy parameters on control
    - 現行の0.5°C刻み・分解能ミスマッチ(ono_effects_2022)の議論は維持
    - UTR: count系metricとの違い(現行L26--27は良いので維持)
    - 使い分けガイダンス + comfort-only scope明示 (D4)
5.3 Relation to the companion field study (D5)
5.4 Limitations
    - 現行4点 + baseline公平性 (D6)
```

### Conclusion(全文シミュレーション)
```tex
This study investigated how the temporal resolution of \ac{gcm} aggregation affects predicted comfort and control burden in dynamically occupied shared offices, using an agentic simulation built on one month of field data (39 participants, 2,608 comfort votes, and reconstructed location logs) from seven office rooms.
Three \acp{gcm} were compared: a \ac{sgcm} based on regular room members, a \ac{dgcm} based on daily attendees, and a \ac{rtgcm} based on occupants present at each control timestep.

The simulation showed that the \ac{rtgcm} achieved the highest mean comfort probability in all rooms and subgroup sizes, and that improvement over the fixed \qty{24}{\celsius} baseline diminished with subgroup size for all policies.
The \ac{sgcm} improvement approached zero around subgroup sizes of five to seven in the studied rooms, whereas the \ac{rtgcm} and \ac{dgcm} maintained improvements of approximately [TODO: 15--20 / 8--15]~percentage points at the largest tested sizes.
The \ac{rtgcm} advantage was concentrated in sparse-occupancy conditions and diminished as daily mean occupancy approached four to five occupants.
At the same time, \ac{rtgcm}-based control required setpoint adjustments that typically met or exceeded the common \qty{0.5}{\celsius} thermostat step, and the share of 30-minute windows requiring action rose with occupant turnover, reaching about \qty{90}{\percent} when \ac{utr} was around 0.7--0.8.

These findings indicate that, within a comfort-only simulation scope, high-resolution occupancy tracking is likely to be worthwhile selectively -- in sparsely and dynamically occupied shared spaces -- and that occupancy metrics such as mean occupancy, subgroup size, and \ac{utr} can screen candidate spaces before investing in tracking infrastructure.
The specific numerical ranges are conditional on the studied building, occupant population, and observation period.
Future work should include closed-loop field tests, energy and \ac{hvac}-dynamics analysis, privacy-aware sensing implementation, and longer deployments across different office types.
```

---

## Part 4. 再帰レビュー(複数視点)

### Round 1

**視点A: 読者ガイド(Mihara型)**
- ○ R1のorientationで解決。ただしR1が「4.3」と手書き番号で参照している → `\autoref`化が必要。**[修正済→Part 3では\autoref前提]**
- △ R4復活図(contour+回帰線)は読み方の一文(軸・系列・値の大小が問いにどう対応するか)がまだ仮置き。図の系列(k4/k6/k8)と「なぜKを固定してもmean occupancyで差が出るのか」の一文が必要。→ **修正1: R4に "This analysis holds subgroup size fixed and varies realized occupancy, complementing Fig.~X where realized occupancy co-varies with $K$." を追加。**

**視点B: 貢献と先行研究(Ono型)**
- ○ D1で3分類は成立。D2のtopic-sentence-firstも成立。
- △ D1の設計含意文が長すぎ、"a decision that this simulation can inform but not settle" はD4と役割重複(観点2.5: 同じ含意の繰り返し)。→ **修正2: D1ではscopeの一言("within a comfort-only simulation scope")に短縮し、詳細なqualitative条件はD4に一本化。**
- △ D5 "our companion field analysis" — 投稿時に二重投稿・自己言及の扱いに注意。査読匿名性が必要な誌なら "a companion field analysis" + 引用形式に。→ **修正3: 表現を匿名性対応可能な形にメモ。**

**視点C: 過剰主張チェッカー**
- ✗ Round 1のConclusion案 "\ac{rtgcm} advantage was concentrated in sparse-occupancy conditions" — R4を復活させる前提でのみ成立。R4不採用ならこの文は削除必須。→ **依存関係を明記(修正4)。R4採用が前提条件。**
- △ "can screen candidate spaces" — screeningは未検証の運用行為。"could serve as screening indicators" に弱める。→ **修正5: Conclusion/D1ともcouldに統一。**
- ○ D4の "subject to verification in the target building" hedgeは観点1.5を満たす。

**視点D: 整合性チェッカー**
- ✗ Round 1のConclusionは "percentage points" を使うが、Results/Abstractは "%"(improvementの単位定義が曖昧)。改善量は確率の差なのでpercentage pointsが正しい。**Results/Abstract側も含め全章でpp表記に統一するか、Resultsのimprovement定義文(R1末尾)に「差である」と明示して%表記を維持するか、どちらかに決める必要。→ 修正6: R1に定義文があるため%維持でも可だが、Jungの「2 percent」との比較箇所は単位の取り違えに注意。**
- ✗ fig:ImpGCDMvsRTGCMの向き問題が未解決のままDiscussionのD3が「RTの優位はwithin-day transitionsのため」と一般論を述べている。もしデータが「優位はKとともに拡大して飽和」なら現行Discussion 5.2の「小さい部屋で有効」系の記述と衝突。→ **修正7: データ確認を最優先タスクに昇格。確認までD3の最終文は "at larger subgroup sizes" の限定を保留。**
- △ 「seven office rooms」(Conclusion案) vs Resultsの「four office rooms」(fig:ComfAgentic) — データ収集は7室、シミュレーション分析対象は4室。Conclusionでの言い方は "from seven office rooms" (データ) と "four analyzed rooms" (分析) を区別。→ **修正8。**

**視点E: 統計レビュアー**
- △ MC 1000試行の変動幅[TODO]は、SDか95%区間かを決めて全図に共通のエラーバー方針を適用すべき。図側にband追加が理想だが、最低限本文で1回言及。
- △ UTR 0.7--0.8の90%は高UTR域のn数併記が必要(fig:CtrlWindowRatioにCIはあるが、binごとのnがない)。→ 本文に "based on relatively few windows" 等の併記か、図にn表示。

### Round 2(修正1--8適用後)

**視点A(再)**: orientation・図の読み方とも解決。R4の補足文で「Kとmean occupancyの2視点」の関係が4.2のheatmap段落(既存L99)と整合することを確認 — 既存文と用語("normalized mean occupancy ratio" vs "daily mean occupancy")が異なる点のみ注意。軸が異なる(ratio vs 人数)ので用語は分けたままが正しい。指摘なし。

**視点B(再)**: D1短縮版で重複解消。key contributions段落の "design parameter" が新アルゴリズム提案と誤読されないか(観点1.7)→ "treats ... as an explicit design parameter" は評価枠組みの記述であり許容。ただしAbstractに同語を輸出しない方が安全。収束。

**視点C(再)**: 残る過剰主張は "carry comfort-relevant information"(D3)のみ。シミュレーション内の帰結なので "in the simulation" を添えれば収束。→ **修正9: D3末文に "in the present simulation" を追加。**

**視点D(再)**: 単位方針(修正6)を「improvement=差、%表記維持、定義文で明示」に確定するなら、Jung比較文で "percentage-point" を使わず "marginal improvement" と質的表現にしたD2案は既に整合。残タスクはfig:ImpGCDMvsRTGCMのデータ確認のみ(執筆で解決不可)。収束。

**視点E(再)**: [TODO]2件(MC変動幅、高UTR域n)はデータ作業として残置。文章側は収束。

### 収束判定
Round 2で文章レベルの指摘は解消。残りは**データ確認3件**(下記)に依存するため、これ以上の文章反復は無意味と判断し打ち切り。

---

## Part 5. 実施順チェックリスト

**データ確認(執筆より先)**
1. fig:ImpGCDMvsRTGCM(RT−DGCM差)のK依存の向き確認 → Results L58--59とDiscussionの「小さい部屋で有効」記述の存否を確定(修正7)
2. DGCM improvementの範囲(5--20% vs 8--15%)、4.2冒頭の「15--30%」を結果ファイルと突合
3. MC 1000試行の変動幅(SD/95%区間)と高UTR binのn数を算出(新規再集計ではなく既存結果ファイルからの転記が原則)

**必須修正(不整合)**
4. 重複図削除、fig:UTRexamplesキャプション修正、"dynamic group control"→RTGCM統一、誤植3件(R5)
5. analysis72復活(R4)またはAbstract/Conclusionのsparse-occupancy主張削除 — どちらかに確定
6. Abstract用語統一(A1)

**構成改善**
7. Results orientation(R1)、メカニズム文の移動(R3→D3)、L103実務文削除
8. Discussion: D1(短縮版)、D2、D4、D5(companion paper)、D6
9. Conclusion差し替え(Part 3、修正5・8適用)
10. D5とcausality論文Discussionの差分軸の突合(観点9.5)
