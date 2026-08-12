# 引き継ぎ資料: ASIM 2026 会議論文プロジェクト(Claude作業用)

作成日: 2026-07-18。会社アカウントのClaudeへの引き継ぎを想定し、(1) 現状、(2) 苦労した点と回避策、(3) 検証・設定で対応すべきこと、(4) サブエージェント分割の推奨パターン、をまとめる。

---

## 1. プロジェクト現状

- **論文**: IBPSA ASIM 2026 フルペーパー(8ページ上限、参考文献込み)。現在**ちょうど8ページ・コンパイル警告ゼロ**。
- **構成**: `ASIM2026-fullpaper-template.tex`(preamble+Abstract)が `sections/{introduction,method,results,discussion,conclusion}.tex` を`\input`。`appendix-draft.tex` は**意図的に非コンパイル**(ASIMのページ制限はAppendix込みのため)。
- **元データ**: 隣の `OccupancyDynamics` リポジトリ(ジャーナル原稿)。**読み取り専用・コピーのみ可**(著者指示)。図7点はmd5一致で複製済み。
- **実施済み**: 元論文との全数値ファクトチェック → Results/Discussion強化 → 8ページ化 → 可読性レビュー → `ref/ReviewPerspectives_SimulationPaper.md`(11観点)に基づく再帰レビュー2ラウンド → 採用反映。
- **主要ドキュメント**:
  - `content-selection-notes.md` — 章別の「残した/削った/Appendix退避」台帳
  - `review-perspectives-report.md` — 観点別評価、レビュー経過、**削除文の復元台帳(Part 5)**、残タスク(Part 4)
  - 再帰レビューの採用稿は `sections/` へ反映済み。重複していた `sim-update/` とプレビューPDFはGit整理時に削除済み

## 2. 苦労した点と回避策(ビルド環境)

1. **同梱の`tectonic`バイナリはmacOS用**。Claudeのサンドボックス(Linux aarch64)では動かない。
2. **Linux版tectonic 0.15.0にはbiblatex+backend=bibtexのバグ**があり、本文中の引用が「著者名+年」でなくタイトルで出力される。**tectonic 0.16.9(aarch64-unknown-linux-musl)なら正常**。GitHub releasesから取得し `~/bin/tectonic16` に配置して使用した。
3. **マウントされたフォルダ内ではファイル削除が不可**(上書きは可)。中間ファイル(.aux等)を消せないため、**`~/build`にtex/sty/bib/sections/figuresをコピーしてコンパイルし、PDFだけをコピーで書き戻す**方式にした。
4. **バックグラウンドプロセスはbash呼び出し間で死ぬ**(各呼び出しが独立)。長いコンパイルは `timeout 40` の**フォアグラウンド実行**で行う。初回はフォントダウンロードで時間切れになるが、キャッシュが効くので**リトライすれば通る**。
5. **Overleaf同期**: このフォルダはOverleaf Workshop拡張で同期されている。ブラウザでOverleafを開く必要はなく、ローカルコンパイルで検証→同期に任せるのが速い。
6. **ページ収支の管理**: 8ページ制限下では「1文追加=どこかで1文削除」。追記を伴う編集は必ず**試験コンパイルでページ数と溢れ行数を実測**してから確定する(文字数からの推定は約105字≒1行が目安だが、フロート再配置で大きくズレることがある)。

## 3. 内容面で苦労した点(執筆・検証)

1. **元論文の本文と図の不一致**。ジャーナル原稿ch4の本文数値が図と食い違う箇所が複数あり(RT改善15–20%と書くが図は12–15%、UTR 0.7–0.8で90%と書くが図は≈0.9で90%、等)。**会議論文は「図とコード」準拠**で書いた。数値の出典は常に図・結果ファイルにあたること。ジャーナル側の要修正リストは `review-perspectives-report.md` 冒頭と `content-selection-notes.md` 末尾に記録済み。
2. **15分 vs 30分グリッド**。ジャーナルMethodは30分、コード(`GEARoccupancyComfortSimulation.ipynb`)と最終図は15分。会議論文は15分で統一(検証済み)。ジャーナル側は未修正。
3. **図に根拠のない主張の混入リスク**。「平均在室4–5人で頭打ち」は元論文abstract由来だが、会議論文に根拠図(analysis72 contour)がないため**数値主張を撤去し定性表現に変更**した。復活させる場合は図の追加(≈1/3ページ)とセット。
4. **エラーバーの統計定義が元論文でも未定義**(analysis21系の図)。安全な表現「spread across simulation trials」を使用中。fig:control(b)の「95% date-cluster bootstrap, 1,000 resamples」だけは元キャプションと逐語一致で検証済みなので変更しないこと。
5. **用語の正規化**。K関連は「subgroup size $K$」「regular-member pool」、行動指標は「actionable step」に統一済み。**UTRは会議論文で「occupant turnover rate」、ジャーナルは「user turnover rate」のまま**——シリーズ論文としてどちらかに揃える判断が未了。

## 4. 未了タスク(次の作業者へ)

1. 「4–5人で頭打ち」数値の復活可否(contour図追加とセット、Appendix行きも可)
2. companion(causality)論文への言及: `sections/discussion.tex` 末尾にコメントで文案待機。引用可能になったら有効化を判断
3. エラーバーのSD/CI定義と高UTRビンのn数を元結果ファイルで確認(**新規再集計はしない**方針)
4. Jung & Jazizadeh 2020「約6人で約2%に収束」の原文最終確認(レビュアーはDOIアクセス不可だった)
5. ジャーナル原稿側の errata 修正(上記3.1、3.2)
6. UTR名称のシリーズ統一(3.5)

## 5. サブエージェント分割の推奨パターン(今回有効だった構成)

### 基本構成: Orchestrator + 専門サブエージェント
オーケストレーター(メイン)が裁定・統合・コンパイル検証を持ち、サブエージェントには**読み取り専用または単一ファイル所有**の仕事だけを渡す。

| 役割 | モデル目安 | 権限 | 要点 |
|---|---|---|---|
| ファクトチェッカー | Explore/中位 | 読み取り専用 | ドラフト全数値を元データと照合。図はmd5照合。「本文でなく図を信じる」原則 |
| セクション執筆者(Results/Discussion) | 中位(Sonnet級) | **自分のsectionファイルのみ編集可** | 検証済み数値リストを渡し「変更禁止」と明記。長さ収支(±N行)を義務化 |
| 軽微セクションレビュー | 軽量(Haiku級) | 読み取り専用 | 削減候補の列挙など、判断より列挙が主の仕事に向く |
| レビューパネル(並列3視点) | 中位 | 読み取り専用 | ①フレーミング+過剰主張 ②読者ガイド+図表 ③Prior work+用語+整合+統計。**各自に削減案ノルマ**(N行分)を課すとページ収支が回る |
| Round 2(独立2系統) | 中位 | 読み取り専用 | ①コメント充足チェック(前ラウンド全項目の対応検証) ②**前情報なしの**過剰主張チェック(fresh eyes)。収束判定させる |

### 運用上の教訓
- **共有ファイルの同時編集はさせない**。並列執筆は章別ファイル分割が前提(今回`sections/`分割はそのために実施)。
- **サブエージェントには文脈を明示的に渡す**。検証済み数値リスト、ページ収支、読み取り専用フォルダ、引用可能なbibキー一覧を毎回プロンプトに含める。省くと再調査で時間を浪費するか、誤った"修正"をする。
- **レビュアー間の指摘は矛盾する**(例: 同じ文をAは削除・Bは維持と主張)。裁定はオーケストレーターの仕事として残し、裁定理由をレポートに記録する(`review-perspectives-report.md` Part 3の形式)。
- **削除は台帳に記録**して撤回可能にする(ReviewPerspectives §11.3)。
- 本番ファイルを直接いじらせたくない検討作業は **`sim-update/`方式**(ドラフト用ディレクトリ+試験コンパイル+プレビューPDF)が安全。採否だけユーザーに確認。
- レビュー基準は `ref/ReviewPerspectives_SimulationPaper.md` をプロンプトで参照させる。ジャーナル側の同種レビュー(`OccupancyDynamics/ref/review_simupaper_perspectives_recursive_20260718.md`)との整合も確認事項に含めること。

### ビルド検証の定型手順
```
# 1) Linux用tectonic 0.16.9を ~/bin/tectonic16 に配置(0.15はbiblatexバグあり)
# 2) プロジェクトを ~/build にコピー(マウント先では.aux等を消せないため)
cp -r <mount>/{ASIM2026-fullpaper-template.tex,Asim2026.sty,references.bib,sections,figures} ~/build/
# 3) フォアグラウンドでコンパイル(初回はフォントDLでtimeoutしうる→リトライ)
cd ~/build && timeout 40 ~/bin/tectonic16 -X compile --keep-logs ASIM2026-fullpaper-template.tex
# 4) 検証3点セット: ページ数 / Overfull / 溢れ内容
pdfinfo ASIM2026-fullpaper-template.pdf | grep Pages
grep -c Overfull ASIM2026-fullpaper-template.log
pdftotext -f 9 -l 9 ASIM2026-fullpaper-template.pdf -   # 9ページ目が存在しないことを確認
# 5) PDFのみマウント先へ書き戻し
cp ASIM2026-fullpaper-template.pdf <mount>/
```
仕上げ時は `pdftoppm -png` でページ画像を出して視覚確認(フロート配置・キャプション・参考文献の体裁)。
