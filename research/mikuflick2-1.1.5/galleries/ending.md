# ending：图片与意义

来源：`ending.png` + `ending.plist`；画布 [1024, 1024]；1个frame。场景：背景/版权/结尾画面。

裁切几何来自plist，已确认。用途说明默认按资源名称、图像内容和所属场景解释；只有附有具体函数证据的条目提升为静态确认。on/off一般表示高亮/常态；不保证等于功能启用/禁用。frame序号是程序全局名称表索引，不能当作plist文件里的排列次序。

![总览](../contact_sheets/ending.jpg)

| 图像（点击看原尺寸） | 名称 / 全局索引 | 意义与证据 | 裁切矩形 x,y,w,h |
|---|---|---|---|
| [<img src="../sprites/ending/bg_ending.png" width="100">](../sprites/ending/bg_ending.png) | `bg_ending.png` / 449 | 结尾滚动名单的装饰背景；名单文字由程序另行绘制<br>**静态确认**：WindowEnding 0x38940；文字表0x1413b8，背景和名单文字分别绘制 | `[0, 0, 640, 960]` |
