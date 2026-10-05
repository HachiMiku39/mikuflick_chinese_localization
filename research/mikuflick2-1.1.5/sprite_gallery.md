# 按plist裁切的图片与意义

21份TexturePacker格式plist，450个frame全部裁切。每页附图片、用途解释、全局索引、源PNG/plist与裁切坐标。当前样本的offset全部为0，originalSize与裁切尺寸一致，没有旋转/修剪还原问题。原app另有独立PNG及复用布局的替代图集，它们的文件作用见[资源全表](resources.md)。

用户提供的圆形双箭头按钮已被指认为随机选曲。截图视觉对应replay_on.png（frame80）。shuffle_on/off（86/87）是另一组PV控制贴图。资源名与用户确认的作用分别记录，圆形按钮的具体运行调用仍待核。

| 图集 | 数量 | 场景 |
|---|---:|---|
| [UI_tex_01](galleries/UI_tex_01.md) | 101 | 选曲、PV播放控制、通用菜单 |
| [UI_tex_02](galleries/UI_tex_02.md) | 69 | 结果、解锁、收藏与载入 |
| [UI_tex_03](galleries/UI_tex_03.md) | 13 | 音量、帮助、左右手设置 |
| [UI_tex_04](galleries/UI_tex_04.md) | 16 | 键盘、花形提示与面板引导设置 |
| [UI_tex_05](galleries/UI_tex_05.md) | 12 | 标题画面 |
| [UI_tex_06](galleries/UI_tex_06.md) | 39 | 商店、购买与已安装内容管理 |
| [UI_tex_07](galleries/UI_tex_07.md) | 12 | 下载进度与恢复购买 |
| [bg_tex_01](galleries/bg_tex_01.md) | 1 | 背景/版权/结尾 |
| [bg_tex_02](galleries/bg_tex_02.md) | 2 | 背景/版权/结尾 |
| [bg_tex_03](galleries/bg_tex_03.md) | 1 | 背景/版权/结尾 |
| [bg_tex_04](galleries/bg_tex_04.md) | 1 | 背景/版权/结尾 |
| [bg_tex_05](galleries/bg_tex_05.md) | 1 | 背景/版权/结尾 |
| [bg_tex_06](galleries/bg_tex_06.md) | 1 | 背景/版权/结尾 |
| [bg_tex_07](galleries/bg_tex_07.md) | 4 | 背景/版权/结尾 |
| [credits_ja](galleries/credits_ja.md) | 1 | 背景/版权/结尾 |
| [ending](galleries/ending.md) | 1 | 背景/版权/结尾 |
| [game_effect_01](galleries/game_effect_01.md) | 13 | 游戏输入特效 |
| [game_tex_01](galleries/game_tex_01.md) | 84 | 游戏HUD、判定与引导 |
| [game_tex_02](galleries/game_tex_02.md) | 66 | 原始假名键盘 |
| [music_00_01](galleries/music_00_01.md) | 6 | 预装歌曲封面与标题 |
| [thum_01_01](galleries/thum_01_01.md) | 6 | 附加歌曲介绍图片；当前包缺少动态商店配置 |

## 机器可读对应表

[sprite_mapping.json](data/sprite_mapping.json)保存每张图片的坐标、语义、确认等级和摘要；[atlas_metadata.json](data/atlas_metadata.json)保存全部原始布局字段；[image_metadata.json](data/image_metadata.json)列出全部98张PNG的尺寸与源文件SHA-256。
