# 资源、文件与操作映射

本轮针对一个`.app`样本统计195个文件（包括3个AppleDouble附属文件）；165项用途得到静态确认，21项仅内容确认、具体触发待查，另9项触发待查。确认具体用途不等于已验证所有运行路径，一个文件也可以服务多个按钮。

完整机器可读记录：[`file_mapping.json`](data/file_mapping.json)。它只提供文件名、大小、用途、确认程度和定位证据；引用图片内容的观察均来自本地原件，本仓库附450张研究用切图，不包含音频、MV、IPA、Ghidra含二进制的工程或整首歌词/谱面。

## 1. ending三个文件的关系

| 文件 | 内容与用途 | 关键证据 |
|---|---|---|
| `ending.usm` | 320×480 MPEG-1视频，20fps、162帧约8.1s；一条44.1kHz双声道ADX音轨；无歌词/谱面CUE表 | 完整容器块扫描；`WindowPreEnding init @0x79d18`加载 |
| `ending.png` | 1024×1024图集画布，包含640×960的结尾背景区域 | plist的frames/metadata与本地图像 |
| `ending.plist` | 图集布局索引：逻辑frame、裁切矩形、尺寸/偏移和纹理元数据；不是电影或歌词文件 | `TPManager init @0x3051c`解析图集布局 |

`ending.usm`是结尾前的短演出，后续滚动名单由`WindowEnding init @0x38940`遍历主程序`_s_tbl_Ending @0x1413b8`的76项记录，使用TexTextManager动态绘制，配合ending背景和BGM04。名单文本不是藏在ending视频的独立字幕轨里。

## 2. Crypton / SEGA文字定位

- 主程序结尾表含公司名和版权行：Crypton Future Media, INC.、SEGA Corporation、© SEGA、© Crypton Future Media, INC.，以及piapro网址。
- `UI_tex_05`内的`copyright.png`也是版权文字资源；不能把atlas小图名当作包内独立PNG。
- `logo_sega.png` / `logo_crypton.png`由标题加载流程使用。
- `credits_en.png` / `credits_ja.png`用于OPTIONS → CREDITS页面，和结尾动态滚动名单不同。

## 3. 图集与plist

程序注册21个布局表、450个frame名称，PNG既可能为图集也可能是独立图片。程序按frame编号取矩形，再从所选纹理渲染。plist被使用与同名PNG被使用是两条不同证据，尤其是动态商店缩略图。

完整注册名称见[`texture_name_tables.json`](data/texture_name_tables.json)。`music_00_01`等为歌曲表提供的封面名；歌曲映射见[`song_mapping.json`](data/song_mapping.json)。

## 4. 音效、选曲试听与两条歌曲音轨

本地12个USM：11首歌曲各含一路视频、两条ADX音轨及CUE；ending只含一路视频、一条音轨。双轨结构与原唱/伴奏切换相符，但轨道角色需结合音量控制和实际试听识别，源文件名不是通用角色标签。

30项SoundManager注册表见[`sound_table.json`](data/sound_table.json)。11个独立预览ADX由MusicData的`PreSoundFileName`供选曲试听读取。转换出的42个MP3只是本地试听交付，没有作为原始音频上传。

| 触发 | 音效 | 代码定位 |
|---|---|---|
| SAD，且失败音关闭标志未开启 | `SE03.caf`，ID2 | `NoteNormal checkResult @0x22e10`，共享Play调用`0x23282` |
| SAFE | `SE01_03.caf`，ID18 | 同上 |
| FINE或普通COOL | `SE02.caf`，ID1 | 同上 |
| Crimax COOL，续连后Combo≥100 | `SE01.caf`，ID0 | 同上，另加200分 |
| 间奏FINE/COOL | `SE04.caf`，ID3 | `NoteInterlude checkResult @0x2ffdc` |
| 全部间奏成功 | `SE02.caf`，ID1 | 同上，额外39分 |
| Perfect结算 | `SE14.caf`，ID13 | `WindowResult exec @0x4d6ac` |
| S/A结算 | `SE13.caf`，ID12 | 同上 |
| B/C/D结算 | `SE12.caf`，ID11 | 同上 |
| E/GameOver结算 | `SE11.caf`，ID10 | 同上 |
| 新纪录提示 | `SE05_01.caf` | `setHighScoreMode` |

分支会共享调用地址。不能只用线性“最近一次r2赋值”确定声音ID；应检查控制流前驱。未定位到播放触发不证明资源从未使用或可以删除。

## 5. 动态DLC封面与商店缩略图

- `ExPackManager Load @0x60fa8`从`ShopList_enc.txt`读取商店数据，封面名来自`%03d_%03d_ArtWorkFileName`。
- `CoverTexUnit fncLoadTexture @0x3f668`按MusicData传入的名称查找PNG。
- 商店缓存路径由`GetThumFilePath @0x62518`生成：`GetInstallPath()/Thum_<PackID>/thum_<PackID>.png`。
- `LoadThumTex @0x60c78`检查缓存，缺失时下载，再加载`m_ThumTex`。
- `WindowPackage RenderInfo @0x16580`使用frame445～447；矩形来自`thum_01_01.plist`，纹理来自曲包缓存。

因此不能仅凭`thum_01_01.plist`在注册表里就断言包内`thum_01_01.png`一定用于商店。当前.app没有完整商店配置和设备缓存，四张附加曲包PNG的具体选择仍待确认。

## 6. Twitter与Shuffle

`SA_OAuthTwitterController loadView @0x86bf4`明确把`twitter_load.png`用作OAuth登录背景。这是历史客户端代码用途，不等于该服务如今仍可用。

用户提供按钮截图并指认其为Shuffle、随机选曲；截图视觉匹配`replay_on.png`（frame80）；资源名replay与用户确认的随机选曲作用分别保留，其具体调用仍待核。另有独立静态证据：`TouchPVLoopMode update @0x717e0`的模式3使用`shuffle_off/on`（frame86/87），模式2使用`loop_off/on`（48/49）。`GotoNextPV @0x29678`读取flag3后随机起点，再循环寻找播放列表中的可用未播放条目；这不构成均匀随机抽样的证明。

## 7. 具体触发待确认的30项

| 文件 | 已知内容/用途 | 确认程度 |
|---|---|---|
| `Appleicon_miku_100x100_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_1024x1024_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_114x114_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_120x120_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_144x144_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_152x152_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_29x29_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_40x40_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_50x50_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_512x512_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_57x57_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_58x58_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_60x60_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_72x72_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_76x76_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_80x80_Flatdesign.png` | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `BGM02.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE01_01.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE04_01.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE05.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE07.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE08.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE10.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE15.caf` | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE16.caf` | 包内音效；未出现在已恢复的30项 SoundManager 文件表中 | 触发待确认 |
| `music_01_01.png` | 附加曲包封面和曲名图集，画面包含：カラフル×セクシィ、ジェミニ（Gemini）、カンタレラ。封面用途明确；该具体文件是否被当前商店配置选中仍待确认 | 内容确认，触发待确认 |
| `music_02_01.png` | 附加曲包封面和曲名图集，画面包含：カラフル×メロディ、Yellow、こっち向いて Baby。封面用途明确；该具体文件是否被当前商店配置选中仍待确认 | 内容确认，触发待确认 |
| `saisei.png` | 灰色播放按钮图像；具体加载调用未定位 | 内容确认，触发待确认 |
| `thum_01_01.png` | 与附加曲包商店缩略图布局相符的图集，内容对应 カラフル×セクシィ、ジェミニ、カンタレラ。目前实际加载链使用缓存文件，尚不能确认本包PNG被直接使用 | 内容确认，触发待确认 |
| `thum_02_01.png` | 与附加曲包商店缩略图布局相符的图集，内容对应 カラフル×メロディ、Yellow、こっち向いて Baby。目前实际加载链使用缓存文件，尚不能确认本包PNG被直接使用 | 内容确认，触发待确认 |

## 8. 195项逐文件清单

这里按包内相对路径列出；逐条地址、引用和细化证据见JSON。文件大小和重复副本是样本观察，不能自动推广到其他IPA版本。

| 文件 | 区域 | 用途 | 证据程度 |
|---|---|---|---|
| `._BGM01.caf` | 辅助元数据 | macOS AppleDouble 附属元数据；对应同名 CAF 文件 | 确认 |
| `._BGM02.caf` | 辅助元数据 | macOS AppleDouble 附属元数据；对应同名 CAF 文件 | 确认 |
| `._BGM03.caf` | 辅助元数据 | macOS AppleDouble 附属元数据；对应同名 CAF 文件 | 确认 |
| `AppIcon29x29.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon29x29@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon29x29@2x~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon29x29~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon40x40@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon40x40@2x~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon40x40~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon50x50@2x~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon50x50~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon57x57.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon57x57@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon60x60@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon72x72@2x~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon72x72~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon76x76@2x~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `AppIcon76x76~ipad.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Appleicon_miku_100x100_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_1024x1024_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_114x114_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_120x120_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_144x144_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_152x152_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_29x29_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_40x40_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_50x50_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_512x512_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_57x57_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_58x58_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_60x60_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_72x72_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_76x76_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `Appleicon_miku_80x80_Flatdesign.png` | 应用图标 | 初音应用图标的设计导出尺寸版本 | 内容确认，触发待确认 |
| `BGM01.caf` | 音效/背景音乐 | 标题页背景音乐 | 确认 |
| `BGM02.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `BGM03.caf` | 音效/背景音乐 | 设置、成绩、记录、附加曲包界面的背景音乐 | 确认 |
| `BGM04.caf` | 音效/背景音乐 | 结尾滚动名单背景音乐 | 确认 |
| `BGM05.caf` | 音效/背景音乐 | 游戏结算界面背景音乐 | 确认 |
| `DebugViewController.nib` | 原生界面 | 调试视图：跳过、输入模式、回放/录制/双人模式等按钮和开关；常规用户流程是否可进入待确认 | 确认 |
| `Icon-72.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Icon-Small-50.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Icon-Small.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Icon-Small@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Icon.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Icon@2x.png` | 应用图标 | iOS桌面/设置/系统使用的应用图标变体 | 确认 |
| `Info.plist` | 应用配置 | 应用启动入口、版本、Bundle ID、最低iOS、图标、启动图、设备与显示方向配置 | 确认 |
| `J01_01.caf` | 音效/背景音乐 | 解锁通知执行时的提示音 | 确认 |
| `Just_be_friends.usm` | 歌曲/PV | 《Just Be Friends》游戏/PV资源：一条视频、两条ADX音轨、734条谱面/歌词事件 | 确认 |
| `LaunchImage-568h@2x.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `LaunchImage-700-568h@2x.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `LaunchImage-700-Portrait~ipad.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `LaunchImage-700@2x.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `LaunchImage-Portrait~ipad.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `LaunchImage@2x.png` | 启动 | iOS启动时显示的静态加载画面；对应不同分辨率/设备/iOS配置 | 确认 |
| `MikuFlick2` | 程序 | ARMv7 主程序：场景切换、按钮操作、音效、11首预装曲表、76项结尾名单、谱面指令处理 | 确认 |
| `MikuFlick2ViewController-4inch.nib` | 原生界面 | 4英寸iPhone主视图布局 | 确认 |
| `MikuFlick2ViewController-iPad.nib/objects-8.0+.nib` | 原生界面 | iPad主视图布局，含EAGLView、topImage、topMask和ipad_top.png；objects/runtime为归档变体 | 确认 |
| `MikuFlick2ViewController-iPad.nib/objects.nib` | 原生界面 | iPad主视图布局，含EAGLView、topImage、topMask和ipad_top.png；objects/runtime为归档变体 | 确认 |
| `MikuFlick2ViewController-iPad.nib/runtime.nib` | 原生界面 | iPad主视图布局，含EAGLView、topImage、topMask和ipad_top.png；objects/runtime为归档变体 | 确认 |
| `MikuFlick2ViewController.nib` | 原生界面 | 原生 EAGLView 和加载指示器的界面布局 | 确认 |
| `MusicSelect.caf` | 音效/背景音乐 | 切换选曲标题、切换记录文字区域的反馈 | 确认 |
| `Na_SEGA_09_keep.caf` | 音效/背景音乐 | 标题/启动流程中的 SEGA 语音资源 | 确认 |
| `Na_Title_A_03_keep.caf` | 音效/背景音乐 | 标题/启动流程中的标题语音资源 | 确认 |
| `NoahSDK1.5.1.txt` | SDK辅助 | 空的Noah SDK版本/打包标记文件 | 确认 |
| `PkgInfo` | 应用配置 | 应用包类型APPL及签名标识 | 确认 |
| `ResourceRules.plist` | 签名配置 | 应用签名时的资源处理规则 | 确认 |
| `SE01.caf` | 音效/背景音乐 | 高潮段 COOL 奖励反馈：CrimaxMode开启、combo≥100且判定为COOL时，增加200奖励分并播放 | 确认 |
| `SE01_01.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE01_03.caf` | 音效/背景音乐 | SAFE 判定音效；结果编号3选择声音编号18 | 确认 |
| `SE02.caf` | 音效/背景音乐 | FINE 与普通 COOL 判定反馈；全部间奏输入成功时也用于39分奖励提示 | 确认 |
| `SE02_01.caf` | 音效/背景音乐 | 共用点击/确认音：开始、暂停、重试、返回菜单、难度、键盘、商店等大量按钮 | 确认 |
| `SE03.caf` | 音效/背景音乐 | SAD 判定/输入失败反馈；IsDisableFailSound 为真时跳过播放 | 确认 |
| `SE04.caf` | 音效/背景音乐 | 间奏输入成功音效：间奏判定结果>3时播放编号3 | 确认 |
| `SE04_01.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE04v2.caf` | 音效/背景音乐 | WindowCounter 计数显示激活时播放的循环音效 | 确认 |
| `SE05.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE05_01.caf` | 音效/背景音乐 | 结算切换到最高分/新纪录模式时的提示音 | 确认 |
| `SE06.caf` | 音效/背景音乐 | 弹出确认对话框的提示音 | 确认 |
| `SE07.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE08.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE09.caf` | 音效/背景音乐 | 返回按钮、记录页面不可选/边界等反馈 | 确认 |
| `SE10.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE11.caf` | 音效/背景音乐 | 结算评级 E / Game Over 的音效：计分动画结束后播放 | 确认 |
| `SE12.caf` | 音效/背景音乐 | 结算评级 B / C / D 的音效：计分动画结束后播放 | 确认 |
| `SE13.caf` | 音效/背景音乐 | 结算评级 S / A 的音效：计分动画结束后播放 | 确认 |
| `SE14.caf` | 音效/背景音乐 | 结算评级 Perfect 的音效：计分动画结束后播放 | 确认 |
| `SE15.caf` | 音效/背景音乐 | 已注册的音频资源，当前未定位到明确的播放触发 | 触发待确认 |
| `SE16.caf` | 音效/背景音乐 | 包内音效；未出现在已恢复的30项 SoundManager 文件表中 | 触发待确认 |
| `UI_tex_01.plist` | 图集索引 | UI_tex_01.png 的裁切索引，共101张sprite | 确认 |
| `UI_tex_01.png` | 界面图集 | 标题、选曲、难度选择、PV播放设置等共用按钮和装饰 | 确认 |
| `UI_tex_02.plist` | 图集索引 | UI_tex_02.png 的裁切索引，共69张sprite | 确认 |
| `UI_tex_02.png` | 界面图集 | 结算、评级、分数、回放、解锁通知等界面部件 | 确认 |
| `UI_tex_03.plist` | 图集索引 | UI_tex_03.png 的裁切索引，共13张sprite | 确认 |
| `UI_tex_03.png` | 界面图集 | 音量调节与左右手操作设置 | 确认 |
| `UI_tex_04.plist` | 图集索引 | UI_tex_04.png 的裁切索引，共16张sprite | 确认 |
| `UI_tex_04.png` | 界面图集 | 键盘类型、输入面板引导和花朵效果设置 | 确认 |
| `UI_tex_05.plist` | 图集索引 | UI_tex_05.png 的裁切索引，共12张sprite | 确认 |
| `UI_tex_05.png` | 界面图集 | 标题页初音立绘、游戏标志、装饰及版权文字 | 确认 |
| `UI_tex_06.plist` | 图集索引 | UI_tex_06.png 的裁切索引，共39张sprite | 确认 |
| `UI_tex_06.png` | 界面图集 | 附加曲包商店、详情、安装/删除/重新安装、管理、曲包署名 | 确认 |
| `UI_tex_07.plist` | 图集索引 | UI_tex_07.png 的裁切索引，共12张sprite | 确认 |
| `UI_tex_07.png` | 界面图集 | 下载与恢复购买进度窗口 | 确认 |
| `UI_tex_08.png` | 界面图集 | BREAK THE LIMIT 解锁通知 | 确认 |
| `UI_tex_09.png` | 界面图集 | 显示比例/显示方式设置的设备示意图 | 确认 |
| `_CodeSignature/CodeResources` | 签名配置 | 代码签名的资源哈希清单 | 确认 |
| `archived-expanded-entitlements.xcent` | 签名配置 | 打包时展开的应用权限/entitlements配置 | 确认 |
| `bg_tex_01.plist` | 图集索引 | bg_tex_01.png 的裁切索引，共1张sprite | 确认 |
| `bg_tex_01.png` | 场景背景 | 标题界面背景 | 确认 |
| `bg_tex_02.plist` | 图集索引 | bg_tex_02.png 的裁切索引，共2张sprite | 确认 |
| `bg_tex_02.png` | 场景背景 | 选曲界面背景及封面加载占位图 | 确认 |
| `bg_tex_03.plist` | 图集索引 | bg_tex_03.png 的裁切索引，共1张sprite | 确认 |
| `bg_tex_03.png` | 场景背景 | 成绩/记录页的 RESULT 背景 | 确认 |
| `bg_tex_04.plist` | 图集索引 | bg_tex_04.png 的裁切索引，共1张sprite | 确认 |
| `bg_tex_04.png` | 场景背景 | OPTIONS 设置页背景 | 确认 |
| `bg_tex_05.plist` | 图集索引 | bg_tex_05.png 的裁切索引，共1张sprite | 确认 |
| `bg_tex_05.png` | 场景背景 | 游戏结算 RESULTS 背景 | 确认 |
| `bg_tex_06.plist` | 图集索引 | bg_tex_06.png 的裁切索引，共1张sprite | 确认 |
| `bg_tex_06.png` | 场景背景 | 开始/加载阶段背景 | 确认 |
| `bg_tex_07.plist` | 图集索引 | bg_tex_07.png 的裁切索引，共4张sprite | 确认 |
| `bg_tex_07.png` | 场景背景 | 歌曲加载背景、初音角色和加载动画部件 | 确认 |
| `bg_tex_08.png` | 场景背景 | SceneBoot 使用的启动加载背景 | 确认 |
| `bg_tex_09.png` | 场景背景 | SceneBoot 使用的另一启动加载背景 | 确认 |
| `cloverclub.usm` | 歌曲/PV | 《クローバー・クラブ》游戏/PV资源：一条视频、两条ADX音轨、624条谱面/歌词事件 | 确认 |
| `credits_en.png` | 制作名单 | 设置 → CREDITS 的英语/日语静态制作人员名单，包含SEGA/Crypton标志 | 确认 |
| `credits_ja.plist` | 图集索引 | credits_ja.png 的裁切索引，共1张sprite | 确认 |
| `credits_ja.png` | 制作名单 | 设置 → CREDITS 的英语/日语静态制作人员名单，包含SEGA/Crypton标志 | 确认 |
| `en.lproj/InfoPlist.strings` | 本地化 | 英语本地化界面文字：帮助、设置、购买/安装提示、分享和错误消息 | 确认 |
| `en.lproj/Localizable.strings` | 本地化 | 英语本地化界面文字：帮助、设置、购买/安装提示、分享和错误消息 | 确认 |
| `ending.plist` | 图集索引 | ending.png 的裁切索引，共1张sprite | 确认 |
| `ending.png` | 结尾 | 滚动结尾名单的背景；实际名单文字由主程序动态绘制 | 确认 |
| `ending.usm` | 结尾 | 结尾前的演出剪辑视频及一条音轨；WindowPreEnding 调用 ReLoad:ending | 确认 |
| `game_effect_01.plist` | 图集索引 | game_effect_01.png 的裁切索引，共13张sprite | 确认 |
| `game_effect_01.png` | 游戏输入效果 | 输入判定效果：音符面板、箭头、烟花、涟漪等；编号为配色变体 | 确认 |
| `game_effect_02.png` | 游戏输入效果 | 输入判定效果：音符面板、箭头、烟花、涟漪等；编号为配色变体 | 确认 |
| `game_effect_03.png` | 游戏输入效果 | 输入判定效果：音符面板、箭头、烟花、涟漪等；编号为配色变体 | 确认 |
| `game_effect_04.png` | 游戏输入效果 | 输入判定效果：音符面板、箭头、烟花、涟漪等；编号为配色变体 | 确认 |
| `game_effect_05.png` | 游戏输入效果 | 输入判定效果：音符面板、箭头、烟花、涟漪等；编号为配色变体 | 确认 |
| `game_tex_01.plist` | 图集索引 | game_tex_01.png 的裁切索引，共84张sprite | 确认 |
| `game_tex_01.png` | 游戏HUD | 游戏HUD：得分、连击、判定、暂停、音符、轨道、输入方向等 | 确认 |
| `game_tex_02.plist` | 图集索引 | game_tex_02.png 的裁切索引，共66张sprite | 确认 |
| `game_tex_02.png` | 游戏键盘 | 滑动键盘/输入字符图集；original、romanhira、fullroman对应键盘显示类型 | 确认 |
| `game_tex_02_fullroman.png` | 游戏键盘 | 滑动键盘/输入字符图集；original、romanhira、fullroman对应键盘显示类型 | 确认 |
| `game_tex_02_romanhira.png` | 游戏键盘 | 滑动键盘/输入字符图集；original、romanhira、fullroman对应键盘显示类型 | 确认 |
| `hajimete_no_oto.usm` | 歌曲/PV | 《ハジメテノオト》游戏/PV资源：一条视频、两条ADX音轨、430条谱面/歌词事件 | 确认 |
| `hatsune_miku_no_gekisyou.usm` | 歌曲/PV | 《初音ミクの激唱》游戏/PV资源：一条视频、两条ADX音轨、824条谱面/歌词事件 | 确认 |
| `help_01.png` | 帮助 | 帮助页的操作示意截图图集，配合本地化帮助文字 | 确认 |
| `help_02.png` | 帮助 | 帮助页的操作示意截图图集，配合本地化帮助文字 | 确认 |
| `ipad_top.png` | 启动 | iPad 原生视图的初始加载背景 | 确认 |
| `jQueryInject.txt` | 分享 | 嵌入式Twitter OAuth登录页的排版调整JavaScript，包含登录框、allow/deny按钮布局；横屏版本命名 | 确认 |
| `jQueryInjectLandscape.txt` | 分享 | 嵌入式Twitter OAuth登录页的排版调整JavaScript，包含登录框、allow/deny按钮布局；横屏版本命名 | 确认 |
| `ja.lproj/InfoPlist.strings` | 本地化 | 日语本地化界面文字：帮助、设置、购买/安装提示、分享和错误消息 | 确认 |
| `ja.lproj/Localizable.strings` | 本地化 | 日语本地化界面文字：帮助、设置、购买/安装提示、分享和错误消息 | 确认 |
| `koi_wa_sensou.usm` | 歌曲/PV | 《恋は戦争》游戏/PV资源：一条视频、两条ADX音轨、313条谱面/歌词事件 | 确认 |
| `logo_cri.png` | 启动标志 | CRIWARE启动标志 | 确认 |
| `logo_crypton.png` | 启动标志 | Crypton启动标志 | 确认 |
| `logo_sega.png` | 启动标志 | SEGA启动标志 | 确认 |
| `magnet.usm` | 歌曲/PV | 《magnet》游戏/PV资源：一条视频、两条ADX音轨、462条谱面/歌词事件 | 确认 |
| `mf_hiragana_blank.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_hiragana_blank_fullroman.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_hiragana_blank_romanhira.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_hiragana_telop.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_hiragana_telop_fullroman.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_hiragana_telop_romanhira.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_katakana_blank.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `mf_katakana_telop.png` | 游戏字符 | 游戏输入字符字形位图；平假名/片假名及罗马字显示版本，blank/telop为绘制状态变体 | 确认 |
| `migikata_no_tyou.usm` | 歌曲/PV | 《右肩の蝶》游戏/PV资源：一条视频、两条ADX音轨、660条谱面/歌词事件 | 确认 |
| `music_00_01.plist` | 图集索引 | music_00_01.png 的裁切索引，共6张sprite | 确认 |
| `music_00_01.png` | 选曲封面 | 11首预装歌曲的封面插画、曲名与作者标识图集 | 确认 |
| `music_00_02.png` | 选曲封面 | 11首预装歌曲的封面插画、曲名与作者标识图集 | 确认 |
| `music_00_03.png` | 选曲封面 | 11首预装歌曲的封面插画、曲名与作者标识图集 | 确认 |
| `music_00_04.png` | 选曲封面 | 11首预装歌曲的封面插画、曲名与作者标识图集 | 确认 |
| `music_01_01.png` | 附加曲包 | 附加曲包封面和曲名图集，画面包含：カラフル×セクシィ、ジェミニ（Gemini）、カンタレラ。封面用途明确；该具体文件是否被当前商店配置选中仍待确认 | 内容确认，触发待确认 |
| `music_02_01.png` | 附加曲包 | 附加曲包封面和曲名图集，画面包含：カラフル×メロディ、Yellow、こっち向いて Baby。封面用途明确；该具体文件是否被当前商店配置选中仍待确认 | 内容确认，触发待确认 |
| `promise.usm` | 歌曲/PV | 《Promise》游戏/PV资源：一条视频、两条ADX音轨、457条谱面/歌词事件 | 确认 |
| `pv_001_lp.adx` | 选曲试听 | 选曲时《恋は戦争》的循环试听音频 | 确认 |
| `pv_042_lp.adx` | 选曲试听 | 选曲时《初音ミクの激唱》的循环试听音频 | 确认 |
| `pv_044_lp.adx` | 选曲试听 | 选曲时《magnet》的循环试听音频 | 确认 |
| `pv_054_lp.adx` | 选曲试听 | 选曲时《炉心融解》的循环试听音频 | 确认 |
| `pv_056_lp.adx` | 选曲试听 | 选曲时《右肩の蝶》的循环试听音频 | 确认 |
| `pv_061_lp.adx` | 选曲试听 | 选曲时《クローバー・クラブ》的循环试听音频 | 确认 |
| `pv_062_lp.adx` | 选曲试听 | 选曲时《Promise》的循环试听音频 | 确认 |
| `pv_065_lp.adx` | 选曲试听 | 选曲时《ハジメテノオト》的循环试听音频 | 确认 |
| `pv_066_lp.adx` | 选曲试听 | 选曲时《Just Be Friends》的循环试听音频 | 确认 |
| `pv_082_lp.adx` | 选曲试听 | 选曲时《裏表ラバーズ》的循环试听音频 | 确认 |
| `pv_102_lp.adx` | 选曲试听 | 选曲时《多重未来のカルテット》的循环试听音频 | 确认 |
| `roshin_yuukai.usm` | 歌曲/PV | 《炉心融解》游戏/PV资源：一条视频、两条ADX音轨、546条谱面/歌词事件 | 确认 |
| `saisei.png` | 界面图像 | 灰色播放按钮图像；具体加载调用未定位 | 内容确认，触发待确认 |
| `tajyuumirai_no_quartet.usm` | 歌曲/PV | 《多重未来のカルテット》游戏/PV资源：一条视频、两条ADX音轨、472条谱面/歌词事件 | 确认 |
| `thum_01_01.plist` | 图集索引 | 商店缩略图的裁切坐标模板；包含3张PV截图和3张歌曲缩略图，供同布局的曲包纹理复用 | 确认 |
| `thum_01_01.png` | 附加曲包 | 与附加曲包商店缩略图布局相符的图集，内容对应 カラフル×セクシィ、ジェミニ、カンタレラ。目前实际加载链使用缓存文件，尚不能确认本包PNG被直接使用 | 内容确认，触发待确认 |
| `thum_02_01.png` | 附加曲包 | 与附加曲包商店缩略图布局相符的图集，内容对应 カラフル×メロディ、Yellow、こっち向いて Baby。目前实际加载链使用缓存文件，尚不能确认本包PNG被直接使用 | 内容确认，触发待确认 |
| `twitter_load.png` | 分享 | Twitter OAuth 登录页背景：SA_OAuthTwitterController loadView 用 UIImage imageNamed 加载并创建 UIImageView | 确认 |
| `ura_omote_lovers.usm` | 歌曲/PV | 《裏表ラバーズ》游戏/PV资源：一条视频、两条ADX音轨、1296条谱面/歌词事件 | 确认 |

## 图片及字体补充

全部450张切图与意义见[sprite_gallery.md](sprite_gallery.md)，动态英文字体的证据见[fonts.md](fonts.md)。
