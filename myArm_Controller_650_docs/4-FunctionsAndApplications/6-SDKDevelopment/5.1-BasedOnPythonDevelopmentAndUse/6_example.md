# 演示代码与视频

以下视频供参考。

> **注：** 各款设备的对应的波特率不尽相同，使用时请查阅资料了解其波特率，串口编号可通过 [计算器设备管理器](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip)或串口助手进行查看。

## 1 获取关节角度

```python
from pymycobot import MyArmC

myarmc = MyArmC("COM3")

# 获取所有关节的当前角度
angles = myarmc.get_joints_angle()
print(f"当前所有的关节角度是: {angles}")

# 获取关节1的角度
angle = myarmc.get_joint_angle(1)
print(f"关节1当前的角度为 {angle}")
```

## 2 获取 Atom 按钮状态

```python
from pymycobot import MyArmC

myarmc = MyArmC("COM3")

# 获取Atom按钮状态
atom_status = myarmc.is_tool_btn_clicked()
if atom_status:
    print("Atom 处于摁下状态")
else:
    print("Atom 处于松开状态")

```

[← 上一页](2_API.md) | [下一节 →](../5.2-DevelopmentAndUseBasedOnROS1/1_download.md)
