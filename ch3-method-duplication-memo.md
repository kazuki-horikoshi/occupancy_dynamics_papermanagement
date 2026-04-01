# ch3-Method 重複候補メモ

`chapters/ch3-Method.tex` を確認し、現行本文・コメントアウト・Appendix 側で重複している内容を拾い出したメモです。  
ここでは「完全一致に近いもの」または「役割がほぼ同じで整理対象になりそうなもの」を優先しています。

## 1. 現行本文とコメントアウトで重複している候補

### 1-1. PCM の導入説明と基本式
- 現行: `chapters/ch3-Method.tex:111-129`
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:510-520`
- 内容:
  - PCM を各参加者ごとに構築する説明
  - 入力が室温中心であること
  - Daum et al. ベースのロジスティック回帰
  - `P(S_{th}=s \mid t_i)` に相当する基本式
- 判定: ほぼ重複
- メモ: コメントアウト側は旧版の簡略記述で、現行版の方が少し詳しいです。
- 対応状況: 4/1修正済み

### 1-2. 個人快適温度 `T^p_i` と快適範囲 `[T^c_i, T^h_i]`
- 現行: `chapters/ch3-Method.tex:138-152`
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:533-549`
- 内容:
  - Preferred Temperature の定義
  - Individual Comfort Range の定義
  - その快適範囲を coverage 評価に使う説明
- 判定: 実質重複
- 対応状況: 4/1修正済み

### 1-3. GCM の定義と Occupancy Metrics の定義
- 現行: `chapters/ch3-Method.tex:154-189`
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:554-592`
- 内容:
  - Dynamic GCM の説明
  - `\mu_t` の定義
  - `N_t`, `\sigma^{(W)}_{N,t}`, `UTR^{(W)}_t` の定義
- 判定: ほぼ重複
- メモ: コメントアウト側は wording が少し古く、`User Turnover Rate (UTR)` の書き方が現行と少し違う程度です。
- 対応状況: 4/1修正済み

### 1-4. Baselines and deviations
- 現行: `chapters/ch3-Method.tex:352-377`
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:619-650`
- 内容:
  - Static / Daily baseline の定義
  - `\Delta T^{\mathrm{Static}}_t`, `\Delta T^{\mathrm{Daily}}_t` の定義
  - `|\Delta T|` を分析対象にする説明
- 判定: 実質重複
- 対応状況: 4/1修正済み

## 2. 現行本文と Appendix 側で役割が重なっている候補

### 2-1. Occupancy log reconstruction 手順
- Method: `chapters/ch3-Method.tex:53-58`
- Appendix: `chapters/chap-appendices.tex:13-29`
- 内容:
  - Room Entry / General Presence / Building Exit の 3 種イベント説明
  - stay log の生成ルール
  - 当日最終イベントで stay を閉じる説明
  - anonymized ID, location, start-end times の出力
- 判定: 旧版では役割重複気味だったが、現在は整理済み
- メモ: 4/1 時点では Method 側が要約版、Appendix 側が詳細版になっており、役割分担は整理されています。
- 対応状況: 4/1修正済み

### 2-2. Thermal comfort survey 項目一覧
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:657-677`
- Appendix: `pic/chap-appe/ThermalComfort.tex:9-25`
- 内容:
  - Context items
  - Thermal comfort items
  - Personal factors
  - 各選択肢の詳細
- 判定: 実質重複
- メモ: これは「本文から外して Appendix 表に回した」痕跡としてかなり明確です。
- 対応状況: 4/1修正済み

### 2-3. Occupancy-related literature table の差し戻し痕跡
- 旧コメントアウト位置: 旧版 `chapters/ch3-Method.tex:557-569`
- Appendix: `chapters/chap-appendices.tex:31-39`
- 内容:
  - `table:OccuMetrics` の表を本文に置く旧案
  - 現在は Appendix に配置済み
- 判定: 配置先の重複候補
- メモ: 表の本文そのものが二重定義されているわけではないですが、「本文に置く旧記述」が残っていました。
- 対応状況: 4/1修正済み

## 3. 現行本文の中で繰り返し気味な箇所

### 3-1. stay log 生成の説明が 2 回続いていた件
- 旧版箇所: 旧版 `chapters/ch3-Method.tex:56-57` と 旧版 `chapters/ch3-Method.tex:66-67`
- 現状: `chapters/ch3-Method.tex:55-58`
- 内容:
  - 旧版では `structured stay log` の説明が近接して 2 回出ていた
  - 現在は簡潔な説明 + Appendix 参照に整理されている
- 判定: 解消済み
- 対応状況: 4/1修正済み

### 3-2. `|\Delta T|` を分析対象にする説明が再登場
- 1 回目: `chapters/ch3-Method.tex:370-377`
- 2 回目: `chapters/ch3-Method.tex:394-397`
- 内容:
  - `\Delta T^{\mathrm{Static}}_t`, `\Delta T^{\mathrm{Daily}}_t` の再掲
  - magnitudes を分析する説明の再掲
- 判定: 軽い重複
- メモ: TOST 節の `Outcomes` では「defined as in Eq. ...」だけに寄せても十分そうです。
- 対応状況: 未対応

## 4. 確認結果まとめ

4/1時点で対応済み:
- PCM 導入の旧コメントアウト重複
- 個人快適温度・快適範囲の旧コメントアウト重複
- GCM / Occupancy Metrics の旧コメントアウト重複
- Baselines and deviations の旧コメントアウト重複
- Occupancy log reconstruction の本文/Appendix の役割重複
- Survey 項目一覧の本文旧案と Appendix 表の重複
- OccuMetrics 表の本文旧案の残骸
- stay log 説明の近接重複

未対応:
- `|\Delta T|` を分析対象にする説明の軽い再掲
