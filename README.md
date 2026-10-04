# Miku Flick 简体中文汉化/2026年以后的iOS6/9越狱方式教学

为 iOS 游戏 **Miku Flick（一代）** 与 **Miku Flick/02** 提供简体中文本地化文本，包括游戏帮助与说明。汉化通过替换 `Localizable.strings` 实现，不修改游戏逻辑、谱面或 UI 布局，也不保证图片中的文字会变成中文。

**本教程必须在已越狱、且越狱环境正常工作的设备上操作。安装证书或连接爱思助手本身不等于完成越狱。**
**MikuFlick只支持iOS5-iOS10的32位设备**
**如果你已经越狱，请跳到第四章**

[下载汉化文件](https://github.com/HachiMiku39/mikuflick_chinese_localization/releases/tag/MikuFlick-CN)

## 一、先确认设备与网络

1. 在“设置 → 通用 → 关于本机”记录设备型号和 iOS 版本，并确认原版游戏能够正常启动。
2. 备份设备数据，以及稍后要替换的原始 `Localizable.strings`。
3. 确认设备已经越狱，能够打开 Cydia，并能通过文件工具访问游戏的 `.app` 程序包。若尚未越狱，先按对应设备和系统版本完成越狱。
4. **中国大陆用户请提前准备能稳定访问国际互联网的网络，并在越狱、证书下载、添加软件源、刷新源和安装补丁的全过程保持连通。** 需要确认手机自身能访问相关站点；电脑能打开，不代表手机也能打开。

以下以 **iPhone 4S / iOS 6/9 / Carbon** 的准备流程为例。Carbon 当前标明支持 **32 位设备、iOS 8.0–9.3.6**；不要把这套方法直接套用到 iPhone 5s 等 64 位设备或其他系统版本。[Carbon 使用指南](https://ios.cfw.guide/using-carbon/)

关于iOS10设备，请参见另一个branch。 iOS10对于比较新的设备只有不完美越狱

关于iOS9设备，如果是iPhone 4S，建议降级到iOS6. 
GitHub有Legacy-iOS-Kit可以协助降级。

## 二、iOS 6/9：准备日期、证书与 Carbon

本项目维护者此前操作时，需要先调整日期，再处理 Carbon 页面提供的证书。按这次使用的流程：

1. 进入“设置 → 通用 → 日期与时间”，关闭自动设置，将日期**临时调整到 2026 年 6 月之前**。维护者未指定唯一的一天，请不要把某个猜测日期当作固定要求。
2. 在设备的 Safari 中打开 [Carbon 官网](http://carbon.sep.lol/)。
3. 使用页面上的 **Install certs** 入口，按设备提示检查并安装所需的证书描述文件。这里是根证书准备步骤，不是给 IPA 使用的企业签名证书。
4. 返回 Carbon，按当前页面说明执行 **Run**。首次过程可能需要在线下载资源，保持网络连通，等待页面和设备完成操作。
5. 完成日期兼容处理后，恢复正确的日期与时间，再继续刷新软件源。长期停留在过去的日期，可能使其他证书被判断为尚未生效。
6. 确认 Cydia 可以打开，并能刷新软件源。仅出现图标不能证明后续文件访问和插件已经正常工作。

> 日期调整是本项目当时使用入口时遇到的兼容处理，并不是所有 Carbon 版本的统一前置要求。当前公开指南没有要求所有用户回拨日期；如果入口或证书说明已更新，以对应版本的说明为准。证书和 TLS 补丁也不是同一件事。

## 三、添加软件源并安装 TLSFix、AppSync 与 AFC2

在 Cydia 中打开“软件源 → 编辑 → 添加”，逐个添加所需源，等待刷新完成。旧系统出现连接错误时，先检查网络和正确时间，再处理证书与 TLS；反复添加同一个源不能解决这些问题。

### 1. TLSFix：修复旧系统的 HTTPS 兼容性

维护者此次使用的软件源为：

```text
http://cydia.skyglow.es/
```

添加后搜索并安装 **TLSFix**，按包说明完成重启或相关进程重启。其开发者还要求使用更新的根证书信任库；可按 [TLSFix 项目说明](https://github.com/nfzerox/TLSFix) 前往 [根证书页面](https://tlsroot.litten.ca/) 选择适用于旧 iOS 的证书包。已经完成证书更新时，先确认现有状态，不要盲目重复安装。

根证书帮助系统验证服务器身份；TLSFix 处理旧系统与现代 HTTPS 的协议兼容问题。两者都不能替代国际互联网连通性，也不会恢复已关闭的游戏服务器。

### 2. AppSync Unified：准备游戏安装环境

添加开发者的软件源：

```text
https://cydia.akemi.ai/
```

搜索 **AppSync Unified**，按软件包要求安装依赖并完成提示的重启操作。本教程把它作为安装或重新安装游戏 IPA 的准备项；它不负责翻译文本，也不提供 USB 文件访问。[AppSync 项目说明](https://github.com/akemin-dayo/AppSync)

### 3. AFC2：让电脑访问越狱文件系统

在 Cydia 搜索并安装适用于当前系统的 **Apple File Conduit “2” / AFC2**。原作者的软件包标识为 `com.saurik.afc2d`，安装前核对来源与系统兼容性。[原作者软件包页面](https://cydia.saurik.com/package/com.saurik.afc2d/)

安装完成后，按提示重启服务或设备，再重新连接电脑。如果设备重启后越狱环境没有自动恢复，先按所用越狱方案重新激活，再检查 AFC2；不要只凭爱思助手里显示“已越狱”就跳过文件访问检查。

## 四、下载对应游戏的汉化文件

在 [Release](https://github.com/HachiMiku39/mikuflick_chinese_localization/releases/tag/MikuFlick-CN) 中下载附件，避免把 GitHub 文件预览网页另存为 `.strings`。

| 游戏 | 下载的文件 | 导入时的文件名 | 替换位置 |
|---|---|---|---|
| Miku Flick（一代） | `Localizable.strings` | `Localizable.strings` | 该游戏 `.app/en.lproj/` |
| Miku Flick/02 | `Localizable2.strings` | **重命名为 `Localizable.strings`** | 该游戏 `.app/en.lproj/` |

**当前两份 Release 汉化文件都基于英语本地化资源制作。只替换对应游戏的 `en.lproj`，不要将同一份文件同时放进日语目录。** 旧版 Release 文字中“02 适用于日语和英语”的说法不适用于当前这两份附件，应以这里的文件对应关系为准。

英语与日语原文件的帮助文本分行、空白位置和内容分配不同。此前跨语言目录替换时出现过叠字，因此不能仅凭文件同名就混用。一代和 02 的文件也不能互换。

## 五、使用爱思助手等工具替换文件

1. **完全退出游戏**，包括后台任务。
2. 用数据线连接电脑，解锁设备，并完成设备要求的电脑信任操作。
3. 打开爱思助手或其他支持越狱文件系统的工具，确认能访问游戏的 `.app` 程序包。如果只能看到照片或有限的应用文档，先检查 AFC2 和越狱是否生效。
4. 定位要汉化的游戏程序包，再打开其中的 **`en.lproj`**。正确拼写是 `en.lproj`，不是 `en.proj`。
5. 将目录中原有的 `Localizable.strings` 导出到电脑备份，按游戏名称分别保存。
6. 按上表准备汉化文件。02 的文件要先去掉文件名中的数字 `2`，然后替换原文件。确认没有被系统追加 `.txt` 或重复扩展名。
7. 保持文件能够被游戏读取，等待传输结束，再启动游戏检查帮助页面。

最终替换位置如下，程序包名称以你的设备实际显示为准：

```text
<对应游戏的程序包>.app/
└── en.lproj/
    └── Localizable.strings
```

不同 iOS 版本的应用目录结构不同，路径中也可能使用一串标识符。不要照搬旧说明中的 `/var/mobile/Applications/MikuFlick`；应通过工具确认实际程序包位置。**汉化文件放在 `.app` 内，不是存档使用的 `Documents` 文件夹。**

## 六、检查效果与常见问题

先打开游戏帮助，检查文字、换页和排版。本项目仅替换本地化资源，图片文字和部分固定 UI 可能仍保留原语言。

| 现象 | 优先检查 |
|---|---|
| Carbon 或 Cydia 无法连接 | 手机自身的国际互联网连通性、日期、证书与 TLSFix；不要把所有连接问题都归因于越狱失败 |
| 爱思助手无法打开游戏程序包 | 设备是否解锁、连接是否可信、AFC2 是否生效、重启后越狱是否仍有效 |
| 替换后仍显示原文 | 是否替换了正在使用的游戏；02 是否已重命名；是否完全退出后重开；游戏是否选择了英语资源 |
| 系统为日语，汉化未生效 | 请检查你的手机语言是不是日语。本游戏只针对英语进行翻译，SEGA的设定是非日语的所有语言默认使用英语UI。当前补丁只替换英语资源。可临时把系统语言设为英语后重新打开游戏验证，不要直接覆盖日语目录 |
| 帮助页面叠字或错行 | 检查是否混用一代/02，或把英语底稿补丁放进日语目录；先恢复原文件再排查 |
| 显示方框或缺字 | 可能是游戏字库缺字，与 TLS 无关；保留设备、系统、游戏版本和问题位置供反馈 |
| 修改后闪退 | 恢复备份的原始文件，检查文件版本、完整性和读取权限 |

`.strings` 文件可能是二进制 plist，文本编辑器显示乱码不代表损坏。直接使用下载的附件，不要为了让它“可读”而随意改变编码或保存格式。

完成越狱、补丁安装和文件下载后，汉化文件的本地替换本身不需要联网。国际互联网连通要求针对前面的在线准备过程。

## 版本与反馈

此说明于 **2026 年 9 月 14 日** 根据维护者提供的操作经历及项目文档整理。Carbon、证书和软件源可能更新；其他设备与系统版本需单独确认。反馈问题时请提供设备型号、iOS 版本、游戏是一代还是 02、所用汉化文件及替换路径。

## USM 解析与歌词修改实验（Miku Flick/02）

**本节仍属于实验性研究。已实机确认两项结果：MV 播放时开启歌词可显示中文；修改一个逐字事件的 EASY 参数，可以只移除 EASY 的对应音符。完整自制谱面、中文输入玩法与新增曲包仍未验证成功。**

上文的 `.strings` 汉化与本节的 USM 实验是两项不同工作。以下记录基于《＊ハロー、プラネット。》的 `hello_planet.usm`、已解析的资源 / 存档，以及维护者于 **2026 年 9 月 14 日** 提供的游戏内操作与测试反馈；不能直接推广到一代、所有歌曲或所有 USM 文件。

| 项目 | 当前证据与范围 |
|---|---|
| MV 中文整句歌词 | 已实机确认：仅针对 MV 播放并开启歌词显示 |
| 五档逐字参数及操作对应 | 首句五个难度的 29 次操作全部与解析结果对应；EASY 单音符禁用另有修改实测 |
| EASY 首句「ル」移除 | 已实机确认：只影响 EASY，其他难度的「ル」保留 |
| 间奏点击模式 | 已观察到键盘隐藏；NORMAL 第一段 8 次点击与事件统计一致 |
| 任意增删音符、改变方向或时间 | 尚未逐项实机验证 |
| 新增 `Mov_18` 自制曲包 | 方案假设；资源注册、读取与重启持久化尚未验证 |

### 1. 这个 USM 里装了什么

USM 是 CRIWARE 的音视频与事件流容器。音视频数据块按播放顺序交错存放，下面是逻辑组成：

```text
hello_planet.usm
├── CRID：目录、轨道信息、源文件名
├── @SFV：1 路 MV 视频
├── @SFA / 通道 0：1 路音频
├── @SFA / 通道 1：另 1 路音频
├── @CUE：歌词、逐字音符与控制事件
└── 元数据：UTF 表、视频跳转索引、长度及对齐信息
```

| 内容 | 本次样本的解析结果 |
|---|---|
| 文件大小 | 102,646,144 字节，已逐块解析到文件末尾 |
| 视频 | MPEG-1，320 × 480，20 fps，4075 帧，约 203.75 秒 |
| 两路音频 | 均为 ADX、44,100 Hz、双声道，约 204 秒 |
| 音频源文件名 | `pv_083vo2.aif`、`pv_083ok2.aif`；实际嵌入编码为 ADX |
| 游戏事件 | `@CUE` 中的 `CUEPOINT_INFO` 表，共 505 条 |
| 事件字段 | `name`、`time`、`cue_type`、`parameter` |
| 时间基准 | `time_unit = 1000`，即每秒 1000 单位 |
| 整句歌词 | 26 条歌词行事件，含 1 条音乐符号行 |
| 逐字音符 | 376 条含假名与数字参数的事件 |

`vo2` / `ok2` 的命名强烈支持“原唱 / 卡拉 OK 伴奏”两轨的解释，但这不是明确的轨道角色标签。本样本只有一条视频，符合切换音轨、共用 MV 的结构；不能据此说它内含两个独立 MV。

`@UTF` 是 CRI 的二进制表格格式，歌词字符串使用 UTF-8 编码。LRC、CSV、JSON 是解析后导出的编辑材料，原 USM 中没有直接存放一个 LRC 文件。本样本也没有常规 `@SBT` 字幕轨；只用普通播放器或 FFprobe 查看媒体轨道，会漏掉 `@CUE` 中的歌词与谱面相关数据。

### 2. 已确认的中文歌词显示实验

本次只修改 `parameter` 以 `3` 开头的整句歌词事件：保留前缀与时间，替换后面的日文句子。26 条行事件中，25 条改成中文，音乐符号行保留。

- **已实机确认：进入 MV 播放，并选择开启歌词显示后，中文歌词生效。**
- 当前确认范围仅限上述 MV 歌词显示，不应写成游玩模式的逐字歌词、输入目标或谱面也已汉化。
- 逐字音符中的日文假名、五档参数和其他控制事件均未修改；原日文谱面保留。
- 视频、两条音轨及全部事件时间戳保持原样，没有重新编码音视频。
- 字库与排版仍需按具体文本和设备验证，单首样本成功不代表所有汉字均可显示。

中文文本没有超过各自原有的字节空间，因此可以在原位置覆盖、补零，并更新文本长度字段。修改后文件大小和所有区块位置不变，视频跳转索引也不需要移动。逐块比对只改变了 1 个 CUE 元数据块；其余区块完全一致。

### 3. 逐字谱面与日语 T9 的对应关系

本样本的容器字段 `cue_type` 全部为 `0`。以下“前缀”均指 **`parameter` 的第一个字符**，不要把它与 `cue_type` 混为一谈。所有事件的 `name` 为 `note`，并不表示每条事件都是可点击音符。

前缀 `0` 的结构可按下式解释：

```text
0 + 假名字符 + EASY / NORMAL / HARD / EXTREME / BTL 五项代码
```

全部 376 条记录都能使用 `11`、`0`、`2`、`3`、`4`、`5` 拆成恰好五项。**`11` 在此作为一个有效操作代码处理，不能按五个十进制数字读取。** 这描述的是目前可复现的解析规则；程序内部是否把 `11` 再拆成两个子字段，尚未反汇编确认。

| 逐字事件代码 | 首句实机操作对应 |
|---|---|
| `0` | 该难度不出现此音符；EASY「ル」的修改实测也确认了这一点 |
| `11` | 点击 |
| `2` | 上滑 |
| `3` | 右滑 |
| `4` | 下滑 |
| `5` | 左滑 |

操作所用的键位由假名所在行解释。维护者使用的编号为：

| 键号 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| 五十音行 | あ | か | さ | た | な | は | ま | や | ら | わ |

因此「ル」是 9 键上滑，「め」是 7 键右滑，「お」是 1 键下滑。「タ」「が」「さ」都使用 `11`，却分别点击 4、2、3 键，说明后缀代码不是 T9 键号。假名如何在程序内部映射到键位、浊音与特殊字符如何处理，仍需进一步分析。

首句原文为 `シェルターのおと　ひとりめがさめた`。以下时间均为 CUE 时间，不直接等同于已校准的判定时刻；音符提前显示与媒体同步偏移尚未测定。

| CUE 时间（秒） | 原始 parameter | EASY | NORMAL | HARD | EXTREME | BTL |
|---:|---|---|---|---|---|---|
| 6.340 | `0シ00005` | 0 | 0 | 0 | 0 | 5 |
| 6.540 | `0ル22222` | 2 | 2 | 2 | 2 | 2 |
| 6.740 | `0タ000011` | 0 | 0 | 0 | 0 | 11 |
| 7.140 | `0の00004` | 0 | 0 | 0 | 0 | 4 |
| 7.340 | `0お00444` | 0 | 0 | 4 | 4 | 4 |
| 7.540 | `0と00004` | 0 | 0 | 0 | 0 | 4 |
| 7.940 | `0ひ00005` | 0 | 0 | 0 | 0 | 5 |
| 8.140 | `0と00044` | 0 | 0 | 0 | 4 | 4 |
| 8.340 | `0り00005` | 0 | 0 | 0 | 0 | 5 |
| 8.540 | `0め03333` | 0 | 3 | 3 | 3 | 3 |
| 8.740 | `0が000011` | 0 | 0 | 0 | 0 | 11 |
| 8.940 | `0さ0001111` | 0 | 0 | 0 | 11 | 11 |
| 9.140 | `0め00003` | 0 | 0 | 0 | 0 | 3 |
| 9.340 | `0た1111111111` | 11 | 11 | 11 | 11 | 11 |

维护者逐档操作反馈与上表一致：

| 难度 | 首句出现的音符 | 实际输入（数字为键号） |
|---|---|---|
| EASY | ル、た（2 个） | 上滑 9、点击 4 |
| NORMAL | ル、め、た（3 个） | 上滑 9、右滑 7、点击 4 |
| HARD | ル、お、め、た（4 个） | 上滑 9、下滑 1、右滑 7、点击 4 |
| EXTREME | ル、お、と、め、さ、た（6 个） | 上滑 9、下滑 1、下滑 4、右滑 7、点击 3、点击 4 |
| BTL | シ、ル、タ、の、お、と、ひ、と、り、め、が、さ、め、た（14 个） | 左滑 3、上滑 9、点击 4、下滑 5、下滑 1、下滑 4、左滑 6、下滑 4、左滑 9、右滑 7、点击 2、点击 3、右滑 7、点击 4 |

首句的 `4ェ`、`4ー` 没有对应 BTL 输入，与补充显示字符的解释相符，但还不能把所有前缀 `4` 事件认定为可以任意删除的装饰。按同一拆分规则统计整首前缀 `0` 的非零项，五档分别为 **65 / 107 / 161 / 225 / 376**；这是逐字事件的解析统计，不含间奏与特殊事件，不是已经实测的总物量。

### 4. 已实机确认：只移除 EASY 首句「ル」

这次测试从原始日文 USM 制作，只改一个字节，未叠加中文歌词补丁：

```text
事件：从 0 计数的第 6 条，time = 6540
修改前：0ル22222 → EASY=2，NORMAL=2，HARD=2，EXTREME=2，BTL=2
修改后：0ル02222 → EASY=0，NORMAL=2，HARD=2，EXTREME=2，BTL=2
```

| 检查项 | 结果 |
|---|---|
| 预期 | EASY 首句「ル」消失，只剩句末「た」；其他难度的「ル」保留 |
| 实机反馈 | **与预期一致** |
| 字节修改 | 本样本偏移 `0x5C6C`（十进制 23660），ASCII `2`（`0x32`）→ `0`（`0x30`） |
| 容器比对 | 文件仍为 102,646,144 字节；除这 1 字节外，其余 USM 字节完全一致 |
| 原文件 SHA-1 | `5c3a4a663c97528b34fe509b94b087a17800d2f5` |
| 修改后 SHA-1 | `7562bb0d3a39f829b4874c99f8fbd4f86b30e923` |
| 外部校验 | 同步更新 `verificationFile.dat` 中该 USM 的摘要 |

该测试证明了**现有逐字谱面可以按难度单独禁用音符**，并支持五档顺序的解释。它没有验证任意添加记录、改方向、改判定时间、改输入字符或新增歌曲。上述偏移仅适用于指定原文件，其他版本必须重新定位事件，不能直接套用。

### 5. 间奏点击模式与尚未解明的事件

维护者观察到，在 `メモリのなかのキミに　オハヨーハヨー` 与 `しずかに　ねむる　きみをみた` 之间，T9 键盘不出现，改为普通点击音符，**NORMAL 共点击 8 次**。

这一段的事件顺序为：

```text
98.140 秒  2
98.940 秒  3♪♪♪♪♪．．．
99.740～107.740 秒  15 条前缀 5 事件
110.140 秒  1
110.340 秒  3しずかに…（下一句）
```

前缀 `5` 的候选结构是 `5 + 五档各一位状态`，与前缀 `0` 的操作 token 规则不同：

| 参数 | 本段条数 | EASY / NORMAL / HARD / EXTREME / BTL | 当前解释 |
|---|---:|---|---|
| `501111` | 8 | `0 / 1 / 1 / 1 / 1` | NORMAL 等难度的普通点击候选 |
| `500111` | 3 | `0 / 0 / 1 / 1 / 1` | HARD 及以上的普通点击候选 |
| `500011` | 3 | `0 / 0 / 0 / 1 / 1` | EXTREME、BTL 的普通点击候选 |
| `502222` | 1 | `0 / 2 / 2 / 2 / 2` | 非普通点击状态；可能是结束标记，未单独修改验证 |

NORMAL 第二档为 `1` 的时间是 **99.740、100.940、102.540、103.740、104.540、105.340、106.540、107.340 秒**，恰好 8 条，与实际点击数一致。107.740 秒另有 `502222`，所以不能把“非零状态”全部计为普通点击，否则会误算成 9 个。这里的 `2` 也不能照搬逐字事件解释成“上滑”。

| 间奏 | EASY | NORMAL | HARD | EXTREME | BTL |
|---|---:|---:|---:|---:|---:|
| 第一段，按状态 `1` 统计 | 0 | **8（实机数量吻合）** | 11 | 14 | 14 |
| 第二段，按状态 `1` 统计 | 0 | 18 | 31 | 32 | 32 |

除第一段 NORMAL 的数量外，上表均是解析预测。两段共 48 条前缀 `5` 事件，其中含两个 `502222`，不能直接写成 48 个可游玩音符。单字符 `2`、`1` 在第一段两侧出现，支持它们与区段 / 键盘状态切换有关的猜想；具体职责仍需单变量测试，不能只凭时序认定。

其余事件的当前状态如下：

| parameter 前缀 | 全曲数量 | 内容与验证状态 |
|---|---:|---|
| `0` | 376 | 逐字谱面；首句对应与 EASY 单音符禁用已验证 |
| `3` | 26 | 整句歌词 / 音乐符号；MV 中文显示已验证 |
| `4` | 37 | 小假名、长音等；完整语义待分析 |
| `5` | 48 | 间奏状态；第一段 NORMAL 的 8 次点击吻合 |
| `6` | 10 | 如 `600010`、`600110`、`601110`；特殊事件含义未知 |
| `1`、`2` | 各 3 | 区段 / 显示切换候选，尚未孤立验证 |
| `7`、`8` | 各 1 | 时间 0 的 `71900`、`8150`；初始化参数候选 |

`8150` 可能涉及 BPM 150，首句部分事件间隔 200 ms 与该速度的八分音符相容，但尚无独立验证；`71900` 的含义未确认。做编辑器时应原样保留未知事件，不应先把猜想写死为规则。
### 6. 自制曲包的结构假设：从资源替换到新增 Mov_18

**以下是待测试方案，不是已成功的安装教程。** 现有结果证明可以修改已注册歌曲的 CUE 内容；新增一个曲包还涉及歌曲目录、资源映射与程序对编号的接受范围。仅创建 `Mov_18` / `Thum_18`，不能保证游戏自动发现它。

#### 6.1 候选目录结构

```text
<MikuFlick02 的应用数据容器>/Library/InstallData/
├── Mov_18/
│   ├── songname.usm
│   ├── songname2.usm
│   ├── songname3.usm
│   ├── music_18_01.png
│   ├── pv_xxx_lp.adx
│   ├── pv_yyy_lp.adx
│   ├── pv_zzz_lp.adx
│   └── verificationFile.dat
└── Thum_18/
    └── thum_18.png
```

`xxx`、`yyy`、`zzz` 是三个不同的三位编号，候选方案中还应避开现有资源编号。目录名中的下划线是普通 `_`，不是反斜杠转义；缩略图采用已观察到的 `thum_17.png` 命名规律，即候选名为 **`thum_18.png`**，不是 `thum18.png`。实际应用数据容器路径随系统和安装情况变化。

按“三首歌曲一包”设计与现有 DLC 结构相符：已解析注册表有 21 个 DLC 包，每包 3 首；另有 0 号基础包，包含 11 首。因此“三首”是目前采用的 DLC 模板约束，**还没有证明引擎最多只能装三首**。三位预览音频编号全局不重复也是保守约定，尚未证明是引擎硬性要求。

| 文件 | 作用 / 目前理解 | 编辑时需要保留或确认的内容 |
|---|---|---|
| 三个 `.usm` | 各歌曲 MV、音轨、歌词与谱面事件 | 内部流、CUE、偏移、时间、索引；换媒体与增删事件需另测 |
| `pv_*_lp.adx` | 选歌试听资源；存档字段 `m_PreSoundFileName` 指向它 | 歌曲与试听文件的一一映射；不等同于 USM 内的完整音轨 |
| `music_18_01.png` | 候选歌曲图集；现有 `music_11_01.png` 为 1024 × 1024，含歌曲 logo、作者信息与封面元素 | 图集尺寸、各元素位置及歌曲顺序；不是三张独立封面简单拼接 |
| `thum_18.png` | 候选缩略图集；现有 `thum_17.png` 为 512 × 512，含游戏截图与小封面 | 保留原图集布局；不能假定程序会自动识别新裁切区域 |
| `verificationFile.dat` | 已观察到的文件名 / SHA-1 清单 | 按实际文件名与内容更新全部受影响条目，不能直接复制旧摘要 |

图集与 `m_ArtWorkIndex` 的 0、1、2 索引支持“按歌曲索引取图”的解释，但完整裁切坐标与读取规则尚未确认。制作新图集时应先沿用一个已工作的包的尺寸、位置与顺序。

#### 6.2 17 号包参考与附件边界

已检查的 17 号包资源清单与注册记录对应如下：

| 歌曲原名 | 全局 `m_Index` | USM 文件 | 试听文件 | `m_ArtWorkIndex` |
|---|---:|---|---|---:|
| 孤独の果て -extend edition- | 59 | `kodokunohate.usm` | `pv_085_lp.adx` | 0 |
| ローリンガール | 60 | `rolling_girl.usm` | `pv_091_lp.adx` | 1 |
| 透明水彩 | 61 | `toumei_suisai.usm` | `pv_210_lp.adx` | 2 |

该包另含 `music_17_01.png`、`verificationFile.dat`，缩略图为 `Thum_17/thum_17.png`；注册包名为 `Rock_Pack01`。

**本轮提供的附件并非完整的 17 号包：** `thum_17.png` 属于 17 号，而 `music_11_01.png` 和所提供的 `verificationFile.dat` 仍对应 11 号包（`double_lariat`、`from_y_to_y`、`hello_planet`；试听编号 046、057、083）。不能把这份 11 号清单直接当作 17 / 18 号包的模板内容。上表来自此前检查的 17 号包清单与注册记录，而不是由这三份附件全部推导。

#### 6.3 还需要歌曲注册记录

解析到的 `MikuFlick2.dat` 是 NSKeyedArchiver 归档。其根对象的 `m_MusicPackArray` 保存包对象，每个包再通过 `m_MusicDataArray` 保存歌曲对象。它不是只靠文件名就能生成的普通 JSON；回写时还需要保持归档对象引用。

| 层级 | 已观察到的字段 | 与新包有关的问题 |
|---|---|---|
| 包 | `m_PackID`、`m_PackName`、`m_Date` | 新包编号、名称、日期是否被游戏接受 |
| 包状态 | `m_IsBuy`、`m_IsInstalled` | 记录状态与实际资源是否一致；写入已安装状态不等于文件已安装 |
| 包内歌曲 | `m_MusicDataArray` | 三首歌曲对象的组织与引用 |
| 歌曲身份 | `m_Index`、`m_Title`、`m_Artist` | 全局唯一歌曲编号与选歌文字 |
| 资源映射 | `m_MovieDataFileName`、`m_PreSoundFileName`、`m_ArtWorkFileName`、`m_ArtWorkIndex` | USM、试听、图集名称及图内索引；样本中的资源引用使用无扩展名的名称 |
| 难度与进度 | `m_DifficultNum0`～`m_DifficultNum4`，以及解锁 / 分数等记录 | 难度显示与新歌曲状态是否完整；不能推定改难度数字就会生成谱面 |

样本中的 `m_LogoFileName` 为 null，不能仅凭字段名断定它就是 `music_18_01.png` 的入口。注册表也可能在启动时被程序内部目录重建，所以编辑存档后必须检查重启是否保留。

已解析的 22 个包编号为 **0～17、96～99**，歌曲全局索引为 **0～73**。18 号在这份样本中未使用，但“空闲”不代表程序一定接受。特别是 96～99 号包已经占用歌曲索引 62～73，新增三首时不能从 62 开始；**74、75、76** 可作为本样本的候选索引，实际制作前仍需核对目标设备最新存档。

#### 6.4 建议的分阶段验证

1. **现有歌曲内修改：** 在已工作的曲包内继续做单个音符的启用、方向、时间测试；目前完成的是 EASY 单音符禁用。
2. **验证新包注册：** 以可正常运行的三首歌包为模板，复制资源并使用新名称，添加候选包与歌曲记录，更新校验清单。先保持原媒体和事件内容，检查选歌是否出现、三首标题 / 图集 / 试听是否对应、MV 与各难度是否可进入。此步骤尚未完成。
3. **检查重启持久化：** 完全退出再启动，确认新包仍存在，且没有重建目录、覆盖记录或编号越界问题。
4. **逐步替换自制内容：** 注册可用后，分别测试媒体替换、整句歌词、逐字谱面和间奏事件；每次只改变一个因素。

目前较有依据的谱面设计是“共用逐字时间轴，每条记录为五个难度分别指定操作；歌词行与间奏事件独立控制显示 / 输入段落”。但新增事件后的总物量、评分、连击、进度、时间同步与结算是否需要其他元数据配合，仍需验证。新包也可能受硬编码包表、编号范围或其他目录文件限制；发现文件夹并不足以证明完整自制包可行。
### 7. 加密、校验与修改方式

本样本的歌词可以直接读取，音视频无需提供密钥即可解码，本次没有解密步骤。USM 格式可以使用可选的加密 / 掩码处理，所以其他游戏或其他来源的文件仍可能需要密钥。

曲包中的 `verificationFile.dat` 是文件名与 SHA-1 的校验清单，不是密钥或数字签名。修改 USM 后，需要更新对应文件的摘要；是否存在其他运行时检查，应以实机为准。

仅修改本样本的歌词时，可采用以下流程：

1. 备份原 USM 与对应的 `verificationFile.dat`。
2. 解析 CUE / UTF 表并导出歌词，保留原始事件和时间。
3. 编辑译文，按 UTF-8 **字节数**检查长度，保留参数前缀。
4. 若译文不超过原空间，在原位置覆盖、补零，并更新对应长度字段。本样本该长度字段为大端序，原参数长度包含末尾的 `00`。
5. 回读修改后的表格，逐项确认只有预期歌词变化；检查音视频、其他事件及索引。
6. 更新校验清单中该 USM 的 SHA-1。
7. 完全退出游戏，将 USM 和校验文件一起替换回同一曲包的原位置；进入 MV 播放并开启歌词显示测试。

如果新文本超出原空间，或需要增删事件、更换音视频，就必须重建相关 UTF 偏移、USM 区块长度与对齐，并修正受影响的目录信息和跳转索引。不能通过文本编辑器直接插入字符，也不能把 LRC 文件直接放进曲包代替事件表。

### 8. Windows 与 macOS 工具

| 用途 | Windows | macOS |
|---|---|---|
| 查看、提取 CRI 容器 | CriStudio / CriCodecs | CriStudio / CriCodecs |
| 检查媒体轨道、提取音视频 | FFmpeg / FFprobe | FFmpeg / FFprobe |
| 查看及覆盖二进制字节 | HxD | Hex Fiend |
| 编辑导出的歌词与 JSON | VS Code 等文本编辑器 | VS Code 等文本编辑器 |
| 准确解析并回写游戏事件 | Python 脚本 | Python 脚本 |

本次修改使用 Python 解析并在原位置回写。通用工具可用于辅助检查，但尚未验证 CriStudio 的保存流程能完整保留本游戏的自定义 CUE 事件。FFmpeg 可提取音视频；本次使用的 FFmpeg 支持 USM 读取，没有 USM 输出封装器，不能用一次普通转码代替完整的游戏资源回封。十六进制编辑器应使用覆盖模式，且必须理解长度与偏移字段。

计算修改后文件的 SHA-1：

Windows PowerShell：

```powershell
Get-FileHash "hello_planet.usm" -Algorithm SHA1
```

macOS 终端：

```bash
shasum -a 1 hello_planet.usm
```

将得到的 40 位摘要填回校验清单中 `hello_planet.usm` 对应行，其他文件的摘要保留。
# MikuFlick2 1.1.5 游戏机制逆向笔记

> 基于 `MikuFlick2` iOS 版 1.1.5（ARMv7）在 Ghidra 中的静态分析结果整理。  
> 本文只记录本轮已经从二进制中确认或能够高置信推导出的机制。尚未完全追踪的部分会明确标注。

---

## 0. 研究对象与可信度标记

### 二进制基本信息

- App：`MikuFlick2`
- 版本：1.1.5
- 主程序：`Payload/MikuFlick2.app/MikuFlick2`
- Mach-O：32 位 ARMv7
- Universal/Fat：否，仅 `armv7`
- FairPlay：
  - `LC_ENCRYPTION_INFO`
  - `cryptid 0`
  - 当前样本代码段已解密，可直接静态分析
- 主要框架风格：
  - Objective-C
  - C / C++
  - CRI Middleware（CRI Mana / CRI Atom）
- 反编译工具：Ghidra 12.1.4

### 本文标记

- **[确认]**：可直接从函数、数据表或控制流中确认。
- **[高置信推断]**：代码关系已经非常明确，但尚未追到所有外围逻辑。
- **[未完成]**：当前尚未继续深挖。

---

# 1. 游戏主循环

核心入口：

```text
-[SceneGame_Exec]
```

目前确认的每帧执行顺序：

```text
SceneGame_Exec
│
├─ 更新时间 / 游玩时间
├─ MikuFlickCriManager_Exec
├─ NoteManager_exec
├─ ReplayManager_Replay       （仅 Replay Mode）
├─ TouchManager_exec
├─ StageManager_exec
├─ WindowManager_exec
└─ EffectManager_exec
```

## 1.1 Note 更新顺序

`+[NoteManager_exec]` 会遍历当前 Note 集合，对每个 Note：

```text
note.exec()
setNextTarget(0)
根据 active 状态调整 Z 位置
```

随后再次遍历 Note，找到第一个 active Note：

```text
setNextTarget(1)
```

因此 `NextTarget` 本质上是当前需要优先提示/显示的目标 Note。

---

# 2. 时间系统：判定不是跟着渲染帧跑

这是整个判定系统里非常关键的一点。

## 2.1 播放计数器

`+[MikuFlickCriManager_Exec]`：

```c
playTime = CriManager::GetPlayTime();
PlayCnt = ceil(playTime * 30.0f);
```

全局播放计数器：

```text
DAT_00164340
```

`+[MikuFlickCriManager_GetPlayCnt]` 只是：

```c
return DAT_00164340;
```

## 2.2 Note 自己的时间

`-[NoteNormal_exec]` 中：

```c
m_Cnt = MikuFlickCriManager_GetPlayCnt() - m_BaseTime;
```

所以 Note 不是简单地：

```text
每画一帧 → m_Cnt++
```

而是：

```text
CRI 音频播放时间
        ↓
转换成 30 Hz PlayCnt
        ↓
减去 Note 的 BaseTime
        ↓
得到 Note 当前 m_Cnt
```

### 结论

**[确认]**

```text
1 tick ≈ 1 / 30 秒 ≈ 33.33 ms
```

这意味着游戏逻辑时间与音频时钟绑定，而不是与屏幕刷新帧率绑定。

这对于 2012 年移动设备非常重要：即使画面掉帧，判定时钟也不应该跟着漂移。

## 2.3 CRI 时间来源

调用链：

```text
MikuFlickCriManager_Exec
↓
CriManager::GetPlayTime
↓
_criManaPlayer_GetTime
↓
CriMvEasyPlayer::GetTime
```

`CriManager::GetPlayTime()` 最终返回：

```text
timeValue / timeBase
```

并且 `CriMvEasyPlayer::GetTime()` 中可看到与：

```text
0.0333667
```

相关的时间修正逻辑，约等于 29.97 fps 的帧周期。

---

# 3. 判定枚举

从 `NoteNormal_checkResult::::`、结果画面以及 `StatusData` 统计逻辑可以完全确定判定索引：

| 内部值 | 判定 |
|---:|---|
| 0 | 内部无有效判定 / 空结果 |
| 1 | WORST |
| 2 | SAD |
| 3 | SAFE |
| 4 | FINE |
| 5 | COOL |

结果画面直接按以下顺序读取：

```text
GetTmpNoteResult(5) → Cool
GetTmpNoteResult(4) → Fine
GetTmpNoteResult(3) → Safe
GetTmpNoteResult(2) → Sad
GetTmpNoteResult(1) → Worst
```

`0` 不作为五种玩家可见判定显示，但内部数组和最高成绩记录会保留 `0~5` 六个槽位。

---

# 4. 普通 Note 的判定窗

相关数据表：

```text
s_tblNoteNormal_Front @ 0x00139488
s_tblNoteNormal_Back  @ 0x001394B4
```

定义：

```text
Front = 玩家输入早于 JustFrame
Back  = 玩家输入晚于 JustFrame
```

因为代码计算：

```c
delta = JustFrame - TouchFrame;
```

所以：

```text
delta > 0 → 提前
delta < 0 → 延后
```

## 4.1 提前判定表

`s_tblNoteNormal_Front`：

| 提前 tick | 判定 | 约时间 |
|---:|---|---:|
| 0 | COOL | 0 ms |
| 1 | COOL | 33 ms |
| 2 | COOL | 67 ms |
| 3 | FINE | 100 ms |
| 4 | FINE | 133 ms |
| 5 | FINE | 167 ms |
| 6 | FINE | 200 ms |
| 7 | SAFE | 233 ms |
| 8 | SAFE | 267 ms |
| 9 | SAD | 300 ms |
| 10 | SAD | 333 ms |

## 4.2 延后判定表

`s_tblNoteNormal_Back`：

| 延后 tick | 判定 | 约时间 |
|---:|---|---:|
| 0 | COOL | 0 ms |
| 1 | COOL | 33 ms |
| 2 | COOL | 67 ms |
| 3 | COOL | 100 ms |
| 4 | FINE | 133 ms |
| 5 | FINE | 167 ms |
| 6 | FINE | 200 ms |
| 7 | FINE | 233 ms |
| 8 | SAFE | 267 ms |
| 9 | SAFE | 300 ms |
| 10 | SAD | 333 ms |

### 非对称性

**[确认]**

晚按比早按多给约 1 tick 的宽容：

```text
提前 COOL：0~2
延后 COOL：0~3

提前 FINE：3~6
延后 FINE：4~7

提前 SAFE：7~8
延后 SAFE：8~9
```

这是非常明显的触屏输入补偿设计。

---

# 5. TouchDown / TouchUp 合并规则

普通 Flick Note 并不是只在一个触摸时刻判断。

`-[NoteNormal_checkResult::::]` 同时计算：

```text
JustFrame - TouchDownFrame
JustFrame - TouchUpFrame
```

两者都会查普通 Note 的 Front / Back 判定表。

## 5.1 基本组合逻辑

**[确认]**

当 TouchDown 和 TouchUp 都处于有效判定范围时，系统通常会取两者中较差的判定：

```text
TouchDown 判定
TouchUp 判定
       ↓
取较差者
```

但存在针对“提前按住再 Flick”的特殊修正。

## 5.2 提前按住的容错

如果 TouchDown 提前，并且组合出来的结果低于 SAFE：

```c
if (result < SAFE && TouchDown 在 JustFrame 之前)
    result = SAFE;
```

另外，如果 TouchDown 已经远早于正常窗口，但 TouchUp 时机仍然有效：

```text
最终结果最高被限制到 SAFE
```

### 设计意义

**[高置信推断]**

这允许玩家：

```text
提前把手指放到屏幕上
↓
等待节奏点
↓
在正确时机完成 Flick / 抬手
```

但这种输入方式不能轻易拿到 FINE / COOL。

这是一套明显为触摸 Flick 操作设计的“预触摸容错”。

---

# 6. Flick 方向与 BoardType

## 6.1 Flick 方向错误

代码比较：

```text
m_FlickResult
与
本次输入期望 Flick 方向
```

若方向不一致：

```text
最高判定被限制为 SAFE（3）
```

因此方向错不会得到 FINE / COOL。

## 6.2 BoardType 不匹配

如果 Note 的 `m_BoardType` 与输入 Board 不一致：

```text
result = SAD（2）
```

这是一个直接降级路径。

## 6.3 BTL 特殊行为

在 `Difficulty == 4`（Break The Limit）时，普通判定函数存在特殊分支：

```c
if (difficulty == 4) {
    if (result == SAD)
        result = 0;
}
```

并且这一分支不会调用普通的：

```text
NoteManager_AddTensionGauge
```

同时，普通难度下失误会执行的 `ResetCombo()`，在 BTL 分支中也被跳过。

### 当前结论

**[确认代码行为 / 未完成玩法解释]**

BTL 明显不是普通五难度机制的简单数值增强，而是对：

```text
Gauge
SAD
Combo Reset
```

有独立处理。

具体 BTL 完整玩法尚未继续追踪。

---

# 7. WORST 与 Note 生命周期

`NoteNormal_exec` 中，Note 会根据 `m_JustFrame` 判断是否处于判定区域。

普通难度：

```text
InsideJudge：
JustFrame - 11
到
JustFrame + 11 附近
```

但判定表实际只给出了 `0~10 tick` 的正常判定结果。

因此边缘存在 1 tick 的“缓冲/无有效判定”区域。

## 7.1 自动 WORST

普通难度在：

```text
m_Cnt >= JustFrame + 12
```

之后，Note 自动失活，并记录：

```text
WORST
Gauge 惩罚
ResetCombo
失败特效
```

约等于：

```text
晚 12 tick ≈ 400 ms
```

## 7.2 Break The Limit

数据表：

```text
s_tblDifficultEndTimeOfs
```

内容：

| 难度 | Offset |
|---|---:|
| Easy | 0 |
| Normal | 0 |
| Hard | 0 |
| Extreme | 0 |
| Break The Limit | -2 |

因此 BTL 的 Note 生命周期尾端缩短约：

```text
2 tick ≈ 66.7 ms
```

---

# 8. 基础得分

数据表：

```text
s_tblAddScore @ 0x001394E4
```

主要判定组：

| 判定 | 基础 Stage Score |
|---|---:|
| 无有效判定 | 0 |
| WORST | 0 |
| SAD | 30 |
| SAFE | 50 |
| FINE | 150 |
| COOL | 300 |

因此：

```text
COOL = 300
FINE = 150
SAFE = 50
SAD  = 30
WORST = 0
```

## 8.1 第二组分数

表中还存在第二组：

```text
0, 0, 30, 50, 150, 250
```

该组通过 `local_28` 分支选择。

当前已追踪到的普通 Flick 方向错误路径同时会把结果最高限制到 SAFE，因此第二组中的高档 `150/250` 在当前已观察路径中没有正常发挥。

**[未完成]**

这部分可能存在其他调用情形或历史遗留逻辑，暂不强行解释。

---

# 9. Combo

## 9.1 续 Combo 条件

**[确认]**

```text
COOL / FINE → AddCombo
SAFE / SAD / WORST → ResetCombo
```

即：

```text
result >= 4 → 续 Combo
result < 4  → 断 Combo
```

普通难度中成立。

BTL 在该函数中跳过了正常的 ResetCombo 分支。

## 9.2 Max Combo

每次 Combo 增长后：

```text
如果当前 Combo > MaxCombo
→ 更新 MaxCombo
```

结果画面也会读取 `GetMaxCombo()`。

---

# 10. Combo Bonus 公式

在成功续 Combo 后，游戏会计算额外 Combo Score。

反编译中的 magic-number 除法等价于：

```text
floor((Combo + 5) / 10) × 50
```

并且：

```text
最大 500 分
```

因此大致表现为：

| 当前 Combo | 单次 Combo Bonus |
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
| ≥95 | 500 |

该 Bonus 被累计进：

```text
TmpComboScore
```

结果画面总分使用：

```text
TmpStageScore + TmpComboScore
```

---

# 11. Tension Gauge

相关数据：

```text
s_tblTensionGauge @ 0x00138F4C
DAT_00163088       当前 Gauge
```

## 11.1 初始值与上限

初始化函数：

```text
+[NoteManager_Initialize]
```

中：

```c
DAT_00163088 = 0x43000000;
```

`0x43000000` 作为 float：

```text
128.0
```

而 `AddTensionGauge` 中最大值：

```text
0x43800000 = 256.0
```

所以：

```text
初始 Gauge = 128
最大 Gauge = 256
开局 = 50%
```

这与实际游戏 UI 开局显示半管一致。

---

# 12. Gauge 判定权重

`s_tblTensionGauge`：

| 判定 | 权重 |
|---|---:|
| 无有效判定 | 0 |
| WORST | -10 |
| SAD | -5 |
| SAFE | 0 |
| FINE | +2 |
| COOL | +2 |

但实际 Gauge 变化不是直接加减这些整数。

## 12.1 谱面长度归一化

`+[NoteManager_AddTensionGauge:]` 会根据总 Note 数计算系数：

```text
GaugeCoefficient ≈ 64 / TotalNotes + 0.01
```

实际变化：

```text
Gauge += JudgeWeight × GaugeCoefficient
```

然后上限 clamp 到：

```text
256
```

因此：

```text
COOL  +2 × coefficient
FINE  +2 × coefficient
SAFE   0
SAD   -5 × coefficient
WORST -10 × coefficient
```

### 设计意义

Note 越少的谱面：

```text
单个判定对 Gauge 的影响越大
```

Note 越多的谱面：

```text
单个判定的影响会自动缩小
```

这是一个按谱面 Note 数量做生存难度归一化的设计。

---

# 13. Game Over 条件

`AddTensionGauge` 中可以确认存在两套失败条件。

## 13.1 Gauge 归零

如果：

```text
Gauge <= 0
```

则：

```c
DAT_00163088 = 0.0;
StatusData_SetGameOver(1);
SceneManager_NextScene(8);
```

也就是说：

```text
Gauge <= 0
→ Game Over
→ Gauge 强制清零
→ 切换到 Scene 8
```

## 13.2 “理论上已经不可能达到 50%”提前失败

游戏计算：

```text
成功判定数 = SAFE + FINE + COOL
剩余 Note 数 = TotalNotes - 已判定 Note 数
```

然后估算：

```text
(成功判定数 + 剩余 Note 数) / TotalNotes
```

这代表：

> 假设从现在开始剩下的 Note 全部至少打到 SAFE，理论上最高还能达到多少成功率。

如果该比例：

```text
< 50%
```

则立即 Game Over。

因此即使 Gauge 还有剩余，只要：

```text
数学上已经不可能达到 50% 的 SAFE-or-better
```

也会提前结束游戏。

---

# 14. Gauge 与 BGM 音量联动

Gauge 不只影响生存，还直接控制主音频音量。

代码等价于：

```text
volumeFactor = min(1.0, Gauge / 128 + 0.35)
```

然后：

```text
MainAudioVolume = 用户 BGM 音量 × volumeFactor
```

因此：

- Gauge 高时：音量保持 100%
- Gauge 越低：BGM 越弱
- Gauge 接近 0 时：约剩 35% 基础倍率
- 进入 Game Over 后 Gauge 被强制清零

这是一个非常典型的“危险状态音频反馈”。

---

# 15. Crimax 系统

Crimax 不是单纯全局开关，而是通过谱面 CuePoint 给特定 Note 打标记。

入口：

```text
CuePointFunc_Crimax
```

## 15.1 CuePoint 按难度读取开关

逻辑：

```text
difficulty = GetDifficulty()

取 CuePoint 字符串中：
[difficulty + 1] 的一个字符
↓
intValue
```

若该字符非 0：

```text
GetLastCrimaxEnableNote()
↓
setCrimaxMode(1)
```

因此同一个 Crimax CuePoint 可以针对：

```text
Easy
Normal
Hard
Extreme
BTL
```

分别指定是否生效。

---

# 16. Crimax 目标 Note 选择

`+[NoteManager_GetLastCrimaxEnableNote]`：

```text
从当前 Note 列表末尾开始
↓
最多向前检查 4 个 Note
↓
第一个 isCrimaxEnable == 1 的 Note
↓
返回
```

因此 CuePoint 不要求与目标 Note 精确一一对齐，而是允许在最近 4 个 Note 内寻找目标。

## 16.1 isCrimaxEnable

`-[NoteNormal_isCrimaxEnable]` 实际上只看：

```text
m_OptCharIdx < 0
```

即：

```text
m_OptCharIdx < 0  → 可 Crimax
m_OptCharIdx >= 0 → 不可 Crimax
```

---

# 17. Crimax 的 Rainbow 效果

数据表：

```text
s_tblRainbow @ 0x00139310
```

长度：

```text
84 个 float
= 28 组 RGB
= 每组 3 × float32
```

颜色范围使用：

```text
0~255
```

渲染时再除以：

```text
255.0
```

转换成 OpenGL/渲染使用的 `0.0~1.0`。

## 17.1 Rainbow 触发条件

`-[NoteNormal_render]` 中明确要求同时满足：

```text
m_OptCharIdx < 0
m_Active != 0
m_CrimaxMode != 0
Combo >= 100
```

才进入彩虹渲染。

否则走普通 Note 渲染。

## 17.2 Rainbow 索引

索引等价于：

```text
(m_CrimaxCnt + 10) % 28
```

每组 RGB 占：

```text
12 bytes
```

`m_CrimaxCnt` 在 Note 更新中循环：

```text
0~27
```

因此 Note 会在 28 色表中持续轮转。

### 结论

Crimax Rainbow 不是普通装饰，而是：

```text
Crimax 标记
+
Note Active
+
Combo ≥ 100
↓
彩虹 Note
```

它是 100 Combo 以上 Crimax 奖励状态的直接视觉提示。

---

# 18. Crimax 额外得分

在普通 Note 判定成功后：

```text
m_CrimaxMode != 0
且
result > 4
```

由于判定最大为 5，所以这里实际上要求：

```text
COOL
```

然后再检查：

```text
Combo >= 100
```

满足后：

```text
TmpStageScore +200
```

同时触发：

```text
StartSpScoreEffect
```

因此：

```text
Crimax Note
+ COOL
+ Combo ≥ 100
= 额外 200 Stage Score
```

FINE 不触发这个额外 200 分。

---

# 19. ClearCrimax

`+[NoteManager_ClearCrimax]` 会：

```text
遍历当前所有 Note
↓
setCrimaxMode(0)
```

也就是说它不是只清一个 Note，而是全局清除当前 Note 集合中的 Crimax 标记。

**[未完成]**

目前尚未可靠定位真正调用 `ClearCrimax` 的游戏逻辑位置。Ghidra 给出的一个直接 XREF 已确认属于 CRI Atom 区域的假引用。

因此：

```text
Crimax 如何在完整流程中结束
```

尚未继续深挖。

---

# 20. Interlude：间奏小游戏

Interlude 已确认是游戏中的“间奏单键小游戏”。

CuePoint 入口：

```text
CuePointFunc_Interlude
```

它与 Crimax 类似，也会：

```text
读取当前 Difficulty
↓
从 CuePoint 字符串中取 difficulty + 1 位置的字符
↓
转成 int
↓
通过函数表分发
```

## 20.1 Interlude 类型表

```text
s_tblInterludeType
```

内容：

| Type | 函数 |
|---:|---|
| 0 | `InterludeType_None` |
| 1 | `InterludeType_Normal` |
| 2 | `InterludeType_FadeOut` |

---

# 21. Interlude 开始与结束

## 21.1 Normal

`InterludeType_Normal()`：

```c
WindowManager_StartInterludeMode();
NoteManager_AddNote::::(1, 0, 1, 0);
```

也就是：

```text
进入 Interlude Mode
↓
生成一个 NoteInterlude
```

## 21.2 FadeOut

`InterludeType_FadeOut()`：

```c
WindowManager_EndInterludeMode();
```

所以该类型实际上用于结束 Interlude 段。

---

# 22. NoteInterlude 判定

`NoteInterlude` 拥有完整的：

```text
exec
render
setTouchDown
setTouchUp
checkResult::::
isJustFrame
```

但它不是 Flick 方向玩法，而是单键时机输入。

## 22.1 时间窗

`NoteInterlude_checkResult::::` 直接复用：

```text
s_tblNoteNormal_Front
s_tblNoteNormal_Back
```

因此时间精度与普通 Note 相同：

```text
30 Hz tick
COOL / FINE / SAFE / SAD
```

## 22.2 成功条件

真正计为 Interlude 成功：

```text
result > 3
```

即：

```text
FINE
或
COOL
```

SAFE / SAD 不计成功。

这符合实际玩法：

> 间奏里只出现一个键，玩家按节奏点按音符即可。

---

# 23. Interlude 得分

每次 Interlude 成功：

```text
TmpInterludeCnt +1
TotalInterludeSuccess +1
TmpStageScore +1
```

如果当前歌曲 / 难度下：

```text
TmpInterludeCnt >= TotalInterlude
```

也就是所有 Interlude 全成功，则追加：

```text
TmpStageScore +39
```

并：

```text
播放特殊音效
StartSpScoreEffect(39)
EffectManager_AddEffect2D(..., 7, ...)
```

因此最后一个 Interlude 成功时：

```text
该次基础 +1
全成功奖励 +39
总计 +40
```

---

# 24. 难度枚举

结果界面已经确认：

| 内部值 | 难度 |
|---:|---|
| 0 | Easy |
| 1 | Normal |
| 2 | Hard |
| 3 | Extreme |
| 4 | Break The Limit |

BTL 在普通 Note 判定、Gauge、Combo Reset、Note 生命周期尾窗中均存在特殊逻辑。

---

# 25. 结算与 Clear Rank

结果界面会读取：

```text
Total Score
Stage Score
Combo Bonus
Max Combo
Total Notes
Cool
Fine
Safe
Sad
Worst
Interlude
Difficulty
```

总分：

```text
TmpStageScore + TmpComboScore
```

## 25.1 Rank 初步规则

当前已经看到结果界面利用：

```text
COOL + FINE + SAFE
```

与 `TotalNotes` 的比例进行 Rank / Clear 判定。

代码中明确出现：

```text
70%
80%
95%
100%
```

等阈值。

此外：

```text
GetMaxCombo() == TotalNotes
```

时：

```text
SetPerfectClear(...)
```

**[未完成]**

当前尚未完整整理所有 Rank 数值 `0~6` 与游戏界面具体称呼的映射，因此暂不在本文强行命名。

---

# 26. 当前可用于现代化重构的简化模型

如果目标不是 1:1 恢复所有旧代码，而是做 64 位现代化版本，目前已经足够把核心逻辑压缩成下面这个模型。

## 26.1 Timing

```text
playTick = ceil(audioPlayTimeSeconds × 30)
noteTick = playTick - note.baseTime
```

## 26.2 Judge

```text
读取 TouchDown / TouchUp tick
↓
查 Front / Back 判定表
↓
合并两个时间判定
↓
应用提前按住修正
↓
检查 Flick 方向
↓
检查 BoardType
↓
得到 0~5 判定枚举
```

## 26.3 Result

```text
5 COOL
4 FINE
3 SAFE
2 SAD
1 WORST
0 INVALID / NONE
```

## 26.4 Combo

```text
COOL/FINE → combo++
SAFE/SAD/WORST → combo reset
```

BTL 除外。

## 26.5 Score

```text
COOL 300
FINE 150
SAFE 50
SAD 30
WORST 0

+ Combo Bonus
+ Crimax Bonus
+ Interlude Bonus
```

## 26.6 Gauge

```text
Start = 128
Max = 256

weight:
COOL  +2
FINE  +2
SAFE   0
SAD   -5
WORST -10

coefficient = 64 / TotalNotes + 0.01
```

## 26.7 Fail

```text
Gauge <= 0
OR
理论最高 SAFE-or-better 成功率 < 50%
→ Game Over
```

## 26.8 Crimax

```text
CuePoint
↓
最近 4 个可 Crimax Note
↓
m_CrimaxMode = 1
↓
Combo >= 100
↓
Rainbow

如果同时 COOL：
+200 Stage Score
```

## 26.9 Interlude

```text
Interlude Cue
↓
StartInterludeMode
↓
生成 NoteInterlude
↓
单键时机输入
↓
COOL/FINE 成功
↓
每个 +1
↓
全部成功额外 +39
```

---

# 27. 当前尚未继续研究的部分

以下内容目前有入口，但尚未继续完整逆向：

- BTL 完整规则
- Clear Rank 的名称与完整阈值映射
- `ClearCrimax` 的真实调用时机
- 第二套 `s_tblNoteNormal_Front / Back` 的用途
- `s_tblAddScore` 第二组高档分数的实际可达路径
- Replay 对判定结果的具体回放方式
- `NoteThrow`
- `NoteArrow`
- `NoteWait`
- `NoteInterlude.exec`
- StageManager 的完整状态机
- WindowGameWindow HUD 渲染细节
- Telop / SmallTelop
- Lyrics
- FadeIn / FadeOut
- SetBPM / SetDelay
- 谱面文件格式及 Note 生成格式
- TouchManager 的完整 Flick 手势识别算法
- CRI 音视频与谱面同步的完整校正逻辑

---

# 28. 已确认的重要 Ghidra 符号速查

```text
SceneGame_Exec
NoteManager_exec
NoteNormal_exec
NoteNormal_checkResult::::
NoteNormal_render
NoteNormal_isCrimaxEnable
NoteObjBase_isInsideJudgeFrame
NoteObjBase_setCrimaxMode:
MikuFlickCriManager_Exec
MikuFlickCriManager_GetPlayCnt
CriManager::GetPlayTime
CriMvEasyPlayer::GetTime
StatusData_AddFlickTypeNum:
NoteManager_AddTensionGauge:
NoteManager_GetLastCrimaxEnableNote
NoteManager_ClearCrimax
CuePointFunc_Crimax
CuePointFunc_Interlude
InterludeType_Normal
InterludeType_FadeOut
NoteInterlude_checkResult::::
WindowResult_loadTexture
```

关键表：

```text
s_tblTensionGauge          @ 0x00138F4C
s_tblDifficultEndTimeOfs   @ 0x001392FC
s_tblRainbow               @ 0x00139310
s_tblNoteNormal_Front      @ 0x00139488
s_tblNoteNormal_Back       @ 0x001394B4
s_tblAddScore              @ 0x001394E4
```

关键全局：

```text
DAT_00163088 → Tension Gauge
DAT_00164340 → CRI-derived PlayCnt
```

---

# 29. 总结

MikuFlick2 的核心机制可以概括为：

```text
CRI 音频时钟
↓
30 Hz 逻辑 tick
↓
TouchDown / TouchUp 双时间点判定
↓
Flick 方向与 Board 区域修正
↓
COOL / FINE / SAFE / SAD / WORST
↓
Score + Combo + Gauge
↓
Crimax / Interlude 等特殊机制
```

它的判定粒度以今天的音游标准看很粗，但结构并不草率。

相反，当前逆向结果显示它专门处理了：

- 音频时钟同步
- 早按与晚按非对称容错
- 提前按住再 Flick 的触屏行为
- Flick 方向错误降级
- 谱面长度对 Gauge 的归一化
- Gauge 与 BGM 音量联动
- 数学上已无法 Clear 时的提前失败
- Crimax 100 Combo 彩虹反馈
- 间奏单键 Bonus Game

对于 2012 年触屏 Flick 音游而言，这是一套明显经过实际手感调校的系统，而不是简单的“时间差查表”。

---

*整理时间：2026-10-05*  
*样本：MikuFlick2 1.1.5 / ARMv7 / cryptid 0*  
*状态：持续逆向中*

### 9. 格式与工具参考

- [CRI 官方 Sofdec 编码器文档：多音轨与 cuepoint](https://game.criware.jp/manual/native/sofdec2/latest/usr_console_encoder_main.html)
- [PyCriCodecsEx：USM 区块定义](https://mos9527.com/PyCriCodecsEx/_modules/PyCriCodecsEx/chunk.html)
- [PyCriCodecsEx：UTF 表解析](https://mos9527.com/PyCriCodecsEx/_modules/PyCriCodecsEx/utf.html)
- [CriStudio / CriCodecs](https://github.com/Youjose/CriCodecs)
- [HxD](https://mh-nexus.de/en/hxd/) · [Hex Fiend](https://hexfiend.com/)

参考资料用于理解通用容器格式。本文的样本统计、参数与注册字段来自实际文件解析；游戏行为来自维护者的操作反馈与 EASY 单字节修改实测。其余方向 / 时间修改、特殊事件语义与自制包方案已分别标为待验证，不应当作完整格式规范。
