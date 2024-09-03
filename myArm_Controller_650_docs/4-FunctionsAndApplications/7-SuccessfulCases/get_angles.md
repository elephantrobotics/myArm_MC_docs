# python 获取角度信息及坐标信息案例

机械臂开机后，会自动进入串口通信模式

<img src="./img/2.jpg" alt="" width="40%" height="40%">

在设备管理器查看机械臂的串口号


<img src="./img/3.jpg" alt="" width="60%" height="40%">

## 1 获取所有关节角度
```python
from pymycobot import MyArmC
import time
arm=MyArmC("COM18")#填写实际的串口号
while 1:
    print("angles=",arm.get_joints_angle())
```
**运行效果**：

<img src="./img/1.gif" alt="" width="100%" height="40%">



## 2 获取单个关节角度
```python
from pymycobot import MyArmC
import time
arm=MyArmC("COM18")#填写实际的串口号
while 1:
    #joint_id:1-7对应关节1-关节7
    print("angle=",arm.get_joint_angle(1))#获取关节1的角度
```
**运行效果**：

<img src="./img/2.gif" alt="" width="100%" height="40%">

## 3 获取坐标信息
```python
from pymycobot import MyArmC
import time
arm=MyArmC("COM18")#填写实际的串口号
while 1:
    print("coords=",arm.get_joints_coord())
```
**运行效果**：

<img src="./img/3.gif" alt="" width="100%" height="40%">

## 常见问题
程序执行后，指令不生效，返回none现象，先检查屏幕底座的界面是否处于通信界面，且通信界面是否为OK，若显示no,先退出回到主界面，按照下面操作重新进入通信界面

**Step 1**:确认12V适配器及Type-C正确连接你的设备，选中Transponder点击OK进入通信转发界面。


<img src="./img/0.jpg" alt="" width="40%" height="40%">

**Step 2**: 使用串口连接，选中USB UART点击OK进入串口界面。串口界面检测Atom的连接(ok表示连接正常，否则显示no)。

<img src="./img/1.jpg" alt="" width="40%" height="40%">

<p>

<img src="./img/2.jpg" alt="" width="40%" height="40%">

**注意事项**：若是显示no，尝试重新退出后再进入即可
