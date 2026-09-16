<div align="center">

# Virtual Heroine Atlas

**虚拟女主角图鉴**

### 132 female virtual characters, measured and taken apart

why they caught on &nbsp;·&nbsp; how their look is actually designed

[![Obsidian](https://img.shields.io/badge/Obsidian-required-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![cards](https://img.shields.io/badge/cards-132-E11D48)
![images](https://img.shields.io/badge/images-133-0EA5E9)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek-Harness-4D6BFE)](https://github.com/topics/deepseek-harness)
![usage](https://img.shields.io/badge/usage-test%20only-000000)

[中文](README.md) · [**English**](README.en.md) · [日本語](README.ja.md)

</div>

---

## What this is

A research atlas of **female virtual characters**. 132 of them, one card each,
from Japan, Korea, China, the English-speaking scene and Indonesia. Every card asks
the same two questions:

> **What made her travel?** &nbsp;·&nbsp; **How was her look designed?**

The first is a teardown of content and operations. The second is a teardown of design:
palette, costume structure, expression range, speech habits, emotional register,
compressed at the end into a layered prompt you can hand to an image model.

It is **not** a rankings page, **not** a fan wiki, **not** a how-to. 132 entries
answer the same questions in the same shape, so they can be compared, and more
usefully, **mined**.

> The cards themselves are written in Chinese. These three READMEs cover
> Chinese, English and Japanese.

---

## ⚠️ Install Obsidian first, this part is required

**This repository is an Obsidian vault.** Illustrations inside the cards use Obsidian's
wikilink embed syntax (`![[image-name]]`), which means **images do not render when you
open a card on the GitHub website**.

So install Obsidian, then open this folder as a vault:

| Step | What to do |
|---|---|
| **1** | Get Obsidian at **[obsidian.md](https://obsidian.md)** (free; Windows, macOS, Linux, iOS, Android) |
| **2** | Open Obsidian → **Open folder as vault** → pick the repository root |
| **3** | Go to **Settings → Core plugins → turn on "Bases"** (that powers the database views; it ships with Obsidian, nothing extra to install) |

Once that is done you get: `views/library.base` with four tables grouped by language,
platform, status and factor; `views/factors.base` with one table per factor, so
*who was carried by contrast structure* is one click. Images, wikilinks and the graph
view all work too.

> Obsidian is optional for machines: `index/ai-index.json` is the machine-readable
> edition and `query.py` is a command line interface over it. Neither needs Obsidian.

---

## What is in here

```
cards/       132 character cards, grouped by debut platform
model/       the twelve factors, and a 48-point self-check for a new design
templates/   the card format and the look-analysis format
index/       ai-index.json, the whole atlas as one machine-readable file
query.py     CLI over that index (standard library only, nothing to install)
views/       two Obsidian Base files for browsing
images/      133 reference images (test use only, see the disclaimer)
DISCLAIMER.md  disclaimer, in Chinese, English and Japanese
```

**By platform**

| Platform | Cards |
|---|---:|
| hololive | 58 |
| B站-个人势 | 33 |
| 英语圈-独立势 | 10 |
| B站-企业势 | 9 |
| 韩国-虚拟偶像 | 6 |
| A-SOUL | 5 |
| にじさんじ | 5 |

| Language | Cards |
|---|---:|
| 中文 | 50 |
| 日语 | 40 |
| 英语 | 28 |
| 印尼语 | 8 |
| 韩语 | 6 |

Also: 企业虚拟人 3 · 日本-独立势 2 · KAMITSUBAKI 1

---

## The twelve factors

Every card's sixth section names the factors that carried that particular character.
The numbering is global, so `F04` means the same thing everywhere, and a factor can be
traced across platforms and languages.

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

They are not a checklist to tick off. They multiply: an entry close to zero on any one
of them tends to stay there regardless of the others. The model file groups them into
three layers: **being seen, being passed on, being kept**.

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

Sections one to six are the record: who she is, the measured figures, the visual and
vocal design, the shape of her content, the moment it took off, and the factors that
carried it. Section seven takes the look apart. Section eight turns that into a layered
prompt for building someone new.

**Sections seven and eight are the reason the rest exists.**

---

## Three ways to use it

### 1. As an Obsidian vault (recommended)

Follow the three steps above. The Base files in `views/` are working database views
already. Images, backlinks and the graph view are all live.

### 2. As a command line tool

```bash
cd virtual-heroine-atlas

# find comparable cases: everyone carried by contrast structure
python3 query.py --factor F04 --fields id,one_liner --format md

# slice by language / platform / affiliation / status
python3 query.py --language 韩语
python3 query.py --platform B站-个人势
python3 query.py --status 毕业

# pull one character's full design layer
python3 query.py --card 宝钟玛琳

# full-text search for a design move
python3 query.py --grep "ASMR"

# random sample
python3 query.py --random 6 --fields id,factors
```

Standard library only, no install, no network. See [`index/how-to-query.md`](index/how-to-query.md).

### 3. As data

`index/ai-index.json` holds the whole atlas in one file: identity, platform, language,
status, debut, measured figures, which factors apply, the image path, and the prompts.
For anything the index does not carry, the `card` field points back to the card.

---

## About the images

The 133 images here are included **only so the cards preview correctly in
Obsidian**, and are test material. Character designs belong to the streamers, their
agencies and their artists. **This repository claims no rights over them.**

**They are for local research and testing only.** Delete them after use, and do not
redistribute them. Full terms below, or read **[DISCLAIMER.md](DISCLAIMER.md)**.

---

## What this is not

- **Not a ranking.** Figures for different platforms are not comparable and are never
  mixed. A YouTube subscriber count and a Bilibili follower count are two different
  measurements of two different things.
- **Not a recipe.** Every entry here is someone who made it. The ones who did the same
  things and did not make it are not in the file, and there are more of them. Read the
  factor list as description, not as instructions.
- **Not a portfolio.** Character designs belong to the streamers and their artists.
  This atlas describes them; it does not distribute them.
- **Not complete.** Coverage is uneven by design. Where a figure could not be
  established, the card says so rather than estimating: `未核实` means it was not
  verified, not that it is zero.
- **Not about the people behind the characters.** No real identities, no controversies,
  no gossip.

---

## Disclaimer

> **By downloading, cloning, opening or otherwise using this repository, in any form
> whatsoever (including automated AI retrieval, automated installation, mirroring or
> packaged redistribution), you are deemed to have read, understood and fully accepted
> this agreement.**

1. **Test use.** This repository is a research and testing artefact, provided "as is",
   without warranty of any kind, express or implied.
2. **Images are test-only.** Copyright in the character images under `images/` belongs
   to their original authors, the streamers and their agencies. They are included here
   purely for technical testing and local research preview. **Delete them after use. Do
   not redistribute, re-upload or use them commercially.**
3. **No further distribution.** Do not re-upload, mirror, package or redistribute this
   repository (especially `images/`), and do not use it to train, fine-tune or publish
   any model or dataset.
4. **Your responsibility.** You must confirm that your use complies with the law where
   you are and with the terms of the relevant platforms. All consequences and liability
   arising from your use, copying or distribution of this content rest with you.
5. **Nothing to do with the author.** Any redistribution, re-upload or commercial
   exploitation of this repository's contents by a third party is **entirely unrelated
   to the developer of this atlas**. The author accepts no joint liability and has
   authorised no such act.
6. **Takedown.** If you are a rights holder, or an agent of one, and believe this
   repository infringes your rights, please raise it and the material will be **removed
   immediately**.
7. **Acceptance.** Opening, downloading, cloning or retrieving this repository brings
   this agreement into effect automatically and it remains in force. If you disagree
   with any part of it, stop using the repository and delete all local copies now.

**Full trilingual text: [DISCLAIMER.md](DISCLAIMER.md).**
