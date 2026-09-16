<div align="center">

# 虚拟女主角图鉴

**Virtual Heroine Atlas**

### 132 位女性虚拟形象的实测资料库

她们为什么火 · 她们的形象是怎么被设计出来的

[![Obsidian](https://img.shields.io/badge/Obsidian-%E5%BF%85%E8%A3%85-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![cards](https://img.shields.io/badge/cards-132-E11D48)
![images](https://img.shields.io/badge/images-133-0EA5E9)
[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek-Harness-4D6BFE)](https://github.com/topics/deepseek-harness)
![usage](https://img.shields.io/badge/usage-%E4%BB%85%E9%99%90%E6%B5%8B%E8%AF%95-000000)

[**中文**](README.md) · [English](README.en.md) · [日本語](README.ja.md)

</div>

---

## 这是什么

一个关于**女性虚拟形象**的研究资料库。132 位来自全球的女性虚拟主播与虚拟角色，
每一位一张卡，问的是同样两个问题：

> **她是怎么火起来的？** &nbsp;·&nbsp; **她的形象是怎么被设计出来的？**

前者是内容与运营层的复盘，后者是设计层的拆解——配色、服装结构、表情谱、语言习惯、
情绪定位，最后压成一段可以直接喂给绘图模型的分层提示词。

它**不是**排行榜，**不是**粉丝维基，**不是**教程。同一个问题，132 张卡用同一套结构回答，
所以这些卡可以横向比较，更可以**被检索和复用**。

> 卡片正文是中文。三份 README 覆盖中 / 英 / 日。

---

## ⚠️ 先装 Obsidian，这是必须的

**本仓库是 Obsidian 仓库格式。** 卡片里的插图用的是 Obsidian 的双链嵌入语法
（`![[图片名]]`），**在 GitHub 网页上点开卡片是看不到图的**。

请一定先安装 Obsidian，再把仓库当 vault 打开：

| 步骤 | 做什么 |
|---|---|
| **1** | 到 **[obsidian.md](https://obsidian.md)** 下载并安装（免费，Windows / macOS / Linux / iOS / Android 全平台） |
| **2** | 打开 Obsidian → **「打开文件夹作为仓库」**（Open folder as vault）→ 选中本仓库根目录 |
| **3** | 进 **设置 → 核心插件 → 打开「Bases」**（数据库视图要用它；它是官方核心插件，不需要另外装东西） |

装好之后你会得到：`views/library.base` 按语言 / 平台 / 状态 / 要素分组的四张总表，
`views/factors.base` 每个要素一张表，点一下就筛出「谁靠反差结构火的」。
卡片里的插图、双链跳转、图谱视图也都会正常工作。

> 不想装 Obsidian 也能用：`index/ai-index.json` 是机器可读的，
> `query.py` 是命令行接口，两者都不依赖 Obsidian。

---

## 仓库里有什么

```
cards/       132 张角色卡，按出道平台分目录
model/       十二要素模型 + 48 项自检清单
templates/   卡片格式、形象分析格式
index/       ai-index.json，整个库的机器可读版
query.py     命令行调取接口（只用标准库，无需安装）
views/       两个 Obsidian Base 文件，用来浏览
images/      133 张参考图（仅限测试用途，见文末免责协议）
DISCLAIMER.md  免责协议，中英日三语
```

**平台分布**

| 平台 | 卡片数 |
|---|---:|
| hololive | 58 |
| B站-个人势 | 33 |
| 英语圈-独立势 | 10 |
| B站-企业势 | 9 |
| 韩国-虚拟偶像 | 6 |
| A-SOUL | 5 |
| にじさんじ | 5 |

| 语言 | 卡片数 |
|---|---:|
| 中文 | 50 |
| 日语 | 40 |
| 英语 | 28 |
| 印尼语 | 8 |
| 韩语 | 6 |

另外还有：企业虚拟人 3 · 日本-独立势 2 · KAMITSUBAKI 1

---

## 十二要素：她们靠什么火

每张卡的第六段会点名这个人身上的要素。编号是全局的，所以 `F04` 在任何一张卡里都是同一件事，
同一个要素可以跨平台、跨语言追踪。

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

这三层不是可以逐项打勾的清单，它们是相乘的：任何一项接近于零，其他项再高也难留住人。
`model/viral-factor-model.md` 把它们分成三层——**被看见、被传播、被留下**。

---

## 一张卡里有什么

八段，每张卡都是同样八段：

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

一到六段是**记录**：她是谁、实测数字、视觉与声音设计、内容结构、爆火节点、可复用要素。
第七段把形象拆开：性格、服装、表情、语言、情绪、配色。
第八段把前两段的结论压成一段分层提示词，用来造一个**新人**。

**第七段和第八段是这个库存在的理由。**

---

## 三种用法

### 一、当 Obsidian 仓库用（推荐）

按上面三步装好后，`views/` 里的 Base 文件就是现成的数据库视图。
图像、双链、关系图谱都直接可用。

### 二、当命令行工具用

```bash
cd virtual-heroine-atlas

# 找同类参考：靠「反差结构」起来的人
python3 query.py --factor F04 --fields id,one_liner --format md

# 按语言 / 平台 / 阵营 / 状态筛
python3 query.py --language 韩语
python3 query.py --platform B站-个人势
python3 query.py --status 毕业

# 取一个人的完整设计层
python3 query.py --card 宝钟玛琳

# 全文检索某种设计动作
python3 query.py --grep "ASMR"

# 随机抽样
python3 query.py --random 6 --fields id,factors
```

标准库，无需安装，不联网。详见 [`index/how-to-query.md`](index/how-to-query.md)。

### 三、当数据用

`index/ai-index.json` 是一份文件装下整个库：身份、平台、语言、状态、出道时间、
实测数字、适用要素、插图路径，以及能直接用的提示词。
索引里没有的东西，用 `card` 字段回卡片正文取。

---

## 关于图片

仓库里的 133 张图**只是为了让卡片在 Obsidian 里能正常预览**而附带的测试素材。
角色形象版权属于各主播本人、其所属机构与角色设计者，**本仓库不主张任何权利**。

**它们仅供本地研究与测试使用。** 请在使用后删除，或至少不要对外分发。
完整条款见文末，或直接读 **[DISCLAIMER.md](DISCLAIMER.md)**。

---

## 这个库不是什么

- **不是排行榜。** 不同平台的数字不可比，也从不混着用。YouTube 订阅数和 B 站粉丝数是两件事。
- **不是配方。** 这里每个人都是成了的人。做了一样的事却没能成的人不在这个文件里，而且他们更多。
  要素清单是**描述**，不是**指令**。
- **不是作品集。** 角色设计属于主播与画师。本仓库描述它们，不发行它们。
- **不完整。** 覆盖度天生不均：有的平台公开得多，有的几乎没有。取不到的数字，卡片会写「未核实」，
  而不是估一个——`未核实` 的意思是真的没核实到，不是零。
- **不涉及中之人。** 没有真实身份，没有争议，没有八卦。

---

## 免责协议

> **下载、克隆、打开或以任何方式使用本仓库（包括通过 AI 自动检索、自动安装、镜像、打包分发
> 等一切形式），即视为你已阅读、理解并全部接受本协议。**

1. **测试用途。** 本仓库是研究与测试性质的资料库，按「现状」提供，不附带任何明示或暗示的担保。
2. **图片仅限测试。** `images/` 下的角色形象版权归原作者、主播本人及所属机构所有，本仓库仅作
   技术测试与本地研究预览之用。**使用后请删除，不要对外分发、不要再上传、不要用于任何商业用途。**
3. **不得外传。** 请勿将本仓库（尤其是 `images/` 目录）再次上传、镜像、打包分发或用于训练、
   微调、发布任何模型与数据集。
4. **责任自负。** 使用者应自行确认其使用方式符合所在地法律与相关平台条款。因使用、复制、
   传播本仓库内容所引起的一切后果与法律责任，由使用者自行承担。
5. **与作者无关。** 任何第三方对本仓库内容的外传、再分发、二次上传或商业利用，
   **均与本书库的开发作者无关**，作者不承担任何连带责任，也未授权任何此类行为。
6. **权利主张。** 若你是任一内容的权利人或其代理人，认为本仓库侵犯了你的权益，
   请提出，相关内容会被**立即移除**。
7. **接受方式。** 打开、下载、克隆、检索到本仓库，即视为本协议自动生效并持续有效；
   若你不同意其中任何一条，请立即停止使用并删除全部本地副本。

**完整版本（中 / 英 / 日）见 [DISCLAIMER.md](DISCLAIMER.md)。**
