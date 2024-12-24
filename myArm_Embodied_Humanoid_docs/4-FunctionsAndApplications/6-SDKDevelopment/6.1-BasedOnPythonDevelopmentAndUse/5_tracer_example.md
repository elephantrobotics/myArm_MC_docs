# Case steps

## 1. Enable the Tracer chassis node

- To ensure that the CAN bus is enabled, run this command every time you turn on the power and restart the system:

```bash
rosrun tracer_bringup setup_can2usb.bash
```

- Start the chassis car ROS node:

```bash
roslaunch tracer_bringup tracer_robot_base.launch
```

If the can-to-usb has been connected to the TRACER robot, the car has been powered on, the CAN bus has been enabled, and the chassis node has been turned on, use the following command to monitor the data of the TRACER chassis

```bash
candump can0
```

If the chassis data is normal, the terminal will always output the following data:

![tracer cano data](../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/tracer_example/can0-data.png)

## 2. Case Implementation

>> Note: Before using the API interface, you need to ensure that the terminal directory is located in the target path; before moving, ensure that there is enough space around the car for movement.

- Switch the terminal to the target path:

```bash
cd ~/catkin_ws/src/mc_embodied_kit_ros/tracer_bringup/scripts
```

```python
# Example
from chassis_controller import ChassisController
import time

cc = ChassisController()

# # Move forward for 2 seconds, at a speed of 0.5 m/s
cc.move_forward(0.5, 2)

time.sleep(3)

# Move backward for 2 seconds, at a speed of -0.5 m/s
cc.move_backward(-0.5, 2)

timme.sleep(3)

# Turn left for 5 seconds, at a speed of 0.5 m/s
cc.turn_left(0.5, 5)

time.sleep(3)

# Turn right for 5 seconds, at a speed of -0.5 m/s
cc.turn_right(-0.5, 5)

# Stop the car
cc.stop()
```

---

[← Previous page](./4_tracer_API.md) | [Next page →](../5.2-DevelopmentAndUseBasedOnROS1/1_download.md)