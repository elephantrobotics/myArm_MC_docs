# 机器人参数说明

> 第一章中，我们探讨了产品的卖点及其设计理念，为您提供了对产品高层次理解的全景视角。现在，让我们进入第二章——机器人参数说明。这一章节将是您理解产品技术细节的关键。详细了解这些技术参数，不仅可以帮助您充分认识到我们产品的先进性和实用性，而且还能够确保您能够更有效地利用这些技术来满足您的具体需求。

## 1.机器人规格参数

<!-- <img src="../../resources/9-FilesDownload/2-serialproduct/image.png" width="800" height="auto" /> -->

| 规格         | 参数                |
| :----------- | :------------------ |
| DOF          | 6+1                 |
| 水平伸展范围 | 650                 |
| 总跨度       | 1300mm              |
| 自重         | 1.8kg               |
| 电源规格     | 12V5A               |
| 重复定位精度 | ±1mm                |
| 精确度       | 5 - 8mm             |
| 工作载荷     | -                   |
| 舵机数量     | 8                   |
| 舵机类型     | 高精度数字伺服电机  |
| 旋转能力     | +/- 180°            |
| 末端执行器   | 双指遥控+双按钮控制 |
| USB 连接     | Type-C              |
| Atom 末端    | 5\*5 LED 灯矩阵     |
| 通讯帧率     | >50Hz               |


## 2.控制核心参数

### 主控制器规格表

| **指标** | **参数**                                                          |
| :------- | :---------------------------------------------------------------- |
| **主控制**   | M5Stack-basic                                                     |
| **主控型号** | ESP32                                                             |
| **CPU**      | 240MHz 双核心。<br> 600 DMIPS、520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| **蓝牙**     | 2.4G/5G                                                           |
| **无线**     | 2.4G 3D Antenna                                                   |
| **输入**     | 1, 2, 3, 5, 18, 19, 21, 22, 23, 25, 26, 35, 36                    |
| **输出**     | 同输入共用                                                        |
| **LCD 显示器**         | 2.0" @ 320*240 ILI9342C IPS panel, maximum brightness 853nit         |
| **实体按键**           | 

### 辅助控制器规格表


| **指标**           | **参数**                                                        |
| :----------------- | :-------------------------------------------------------------- |
| **辅助控制**            | Atom                                                            |
| **辅助控制型号**        | ESP32                                                           |
| **辅助控制器核心参数**  | 240MHz 双核。<br> 600 DMIPS，520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| **辅助控制器闪光灯**    | 4MB                                                             |
| **LED矩阵**         | 5*5 LED灯矩阵                                         |
| **LCD 显示**           | 2.0"@320\*240 ILI9342C IPS 面板，<br> 最大亮度 853nit           |
| **C 型**                | \*1                                                             |
| **辅控扩展IO**      | G19, G21, G22, G23, G25, G33                          |



---

## 3.结构尺寸参数

> ！本章以毫米为距离单位，以度为角度单位。

### 产品尺寸和工作空间

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_00.jpg" width="800" height="auto" />

### 底座安装尺寸

- 底座需采用法兰安装，可使用 M6 螺丝固定在对应的固定底座上。
- 使用前请确认安装的底座可以承受 3 倍于机身重量的承载，以防止使用过程中因运动速度提升导致产品固定松动而引起产品损坏。

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\base-D.png" width="800" height="auto" />

图 1 底座正视图

### 手臂末端

- 机械臂的末端可与乐高组件孔和螺纹孔兼容。

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_01.jpg" width="800" height="auto" />

### 产品展示

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_03.jpg" width="800" height="auto" />



<!-- [PDF Views](<../../resources/2-ProductFeature/320%202022款技术图示(1).pdf>) -->

### 3D 模型下载

资料更新中...

<!-- Download link: [https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP](https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP) -->

<!-- <iframe
    src=""
    width="100%"
    height="600px"
    allowfullscreen="true"
    webkitallowfullscreen="true"
    mozallowfullscreen="true"
    frameborder="0">
</iframe> -->

---

[← 上一章](../1-ProductIntroduction/1-ProductIntroduction.md) | [下一章 →](../../3-BasicSettings/3-UserInstructions/3-UserInstructions.md)
