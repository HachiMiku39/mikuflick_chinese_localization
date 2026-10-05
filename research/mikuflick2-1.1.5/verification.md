# 下一轮Codex独立复核清单

日期：2026-10-05。目的是让另一个进程用自有原件重新检查关键结论，记录一致、分歧和证据，而不是直接把本报告当作已经通过的运行测试。

## 1. 先确认版本和复核边界

1. 输入是`MikuFlick2.app/MikuFlick2`，版本1.1.5、薄32位ARMv7 Mach-O、cryptid 0。
2. SHA-256应为`869caa22613c5ebfbde6b4c9e1a93362a4f30519231b6dfc9ac3ff31d414b87f`。不匹配时重新定位，不直接套地址。
3. 保留原件，在独立Ghidra项目中工作；这份仓库不含可执行文件或Ghidra完整工程。
4. 先读主README的已有实机记录，再读[mechanics.md](mechanics.md)。`hello_planet.usm`、设备沙盒、商店配置不是本轮预装曲样本的一部分。
5. 安装、越狱、老设备软件修改章节和两份`.strings`不在本次研究修订范围；如发现文字问题，另列核对结果，不自动修改。

可先运行纯读取脚本：

```bash
python3 research/mikuflick2-1.1.5/tools/inspect_macho.py /path/to/MikuFlick2.app/MikuFlick2 \
  --compare-data research/mikuflick2-1.1.5/data/numeric_tables.json

python3 research/mikuflick2-1.1.5/tools/mechanics_model.py --self-test
```

`inspect_macho.py`直接按Mach-O段映射读文件字节；它不是反编译器。模型边界检查只是可复算模型自检，不证明原版已经动态验证。

## 2. Ghidra立即数误译

地址`0xe5c6`，文件中的4字节为`80 ef 10 0f`。Apple otool按指令字展示为`ef800f10`，解为：

```text
0000e5c2  cmp       r2, #0x96
0000e5c4  bge       0xe5cc
0000e5c6  vmov.f32  d0, #2.000000e+00
0000e5ca  b         0xe628
```

Ghidra 12.1.4在该指令显示`#0`，进而把BPM140—149分支反编译成0.0。原始字节、独立指令解码和相邻BPM区间共同支持2秒；不要据这个伪C值声称存在0秒行进时间。当前研究只添加说明，未修改源指令。

macOS可用`otool -tvV`检查；其他环境可以用独立ARM/Thumb反汇编器复核。不要将“确认当前工具的一处误译”扩大成对所有浮点表达式都已验证。

## 3. 优先核对的函数、表与结论

| 优先级 | 定位 | 核对点 |
|---|---|---|
| P0 | `0x29b54`、表`0x140c44`、`0x29fc4` | NSString范围是否固定为difficulty+2、length1；1～5是否全指向同一个函数 |
| P0 | `0xde28`、`0x21dc0`、表`0x13a454/0x13a74c/0x139c80` | 假名减0x3041后的键位/方向/子类型查表；数字后缀是否另有覆盖方向路径 |
| P0 | `0x291dc` | 总物量只数前缀0非零选择子；间奏只数前缀5状态1 |
| P0 | `0x22e10` | TouchDown/Up取较差值、提前按住SAFE例外、错方向封顶SAFE、错键SAD |
| P0 | 表`0x139488/0x1394b4`、`0x22160` | 晚端包含11；候选区和超时与查表边界分开；BTL offset=-2 |
| P0 | 表`0x1394e4`、`0x22e10` | 基础分、共享声音分支、连击增加后的奖励计算、16位截断、Crimax+200 |
| P0 | `0x4ba80`、常数`0x4c424/428/42c` | 评级70/80/95/100阈值、PerfectClear=maxCombo、BTL BreakClear的rank>3条件 |
| P0 | `0xe040`、`0xd218` | Gauge初始128、上限256、64/N+.01权重与比例失败；调用前后的判定计数顺序 |
| P1 | `0x28eb4`、`0x21900` | CRI时间分子/分母得到秒，PlayCnt=ceil(seconds×30) |
| P1 | `0x21dc0`、`0xe57c`、`0x29e10/0x29e84` | NoteDelay单位、BPM行进表、CUE目标时刻和校准项的取整 |
| P1 | `0x29d38`、表`0x140c38`、`0x29efc/0x29f4c` | 间奏1创建，2结束，不把2计成点击 |
| P1 | `0x2ffdc`、表`0x13ac6c/0x13ac98` | 第二份表用于间奏；成功1分、全部成功39分，不进入普通判定计数 |
| P1 | `0x29d94`、`0xe36c`、`0x23364` | Crimax只标最近四个对象中的合格音符，条件与事件数/得分数不同 |
| P1 | `0x29c24/0x29ca4/0x29bd4/0x29bfc` | PV歌词flag1、补充字符不可判定、UI淡入淡出 |
| P1 | `0x6ef60/0x6fcb8/0x6fd70/0x6fddc` | 平方距离256阈值、角度分区、touchUp结算、内部坐标与屏幕缩放区别 |
| P1 | `0x1cdd0`、`0x4ba80` | Normal→Hard、Hard→Extreme、PV解锁和预装/DLC BTL不同分支 |
| P1 | `0x717e0`、`0x29678`、`0x45618` | Shuffle模式3、frame86/87、随机起点后循环筛选，不假定均匀分布 |
| P2 | `0x38940`、`0x1413b8`、`0x79d18` | ending短视频、背景、名单表与动态文字绘制的分工 |
| P2 | `0x60fa8/0x62518/0x60c78/0x16580` | 商店动态封面、缓存缩略图与包内同名PNG的使用证据分开 |
| P2 | `0x86bf4` | twitter_load背景创建及历史客户端场景 |

更多函数名和地址见[`function_index.json`](data/function_index.json)。记录分支时，应核对ARM/Thumb状态、ObjC消息参数及共享调用的前驱；不要只按反编译变量名或字符串附近的函数下结论。

## 4. 重算11首歌曲的统计

已有CUE导出时，按下列规则复算。NSString位置为UTF-16 code unit；本次目标假名在BMP内，因此Python单字符索引与该字段位置一致，但不能推广到含非BMP字符的新事件。

```python
for event in cues:
    s = event['parameter']
    if s[0] == '0':
        for difficulty in range(5):
            ordinary[difficulty] += int(s[difficulty + 2] != '0')
    elif s[0] == '5':
        for difficulty in range(5):
            interlude[difficulty] += int(s[difficulty + 1] == '1')
```

预期6818条总CUE、5280条前缀0记录；曲目逐档统计见[`chart_counts.json`](data/chart_counts.json)。4233条满足五项`11|0|2|3|4|5`拆分的本地记录，其启用掩码恰好与固定位置法一致。剩余记录中有单个1的格式，不能强行套统一可变token法。

不要从“数目相等”推论方向读取也相等；也不要把Crimax标记事件数直接乘200当作加分上限。BPM核对时以事件变化为准，尤其《多重未来のカルテット》195→150。

## 5. 最有区分力的实机实验

以下均为建议实验，当前没有完成记录。用户原件和安装副本先保留，修改长度、元数据和摘要应按具体样本重新定位，不能套另一个USM偏移。

| 实验 | 静态预期 | 能排除什么 |
|---|---|---|
| 假名不变，仅把启用数字2改3 | 仍由原假名决定输入方向 | 数字就是方向字段的解释 |
| 构造混合点击/禁用后缀，让固定位置法和11-token法产生不同启用掩码 | 当前程序按固定位置法 | 现有样本两种统计恰好一致造成的歧义 |
| 普通模式在同一目标分别调整按下和抬起 | 取较差端点，提前按住有SAFE兜底 | 只判抬起或只判按下的模型 |
| BTL正确行但错方向 | 可能SAFE、50分、连击保留 | 帮助文字“SAFE及以下不存在”的字面解释 |
| BTL输入可查表晚10/11格 | 对象可能已被exec失活 | 把共享Back表直接当BTL窗口 |
| 100个FINE全连 | 全连标志、S级，普通理论40500分（排除间奏/Crimax） | PerfectClear与全COOL评级混同 |
| 全部间奏成功及漏掉1个作对照 | 单个1分，全成功额外39 | 间奏计入普通Combo/Rank的解释 |
| NoteDelay和输入校准逐档测量 | 目标受两者及30Hz量化影响 | CUE时间直接等于理想输入时刻的解释 |

BTL建议实验和BreakClear含义必须记录结果画面/存档变化，单靠当前静态分支不能解释玩家侧设计意图。

## 6. 尚需继续逆向的内容

- `ClearCrimax`真实调用时机；Rainbow呈现，原README已有的颜色表/动画观察需独立重核。
- Replay文件布局、注入时刻、参数中的回放结果、跨设备一致性。
- NoteThrow/Arrow/Wait、StageManager完整状态机和HUD表现。
- 整体音画同步和不同设备上真实触摸/音频延迟。
- 动态ShopList、设备缓存、4个附加曲包PNG；9项音频、16项Appleicon和saisei的具体使用。
- 中文逐字输入和自制曲包完整安装、注册、重启持久化；目前不能据MV中文歌词成功直接认定完成。

## 7. 本轮验证记录与复核结果写法

本地原报告完成：450个sprite裁切边界检查、11份CUE数量与容器头一致、42个音频兼容解码、判定模拟器24个边界用例、更新后Ghidra工程重新导入保留注释与原指令。网页做了链接和JS检查，未进行浏览器视觉渲染测试；也未新增旧iOS设备运行测试。

本仓库另外提供可独立运行的Python模型与原始表读取工具，当前执行结果见[`validation.json`](data/validation.json)。它们的“通过”含义与实机测试分开。

下一轮建议每项记录：**样本摘要 → 地址/分支 → 复核方法 → 结果 → 是否更改结论 → 剩余边界**。对于此前已写入README但本轮未重核的内容，不应直接沿用“完全确认”的表述。

## 英文标题字体追加复核

PV / RHYTHM GAME已追到Rewrite与Render，代码请求Futura-Medium，用户反馈字形不同。需在原版本设备验证UIFont返回对象的fontName、字体对象是否为空，捕获文字纹理与显示截图；不要单凭UIFont请求名称宣布实机字形匹配，也不要把图集底框误认成英文文字贴图。见[fonts.md](fonts.md)。
