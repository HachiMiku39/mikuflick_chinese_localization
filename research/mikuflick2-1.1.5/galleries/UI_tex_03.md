# UI_tex_03：图片与意义

来源：`UI_tex_03.png` + `UI_tex_03.plist`；画布 [1024, 1024]；13个frame。场景：音量、帮助、左右手设置。

裁切几何来自plist，已确认。用途说明默认按资源名称、图像内容和所属场景解释；只有附有具体函数证据的条目提升为静态确认。on/off一般表示高亮/常态；不保证等于功能启用/禁用。frame序号是程序全局名称表索引，不能当作plist文件里的排列次序。

![总览](../contact_sheets/UI_tex_03.jpg)

| 图像（点击看原尺寸） | 名称 / 全局索引 | 意义与证据 | 裁切矩形 x,y,w,h |
|---|---|---|---|
| [<img src="../sprites/UI_tex_03/arrow_00.png" width="100">](../sprites/UI_tex_03/arrow_00.png) | `arrow_00.png` / 170 | 设置页箭头；变体 00<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[934, 38, 68, 37]` |
| [<img src="../sprites/UI_tex_03/arrow_01.png" width="100">](../sprites/UI_tex_03/arrow_01.png) | `arrow_01.png` / 171 | 设置页箭头；变体 01<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[934, 0, 68, 37]` |
| [<img src="../sprites/UI_tex_03/helpline.png" width="100">](../sprites/UI_tex_03/helpline.png) | `helpline.png` / 172 | 帮助指引线<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[0, 0, 640, 12]` |
| [<img src="../sprites/UI_tex_03/helpmeter_off.png" width="100">](../sprites/UI_tex_03/helpmeter_off.png) | `helpmeter_off.png` / 173 | 帮助/提示量表选项；常态/未选中<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[1003, 18, 17, 17]` |
| [<img src="../sprites/UI_tex_03/helpmeter_on.png" width="100">](../sprites/UI_tex_03/helpmeter_on.png) | `helpmeter_on.png` / 174 | 帮助/提示量表选项；高亮/选中状态<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[1003, 0, 17, 17]` |
| [<img src="../sprites/UI_tex_03/lefthand_off.png" width="100">](../sprites/UI_tex_03/lefthand_off.png) | `lefthand_off.png` / 175 | 左手模式；常态/未选中<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[0, 13, 270, 352]` |
| [<img src="../sprites/UI_tex_03/lefthand_on.png" width="100">](../sprites/UI_tex_03/lefthand_on.png) | `lefthand_on.png` / 176 | 左手模式；高亮/选中状态<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[641, 0, 292, 395]` |
| [<img src="../sprites/UI_tex_03/righthand_off.png" width="100">](../sprites/UI_tex_03/righthand_off.png) | `righthand_off.png` / 177 | 右手模式；常态/未选中<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[271, 13, 267, 352]` |
| [<img src="../sprites/UI_tex_03/righthand_on.png" width="100">](../sprites/UI_tex_03/righthand_on.png) | `righthand_on.png` / 178 | 右手模式；高亮/选中状态<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[498, 396, 289, 395]` |
| [<img src="../sprites/UI_tex_03/speaker.png" width="100">](../sprites/UI_tex_03/speaker.png) | `speaker.png` / 179 | 扬声器图标<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[788, 396, 234, 234]` |
| [<img src="../sprites/UI_tex_03/volumemeter_off.png" width="100">](../sprites/UI_tex_03/volumemeter_off.png) | `volumemeter_off.png` / 180 | 音量调节量表；常态/未选中<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[960, 76, 25, 34]` |
| [<img src="../sprites/UI_tex_03/volumemeter_on.png" width="100">](../sprites/UI_tex_03/volumemeter_on.png) | `volumemeter_on.png` / 181 | 音量调节量表；高亮/选中状态<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[934, 76, 25, 34]` |
| [<img src="../sprites/UI_tex_03/volumewindow.png" width="100">](../sprites/UI_tex_03/volumewindow.png) | `volumewindow.png` / 182 | 音量设置窗口<br>**名称/图像推断**：plist几何 + frame名称 + 图像内容 | `[0, 396, 497, 540]` |
