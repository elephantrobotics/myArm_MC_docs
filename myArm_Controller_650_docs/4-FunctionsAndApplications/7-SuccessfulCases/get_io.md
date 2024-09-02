# python 实时获取IO输入状态案例

机械臂开机后，会自动进入串口通信模式，若是显示no,按照下面的操作重新进入串口通信模式即可
![](./img/2.jpg)

**Step 1**:确认12V适配器及Type-C正确连接你的设备，选中Transponder点击OK进入通信转发界面。
![](./img/0.jpg)

**Step 2**: 使用串口连接，选中USB UART点击OK进入串口界面。串口界面检测Atom的连接(ok表示连接正常，否则显示no)。
![](./img/1.jpg)

![](./img/2.jpg)

**注意**：若是显示no，尝试退出后再进入即可

**Step 3**：在设备管理器查看机械臂的串口号
![](./img/3.jpg)

## 1 获取底部IO1输入状态
将杜邦线一端插到3.3V，杜邦线的另一端插到GPIO35上，模拟按键按下的效果
![](./img/4.jpg)

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")
while 1: 
    #当杜邦线接通时输出1,未接通输出0
    print(arm.get_master_in_io_state(1))
```

## 2 获取底部IO2输入状态
将杜邦线一端插到3.3V，杜邦线的另一端插到GPIO36上，模拟按键按下的效果
![](./img/5.jpg)

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")
while 1: 
    #当杜邦线接通时输出1,未接通输出0
    print(arm.get_master_in_io_state(2))
```