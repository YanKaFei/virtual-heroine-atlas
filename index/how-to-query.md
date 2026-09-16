# 调取接口：怎么用这个库生成一个新人设

这个仓库有两层：**卡片**（`cards/`，人的可读层）和**索引**（`index/ai-index.json`，机器可读层）。
调取走索引，正文走卡片。

---

## 一、`ai-index.json` 的结构

```json
{
  "generated_from": "132 位虚拟主播卡",
  "characters": [
    {
      "id": "宝钟玛琳",
      "name": "宝钟玛琳",
      "platform": "hololive",
      "platform_dir": "hololive",
      "language": "日语",
      "affiliation": "hololive",
      "status": "活动中",
      "debut": "2019-08",
      "one_liner": "把「海贼船长」做成可长期经营的整活符号的那一个。",
      "metrics": {
        "youtube_subscribers": 4429000,
        "youtube_subscribers_display": "442.9 万",
        "bilibili_fans": null,
        "twitch_followers": null,
        "measured_at": "2026-06-30"
      },
      "factors": [{"id": "F01", "name": "一秒可辨识的视觉符号"}],
      "has_look_analysis": true,
      "has_prompt": true,
      "prompt": {"positive": "…", "negative": "…", "palette": "…"},
      "card": "cards/hololive/宝钟玛琳.md"
    }
  ]
}
```

`factors[].id` 是 F01–F12，详见 `model/viral-factor-model.md`。
`has_look_analysis` / `has_prompt` 表示卡片里是否已写「七、人物形象分析」「八、人设生成提示词」。

---

## 二、命令行调取（`query.py`，只用标准库）

```bash
cd vtuber-atlas

# 1) 找同类参考：靠「反差结构」起来的人
python3 query.py --factor F04 --fields id,one_liner --format md

# 2) 限定平台 / 语言 / 阵营 / 状态
python3 query.py --language 韩语            # 日语 / 英语 / 中文 / 韩语 / 印尼语
python3 query.py --platform B站-个人势       # 按平台目录筛
python3 query.py --affiliation 独立         # 按阵营筛
python3 query.py --status 毕业              # 只看已毕业的（历史样本）
python3 query.py --has-prompt               # 只要有提示词层的

# 3) 取一个人的完整设计层（身份 + 形象分析 + 提示词）
python3 query.py --card 宝钟玛琳

# 4) 要完整原文（八段全出）
python3 query.py --card 宝钟玛琳 --full

# 5) 全文检索（找某种设计动作，例如谁在用 ASMR）
python3 query.py --grep "ASMR"

# 6) 随机抽样做「设计动作采集」
python3 query.py --random 6 --fields id,factors
```

同样的筛选在 Obsidian 里也有：打开仓库，用 `views/library.base` 的
「按语言 / 按平台 / 按状态 / 按要素」四个视图。

---

## 三、生成新人设的正确流程

**不要**照抄某一个人的提示词。正确姿势是**拆解 → 借动作 → 重组**：

1. **定意图** — 新人设想切哪个语言位 / 平台？（F12）走音乐还是直播？（F08 / F09）
2. **筛参考** — `python3 query.py --factor F12 --language 韩语` → 拿同类样本
3. **读设计层** — `python3 query.py --card <样本id>` → 看「七、人物形象分析」
4. **抄动作** — 从第七段里挑**可迁移的设计动作**（不是挑颜色）
5. **搭骨架** — 用第八段提示词的**分层结构**（风格层 / 光照层 / 构图层）
6. **换主体** — 把主体描述换成新角色；风格层可跨样本重混
7. **查冲突** — 跨风格混搭时负向词会互相打架，**必须说明丢了什么、为什么**
8. **自检** — 过一遍 `model/self-check.md` 的 B1–B12 清单

### 「可迁移 / 不可迁移」是这一步的关键

每张卡的第七段末尾都有这一行。生成新人设时**只搬可迁移的**：
可迁移的是结构性的设计动作（色彩分工、剪影策略、反差位置），
不可迁移的是绑死在这个人身上的东西（具体色值、动物符号、时机红利）。

---

## 四、卡片的段落地图

| 段 | 内容 | 用途 |
|---|---|---|
| 一、身份 | 角色设定、商业位置 | 判断能不能对标 |
| 二、实测数据 | 订阅 / 播放 / 投稿 / 里程碑 | 定位量级 |
| 三、视觉与声音设计 | 造型、风格坐标、声音、动捕路线 | 快速扫描 |
| 四、内容结构 | 主内容型、直播节奏、切片策略、互动机制 | 学运营结构 |
| 五、爆火节点 | 时间线表格 | 看增长形态 |
| 六、可复用要素 | `F0x` 编号要素 + 不可迁移部分 | **筛选键** |
| 七、人物形象分析 | 形象 / 性格 / 服装 / 表情 / 语言 / 情绪 / 配色 | **设计推理层** |
| 八、人设生成提示词 | 正向 / 负向 / 配色 / 冲突消解记录 | **可直接用的产物** |

---

## 五、这个接口**不**提供什么

- **不提供中之人信息** —— 全库只写角色与商业事实。
- **不提供未核实数字** —— 取不到的字段是 `null`，正文写「未核实」。
- **不保证数字是最新的** —— 每个数字都带 `measured_at`，用之前先看日期。
- **不替你做美术判断** —— 配色与风格层是**参考骨架**，不是复刻目标。
