# A6P subgroup figures: Results / Discussion レビュー

## 対象

確認したファイル:

- `chapters/ch4-Results.tex`
- `chapters/ch5-Discussion.tex`
- `ref/instruction_a6p_subgroup_figure_reference.md`

対象箇所:

- `\subsection{Comfort performance across different resolution of \ac{gcm}}`
- `a6p_static_realtime_daily_by_subgroup`
- `a6p_improvement_vs24_by_subgroup`

このレビューでは `.tex` ファイルは修正していない。

## 全体所見

Resultの章では、「\ac{gcm} の時間解像度が高いほど comfort achievement が高くなる」「subgroup size が大きくなると static model の優位性が小さくなる」という主結果はすでに書けている。

ただし、現状のResultでは元データから直接言える観察が少し不足している。一方で、現在のResultにはメカニズム説明に近い文が含まれており、先生の方針である「ResultではDiscussion-likeなことを書かない」に照らすと、Discussionへ移した方がよい。

Discussionは方向性としては適切だが、subsection title の重複、未完成の参照、A6Pの具体的な結果との接続不足がある。

## Resultに追加できる観察

以下は図と元データから直接読めるため、Resultに入れてよい内容である。

1. Baseline control は subgroup size や room に対してほぼ一定である。

`fixed24_0_ratio` は全体として 0.66--0.68 程度に収まっている。したがって、improvement の低下は baseline 側の変化ではなく、model-based control 側の変化として説明できる。

2. Daily model は一貫して static model と real-time model の中間に位置する。

全ての room と subgroup size で、`daily_fixed_ratio` は `static_ratio` より高く、`dynamic_ratio` より低い。これはResultに書ける明確な順位関係である。

3. Real-time model は全条件で最も高い comfort achievement ratio を示す。

平均値の範囲は、real-time model が約 0.81--0.98、daily model が約 0.74--0.96、static model が約 0.65--0.73 である。過度な解釈をせずに、定量的な結果として述べられる。

4. Static model の improvement は、大きい subgroup size でゼロ付近またはわずかに負になる。

Static improvement は room によって差があるが、おおむね `k = 5--7` 付近でゼロに近づく。Katris Office では `k >= 6`、Shared Office 2 では `k = 7` で負の値になる。

5. Daily model と real-time model の improvement も subgroup size とともに低下するが、最大 subgroup size でも正の値を保つ。

最大 subgroup size では、real-time improvement は約 0.14--0.20、daily improvement は約 0.08--0.15 程度である。この点はResultに入れると、staticとの差が明確になる。

6. Shared Office 2 は real-time / daily の改善幅が大きい例として示せる。

Shared Office 2 では、real-time improvement が `k = 2` で 0.3086、`k = 7` でも 0.2032 である。Roomごとの特徴を1文だけ補足したい場合には使える。

## Resultから外した方がよい内容

現在のResultにある次の文は、観察結果ではなくメカニズム説明になっている。

```tex
This suggests that, in larger rooms, the \ac{rtgcm} benefits from more dynamic occupant transitions, whereas the \ac{dgcm} cannot fully capture time-varying group comfort as occupancy changes.
```

この内容自体は悪くないが、ResultよりDiscussion向きである。Resultでは、次のように観察された差に留める方がよい。

```tex
The difference between the real-time and daily models remained visible at larger subgroup sizes, with the real-time model maintaining higher improvement than the daily model across all rooms.
```

Occupant transitions による解釈はDiscussionへ移すのがよい。

## 現在のResult表現で注意が必要な点

現在のResultには次の文がある。

```tex
The performance of \ac{rt-gcm} and \ac{dgcm} shows decreasing trend with similar ratio as subgroup size increases, while the performance of \ac{sgcm} shows more rapid decrease as subgroup size increases.
```

この表現は、元データと少しずれる可能性がある。Comfort achievement ratio の絶対値で見ると、static model の変化幅は daily / real-time より小さい。一方で、baselineとの差分として見ると、static model の improvement はゼロに近づく。したがって、achievement ratio と improvement を分けて書く方が安全である。

修正案:

```tex
The comfort achievement ratios of all model-based controls generally decreased as subgroup size increased. The static model showed a smaller absolute range, but its improvement over the baseline approached zero at larger subgroup sizes.
```

また、現在の次の文は daily model の値をやや低く見積もっている。

```tex
\ac{dgcm} marks \qtyrange{80}{85}{\percent} with size of subgroup such as 2--5.
```

元データでは、daily model は `k = 2` で約 0.90--0.96、`k = 2--5` 全体では約 0.78--0.96 である。書く範囲を明確にした方がよい。

修正案:

```tex
For the daily model, the comfort achievement ratio was approximately 0.90--0.96 at \(k = 2\), and ranged approximately from 0.78 to 0.96 across \(k = 2\)--5.
```

## Resultへの加筆案

以下は、Resultにそのまま入れやすい簡潔な英文案である。

```tex
Across all rooms, the baseline control remained nearly constant at approximately 0.66--0.68 across subgroup sizes. The real-time model showed the highest comfort achievement ratio for every room and subgroup size, followed by the daily model and then the static model. The mean comfort achievement ratio ranged approximately from 0.81 to 0.98 for the real-time model, 0.74 to 0.96 for the daily model, and 0.65 to 0.73 for the static model.

The improvement relative to the 24 \si{\celsius} baseline decreased as subgroup size increased. Static-model improvement approached zero around subgroup sizes of 5--7 and became slightly negative in some larger subgroups. In contrast, the daily and real-time models maintained positive improvement at the largest tested subgroup sizes, with real-time improvement remaining approximately 0.14--0.20 and daily improvement approximately 0.08--0.15.
```

この案は、順位、範囲、低下傾向、baselineとの差分のみを述べており、メカニズム説明を避けている。

## Discussionのレビュー

最初のDiscussion subsectionは、static model の improvement が大きい subgroup size で小さくなる点を先行研究とつなげており、方向性はよい。

ただし、以下の点は修正した方がよい。

1. `Effect of occupancy parameters to comfort achievement` という subsection title が2回出ている。2つ目は control adjustment に関する内容なので、別タイトルにした方がよい。

2. `Figure \ref{fig:}` と `\autoref{}` が未完成である。コンパイル前に削除または正しい参照へ置換する必要がある。

3. Discussionでは、Resultで整理した「staticはbaselineに近づく」「dailyは中間」「real-timeは最高」という結果を受けて、それが何を意味するかを説明すると流れがよい。

4. Resultから外すべきメカニズム説明は、Discussionへ移すとよい。具体的には、real-time aggregation は control step ごとの在室者構成を反映できるのに対し、daily aggregation はその日の来室者集合、static aggregation は登録メンバーに固定される、という説明である。

5. `jung_energy_2020` との比較は簡潔にした方がよい。先行研究との共通点は「人数が増えると group comfort control の改善幅が小さくなる」点であり、本研究の新規性は static / daily / real-time という時間解像度の比較にある。

## Discussionへの加筆案

以下は、Discussionに入れやすい英文案である。

```tex
The convergence of the static model toward the fixed baseline at larger subgroup sizes is consistent with previous findings that the benefit of group comfort control decreases as the number of occupants increases. In the present simulation, this pattern appeared around subgroup sizes of 5--7, where the static-model improvement became close to zero. This indicates that a static aggregation of regular room members provides limited additional benefit when individual preferences are averaged over a larger group.

By contrast, the daily and real-time models retained positive improvement at the largest tested subgroup sizes. This suggests that the relevant limitation is not only the number of occupants but also the temporal resolution at which occupant composition is represented. The daily model captured the attendee set for each day, whereas the real-time model captured the occupants present at each control step. The consistently higher performance of the real-time model therefore indicates that within-day occupancy transitions can remain relevant even when the subgroup size is relatively large.
```

この案は、Resultで報告した事実を受けて、その意味をDiscussionとして解釈する構成になっている。

## ResultとDiscussionの切り分け

Resultに書くとよい内容:

- 各 model の順位関係
- comfort achievement ratio の範囲
- subgroup size に伴う低下傾向
- baseline がほぼ一定であること
- static improvement がゼロ付近に近づくこと

Resultでは避けるとよい内容:

- `This suggests...` で始まるメカニズム説明
- `rtgcm` がなぜ occupant transitions の恩恵を受けるか
- 実運用上の示唆や推奨

Discussionに書くとよい内容:

- daily model と real-time model の差が temporal resolution によるものであること
- static GCM は実際の在室者構成が登録メンバーとずれる場合に限界があること
- within-day occupancy transition がある部屋では real-time GCM の価値が残る可能性

