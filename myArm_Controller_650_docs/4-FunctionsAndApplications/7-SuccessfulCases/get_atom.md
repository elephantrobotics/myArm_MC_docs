# Python Get the terminal ATOM button status example

After the robot is turned on, it will automatically enter the serial communication mode

<img src="./img/2.jpg" alt="" width="40%" height="40%">

Check the serial port number of the robot in the device manager

<img src="./img/3.jpg" alt="" width="60%" height="40%">

## 1 Get the Atom button status

<img src="./img/6.jpg" alt="" width="40%" height="20%">

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#Fill in the actual serial port number

while 1:
    atom_status = arm.is_tool_btn_clicked()# Get the Atom button status
    if atom_status is not None:
        if atom_status[0]==1:
            print("Atom is in the pressed state")#pressed atom_status[0] is 1
        else:
            print("Atom is in the released state")#not pressed atom_status[0] is 0
```
**Running effect**:

<img src="./img/4.gif" alt="" width="90%" height="40%">

## Common Problems
After the program is executed, the command does not take effect and returns to none. First check whether the interface of the screen base is in the communication interface and whether the communication interface is OK. If it shows no, exit and return to the main interface first, and follow the following steps to re-enter the communication interface

**Step 1**: Confirm that the 12V adapter and Type-C are correctly connected to your device, select Transponder and click OK to enter the communication forwarding interface.

<img src="./img/0.jpg" alt="" width="40%" height="40%">

**Step 2**: Use the serial port connection, select USB UART and click OK to enter the serial port interface. The serial port interface detects the connection of Atom (ok means the connection is normal, otherwise it displays no).

<img src="./img/1.jpg" alt="" width="40%" height="40%">

<p>

<img src="./img/2.jpg" alt="" width="40%" height="40%">

**Note**: If it displays no, try to exit and then enter again

---
[← Previous chapter](./get_angles) | [Next chapter →](./get_io.md)
