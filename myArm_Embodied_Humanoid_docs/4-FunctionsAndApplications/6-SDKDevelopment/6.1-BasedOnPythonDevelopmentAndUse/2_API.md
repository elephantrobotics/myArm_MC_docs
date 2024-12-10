# Introduction to API

API or Application Programming Interface refers to a number of preset programs. Before utilization, it is required to import API library:

```python
from pymycobot import MyArmM 

# Example
myarmm = MyArmM('/dev/ttyAMA1')

# Gets the current angle of all joints
angles = myarmm.get_joints_angle()
print(angles)

# Set joint 1 to move to 40 and set the speed to 20
myarmm.set_joint_angle(1, 40, 20)
```

# 1. Query the status of the bot


**1.1** `get_robot_modified_version()`

- **Function:** Get the bot correction version number
- **Parameters:** None
- **Return value:** None

**1.2** `get_robot_firmware_version()`

- **Function:** Obtaining the Robot Firmware Version (Major and Minor Versions)
- **Parameters:** None
- **Return value:** None

**1.3** `get_robot_tool_modified_version()`

- **Function:** Get the remediation version of the bot tool
- **Parameters:** None
- **Return value:** None

**1.4** `get_robot_tool_firmware_version()`

- **Function:** Get the Robot Tool Firmware Version (End Atom)
- **Parameters:** None
- **Return value:** None

**1.5** `set_robot_err_check_state(status)`

- **Function:** Set Error Detection Status You can turn off error detection, but do not turn it off unless necessary
- **Parameters:**
  - **status** - int
    - 1 - open
    - 0 - close
- **Return value:** None

**1.6** `get_robot_err_check_state()`

- **Function:** Read error detection status
- **Parameters:** None
- **Return value:**
  - 1 - open
  - 0 - close

**1.7** `get_robot_error_status()`

- **Function:** Get the bot error status, this interface returns within 15s
- **Parameters:** None
- **Return value:** No error: [0,0,0,0,0,0,0,0] assuming that error 1 and 3 are reported in section 1, it should return: [[1,3],0,0,0,0,0,0,0]

**1.8** `get_robot_power_status()`

- **Function:** Get the robot power status
- **Parameters:** None
- **Return value:**
  - 1 - power on
  - 0 - power off

**1.9** `set_robot_power_on()`

- **Function:** Set the robot to the power-on state
- **Parameters:** None
- **Return value:** None

**1.10** `set_robot_power_off()`

- **Function:** Set the robot to a shutdown state
- **Parameters:** None
- **Return value:** None

**1.11** `clear_robot_err()`

- **Function:** Clear the robot abnormality, ignore the error joint, and continue to move
- **Parameters:** None
- **Return value:** None

**1.12** `get_recv_queue_max_len()`

- **Function:** The total length of the queue for read and receive commands
- **Parameters:** None
- **Return value:** 
  - `max_len`: `(int)` Total length of the command queue, default value `100`

**1.13** `set_recv_queue_max_len(max_len)`

- **Function:** Set the total length of the receiving command queue
- **Parameters:** 
  - `max_len`: `(int)` Queue length
- **Return value:** None

**1.14** `clear_recv_queue()`

- **Function:** Clear the queue for receiving commands
- **Parameters:** None
- **Return value:** None

**1.15** `get_recv_queue_len()`

- **Function:** The current length of the read and receive command queue
- **Parameters:** None
- **Return value:** 
  - `queue_len`: `(int)` The current command queue length

# 2. Joint servo control

**2.1** `set_joint_angle(joint_id, angle, speed)`

- **Function:** Set the individual joints to move to the target angle

- **Parameters:**
  - `joint_id`: `(int)` Joint number
  - `angle`: `(int)` Target angle
  - `speed`: `(int)` Movement speed, value range `1 - 100`

- **Return value:** None

**2.2** `get_joint_angle(joint_id)`

- **Function:** Gets the current angle of the specified joint
- **Parameters:**
  - `joint_id`: The designated joint of the robotic arm, with a range of 1~6
- **Return value:** 
  - `angle` Represents the angle of the current joint

**2.3** `set_joints_angle(angles, speed)`

- **Function:** Set all joints to move to the target angle
- **Parameters:**
  - `angles`: `(list[int])` Target angle
  - `speed`: `(int)` Movement speed, value range `1 - 100`
- **Return value:** None

**2.4** `get_joints_angle()`

- **Function:** Gets the current angle of all joints
- **Parameters:** None
- **Return value:** 
  - `angles` Returns a floating-point list representing the current angles of all joints

**2.5** `get_joints_max()`

- **Function:** Read the maximum angle of all joints
- **Parameters:** None
- **Return value:** 
  - `angles` Returns a floating-point list representing the maximum angle of all joints

**2.6** `get_joints_min()`

- **Function:** Read the minimum angle of all joints
- **Parameters:** None
- **Return value:** 
  - `angles` Returns a floating-point list representing the minimum angle of all joints

**2.7** `is_robot_moving()`

- **Function:** See if the bot is moving
- **Parameters:** None
- **Return value:**
    - 1 - moving
    - 0 - stop

**2.8** `stop_robot()`

- **Function:** The robot stops moving
- **Parameters:** None
- **Return value:** None

# 3. Servo motor control

**3.1** `set_servo_calibrate(servo_id)`

- **Function:** Sets the zero position of the specified servo motor
- **Parameters:** 
  - `servo_id` Indicates the servo motor index bit, with values ranging from `1 - 6`.
- **Return value:** None

**3.2** `set_servo_encoder(servo_id, encoder, speed)`

- **Function:** Set the individual motor motion to the target encoder potential value
- **Parameters:**
  - `servo_id`: `(int)` Indicates the servo motor index bit, and the value returns `1 - 6`
  - `encoder`: `(int)` Motor potential, range `0 - 4095`
  - `speed`: `(int)` Motor moving speed, value range `1 - 100`
- **Return value:** None

**3.3** `get_servo_encoder(servo_id)`

- **Function:** Gets the current encoder potential value for the specified servo motor
- **Parameters:** 
  - `servo_id`: `(int)` Indicates the servo motor index bit, with values ranging from `1 - 6`.
- **Return value:** 
  - `encoder`:`(int)` Represents the potential value of the robotic arm, and the value range is 0 ~ 4096

**3.4** `set_servos_encoder(positions, speed)`

- **Function:** Sets the encoder potential values for multiple motors moving to the target
- **Parameters:**
  - `positions`: `(list[int])` Target potential values for multiple motors `0 - 4095`
  - `speed`: `(int)` Motor moving speed, value range `1 - 100`
- **Return value:** None

**3.5** `get_servos_encoder()`

- **Function:** Obtain the current encoder potential values for multiple servo motors
- **Parameters:** None
- **Return value:** 
  - `encoders`: `(list[int])` Represents the potential value of the manipulator, the value range is 0 ~ 4096, the length of the six axes is 6, the length of the four axes is 4, and the expression method is: [2048,2048,2048,2048,2048,2048]

**3.6** `get_servos_speed()`

- **Function:** Gets the current motion speed of multiple servo motors
- **Parameters:** None
- **Return value:** 
  - `speeds`: `(list[int])` Servo motor movement speed 

**3.7** `set_servos_encoder_drag(encoders, speeds)`

- **Function:** Set multiple servo motors with a specified speed to the target encoder potential value
- **Parameters:**
  - `encoders`: `(list[int])` encoders
  - `speeds`: `(list[int])` speeds
- **Return value:** None

**3.8** `get_servos_encoder_drag()`

- **Function:** Reads the current encoder value and operating speed of all servo motors
- **Parameters:** None
- **Return value:**
  - `encoders`: `(list[int])` encoders
  - `speeds`: `(list[int])` speeds

**3.9** `is_all_servos_enabled()`

- **Function:** Get the connection status of multiple servo motors
- **Parameters:** None
- **Return value:** 
  - `status`: `(list[int])`
    - 1 : The connection is successful
    - 0 : The connection failed

**3.10** `get_servos_temp()`

- **Function:** Obtain the temperature of multiple servo motors
- **Parameters:** None 
- **Return value:** `list(float)` The temperature of each servo motor

**3.11** `get_servos_voltage()`

- **Function:** Get the voltage of multiple servo motors
- **Parameters:** None 
- **Return value:** `list(float)` The voltage of each servo motor

**3.12** `get_servos_current()`

- **Function:** Obtain the current of multiple servo motors
- **Parameters:** None 
- **Return value:** `list(float)` Current per servo motor

**3.13** `get_servos_status()`

- **Function:** Get all the statuses of multiple servo motors
- **Parameters:** None 
- **Return value:** `list(int)` The status of each servo motor

**3.14** `get_servos_protect_current()`

- **Function:** Multiple servo motor protection currents are obtained
- **Parameters:** None 
- **Return value:** `list(int)` Protection current for each servo motor

**3.15** `set_servo_enabled(joint_id, state)`

- **Function:** Set the torque switch of the servo motor
- **Parameters:**
  - `joint_id`: `(int)`Motor index bits
  - `state`: `(int)`
    - 1 - focus
    - 0 - release
- **Return value:** None

# 4. Servo motor system parameter modification

**4.1** `set_servo_p(servo_id, data)`

- **Function:** Sets the proportionality factor of the position loop P of the specified servo motor
- **Parameters:**
  - `servo_id`: `(int)` Motor index bits
  - `data`: `(int)` Ring P scale factor
- **Return value:** None

**4.2** `get_servo_p(servo_id)`

- **Function:** Reads the position loop P scale factor of the specified servo motor
- **Parameters:**
  - `servo_id`: `(int)` Motor index bits
- **Return value:** Ring P scale factor

**4.3** `set_servo_i(servo_id, data)`

- **Function:** Set the proportional factor of the position ring I of the specified servo motor

- **Parameters:**
  - `servo_id`: `(int)` Motor index bit, value range `0 - 254`
  - `data`: `(int)` Ring I scale factor, value range `0 - 254`
- **Return value:** None

**4.4** `get_servo_i(servo_id)`

- **Function:** Reads the position loop I scale factor of the specified servo motor
- **Parameters:** 
  - `servo_id`: `(int)` Motor index bit, value range `0 - 254`
- **Return value:** 
  - `data`: `(int)` Ring I scale factor, range `0 -254`

**4.5** `set_servo_d(servo_id, data)`

- **Function:** Sets the proportional factor for the position ring D of the specified servo motor

- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
  - `data`: `(int)` `0 - 254`

- **Return value:** None

**4.6** `get_servo_d(servo_id)`

- **Function:** Reads the position ring D scale factor for the specified servo motor
- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
- **Return value:** 
    - `data`: `(int)` `0 - 254`

**4.7** `set_servo_cw(servo_id, data)`

- **Function:** Sets the clockwise insensitivity zone of the encoder for the specified servo motor
- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
  - `data`: `(int)` `0 - 32`
- **Return value:** None

**4.8** `get_servo_cw(servo_id)`

- **Function:** Reads the clockwise insensitive area of the encoder for the specified servo motor

- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
- **Return value:** 
  - `data`: `(int)` `0 - 32`

**4.9** `set_servo_cww(servo_id, data)`

- **Function:** Sets the counterclockwise insensitive zone of the encoder for the specified servo motor
- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
  - `data`: `(int)` `0 - 32`
- **Return value:** None

**4.10** `get_servo_cww(servo_id)`

- **Function:** Reads the counterclockwise insensitive area of the encoder of the specified servo motor
- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
- **Return value:** None

**4.11** `set_servo_system_data(servo_id, addr, data, mode)`

- **Function:** Set the system parameters for the specified servo motor

- **Parameters:**
  - `servo_id`: `(int) ` The index number of the servo motor, `1 - 6` according to the joint ID
  - `addr`: `(int)` Data address
  - `data`: `(int)` `0-4096` data
  - `mode`: `(int)` `1/2`
- **Return value:** None

**4.12** `get_servo_system_data(servo_id, addr, mode)`

- **Function:** Read the system parameters of the specified servo motor

- **Parameters:**
  - `servo_id`: `(int)` The index number of the servo motor, `1 - 6` according to the joint ID
  - `addr`: `(int)` Data address
  - `mode`: `(int)` `1/2`

- **Return value:** data

# 5. IO 控制

**5.1** `set_master_out_io_state(io_number, status)`

- **Function:** Set the master pin status
- **Parameters:**
  - `io_number`: `(int)` Pin position, value range `1 - 2`
  - `status`: `(int)`
    - 1 - High level
    - 0 - Low level
- **Return value:** None

**5.2** `get_master_in_io_state(io_number)`

- **Function:** Read the status of the master pins
- **Parameters:**
  - `io_number`: `(int)` Pin position, value range `1 - 2`
- **Return value:**
  - 1 - High level
  - 0 - Low level

**5.3** `set_tool_out_io_state(io_number, status)`
- **Function:** Sets the end pin status
- **Parameters:**
  - `io_number`: `(int)` Pin position, value range `1 - 2`
  - `status`: `(int)`
    - 1 - High level
    - 0 - Low level
- **Return value:** None

**5.4** `get_tool_in_io_state(io_number)`

- **Function:** Read the state of the end pins
- **Parameters:**
  - `io_number`: `(int)` Pin position, value range `1 - 2`
- **Return value:**
  - 1 - High level
  - 0 - Low level

# 6. Atom control

**6.1** `set_tool_led_color(r, g, b)`

- **Function:** Set the Atom LED color
- **Parameters:**
  - `R`: `(int)` `0 - 255`
  - `G`: `(int)` `0 - 255`
  - `B`: `(int)` `0 - 255`
- **Return value:** None

**6.2** `is_tool_btn_clicked()`

- **Function:** Read the Atom press status
- **Parameters:** None
- **Return value:**
   - 1 - Pressed
   - 0 - Not pressed

---

[← Previous page](1_download.md) | [Next page →](6_example.md)