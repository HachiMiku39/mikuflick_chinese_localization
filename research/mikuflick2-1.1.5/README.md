# MikuFlick2 1.1.5 研究与复核入口

整理日期：2026-10-05。此目录整理资源拆解、USM/CUE、得分、判定、连击、Gauge、评级、间奏、Crimax、BTL、解锁和历史客户端UI的当前证据。

## 文档

| 文档 | 内容 |
|---|---|
| [mechanics.md](mechanics.md) | 完整机制、运行时谱面读取规则、公式、11首歌五档物量 |
| [sprite_gallery.md](sprite_gallery.md) | 450张按plist切图、21页图解及每张图片意义 |
| [fonts.md](fonts.md) | Futura字体调用与文字贴图的区分 |
| [resources.md](resources.md) | 195项文件用途、21个图集/450个frame、音效、结尾版权、动态DLC边界 |
| [verification.md](verification.md) | 给下一轮Codex的独立复核步骤、函数定位、误译检查、待实机实验 |
| [data/manifest.json](data/manifest.json) | 发布文件与样本身份、文件摘要和保护区校验 |
| [tools/mechanics_model.py](tools/mechanics_model.py) | 可复算逻辑模型和边界检查 |
| [tools/inspect_macho.py](tools/inspect_macho.py) | 在自有本地样本上读取原始数值表和比对SHA-256 |

## 样本身份与覆盖范围

```text
Game: Miku Flick/02
Version: 1.1.5
Executable: MikuFlick2
Architecture: ARMv7, 32-bit Mach-O, 非Fat
LC_ENCRYPTION_INFO cryptid: 0
SHA-256: 869caa22613c5ebfbde6b4c9e1a93362a4f30519231b6dfc9ac3ff31d414b87f
Static tool: Ghidra 12.1.4 + ARM/Thumb汇编 + Apple otool + 原始字节读取
Local dataset: 195文件、12个USM、11首歌曲、6818条CUE、5280条前缀0记录
```

当前包只含预装曲样本；原README的`hello_planet.usm`与设备存档样本不在本次输入内。本轮未重跑原实机实验，也未得到自制曲包安装成功的证据。结论不能自动推广到一代、其他版本或所有DLC。

## 证据等级

| 标记 | 含义 |
|---|---|
| 静态确认 | 本版本调用、分支、常数或结构支持；仍可能有设备调度边界 |
| 原仓库实机记录 | README中维护者先前提供的测试反馈；本轮未重做 |
| 用户指认 | 用户明确说明的UI用途，例如所提供的Shuffle截图 |
| 推断/解释 | 从名称、资源内容或结构推导，不能替代直接调用证据 |
| TODO/UNKNOWN | 缺少代码路径、运行配置或实机证据，保留待查 |

函数名来自符号表；伪代码是研究者整理，不是游戏原始源码。注册表中的文件名不代表所有文件都具有已确认的现场触发。原仓库已有但本轮未重核的Rainbow、Replay等细节保留在主README，并列入复核清单。

## 本次补足与保留的边界

- 计分、普通判定表、评级、Gauge更新、间奏类型2、7/8初始化、固定位置Telop读取有明确定位。
- `11`保留为样本编码观察，不能当作已经反汇编确认的可变长度运行时token。
- 两份Front/Back分别用于普通音符和间奏；相同值不代表同一个地址。
- Ghidra在140—149 BPM分支的立即数误译已另用原字节/otool纠正，未修改游戏指令。
- BTL的低判定保连、SAFE可达与`BreakClear`写入条件是静态结果，玩家侧含义仍需实机核对。
- 本次保留主README第1—4节、EASY实验记录、自制Mov_18/verificationFile说明以及工具/旧设备相关内容原文；不改汉化`.strings`文件。

## 发布内容

提交研究文档、复算工具、地址/名称索引、统计数据，以及用户要求的450张plist裁切PNG和图解。IPA、可执行文件、音视频、歌词全文、完整逐事件谱面、完整反编译文本及含游戏二进制的Ghidra工程留在本地，不包含在此目录。
