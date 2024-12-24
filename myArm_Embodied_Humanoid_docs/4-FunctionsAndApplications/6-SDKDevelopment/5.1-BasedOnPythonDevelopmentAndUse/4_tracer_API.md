### 使用前提

> API (Application Programming Interface), 也称为应用程序编程接口函数，是预定义的函数。使用之前需要导入API库。

* 终端切换到目标目录之后，输入 `python` 指令：

    ```bash
    cd ~/catkin_ws/src/mc_embodied_kit_ros/tracer_bringup/scripts
    python
    ```
* 导入底盘控制的API库

    ```python
    from chassis_controller import ChassisController
    ```
 * 简单使用
    ```python
    # 示例
    from chassis_controller import ChassisController

    cc = ChassisController()

    # 前进、后退
    cc.move_forward(0.5, 2)  # 前进 2 秒, 速度为 0.5 m/s
    cc.move_backward(-0.5, 2)  # 后退 2 秒, 速度为 -0.5 m/s
    # 停止小车
    cc.stop()
    ```

### Python API使用说明

#### 1 `move_forward(speed, duration)`
- **function:** 前进，默认运动1秒
  
- **Parameters:**
  - `speed`: 前进速度，范围为 0.0 ~ 0.5 米/秒。
  - `duration`: 运动时长，正整数，单位：秒。

#### 2 `move_backward(speed, duration)`
- **function:** 后退，默认运动1秒
  
- **Parameters:**
  - `speed`: 后退速度，范围为 -0.5 ~ 0 米/秒。
  - `duration`: 运动时长，正整数，单位：秒。

#### 3 `turn_left(speed, duration)`
- **function:** 向左旋转，默认运动1秒
  
- **Parameters:**
  - `speed`:运动速度，范围为 0.0 ~ 0.5 米/秒。
  - `duration`: 运动时长，正整数，单位：秒。

#### 4 `turn_right(speed, duration)`
- **function:** 向右旋转，默认运动1秒
  
- **Parameters:**
  - `speed`: 运动速度，范围为 -0.5 ~ 0 米/秒。
  - `duration`: 运动时长，正整数，单位：秒。

#### 5 `stop(speed, duration)`
- **function:** 停止运动

---

[← 上一页](./3_example.md) | [下一页 →](./5_tracer_example.md)