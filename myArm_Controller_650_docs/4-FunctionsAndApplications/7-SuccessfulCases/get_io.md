# Python obtains IO input status example
After the robot is turned on, it will automatically enter the serial communication mode

<img src="./img/2.jpg" alt="" width="40%" height="40%">

Check the serial port number of the robot in the device manager

<img src="./img/3.jpg" alt="" width="60%" height="40%">

## 1 Get the bottom IO1 input status
Plug one end of the DuPont line into 3.3V and the other end of the DuPont line into GPIO35 to simulate the effect of pressing the button
<img src="./img/4.jpg" alt="" width="50%" height="40%">

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#Fill in the actual serial port number
while 1:
#When the DuPont line is connected, output 1, and when it is not connected, output 0
    print("IO=",arm.get_master_in_io_state(1))
```
**Running effect**:

<img src="./img/5.gif" alt="" width="60%" height="40%">

## 2 Get the bottom IO2 input status
Plug one end of the DuPont line into 3.3V and the other end of the DuPont line into GPIO36 to simulate the effect of pressing the button
<img src="./img/5.jpg" alt="" width="50%" height="40%">

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#Fill in the actual serial port number
while 1:
#When the DuPont line is connected, output 1, and when it is not connected, output 0
    print(arm.get_master_in_io_state(2))
```
**Running effect**:

<img src="./img/6.gif" alt="" width="60%" height="40%">

## 3 Get the terminal IO1 input status
Plug one end of the DuPont line into GND and the other end of the DuPont line into GPIO19 to simulate the effect of pressing the button
<img src="./img/7.jpg" alt="" width="50%" height="40%">

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#Fill in the actual serial port number
while 1:
    if arm.get_tool_in_io_state(1) is not None:
    #When the DuPont line is not connected, output 1, and when it is connected, output 0
        print("IO=",arm.get_tool_in_io_state(1))
```
**Running effect**:

<img src="./img/7.gif" alt="" width="60%" height="40%">

## 4 Get the terminal IO2 input status
Plug one end of the DuPont line into GND and the other end of the DuPont line into GPIO22 to simulate the effect of pressing the button
<img src="./img/8.jpg" alt="" width="50%" height="40%">

```python
from pymycobot import MyArmC
import time
arm = MyArmC("COM18")#Fill in the actual serial port number
while 1:
    if arm.get_tool_in_io_state(2) is not None:
    #When the DuPont line is not connected, output 1, and when it is connected, output 0
        print("IO=",arm.get_tool_in_io_state(2))
```
**Running effect**:

<img src="./img/8.gif" alt="" width="60%" height="40%">

## Common Problems
After the program is executed, the command does not take effect and returns to none. First check whether the interface of the screen base is in the communication interface and whether the communication interface is OK. If it shows no, exit and return to the main interface first, and follow the following steps to re-enter the communication interface

**Step 1**: Confirm that the 12V adapter and Type-C are correctly connected to your device, select Transponder and click OK to enter the communication forwarding interface.

<img src="./img/0.jpg" alt="" width="40%" height="40%">

**Step 2**: Use the serial port connection, select USB UART and click OK to enter the serial port interface. The serial port interface detects the connection of Atom (ok means the connection is normal, otherwise it shows no).

<img src="./img/1.jpg" alt="" width="40%" height="40%">

<p>

<img src="./img/2.jpg" alt="" width="40%" height="40%">

**Note**: If it shows no, try to exit and then enter again