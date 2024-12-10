### Prerequisites

> API (Application Programming Interface), also known as application programming interface function, is a predefined function. You need to import the API library before using it.

* After the terminal switches to the target directory, enter the `python` command:

    ```bash
    cd ~/catkin_ws/src/mc_embodied_kit_ros/tracer_bringup/scripts
    python
    ```

* Import chassis control API library

    ```python
    from chassis_controller import ChassisController
    ```

* Simple use
  
    ```python
    # Example
    from chassis_controller import ChassisController

    cc = ChassisController()

    # Forward, backward
    cc.move_forward(0.5, 2) # Forward 2 seconds, speed is 0.5 m/s
    cc.move_backward(-0.5, 2) # Backward 2 seconds, speed is -0.5 m/s
    # Stop the car
    cc.stop()
    ```

### Python API usage instructions

#### 1 `move_forward(speed, duration)`
- **function:** Forward, default movement 1 second

- **Parameters:**
  - `speed`: Forward speed, range is 0.0 ~ 0.5 m/s.
  - `duration`: Movement duration, positive integer, unit: seconds.

#### 2 `move_backward(speed, duration)`
- **function:** Backward, default movement 1 second

- **Parameters:**
  - `speed`: Backward speed, range is -0.5 ~ 0 m/s.
  - `duration`: Movement duration, positive integer, unit: seconds.

#### 3 `turn_left(speed, duration)`
- **function:** Turn left, default movement 1 second

- **Parameters:**
  - `speed`: Movement speed, range is 0.0 ~ 0.5 m/s.
  - `duration`: Movement duration, positive integer, unit: seconds.

#### 4 `turn_right(speed, duration)`
- **function:** Turn right, default movement 1 second

- **Parameters:**
  - `speed`: Movement speed, range -0.5 ~ 0 m/s.
  - `duration`: Movement duration, positive integer, unit: seconds.

#### 5 `stop(speed, duration)`
- **function:** Stop movement

---

[← Previous page](./3_example.md) | [Next page →](./5_tracer_example.md)