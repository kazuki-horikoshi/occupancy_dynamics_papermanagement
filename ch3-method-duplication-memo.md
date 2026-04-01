# ch3-Method 重複候補メモ

`chapters/ch3-Method.tex` を確認し、現行本文・コメントアウト・Appendix 側で重複している内容を拾い出したメモです。  
ここでは「完全一致に近いもの」または「役割がほぼ同じで整理対象になりそうなもの」を優先しています。

## 1. 現行本文とコメントアウトで重複している候補

### 1-1. PCM の導入説明と基本式
- 現行: `chapters/ch3-Method.tex:129-147`
- コメントアウト: `chapters/ch3-Method.tex:510-520`
- 内容:
  - PCM を各参加者ごとに構築する説明
  - 入力が室温中心であること
  - Daum et al. ベースのロジスティック回帰
  - `P(S_{th}=s \mid t_i)` に相当する基本式
- 判定: ほぼ重複
- メモ: コメントアウト側は旧版の簡略記述で、現行版の方が少し詳しいです。

### 1-2. 個人快適温度 `T^p_i` と快適範囲 `[T^c_i, T^h_i]`
- 現行: `chapters/ch3-Method.tex:156-170`
- コメントアウト: `chapters/ch3-Method.tex:533-549`
- 内容:
  - Preferred Temperature の定義
  - Individual Comfort Range の定義
  - その快適範囲を coverage 評価に使う説明
- 判定: 実質重複

### 1-3. GCM の定義と Occupancy Metrics の定義
- 現行: `chapters/ch3-Method.tex:172-207`
- コメントアウト: `chapters/ch3-Method.tex:554-592`
- 内容:
  - Dynamic GCM の説明
  - `\mu_t` の定義
  - `N_t`, `\sigma^{(W)}_{N,t}`, `UTR^{(W)}_t` の定義
- 判定: ほぼ重複
- メモ: コメントアウト側は wording が少し古く、`User Turnover Rate (UTR)` の書き方が現行と少し違う程度です。

### 1-4. Baselines and deviations
- 現行: `chapters/ch3-Method.tex:377-402`
- コメントアウト: `chapters/ch3-Method.tex:619-650`
- 内容:
  - Static / Daily baseline の定義
  - `\Delta T^{\mathrm{Static}}_t`, `\Delta T^{\mathrm{Daily}}_t` の定義
  - `|\Delta T|` を分析対象にする説明
- 判定: 実質重複

## 2. 現行本文と Appendix 側で役割が重なっている候補

### 2-1. Occupancy log reconstruction 手順
- 現行: `chapters/ch3-Method.tex:55-74`
- Appendix 側コメントアウト: `chapters/chap-appendices.tex:13-29`
- 内容:
  - Room Entry / General Presence / Building Exit の 3 種イベント説明
  - stay log の生成ルール
  - 当日最終イベントで stay を閉じる説明
  - anonymized ID, location, start-end times の出力
- 判定: ほぼ重複
- メモ: Appendix 側は現在コメントアウトされているので本文と競合してはいませんが、将来戻すと重複になります。

### 2-2. Thermal comfort survey 項目一覧
- コメントアウト: `chapters/ch3-Method.tex:657-677`
- Appendix: `pic/chap-appe/ThermalComfort.tex:9-25`
- 内容:
  - Context items
  - Thermal comfort items
  - Personal factors
  - 各選択肢の詳細
- 判定: 実質重複
- メモ: これは「本文から外して Appendix 表に回した」痕跡としてかなり明確です。

### 2-3. Occupancy-related literature table の差し戻し痕跡
- コメントアウト: `chapters/ch3-Method.tex:557-569`
- Appendix: `chapters/chap-appendices.tex:31-39`
- 内容:
  - `table:OccuMetrics` の表を本文に置く旧案
  - 現在は Appendix に配置済み
- 判定: 配置先の重複候補
- メモ: 表の本文そのものが二重定義されているわけではないですが、「本文に置く旧記述」が残っています。

## 3. 現行本文の中で繰り返し気味な箇所

### 3-1. stay log 生成の説明が 2 回続いている
- 箇所: `chapters/ch3-Method.tex:56-57` と `chapters/ch3-Method.tex:66-67`
- 内容:
  - `structured “stay log” is generated...`
  - `structured ``stay log'' is generated...`
- 判定: 同一段落内の近接重複
- メモ: 1 回にまとめられそうです。

### 3-2. `|\Delta T|` を分析対象にする説明が再登場
- 1 回目: `chapters/ch3-Method.tex:395-402`
- 2 回目: `chapters/ch3-Method.tex:419-422`
- 内容:
  - `\Delta T^{\mathrm{Static}}_t`, `\Delta T^{\mathrm{Daily}}_t` の再掲
  - magnitudes を分析する説明の再掲
- 判定: 軽い重複
- メモ: TOST 節の `Outcomes` では「defined as in Eq. ...」だけに寄せても十分そうです。

## 4. 優先的に整理しやすそうな候補

優先度高:
- `chapters/ch3-Method.tex:510-520`
- `chapters/ch3-Method.tex:533-549`
- `chapters/ch3-Method.tex:554-592`
- `chapters/ch3-Method.tex:619-650`
- `chapters/ch3-Method.tex:657-677`

理由:
- いずれも現行本文か Appendix に内容が既に引き継がれており、削っても情報欠落が起きにくいです。

優先度中:
- `chapters/chap-appendices.tex:13-29`

理由:
- 今はコメントアウト済みなので実害はないですが、本文側と同じ説明が残っています。
