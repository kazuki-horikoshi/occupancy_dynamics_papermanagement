# 内容の取捨選択メモ(ASIM 2026 会議論文)

8ページ制限(参考文献込み)に収めるために「本文に残したもの/削った・圧縮したもの/Appendixに退避したもの」を章別に記録。
あとで内容を再選択する際のチェックリストとして使用。**現状: ちょうど8ページ、コンパイル警告ゼロ。**

- 本文: `ASIM2026-fullpaper-template.tex` + `sections/*.tex`
- 退避先: `appendix-draft.tex`(**意図的に非コンパイル**。ASIMのページ制限はAppendix込みのため)
- 元データ: 隣の `OccupancyDynamics` リポジトリ(読み取り専用。図7点はmd5一致を確認済み)

---

## Abstract

**残したもの**
- 研究目的(daily / real-time GCM が追加の在室情報に見合うかの定量化)
- 主要数値はすべて維持: 39名 / 2,608回答 / 4室 / RT-GCMのベースライン比 +12–15pt / DGCM比 +6–8pt / 最高在室密度でも約0.8°Cのステップ / 15分間隔のactionable率 37%→90%超
- 実務向け結論(疎で構成変動の大きい空間ほどreal-timeが正当化される)

**削った・圧縮したもの**
- 「Static aggregation is simple, but...」の導入文 → 冒頭文に統合
- 「Four weeks of anonymized indoor-environment measurements, thermal-preference surveys, and individual-level location logs were collected...」のデータ取得列挙 → PCM開発の1文に吸収(約4–5行削減)
- 「identity」→「composition」に用語統一(本文と揃えた)

---

## Introduction

**残したもの**
- 4段落構成: OCCの背景と実装障壁 → PCM/GCMと集約問題(Jung研究の減衰知見) → ハイブリッドワークによる問題の変化 → 本研究の3つのRQ
- 引用8件すべて維持
- SGCM / DGCM / RT-GCM の略語を最終段落で定義(初出をMethodのTable 1から前倒し)

**削った・圧縮したもの**
- 「Contemporary OCC frameworks connect sensing, comfort or occupancy learning, and control」の枠組み説明 → 「Real-world implementation, however, remains limited by...」に短縮
- 例示文「Two rooms can have the same occupancy count but different group preferences if different people are present.」→ 削除(前文の言い換えのため)
- メタ文「The conference paper deliberately condenses the field protocol and focuses on...」→ 削除(レビュー指摘: Methodを読む前の読者には評価不能な断り書き)
- 「count and identity」→「count and composition」(全体の用語統一)

**復元候補(スペースができた場合)**
- 元論文のtable:OccuMetrics(在室指標のレビュー: カウント系 vs 入替系)の言及 → Introの「先行研究はカウント偏重」の主張補強に使える(元: ch3 L148, app:OccupancyStudy)

---

## Method

**残したもの**
- 実測概要: 期間(2025/9/29–10/24)、シンガポールのオフィスビル、VAV空調、45名→39名、IRB番号、匿名化
- サーベイ設計: 1日最大6回、ASHRAE 3カテゴリ、入室20分以内の回答除外、2,608回答、実験セットポイント22–27°C
- 滞在ログの再構成(入退室時刻つき連続ステイ)
- PCM(順序多項ロジスティック)+ GCM式(Eq. 1)+ ポリシー比較表(Table 1)
- モンテカルロ設計: K人抽出+PCMランダム割当、Kの定義(潜在メンバー数≠瞬時在室数)、部屋×Kごとに1,000試行
- 評価指標: person-time平均快適確率、ベースライン(24°C固定)比のpt差、RT-GCMステップ幅、actionable判定(0.5°C丸めで0.5°C以上)
- UTR定義(Jaccard、Eq. 2)、15分遷移が主解析であること

**削った・圧縮したもの**
- 45→39名の文、ステイログの文を短文化(情報は維持)
- 「matching the estimation grid of the source analysis」→ 削除(会議論文単体では「source analysis」が未定義でむしろ混乱の元)
- actionable定義の二重記述を一本化(丸め解像度と閾値を1文に)
- 表現修正: 「evaluated by returning it to the PCMs」→「scored against the PCMs」/ 「user turnover rate」→「occupant turnover rate」(UTR略語は維持、全体でoccupantに統一)/ 「valid days」→「days」/ 「feasible K」に上限の説明を追記(部屋のレギュラープール数まで)

**Appendixに退避済み(appendix-draft.tex §Supplementary Method Details)**
- センサー設置詳細(複数センサーの平均処理、air speed・MRTの補助計測)
- セットポイント実験計画の詳細(1°C刻み・日毎ランダム化・午前午後の切替)
- 位置ログのクリーニング手順(重複・オーバーラップ解決、15分グリッドへの変換)
- 室日快適確率CPの完全な数式定義と集計手順
- 変更ステップ解析の閾値詳細(|δT|≥0.05°C)

---

## Results(参考: 今回の主な変更)

**残したもの+強化**
- 全数値は元論文の図から検証済みのまま維持
- 部屋タイプの対比(共有オフィスは日中もUTRが動的、固定席のKDは約0.2–0.4に留まる)
- キャプション修正: 「source analysis」表現を自己完結的な表現に変更、Katris/KDのラベル説明は維持

**見送ったもの**
- RT-GCMの優位が平均在室4–5人付近で頭打ちになる数値主張は、会議論文内に根拠図がないため最終稿から撤去。復活させる場合はanalysis72 contour図の追加とセットにする

**削ったもの**
- 「confirming a room-specific but never-eliminated benefit」「rather than growing indefinitely with K」等の冗長句

**Appendixに退避済み(appendix-draft.tex §Supplementary Results)**
- Fig: セットポイント調整幅のヒートマップ(`setpoint_adjustment_heatmap.png`, K×正規化在室率)→ 本文Fig.3(a)が主傾向を直接伝えるため退避
- Fig: 30分ローリングUTRの部屋別プロファイル(`turnover_profiles_by_room.png`)→ 15分UTRと行動率の主関係には不要と判断し退避

---

## Discussion(参考: 今回の主な変更)

**残したもの+強化**
- 3小節構成を維持(集約解像度の議論 / actionable控制への翻訳 / 限界と今後)
- 追加: Jung & Jazizadeh (2020)の「6人で約2ptに収束」の定量アンカー
- 追加: 連続シミュレーションの0.1°C刻み vs 0.5°C実用ステップの対比(元は「fine setpoint grid」と曖昧だった)
- 追加: 月曜午後の会議によるUTRスパイクの実例(R&D≈1.0、Shared Office 2≈0.8)
- 追加: 展開階層(SGCM=固定席 / DGCM=バッジ・予約データで十分 / RT-GCM=疎で動的)にUTR実測値の裏付け

**削った・圧縮したもの**
- 「Two consecutive intervals can share the same count yet hold entirely different occupants...」→ 月曜スパイクの実例に置換(同じ論点をより具体的に)
- Limitations 3段落を字句レベルで圧縮(論点は全維持: PCMランダム割当の限界 / 公平性未測定 / 省エネ非主張 / プライバシー・統合コスト)

---

## Conclusion

**残したもの**
- RQ1–3への回答を同順で維持: SGCM減衰→ゼロ / RT-GCMの+6–8pt収束 / ステップ幅と頻度の分離 / 選択的展開の実務指針 / UTRの診断的価値

**削った・圧縮したもの**
- 第2段落の3文を短文化(内容は不変)
- 用語統一: 「Static improvement / daily and real-time representations」→「SGCM / DGCM / RT-GCM」、「action frequency」→「frequency of actionable changes」

---

## 完全に見送ったもの(Appendixにも未収載)

- エネルギー影響の議論(元論文でも今後の課題扱い。Limitationsで非主張を明言するに留めた)
- 公平性(fairness)指標の分析(Limitationsで研究ニーズとして言及のみ)
- PCMの個人別フィット詳細・モデル診断
- 元論文ch2(Review)の文献レビュー本体

## 復元・差替えの目安

- 現状ちょうど8ページ(8ページ目の残り≈数行)。**何かを足すには同量を削る必要あり**
- 候補の目安コスト: ヒートマップ図 ≈ 1/3ページ / 30分UTRプロファイル図 ≈ 1/2ページ / 文章の復元は1文≈2–3行
- 逆に削り代が必要になった場合の第一候補: Conclusionの展開指針の3項並列文(約6語圧縮可)、Method冒頭のビル説明

## 元論文(OccupancyDynamics)側の要修正メモ

会議論文はすべて図・コード準拠。ジャーナル原稿の本文が図と不一致の箇所:

- ch4: RT改善「15–20%」→ 図は12–15%(DGCM「5–20%」→ 図は5–9%)
- ch4: 「UTR 0.7–0.8で90%」→ 図は0.7–0.8で約78–82%、90%到達は≈0.9
- ch4: 低在室のステップ幅「約1.0°C (1–5人)」→ 図は1人付近で1.3°C
- ch3: 制御タイムステップ「30分」→ コード(`GEARoccupancyComfortSimulation.ipynb`)と最終図は15分
