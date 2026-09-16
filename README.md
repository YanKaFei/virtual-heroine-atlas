# vtuber-atlas

A reference atlas of **132 virtual streamers** — why they caught on, and how their
characters are actually built.

It is not a rankings page and not a fan wiki. Every entry asks the same two
questions: *what made this one travel*, and *what can be moved from her design*
into a different one. The answers are written the same way every time, so the
entries can be compared and, more usefully, **mined**.

The notes are in Chinese. This page is the map.

---

## What is in here

```
cards/       132 character files, one per streamer, grouped by debut platform
model/       the twelve factors, and a 48-point self-check for a new design
templates/   the card format and the look-analysis format
index/       ai-index.json — the whole atlas as one machine-readable file
query.py     a small stdlib-only CLI over that index
views/       two Obsidian Base files for browsing
```

| Platform | Cards | Language | Cards |
|---|---:|---|---:|
| hololive | 58 | 日语 | 40 |
| にじさんじ | 5 | 英语 | 28 |
| B站-企业势 | 9 | 中文 | 50 |
| B站-个人势 | 33 | 韩语 | 6 |
| 英语圈-独立势 | 10 | 印尼语 | 8 |

Also: 韩国-虚拟偶像 6 · 日本-独立势 2 · 企业虚拟人 3 · A-SOUL 5 · KAMITSUBAKI 1

---

## The twelve factors

Every card's sixth section names the factors that carried that particular
streamer. The numbering is global, so `F04` means the same thing everywhere, and
the same factor can be traced across platforms and languages.

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

They are not a checklist to tick off. They multiply: an entry that is close to
zero on any one of them tends to stay there regardless of the others. The model
file groups them into three layers — being seen, being passed on, being kept.

---

## What one card contains

Eight sections, the same eight every time:

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

Sections one to six are the record: who she is, the measured figures, the visual
and vocal design, the shape of her content, the moment it took off, and the
factors that carried it. Section seven takes the look apart — personality,
costume, expression range, speech habits, emotional register, palette — and
section eight turns that into a layered prompt for building someone new.

The seventh and eighth sections are the reason the rest exists.

---

## Using it

**As a vault.** Open the folder in Obsidian. `views/library.base` gives tables of
all entries grouped by language, by platform, by status, and by factor;
`views/factors.base` gives one view per factor, so *who was carried by F04* is a
single click. Bases is a core plugin, nothing to install.

**As a CLI.** `python3 query.py --factor F04` lists everyone carried by that
factor; `--language`, `--platform`, `--status`, `--grep` and `--random` slice it
other ways. Standard library only, no install, no network.

**As data.** `index/ai-index.json` is the whole atlas in one file — identity,
platform, language, status, debut, measured figures, which factors apply, and the
prompts — with a path back to the card for anything the index does not carry.
`index/how-to-query.md` describes the fields and a working order for using them.

**By hand.** `templates/` has the two formats. Write a new card the same way and
it drops straight into the set.

---

## What this is not

- **Not a ranking.** Figures for different platforms are not comparable and are
  never mixed. A YouTube subscriber count and a Bilibili follower count are two
  different measurements of two different things.

- **Not a recipe.** Every entry here is someone who made it. The ones who did the
  same things and did not make it are not in the file, and there are more of them.
  Read the factor list as description, not as instructions.

- **Not art.** Character designs belong to the streamers and their artists. This
  atlas describes them; it does not distribute them, and there are no images in
  this repository on purpose.

- **Not complete.** Coverage is uneven by design: some platforms publish a great
  deal, others almost nothing. Where a figure could not be established, the card
  says so rather than estimating — `未核实` means it was not verified, not that it
  is zero.

- **Not about the people behind the characters.** No real identities, no
  controversies, no gossip.

