
# 案例步骤

## 1. 开启Tracer小车底盘节点

- 为确保CAN总线使能，每次打开电源、系统重启都需要运行此命令：

```bash
rosrun tracer_bringup setup_can2usb.bash
```

- 启动底盘小车ROS节点：

```bash
roslaunch tracer_bringup tracer_robot_base.launch
```

如果已经将can-to-usb连接到TRACER机器人，并且小车已经开机、CAN总线已经使能、底盘节点已经开启，使用以下命令监控TRACER底盘的数据

```bash
candump can0
```

若底盘数据正常，终端会一直输出如下数据：

![tracer cano data](../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/tracer_example/can0-data.png)

## 2. 案例实现

>> 注意：使用API接口之前，需要确保终端目录位于目标路径；运动之前，确保小车周围有足够的空间场地进行运动。

- 终端切换到目标路径：

```bash
cd ~/catkin_ws/src/mc_embodied_kit_ros/tracer_bringup/scripts
```

```python
# 示例
from chassis_controller import ChassisController
import time

cc = ChassisController()

# # 前进 2 秒, 速度为 0.5 m/s
cc.move_forward(0.5, 2)  

time.sleep(3)

# 后退 2 秒, 速度为 -0.5 m/s
cc.move_backward(-0.5, 2)  

timme.sleep(3)

# 向左旋转 5 秒， 速度为 0.5 m/s
cc.turn_left(0.5, 5)

time.sleep(3)

# 向右旋转 5 秒， 速度为 -0.5 m/s
cc.turn_right(-0.5, 5)

# 停止小车
cc.stop()
```

---

[← 上一页](./4_tracer_API.md) | [下一节 →](../5.2-DevelopmentAndUseBasedOnROS1/1_download.md)
