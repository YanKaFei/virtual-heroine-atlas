<div align="center">

# バーチャルヒロイン図鑑

**Virtual Heroine Atlas**

### 132 名の女性バーチャルキャラクターを実測して分解した資料庫

なぜ伸びたのか &nbsp;·&nbsp; その見た目はどう設計されているのか

[![Obsidian](https://img.shields.io/badge/Obsidian-%E5%BF%85%E9%A0%88-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![cards](https://img.shields.io/badge/cards-132-E11D48)
![images](https://img.shields.io/badge/images-133-0EA5E9)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek-Harness-4D6BFE)](https://github.com/topics/deepseek-harness)
![usage](https://img.shields.io/badge/usage-%E3%83%86%E3%82%B9%E3%83%88%E7%94%A8-000000)

[中文](README.md) · [English](README.en.md) · [**日本語**](README.ja.md)

</div>

---

## これは何か

**女性バーチャルキャラクター**の研究用資料庫です。日本・韓国・中国・英語圏・インドネシアから
132 名、ひとりにつきカード 1 枚。どのカードも同じ二つの問いを立てます。

> **彼女はなぜ広まったのか？** &nbsp;·&nbsp; **その見た目はどう設計されたのか？**

前者はコンテンツと運営の分解、後者はデザインの分解です。配色、衣装の構造、表情のレパートリー、
話し方の癖、感情の定位。最後にそれを、画像生成モデルにそのまま渡せる階層化プロンプトに圧縮します。

**ランキングではありません。** ファン wiki でも、ハウツーでもありません。
132 枚が同じ構造で同じ問いに答えるので、横に並べて比較でき、そして**検索して再利用できます**。

> カード本文は中国語です。README は中国語・英語・日本語の 3 言語を用意しています。

---

## ⚠️ まず Obsidian を入れてください（必須）

**このリポジトリは Obsidian の Vault 形式です。** カード内の挿絵は Obsidian の
ウィキリンク埋め込み記法（`![[画像名]]`）を使っているため、**GitHub の Web 画面でカードを
開いても画像は表示されません**。

Obsidian をインストールしてから、このフォルダを Vault として開いてください。

| 手順 | やること |
|---|---|
| **1** | **[obsidian.md](https://obsidian.md)** からダウンロードしてインストール（無料。Windows / macOS / Linux / iOS / Android） |
| **2** | Obsidian を起動 → **「フォルダを Vault として開く」** → このリポジトリのルートを選ぶ |
| **3** | **設定 → コアプラグイン → 「Bases」をオン**（データベース表示に必要。Obsidian 標準搭載で、別途インストールは不要） |

これで `views/library.base` に言語・プラットフォーム・状態・要素ごとの 4 つの表、
`views/factors.base` に要素ごとの表ができ、「反差結構で伸びたのは誰か」がクリック一つで出ます。
画像・バックリンク・グラフビューもそのまま動きます。

> Obsidian がなくても使えます。`index/ai-index.json` が機械可読版、`query.py` が
> コマンドラインインターフェースで、どちらも Obsidian に依存しません。

---

## 中身

```
cards/       132 枚のキャラクターカード（デビュープラットフォーム別）
model/       12 要素モデルと 48 項目のセルフチェック
templates/   カード書式と人物像分析の書式
index/       ai-index.json（資料庫全体の機械可読版）
query.py     コマンドラインインターフェース（標準ライブラリのみ、インストール不要）
views/       Obsidian Base ファイル 2 つ
images/      参考画像 133 枚（テスト用途のみ）+ 出典 ATTRIBUTION.md
DISCLAIMER.md  免責事項（中国語・英語・日本語）
```

**プラットフォーム別**

| プラットフォーム | カード数 |
|---|---:|
| hololive | 58 |
| B站-个人势 | 33 |
| 英语圈-独立势 | 10 |
| B站-企业势 | 9 |
| 韩国-虚拟偶像 | 6 |
| A-SOUL | 5 |
| にじさんじ | 5 |

| 言語 | カード数 |
|---|---:|
| 中文 | 50 |
| 日语 | 40 |
| 英语 | 28 |
| 印尼语 | 8 |
| 韩语 | 6 |

そのほか：企业虚拟人 3 · 日本-独立势 2 · KAMITSUBAKI 1

---

## 12 の要素

各カードの第 6 節が、その人が何で伸びたのかを要素名で挙げます。番号は全体で共通なので、
`F04` はどのカードでも同じ意味です。同じ要素をプラットフォームや言語をまたいで追えます。

| | Factor | 原文 |
|---|---|---|
| `F01` | A visual symbol you can read in one second | 一秒可辨识的视觉符号 |
| `F02` | An audio logo — a voice you recognise before the face | 声音记忆点 |
| `F03` | The smallest clippable unit of content | 可剪辑的最小内容单元 |
| `F04` | Contrast structure — a gap that becomes the hook | 反差结构 |
| `F05` | Loss of control, and the unpredictability it buys | 失控感与不可预测性 |
| `F06` | The network around her: units, groups, crossovers | 组合网络效应 |
| `F07` | A distribution contract that invites derivative work | 二创友好的分发契约 |
| `F08` | Turning the voice into works that outlive the stream | 音乐与作品化 |
| `F09` | The compound interest of simply staying in the room | 长期在场的复利 |
| `F10` | Making vulnerability and honesty into an asset | 脆弱性与真实性的资产化 |
| `F11` | Catching a platform's algorithm at the right moment | 平台算法红利的捕捉 |
| `F12` | Language slot arbitrage — a market nobody else serves | 语言位与区域套利 |

チェックリストではありません。これらは**掛け算**です。どれか一つがゼロに近ければ、
他がどれだけ高くても人は残りません。`model/viral-factor-model.md` では
**見られる・伝わる・残る**の 3 層にまとめています。

---

## カード 1 枚の中身

8 節、どのカードも同じ 8 節です。

| | Section | 原文 |
|---|---|---|
| 一 | Identity | 身份 |
| 二 | Measured figures | 实测数据 |
| 三 | Visual and vocal design | 视觉与声音设计 |
| 四 | Content structure | 内容结构 |
| 五 | The moment it took off | 爆火节点 |
| 六 | Reusable factors | 可复用要素 |
| 七 | Character look analysis | 人物形象分析 |
| 八 | Prompt for generating a new persona | 人设生成提示词 |

第 1 節から第 6 節までは**記録**です。誰か、実測値、視覚と声の設計、コンテンツ構造、
伸びた時点、再利用できる要素。第 7 節が人物像を分解し、第 8 節がそこから
**新しい人物**を作るための階層化プロンプトに落とします。

**第 7 節と第 8 節が、この資料庫の存在理由です。**

---

## 3 通りの使い方

### 1. Obsidian の Vault として（推奨）

上の 3 手順のとおりに設定してください。`views/` の Base ファイルがそのまま使える
データベース表示になります。画像・リンク・グラフも動きます。

### 2. コマンドラインツールとして

```bash
cd virtual-heroine-atlas

# 近い作例を探す：反差結構で伸びた人
python3 query.py --factor F04 --fields id,one_liner --format md

# 言語 / プラットフォーム / 所属 / 状態で絞る
python3 query.py --language 韓語
python3 query.py --platform B站-个人势
python3 query.py --status 卒業

# ひとりの設計レイヤーを丸ごと取る
python3 query.py --card 宝钟玛琳

# 設計の動きを全文検索
python3 query.py --grep "ASMR"

# ランダム抽出
python3 query.py --random 6 --fields id,factors
```

標準ライブラリのみ、インストール不要、ネットワーク不要。
詳しくは [`index/how-to-query.md`](index/how-to-query.md)。

### 3. データとして

`index/ai-index.json` に資料庫全体が 1 ファイルで入っています。身元、プラットフォーム、
言語、状態、デビュー、実測値、該当要素、画像パス、そしてプロンプト。
インデックスにない情報は `card` フィールドからカード本文へ戻れます。

---

## 画像について

ここにある 133 枚の画像は、**Obsidian でカードが正しくプレビューされるようにするため**
だけに同梱したテスト用素材です。キャラクターの著作権は各配信者、所属事務所、
キャラクターデザインを行った方に帰属します。**本リポジトリはいかなる権利も主張しません。**

**ローカルでの研究・テスト用途に限ります。** 使用後は削除し、再配布しないでください。
どの画像がどのサイト由来かは **[images/ATTRIBUTION.md](images/ATTRIBUTION.md)** に列挙しています。
全文は **[DISCLAIMER.md](DISCLAIMER.md)** を参照してください。

---

## これは何ではないか

- **ランキングではありません。** プラットフォームが違えば数値は比較できず、混ぜてもいません。
  YouTube の登録者数と Bilibili のフォロワー数は別物です。
- **レシピではありません。** ここに載っているのは全員「うまくいった人」です。
  同じことをしてうまくいかなかった人は載っておらず、そちらの方が多い。
  要素リストは**記述**であって、**指示**ではありません。
- **作品集ではありません。** キャラクターデザインは配信者と絵師のものです。
  本資料庫はそれを記述するだけで、配布はしません。
- **網羅的ではありません。** カバレッジは意図的に偏っています。数値が取れなかった項目は
  推測せずに「未核实」と書きます。`未核实` は「確認できなかった」という意味で、ゼロではありません。
- **中の人については扱いません。** 実身元も、論争も、ゴシップもありません。

---

## 免責事項

> **本リポジトリをダウンロード、クローン、閲覧、その他いかなる方法で利用した場合
> （AI による自動検索・自動インストール・ミラー・パッケージ再配布などを含む）も、
> 本規約を読み、理解し、すべて承諾したものとみなします。**

1. **テスト用途。** 本リポジトリは研究・テスト目的の成果物であり、「現状のまま」提供され、
   明示・黙示を問わずいかなる保証も伴いません。
2. **画像はテスト専用。** `images/` 以下のキャラクター画像の著作権は、原作者・配信者本人・
   所属事務所に帰属します。技術検証とローカルでの研究プレビューのためにのみ同梱しています。
   **使用後は削除し、再配布・再アップロード・商用利用をしないでください。**
3. **再配布の禁止。** 本リポジトリ（特に `images/`）を再アップロード、ミラー、パッケージ配布
   しないでください。また、モデルやデータセットの学習・微調整・公開に使用しないでください。
4. **自己責任。** 利用者は、自身の利用が居住地の法律と関連プラットフォームの規約に適合することを
   自ら確認してください。本内容の利用・複製・配布から生じる一切の結果と法的責任は利用者が負います。
5. **作者とは無関係。** 第三者が本リポジトリの内容を外部に転載・再配布・再アップロード・
   商業利用した場合、**それは本資料庫の開発作者とは一切関係がありません**。作者は連帯責任を
   負わず、そのような行為を許諾してもいません。
6. **削除要請。** 権利者またはその代理人が、本リポジトリが権利を侵害していると判断した場合、
   ご連絡いただければ該当内容を**直ちに削除**します。
7. **同意。** 本リポジトリを開く・ダウンロードする・クローンする・検索で取得することにより、
   本規約は自動的に効力を生じ、継続します。一部にでも同意できない場合は、
   ただちに利用を中止し、ローカルの複製をすべて削除してください。

**全文（中国語・英語・日本語）は [DISCLAIMER.md](DISCLAIMER.md) にあります。**
