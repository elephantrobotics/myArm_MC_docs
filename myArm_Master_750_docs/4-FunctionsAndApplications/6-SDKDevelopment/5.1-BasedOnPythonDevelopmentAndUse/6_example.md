# 演示代码与视频

以下视频供参考。

> **注：** 各款设备的对应的波特率不尽相同，使用时请查阅资料了解其波特率，串口编号可通过 [计算器设备管理器](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip)或串口助手进行查看。

## 1 获取关节角度

```python
from pymycobot import MyArmM
import time

myarmm = MyArmM("COM3")

# 获取所有关节的当前角度
angles = myarmm.get_joints_angle()
print(f"当前所有的关节角度是: {angles}")

time.sleep(0.1)

# 获取关节1的角度
angle = myarmm.get_joint_angle(1)
print(f"关节1当前的角度为 {angle}")

# 获取关节2的角度
angle = myarmm.get_joint_angle(2)
print(f"关节2当前的角度为 {angle}")

# 获取关节3的角度
angle = myarmm.get_joint_angle(3)
print(f"关节3当前的角度为 {angle}")
```

## 2 控制关节移动五个点位

```python
from pymycobot import MyArmM
import time

myarmm = MyArmM("COM3")

# 将所有的关节复位, 速度为40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
# 等待所有关节运动到指定位置
time.sleep(3)

# 将所有的关节按照指定的角度移动, 速度为40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# 等待所有关节运动到指定位置
time.sleep(3)

# 将所有的关节复位, 速度为40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
# 等待所有关节运动到指定位置
time.sleep(3)

# 将所有的关节按照指定的角度移动, 速度为40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# 等待所有关节运动到指定位置
time.sleep(3)

# 将所有的关节复位, 速度为40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
# 等待所有关节运动到指定位置
time.sleep(3)

# 将所有的关节按照指定的角度移动, 速度为40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# 等待所有关节运动到指定位置
time.sleep(3)
```

## 3 C650和M750摇操控制程序案例

## 程序地址

固件版本v1.0:
> https://github.com/elephantrobotics/pymycobot/tree/main/demo/myArm_M&C_demo

固件版本v1.1及以上，请参考[固件版本v1.1 C650和M750摇操控制程序](../../7-SuccessfulCases/7.1-demo_add.md#12-案例程序下载):
> https://github.com/elephantrobotics/pymycobot/tree/main/demo/myArm_M&C_demo_v1.1


## 安装依赖

```shell
pip install -r requirement.txt
```

## 运行程序

```shell
python main.py
```

## 程序使用说明

> 串口的打开有顺序要求：先开启myArmM的串口连接，再开启myArmC的串口连接。


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_1.png" alt="7.1.1-7" style="zoom: 50%;" />

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_2.png" alt="7.1.1-1" style="zoom: 50%;" />

> 两个串口都开启以后就可以通过移动myArmC来控制myArmM运动。

---

[← 上一页](2_API.md) | [下一节 →](../5.2-DevelopmentAndUseBasedOnROS1/1_download.md)

