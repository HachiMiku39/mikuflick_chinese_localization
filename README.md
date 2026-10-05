# Miku Flick / Miku Flick 02 简体中文汉化与逆向研究

> 本仓库同时保存三类内容：原版 iOS 游戏的简体中文本地化、旧 iOS 设备上的安装说明，以及 MikuFlick2 1.1.5 的 USM / 谱面 / 游戏机制逆向研究。
>
> 当前二进制研究对象为 **MikuFlick2 1.1.5 / ARMv7 / cryptid 0**。研究结论来自 Ghidra 静态分析与原版实机测试。未确认的内容会明确标记为 **UNKNOWN / TODO**，不把猜想写成事实。

## 快速入口

- [下载汉化文件](https://github.com/HachiMiku39/mikuflick_chinese_localization/releases/tag/MikuFlick-CN)
- iOS 10 相关安装记录请查看 [`HachiMiku39-patch-iOS10`](https://github.com/HachiMiku39/mikuflick_chinese_localization/tree/HachiMiku39-patch-iOS10) 分支
- 本仓库不提供原版 IPA、商业歌曲或 MV；研究目录附有按 plist 裁切的界面图片及用途说明

## 目录

1. [项目范围](#1-项目范围)
2. [汉化文件与安装](#2-汉化文件与安装)
3. [旧 iOS 环境准备](#3-旧-ios-环境准备)
4. [常见问题](#4-常见问题)
5. [USM 与谱面研究](#5-usm-与谱面研究)
6. [MikuFlick2 1.1.5 游戏机制逆向](#6-mikuflick2-115-游戏机制逆向)
7. [当前仍未确认的部分](#7-当前仍未确认的部分)
8. [工具与参考资料](#8-工具与参考资料)

---

## 1. 项目范围

### 1.1 简体中文本地化

本仓库提供：

| 游戏 | 仓库文件 | 安装时文件名 | 替换位置 |
|---|---|---|---|
| Miku Flick | `Localizable.strings` | `Localizable.strings` | `.app/en.lproj/` |
| Miku Flick/02 | `Localizable2.strings` | **重命名为 `Localizable.strings`** | `.app/en.lproj/` |

汉化只替换英语本地化资源，不修改游戏逻辑、谱面和 UI 布局，也不会自动翻译图片中的文字。

两份汉化文件都以英语资源为底稿。**不要把它们直接覆盖到日语目录，也不要把一代和 02 的文件互换。** 英语与日语帮助文本的分行和布局不同，混用可能出现叠字或错行。

### 1.2 兼容性

Miku Flick 系列原始可执行文件是 **32 位 ARM 应用**。关键限制是系统是否还能运行 32 位 App：

- iOS 5 到 iOS 10 仍可运行 32 位 App
- iOS 11 起 Apple 移除了 32 位 App 运行支持
- 这不等于只能使用 32 位硬件。例如运行 iOS 10 的 iPhone 6s 仍能运行 32 位 MikuFlick

越狱方式取决于具体设备和系统版本。不要把某一代设备的流程直接套到所有设备上。

### 1.3 研究区

本 README 还整合了两条研究线：

- CRIWARE USM 中的 MV、音频、歌词、谱面和 CuePoint
- MikuFlick2 1.1.5 的判定、得分、Gauge、Crimax、Interlude、BTL 和结算 Rank

这些内容主要用于游戏保存、机制复刻和未来 64 位现代化重构。

---

## 2. 汉化文件与安装

### 2.1 安装前准备

1. 确认原版游戏能正常启动。
2. 完全退出游戏，包括后台任务。
3. 备份设备数据和原始 `Localizable.strings`。
4. 确认越狱环境正常，并能访问游戏 `.app` 程序包。
5. 如果使用电脑传文件，确认 AFC2 或等效文件访问方式可用。

### 2.2 下载文件

从 [Release](https://github.com/HachiMiku39/mikuflick_chinese_localization/releases/tag/MikuFlick-CN) 下载附件。不要把 GitHub 文件预览页面另存为 `.strings`。

### 2.3 替换文件

最终位置：

```text
<对应游戏>.app/
└── en.lproj/
    └── Localizable.strings
```

操作要点：

1. 用爱思助手或其他支持越狱文件系统的工具进入对应 `.app`。
2. 打开 `en.lproj`。
3. 先备份原文件。
4. 一代直接替换 `Localizable.strings`。
5. 02 将 `Localizable2.strings` 重命名为 `Localizable.strings` 后再替换。
6. 确认文件没有被追加 `.txt` 或重复扩展名。
7. 重新启动游戏，优先检查 Help 页面。

不同 iOS 版本的 App 容器路径不同，不要照搬旧教程中的固定 `/var/mobile/Applications/...` 路径。

---

## 3. 旧 iOS 环境准备

> 如果设备已经越狱、能正常安装游戏并访问 `.app`，可以直接跳到第 2 节。

### 3.1 iOS 6 / 9 与 Carbon

此前维护者在 iPhone 4S / iOS 6、9 环境中使用过 Carbon 相关流程。Carbon 官方说明面向 **32 位设备、iOS 8.0 到 9.3.6**，不要把它直接套到 64 位设备。

参考：[Carbon 使用指南](https://ios.cfw.guide/using-carbon/)

维护者当时遇到过日期与证书兼容问题，曾临时把系统日期调到 2026 年 6 月之前，再从 Carbon 页面安装证书并执行 Run。这个步骤属于当时入口的兼容处理，**不是所有 Carbon 版本的统一要求**。入口或证书说明更新后，应以对应版本文档为准。

对于 iPhone 4S / iOS 9，若目标主要是运行老游戏，可以考虑使用 [Legacy iOS Kit](https://github.com/LukeZGD/Legacy-iOS-Kit) 降级到更早系统。

### 3.2 TLSFix

旧系统连接现代 HTTPS 服务时可能需要 TLS 与根证书更新。

维护者使用过的软件源：

```text
http://cydia.skyglow.es/
```

参考：

- [TLSFix](https://github.com/nfzerox/TLSFix)
- [旧 iOS 根证书页面](https://tlsroot.litten.ca/)

根证书和 TLS 协议补丁解决的是不同层的问题。它们也不能替代正常的互联网连接。

### 3.3 AppSync Unified

开发者源：

```text
https://cydia.akemi.ai/
```

参考：[AppSync Unified](https://github.com/akemin-dayo/AppSync)

这里把 AppSync 作为重新安装旧 IPA 的环境准备项。它不负责汉化，也不负责 USB 文件访问。

### 3.4 AFC2

如需从电脑访问越狱文件系统，可安装适用于系统版本的 Apple File Conduit 2 / AFC2。

原作者软件包标识：

```text
com.saurik.afc2d
```

参考：[Cydia 软件包页面](https://cydia.saurik.com/package/com.saurik.afc2d/)

### 3.5 iOS 10

iOS 10 的越狱环境和 iOS 6 / 9 不同，尤其是较新的 A9 / A10 设备。相关记录单独维护在：

[`HachiMiku39-patch-iOS10`](https://github.com/HachiMiku39/mikuflick_chinese_localization/tree/HachiMiku39-patch-iOS10)

---

## 4. 常见问题

| 现象 | 优先检查 |
|---|---|
| Cydia 或旧 Safari 无法连接 | 手机自身网络、正确日期、根证书、TLSFix |
| 电脑无法进入游戏程序包 | 越狱是否仍有效、AFC2、设备信任状态 |
| 替换后仍显示原文 | 是否替换了正确游戏；02 是否已重命名；是否完全退出后重开 |
| 日语系统下没有显示汉化 | 当前补丁只替换英语资源；不要直接覆盖日语目录 |
| 帮助页叠字或错行 | 是否混用一代 / 02，或把英语底稿补丁放进了日语目录 |
| 显示方框或缺字 | 游戏内置字库可能缺字，与 TLS 无关 |
| 修改后闪退 | 恢复原文件，检查文件版本、完整性和读取权限 |

`.strings` 可能是二进制 plist。文本编辑器显示乱码不代表文件损坏，不要为了让它可读而随意重新保存编码。

完成越狱、补丁安装和文件下载后，汉化文件的本地替换本身不需要联网。

---

## 5. USM 与谱面研究

### 5.1 当前已实机确认的结论

| 项目 | 状态 |
|---|---|
| MV 中文整句歌词 | **已确认**。MV 播放时打开歌词即可显示中文 |
| 五档逐字参数与输入动作对应 | **已确认首句样本** |
| EASY 单独禁用一个音符 | **已确认**。只影响 EASY，其他难度保留 |
| 间奏点击模式 | **已确认第一段 NORMAL 数量**，8 次点击与事件统计一致 |
| 任意新增/删除事件、改变时间或方向 | TODO |
| 新增 Mov_18 自制曲包 | 设计假设，尚未完成完整安装验证 |

### 5.2 `hello_planet.usm` 样本结构

研究样本：`hello_planet.usm`。

```text
hello_planet.usm
├── CRID：目录、轨道信息、源文件名
├── @SFV：1 路 MV 视频
├── @SFA / ch0：音频
├── @SFA / ch1：音频
├── @CUE：歌词、逐字音符与控制事件
└── @UTF / 索引 / 对齐等元数据
```

已解析数据：

| 内容 | 结果 |
|---|---|
| 文件大小 | 102,646,144 bytes |
| 视频 | MPEG-1，320×480，20 fps，4075 帧，约 203.75 s |
| 音频 | 2 路 ADX，44.1 kHz，双声道，约 204 s |
| CUE 事件 | 505 条 |
| `time_unit` | 1000 |
| 整句歌词事件 | 26 条 |
| 逐字事件 | 376 条 |

`vo2` / `ok2` 的源文件名强烈支持原唱 / 卡拉 OK 两轨解释，但这不是明确的角色标签。本样本只有一条视频。

### 5.3 中文歌词实验

整句歌词事件位于 `parameter` 前缀 `3`。本次实验只替换歌词文本，保留时间、其他事件、视频和两条音轨。

结果：

- 25 条文本改为中文，音乐符号行保留
- 原位置覆盖并补零，没有改变 USM 总大小
- 实机 MV 模式打开歌词后，中文显示成功
- 这不代表游玩模式的逐字输入目标已经汉化

### 5.4 逐字谱面：样本编码与实际读取规则

`hello_planet.usm` 首句的五档输入动作已由维护者实机反馈核对；`11` / `2` / `3` / `4` / `5` 与点击 / 上 / 右 / 下 / 左的对应，是该样本的**编码观察**。

2026-10-05 对 MikuFlick2 1.1.5 的代码追踪补充了运行时规则：

```text
charIdx = parameter.characterAtIndex(1) - 0x3041
selector = intValue(parameter.substringWithRange(difficulty + 2, 1))

selector == 0   → 创建不可判定字符
selector 1...5  → 同一个 TelopType_Enable 函数

BoardType / FlickResult → 按 charIdx 查假名映射表
```

因此，当前版本固定读取一位字符；没有在此调用链中发现按可变长度 `11` token 跳过后缀、或把 `2/3/4/5` 直接当作输入方向的代码。**键位和方向由假名决定，数字选择是否启用该难度的音符。**

这不否定原有实机观察：本地 4233 条能按 `11` 规则拆分的记录，两种解释得出的启用掩码恰好一致。仅核对“出现几个音符”不足以区分读取规则。额外重复 `1` 的制谱工具来源仍为 TODO；直接改数字来改方向也尚未实机验证。

内部键位编号从 0 开始对应 `あ/か/さ/た/な/は/ま/や/ら/わ`；玩家侧编号仍可写成 `1/2/3/4/5/6/7/8/9/0`。内部方向编号为 `0=点击、1=上、2=右、3=下、4=左`。

实例：`ル` 为ら行上滑，`め` 为ま行右滑，`た` 为た行点击。完整表、固定位置读取证据和区分两种假设的实验方案见[详细机制研究](research/mikuflick2-1.1.5/mechanics.md)。

### 5.5 EASY 单音符禁用实测

测试事件：

```text
time = 6540
修改前：0ル22222
修改后：0ル02222
```

结果：EASY 首句的 `ル` 消失，NORMAL / HARD / EXTREME / BTL 的同一音符保留。

该样本只修改一个字节：

```text
0x32 ('2') → 0x30 ('0')
```

原文件 SHA-1：

```text
5c3a4a663c97528b34fe509b94b087a17800d2f5
```

修改后 SHA-1：

```text
7562bb0d3a39f829b4874c99f8fbd4f86b30e923
```

这证明现有逐字谱面可以按难度单独禁用音符，但不等于任意新增事件、改时间或新增歌曲已经验证成功。

### 5.6 Interlude 事件

间奏事件主要使用前缀 `5`。第一段 NORMAL 实机有 8 次点击，而解析中第二档状态为 `1` 的事件也正好有 8 条。

已观察到的模式：

| parameter | 当前解释 |
|---|---|
| `501111` | NORMAL 及以上的普通点击候选 |
| `500111` | HARD 及以上的普通点击候选 |
| `500011` | EXTREME / BTL 的普通点击候选 |
| `502222` | NORMAL及以上调用 `EndInterludeMode`，退出间奏；不生成额外点击音符 |

这里的状态 `2` 不能直接套用逐字事件中的上滑含义。

### 5.7 其他 CUE 前缀

| 前缀 | 数量 | 当前状态 |
|---:|---:|---|
| `0` | 376 | 逐字谱面，已部分实测 |
| `3` | 26 | 整句歌词 / 音乐符号，中文显示已实测 |
| `4` | 37 | 创建不可判定补充字符；完整显示效果仍需逐例核对 |
| `5` | 48 | Interlude 状态，第一段 NORMAL 数量已吻合 |
| `6` | 10 | 按难度标记最近可接受Crimax的音符；COOL且Combo≥100加200分 |
| `1` / `2` | 各 3 | 分别调用UI淡入 / 淡出控制 |
| `7` / `8` | 各 1 | 分别设置NoteDelay（毫秒）/ BPM |

### 5.8 自制 Mov_18 的当前状态

新增曲包仍属于 **待测试方案**。仅创建 `Mov_18` / `Thum_18` 目录并不能证明游戏会自动发现新包。

当前样本中：

- 包编号已观察到 `0~17` 与 `96~99`
- 歌曲全局索引已观察到 `0~73`
- 18 号包在该样本中未使用，但不代表程序一定接受
- 74 / 75 / 76 可作为当前样本的候选歌曲索引，使用前仍应检查目标设备存档

注册数据位于 `MikuFlick2.dat` 的 NSKeyedArchiver 对象图中，涉及：

```text
m_MusicPackArray
m_MusicDataArray
m_PackID
m_PackName
m_IsBuy
m_IsInstalled
m_Index
m_Title
m_Artist
m_MovieDataFileName
m_PreSoundFileName
m_ArtWorkFileName
m_ArtWorkIndex
m_DifficultNum0 ... m_DifficultNum4
```

### 5.9 `verificationFile.dat`

`verificationFile.dat` 是文件名与 SHA-1 的校验清单，不是密钥或数字签名。修改 USM 后需要同步更新摘要。

macOS：

```bash
shasum -a 1 hello_planet.usm
```

Windows PowerShell：

```powershell
Get-FileHash "hello_planet.usm" -Algorithm SHA1
```

---

## 6. MikuFlick2 1.1.5 游戏机制逆向

本节为摘要。完整的[机制、数据和证据索引](research/mikuflick2-1.1.5/README.md)包含计分与判定细节、11首歌的五档物量、195项文件用途、数值表、假名输入映射以及供另一轮Codex复核的步骤。

本次新增结论属于**当前样本的静态分析确认**；原仓库的实机实验单独注明，不把此次整理写成新增实机测试。

### 6.1 二进制信息

```text
Executable: MikuFlick2
Mach-O: ARMv7
Fat/Universal: no
LC_ENCRYPTION_INFO cryptid: 0
Ghidra: 12.1.4
SHA-256: 869caa22613c5ebfbde6b4c9e1a93362a4f30519231b6dfc9ac3ff31d414b87f
```

当前样本代码段已解密，可以直接进行静态分析。

### 6.2 主循环

核心顺序：

```text
SceneGame_Exec
├─ MikuFlickCriManager_Exec
├─ NoteManager_exec
├─ ReplayManager_Replay    (Replay Mode)
├─ TouchManager_exec
├─ StageManager_exec
├─ WindowManager_exec
└─ EffectManager_exec
```

### 6.3 时间系统

原版判定不跟着屏幕刷新率跑，而是绑定 CRI 播放时钟：

```text
PlayCnt = ceil(audioPlayTimeSeconds × 30)
m_Cnt   = PlayCnt - m_BaseTime
```

因此：

```text
1 tick ≈ 33.33 ms
```

这是现代化版本支持 60 / 120 Hz ProMotion 时最关键的兼容原则：**渲染帧率可以改变，判定时基不能改成按显示帧计数。**

### 6.4 判定枚举

| ID | 判定 |
|---:|---|
| 0 | NONE / INVALID |
| 1 | WORST |
| 2 | SAD |
| 3 | SAFE |
| 4 | FINE |
| 5 | COOL |

### 6.5 判定窗

提前 `Front`：

| tick | 判定 |
|---:|---|
| 0~2 | COOL |
| 3~6 | FINE |
| 7~8 | SAFE |
| 9~10 | SAD |

延后 `Back`：

| tick | 判定 |
|---:|---|
| 0~3 | COOL |
| 4~7 | FINE |
| 8~9 | SAFE |
| 10~11 | SAD |

原版对晚按多给约1 tick的宽容。表格是单个端点的查表范围；通常TouchDown和TouchUp取较差判定，并存在提前按住的SAFE兜底。超窗返回NONE，不等同于立即WORST。

BTL的可判定对象在`JustFrame+10`已失活，因此共享Back表不代表BTL仍可现场使用全部晚端窗口。

### 6.6 TouchDown / TouchUp 与 Flick

`NoteNormal_checkResult::::` 同时计算 TouchDown 与 TouchUp 相对 JustFrame 的差值，通常取较差判定，并对提前按住再完成 Flick 的触屏行为提供 SAFE 级容错。

输入修正：

- Flick 方向错误：最高只能 SAFE
- BoardType 错误：直接 SAD
- 正确输入的 FINE / COOL 才进入正常 Combo 增长路径

### 6.7 WORST 与 Note 生命周期

普通难度在约 `JustFrame + 12 tick` 后自动：

```text
WORST
→ Gauge 惩罚
→ ResetCombo
→ 失败特效
```

BTL 的生命周期尾端使用 offset `-2`，因此约早 2 tick 结束。

### 6.8 得分系统

当前 Score Engine 已基本闭环确认。

#### 基础 Stage Score

| 判定 | 分数 |
|---|---:|
| COOL | 300 |
| FINE | 150 |
| SAFE | 50 |
| SAD | 30 |
| WORST | 0 |

`s_tblAddScore` 还保留第二组：

```text
0, 0, 30, 50, 150, 250
```

但当前控制流中，只要进入第二组就意味着输入不匹配：Flick 错误最高只能 SAFE，Board 错误直接 SAD。因此第二组中的 FINE / COOL 项在 1.1.5 当前已确认控制流中不可达，更像遗留或未使用数据。

#### Combo Bonus

只有正确输入的 FINE / COOL 会：

```text
Combo += 1
```

然后按增加后的 Combo 计算：

```text
ComboBonus = min(500, floor((Combo + 5) / 10) × 50)
```

| Combo | 单次 Bonus |
|---:|---:|
| 1~4 | 0 |
| 5~14 | 50 |
| 15~24 | 100 |
| 25~34 | 150 |
| 35~44 | 200 |
| 45~54 | 250 |
| 55~64 | 300 |
| 65~74 | 350 |
| 75~84 | 400 |
| 85~94 | 450 |
| 95+ | 500 |

#### Crimax Bonus

满足：

```text
CrimaxMode
+ COOL
+ Combo >= 100
```

额外：

```text
+200 Stage Score
```

所以高 Combo 下 Crimax COOL 单 Note 最大可得到：

```text
300 Base + 500 Combo + 200 Crimax = 1000
```

#### Interlude Bonus

FINE / COOL 视为 Interlude 成功：

```text
每次成功 +1 Stage Score
全部 Interlude 成功再 +39
```

因此最后一次成功在全成功条件下合计贡献 40 分。

#### 最终总分

结果页明确使用：

```text
Total Score = TmpStageScore + TmpComboScore
```

没有发现额外的 Clear Bonus、Perfect Bonus、Result Bonus 或结算倍率。

### 6.9 Break The Limit

BTL 仍复用普通基础分、Combo Bonus 和 Crimax Bonus，但失误处理不同：

| BTL 结果 | Stage Score | Combo |
|---|---:|---|
| COOL | +300 | +1，并获得 Combo Bonus |
| FINE | +150 | +1，并获得 Combo Bonus |
| SAFE | +50 | 保持，不增加 |
| SAD | 转为内部 0，+0 | 保持 |
| Timeout / Miss | +0，不记录普通 WORST | 保持 |

另外：

- BTL 不走普通 Tension Gauge
- SAFE / SAD / Miss 都不会在 `NoteNormal` 路径里 ResetCombo
- 因此 BTL 的 Combo 更接近累计成功的 FINE / COOL 数量，而不是传统的连续 Combo

### 6.10 Tension Gauge

初始与上限：

```text
Start = 128
Max   = 256
```

内部数值开局为上限的50%；屏幕呈现与实际触摸延迟应按设备另行核对。

判定权重：

| 判定 | 权重 |
|---|---:|
| COOL | +2 |
| FINE | +2 |
| SAFE | 0 |
| SAD | -5 |
| WORST | -10 |

谱面长度归一化系数为以下float32表达式：

```text
64 / TotalNotes + 0.01
```

Game Over 条件包括：

1. Gauge <= 0
2. 即使之后所有剩余 Note 都至少 SAFE，理论 SAFE-or-better 成功率仍已经低于 50%

手动判定先调用Gauge再记录当前判定，所以失败比例检查使用该调用时已有计数；超时WORST先记录再调用Gauge。`50%`本身不触发比例失败，低于它才触发。

Gauge还会影响主音频音量：

```text
volumeFactor = min(1.0, Gauge / 128 + 0.35)
```

### 6.11 Crimax / Rainbow

Crimax CuePoint 会按当前难度读取开关，并在最近 4 个 Note 中寻找 `isCrimaxEnable` 的目标。

`isCrimaxEnable` 当前确认等价于：

```text
m_OptCharIdx < 0
```

Rainbow 条件：

```text
m_OptCharIdx < 0
+ Active
+ CrimaxMode
+ Combo >= 100
```

`s_tblRainbow` 为 28 组 RGB，Note 按 `(m_CrimaxCnt + 10) % 28` 循环取色。

`NoteManager_ClearCrimax` 会遍历当前 Note 并清除 `CrimaxMode`，但其真实游戏调用时机尚未可靠定位。

### 6.12 Interlude

CuePoint 类型：

| Type | 行为 |
|---:|---|
| 0 | None |
| 1 | `StartInterludeMode` 并生成 `NoteInterlude` |
| 2 | `EndInterludeMode` |

`NoteInterlude_checkResult::::` 复用普通 Front / Back 时间表。FINE / COOL 才计入 Interlude 成功。

### 6.13 Result Rank

原版 Texture Atlas 已确认：

```text
Rank 0 → Perfect!
Rank 1 → S
Rank 2 → A
Rank 3 → B
Rank 4 → C
Rank 5 → D
Rank 6 → E
```

判定条件：

| Rank | 条件 |
|---|---|
| Perfect! | 全部 Note 为 COOL |
| S | COOL + FINE = 100%，但不是全 COOL |
| A | COOL + FINE >= 95% |
| B | COOL + FINE >= 80% |
| C | COOL + FINE + SAFE >= 70% |
| D | COOL + FINE + SAFE < 70%，且未 Game Over |
| E | Game Over |

结果音效也分四档：

```text
Perfect      → Sound 0x0D
S / A        → Sound 0x0C
B / C / D    → Sound 0x0B
E            → Sound 0x0A
```

另外，存档中的 `PerfectClear` 与 Perfect Rank 不是同一个概念。结果代码会在 `MaxCombo == TotalNotes` 时写入 `SetPerfectClear`，因此它更接近全连状态。

`BreakClear`是持久化字段，不参与Total Score。当前结果函数在`difficulty==4 && rank>3`（C/D/E）时写入true；这个条件已静态复核，但玩家侧设计含义仍需实机确认，不将其解释为“BTL高等级通关”。

### 6.14 延迟、BPM与总物量

- `7`后缀解析为NoteDelay毫秒；例如`71900`表示1900ms。
- `8`后缀解析为BPM；例如`8150`表示150 BPM。
- 总普通物量加载时扫描CUE重算：前缀0、当前难度的固定位置数字非0；总间奏只数前缀5状态1。
- CUE触发时间不等于已校准的输入时刻；对象还应用NoteDelay、30Hz时钟取整及输入校准。
- 歌曲表BPM不一定是最终BPM：《多重未来のカルテット》表值195，但时间0的`8150`把运行时值设为150。
- Ghidra 12.1.4把`0xe5c6`的NEON立即数2误显示为0。原始指令与Apple otool确认140—149 BPM的行进时间为2秒，详见[复核说明](research/mikuflick2-1.1.5/verification.md)。

### 6.15 Shuffle与资源对应

用户将提供的按钮截图指认为Shuffle、随机选曲；尚未唯一匹配该截图的具体sprite。本包PV控制器的RANDOM模式3明确使用`shuffle_off/on`，后续选曲从随机起点循环寻找可用条目。资源、音效、结尾版权及待确认文件见[资源与操作映射](research/mikuflick2-1.1.5/resources.md)。

---

## 7. 当前仍未确认的部分

已补足Telop启用、SmallTelop不可判定、Lyrics的PV限制、Fade、SetDelay/SetBPM、第二份间奏时间表和基本Flick识别。下面保留未完成部分：

- `ClearCrimax`的真实调用时机，Rainbow呈现与完整动画
- Replay存取、注入顺序和整体一致性（仅看到普通判定接收回放结果的分支）
- `NoteThrow` / `NoteArrow` / `NoteWait`的完整行为
- `NoteInterlude.exec`完整生命周期与动画
- StageManager完整状态机、WindowGameWindow HUD细节
- CRI外围同步、设备触摸/音频延迟及输入校准实测
- 额外重复`1`的制谱工具来源、改方向实验、完整自制谱面
- BTL的SAFE/低判定边界与`BreakClear`玩家侧语义
- 动态商店配置缺失时无法唯一确认的封面/缩略图加载、若干编号音效的具体触发
- 新曲包注册、重启持久化与新增事件流程
- 中文逐字输入；现有假名查表不能直接推广为通用汉字输入

逐项证据、优先级和验证步骤见[下一轮复核清单](research/mikuflick2-1.1.5/verification.md)。

---


## 8. 工具与参考资料

### 8.1 常用工具

| 用途 | Windows | macOS |
|---|---|---|
| CRI 容器检查 | CriStudio / CriCodecs | CriStudio / CriCodecs |
| 媒体轨道 | FFmpeg / FFprobe | FFmpeg / FFprobe |
| 十六进制查看 | HxD | Hex Fiend |
| CUE / UTF 解析与回写 | Python | Python |
| ARMv7 静态分析 | Ghidra | Ghidra |

### 8.2 参考资料

- [CRI 官方 Sofdec 编码器文档](https://game.criware.jp/manual/native/sofdec2/latest/usr_console_encoder_main.html)
- [PyCriCodecsEx：USM 区块定义](https://mos9527.com/PyCriCodecsEx/_modules/PyCriCodecsEx/chunk.html)
- [PyCriCodecsEx：UTF 表解析](https://mos9527.com/PyCriCodecsEx/_modules/PyCriCodecsEx/utf.html)
- [CriStudio / CriCodecs](https://github.com/Youjose/CriCodecs)
- [Legacy iOS Kit](https://github.com/LukeZGD/Legacy-iOS-Kit)
- [TLSFix](https://github.com/nfzerox/TLSFix)

---

## 9. 重要说明


- 文档中的偏移和 SHA-1 只对应明确说明的样本版本，不要机械套用到其他版本。
- 对 UNKNOWN / TODO 项保持原样比编造解释更重要。

---

*更新：2026-10-05*  
*逆向样本：MikuFlick2 1.1.5 / ARMv7 / cryptid 0*  
*状态：汉化可用；USM 与游戏机制研究持续整理中*
