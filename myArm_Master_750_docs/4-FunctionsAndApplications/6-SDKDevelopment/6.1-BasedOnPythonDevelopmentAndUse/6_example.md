# Videos and Codes for Display

Videos given below are for reference.

>  **Notice:** The baud rates are different depending on the type of device. Before using them, refer to the information related thereto. The serial port number can be viewed through [calculator device manager](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-how-to-distinguish-between-cp210x-chip-and-cp34x-chip) or a serial helper.

**Please make sure the robot power on.**


## 1 Get the joint angle

```python
from pymycobot import MyArmM
import time

myarmm = MyArmM("COM3")

# Gets the current angle of all joints
angles = myarmm.get_joints_angle()
print(f"All current joint angles are: {angles}")

time.sleep(0.1)

# Get the angle of joint 1
angle = myarmm.get_joint_angle(1)
print(f"The current angle of joint 1 is {angle}")

# Get the angle of joint 2
angle = myarmm.get_joint_angle(2)
print(f"The current angle of joint 2 is {angle}")

# Get the angle of joint 3
angle = myarmm.get_joint_angle(3)
print(f"The current angle of joint 3 is {angle}")
```

## 2 Control the joint to move five points

```python
from pymycobot import MyArmM
import time

myarmm = MyArmM("COM3")

# Reset all joints at a speed of 40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
#Wait for all joints to move to the specified position
time.sleep(3)

# Move all joints at the specified angle at a speed of 40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# Wait for all joints to move to the specified position
time.sleep(3)

# Reset all joints at a speed of 40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
# Wait for all joints to move to the specified position
time.sleep(3)

# Move all joints at the specified angle at a speed of 40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# Wait for all joints to move to the specified position
time.sleep(3)

# Reset all joints at a speed of 40
myarmm.set_joints_angle([0, 0, 0, 0, 0, 0], 40)
# Wait for all joints to move to the specified position
time.sleep(3)

# Move all joints at the specified angle at a speed of 40
myarmm.set_joints_angle([90, 45, -90, 90, -90, 90], 40)
# Wait for all joints to move to the specified position
time.sleep(3)
```

[← Previous page](2_API.md) | [Next section →](../6.2-DevelopmentAndUseBasedOnROS1/1_download.md)
