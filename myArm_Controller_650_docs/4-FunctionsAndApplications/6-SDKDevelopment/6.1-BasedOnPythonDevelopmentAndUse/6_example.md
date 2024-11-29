# Videos and Codes for Display

Videos given below are for reference.

>  **Notice:** The baud rates are different depending on the type of device. Before using them, refer to the information related thereto. The serial port number can be viewed through [calculator device manager](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip) or a serial helper.

**Please make sure the robot power on.**

## 1 Get the joint angle

```python
from pymycobot import MyArmC

myarmc = MyArmC("COM3")

# Get the current angle of all joints
angles = myarmc.get_joints_angle()
print(f"All current joint angles are: {angles}")

# Get the angle of joint 1
angle = myarmc.get_joint_angle(1)
print(f"The current angle of joint 1 is {angle}")
```

## 2 Get the Atom button state

```python
from pymycobot import MyArmC

myarmc = MyArmC("COM3")

# Get the status of the Atom button
atom_status = myarmc.is_tool_btn_clicked()
if atom_status:
    print("Atom is in a pressed down state")
else:
    print("Atom is not being pressed")

```

[← 上一页](5_Handle_control.md) | [下一节 →](../5.2-DevelopmentAndUseBasedOnROS1/1_download.md)
