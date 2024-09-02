# python 获取末端ATOM按钮状态案例

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

## 1 获取 Atom 按钮状态

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#填写实际的串口号

while 1: 
    atom_status = arm.is_tool_btn_clicked()# 获取Atom按钮状态
    if atom_status is not None: 
        if atom_status[0]==1:
            print("Atom 处于摁下状态")#按下atom_status[0]为1
        else:
            print("Atom 处于松开状态")#未按下atom_status[0]为0
```
