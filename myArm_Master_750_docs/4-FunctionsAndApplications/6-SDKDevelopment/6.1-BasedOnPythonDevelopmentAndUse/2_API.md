# Introduction to API

API or Application Programming Interface refers to a number of preset programs. Before utilization, it is required to import API library

> The M750 firmware supports the following interfaces:
> - [Shake Firmware API](#shake-firmware-api)
> - [Coordinate Firmware API](#coordinate-firmware-api)

# Shake Firmware API

```python
from pymycobot import MyArmM 

# Example
m750 = MyArmM("COM3")

# Gets the current angle of all joints
angles = m750.get_joints_angle()
print(angles)

# Set joint 1 to move to 40 and set the speed to 20
m750.set_joint_angle(1, 40, 20)
```
### 1. Query the status of the bot

#### **1.1** `get_robot_modified_version(self)`

- **function:** Get the bot correction version number
- **Return value:**
  - **version (int): the bot correction version number**
#### **1.2** `get_robot_firmware_version(self)`

- **function:** Obtaining the Robot Firmware Version (Major and Minor Versions)
- **Return value:**
  - **version (int): the robot firmware**
#### **1.3** `get_robot_tool_modified_version(self)`

- **function:** Get the remediation version of the bot tool
#### **1.4** `get_robot_tool_firmware_version(self)`

- **function:** Get the Robot Tool Firmware Version (End Atom)
#### **1.5** `set_robot_err_check_state(self, status)`

- **function:** Set Error Detection Status You can turn off error detection, but do not turn it off unless necessary
- **Parameters:**
  - **status (int): 1 open; o close**
#### **1.6** `get_robot_err_check_state(self)`

- **function:** Read error detection status
#### **1.7** `get_robot_error_status(self)`

- **function:** Get the bot error status
- **Return value:**
  - **No error: [0,0,0,0,0,0,0,0]**
  - **assuming that error 1 and 3 are reported in section 1, it should return: [[1,3],0,0,0,0,0,0,0]**
#### **1.8** `get_robot_power_status(self)`

- **function:** Get the robot power status
- **Return value:**
  - **power_status (int): 0: power off, 1: power on**
#### **1.9** `set_robot_power_on(self)`

- **function:** Set the robot to power on
#### **1.10** `set_robot_power_off(self)`

- **function:** Set the robot to power off
#### **1.11** `clear_robot_err(self)`

- **function:** Clear the robot abnormality Ignore the error joint and continue to move
#### **1.12** `get_recv_queue_max_len(self)`

- **function:** The total length of the read command queue, the default length is 100
#### **1.13** `set_recv_queue_max_len(self, max_len)`

- **function:** Set the total length of the receiving command queue
#### **1.14** `clear_recv_queue(self)`

- **function:** Clear the queue for receiving commands
#### **1.15** `get_recv_queue_len(self)`

- **function:** The current length of the read receive queue

### 2. Joint servo control

#### **2.1** `get_joint_angle(self, joint_id)`

- **function:** Obtain the current angle of the specified joint, when the obtained angle is 200,
  - **it means that the joint has no communication**
- **Parameters:**
  - **joint_id (int): 0 - 254**
- **Return value:**
  - **angle (int)**
#### **2.2** `set_joint_angle(self, joint_id, angle, speed)`

- **function:** Sets the individual joints to move to the target angle
- **Parameters:**
  - **joint_id (int) : 0 - 254**
  - **angle (int) : 0 - 254**
  - **speed (int) : 1 - 100**
#### **2.3** `get_joints_angle(self)`

- **function:** Obtain the current angle of all joints, if one of the angles is 200��,
  - **it means that the joint has no communication**
- **Return value:**
  - **angles list(int): 0 - 254**
#### **2.4** `set_joints_angle(self, angles, speed)`

- **function:** Sets all joints to move to the target angle
- **Parameters:**
  - **angles (list[int]):  0 - 254**
  - **speed (int): 0 - 100**
#### **2.5** `get_joints_coord(self)`

- **function:** Get the coordinates
- **Return value:**
  - **list[float] * 6: joints angle**
#### **2.6** `is_robot_moving(self)`

- **function:** See if the robot is moving
- **Return value:**
  - **1: moving**
  - **0: not moving**
#### **2.7** `stop_robot(self)`

- **function:** The robot stops moving
#### **2.8** `get_joints_max(self)`

- **function:** Read the maximum angle of all joints
#### **2.9** `get_joints_min(self)`

- **function:** Read the minimum angle of all joints

### 3. Servo motor control

#### **3.1** `set_servo_calibrate(self, servo_id)`

- **function:** Sets the zero position of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
#### **3.2** `get_servo_encoder(self, servo_id)`

- **function:** Gets the current encoder potential value for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
- **Return value:**
  - **encoder (int): 0-4095**
#### **3.3** `set_servo_encoder(self, servo_id, encoder, speed)`

- **function:** Sets the individual motor motion to the target encoder potential value
- **Parameters:**
  - **servo_id: (int) 0 - 254**
  - **encoder: (int) 0 - 4095**
  - **speed: (int) 1 - 100**
#### **3.4** `get_servos_encoder(self)`

- **function:** Obtain the current encoder potential values for multiple servo motors
#### **3.5** `set_servos_encoder(self, positions, speed)`

- **function:** Set the encoder potential value for multiple motors moving to the target
- **Parameters:**
  - **positions (list[int * 8]): 0 - 4095:**
  - **speed (int): 1 - 100:**
#### **3.6** `get_servos_speed(self)`

- **function:** Gets the current movement speed of multiple servo motors
#### **3.7** `set_servos_encoder_drag(self, encoders, speeds)`

- **function:** Set multiple servo motors with a specified speed to the target encoder potential value
- **Parameters:**
  - **encoders (list[int * 8]): 0 - 4095:**
  - **speeds (list[int * 8]): -10000 - 10000:**
#### **3.8** `get_servos_encoder_drag(self)`

- **function:** Reads the current encoder value and operating speed of all servo motors
- **Return value:**
  - **encoders (list[int * 8]): 0-4095**
  - **speeds (list[int * 8]): 0-4095**
#### **3.9** `is_all_servos_enabled(self)`

- **function:** Get the connection status of multiple servo motors
- **Return value:**
  - **status: list[int*8] 0: The connection failed 1: The connection is successful**
#### **3.10** `get_servos_temp(self)`

- **function:** Obtain the temperature of multiple servo motors
#### **3.11** `get_servos_voltage(self)`

- **function:** Get the voltage of multiple servo motors
#### **3.12** `get_servos_current(self)`

- **function:** Obtain the current of multiple servo motors
#### **3.13** `get_servos_status(self)`

- **function:** Get all the statuses of multiple servo motors
#### **3.14** `get_servos_protect_current(self)`

- **function:** Obtain multiple servo motor protection currents
#### **3.15** `set_servo_enabled(self, servo_id, state)`

- **function:** Set the servo motor torque switch
- **Parameters:**
  - **servo_id (int): 0-254 254-all**
  - **state: 0/1**
  - **1-focus**
  - **0-release**

### 4. Servo motor system parameter modification

#### **4.1** `set_servo_p(self, servo_id, data)`

- **function:** Sets the proportionality factor of the position loop P of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0-254**
  - **data (int): 0-254**
#### **4.2** `get_servo_p(self, servo_id)`

- **function:** Reads the position loop P scale factor of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0-254**
#### **4.3** `set_servo_d(self, servo_id, data)`

- **function:** Sets the proportional factor for the position ring D of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0-254**
  - **data (int): 0-254**
#### **4.4** `get_servo_d(self, servo_id)`

- **function:** Reads the position ring D scale factor for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0-254**
#### **4.5** `set_servo_i(self, servo_id, data)`

- **function:** Set the proportional factor of the position ring I of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 254**
#### **4.6** `get_servo_i(self, servo_id)`

- **function:** Reads the position loop I scale factor of the specified servo motor
#### **4.7** `set_servo_cw(self, servo_id, data)`

- **function:** Sets the clockwise insensitivity zone of the encoder for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 32**
#### **4.8** `get_servo_cw(self, servo_id)`

- **function:** Reads the clockwise insensitive area of the encoder for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
#### **4.9** `set_servo_cww(self, servo_id, data)`

- **function:** Sets the counterclockwise insensitive zone of the encoder for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 32**
#### **4.10** `get_servo_cww(self, servo_id)`

- **function:** Reads the counterclockwise insensitive area of the encoder of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
#### **4.11** `restore_servo_system_param(self, servo_id)`

- **function:** Restore servo motor system parameters
- **Parameters:**
  - **servo_id: 0 - 255**
#### **4.12** `set_servo_system_data(self, servo_id, addr, data, mode)`

- **function:** Set the system parameters for the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254:**
  - **addr (int):**
  - **data (int): 0 - 4096**
  - **mode (int): 1 - data 1byte. 2 - data 2byte**
#### **4.13** `get_servo_system_data(self, servo_id, addr, mode)`

- **function:** Read the system parameters of the specified servo motor
- **Parameters:**
  - **servo_id (int): 0 - 254**
  - **addr (int):**
  - **mode (int): 1 - data 1byte. 2 - data 2byte**

### 5. Master IO Control

#### **5.1** `set_master_out_io_state(self, pin_number, status = 1)`

- **function:** Set the host I/O pin status
- **Parameters:**
  - **pin_number: M750(1 -6), C650(1-2)**
  - **status: 0/1; 0: low; 1: high. default: 1**
#### **5.2** `get_master_in_io_state(self, pin_number)`

- **function:** get the host I/O pin status
- **Parameters:**
  - **pin_number (int): M750(1 -6), C650(1-2)**
- **Return value:**
  - **0 or 1. 1: high 0: low**

### 6. Slave IO Control

#### **6.1** `set_tool_out_io_state(self, io_number, status = 1)`

- **function:** Set the Atom pin status
- **Parameters:**
  - **io_number (int): 1 - 2**
  - **status: 0 or 1; 0: low; 1: high. default: 1**
#### **6.2** `get_tool_in_io_state(self, pin)`

- **function:** Get the Atom pin status
- **Parameters:**
  - **pin (int): pin**
- **Return value:**
  - **0 or 1. 1: high 0: low**
#### **6.3** `set_tool_led_color(self, r, g, b)`

- **function:** Set the Atom LED color
- **Parameters:**
  - **r: 0-255**
  - **g: 0-255**
  - **b: 0-255**
#### **6.4** `is_tool_btn_clicked(self)`

- **function:** get the end button status
- **Return value:**
  - **int: 0/1, 1: press, 0: no press**

# Coordinate Firmware API
```python
from pymycobot import MyArmMControl 

# Example
arm_control = MyArmMControl('COM3')

# Gets the current angle of all joints
angles = arm_control.get_angles()
print(angles)

# Set joint 1 to move to 40 and set the speed to 20
arm_control.write_angle(1, 40, 20)
```
### 1. System Status

#### **1.1** `get_robot_modify_version(self)`

- **function:** Get the bot correction version number
#### **1.2** `get_robot_system_version(self)`

- **function:** Obtaining the Robot Firmware Version (Major and Minor Versions)
#### **1.3** `get_robot_tool_modify_version(self)`

- **function:** Get the remediation version of the bot tool
#### **1.4** `get_robot_tool_system_version(self)`

- **function:** Get the Robot Tool Firmware Version (End Atom)

### 2. Overall Status

#### **2.1** `power_on(self)`

- **function:** The robotic arm turns on the power
#### **2.2** `power_off(self)`

- **function:** The robotic arm turns off the power
#### **2.3** `is_powered_on(self)`

- **function:** Control core connection status queries
- **Return value:**
  - **1 - power on**
  - **0 - power off**
  - **-1 - error data**
#### **2.4** `release_all_servos(self, data)`

- **function:** The robot turns off the torque output
- **Parameters:**
  - **data: 1 - Un damping (The default is damping)**
#### **2.5** `set_fresh_mode(self, mode)`

- **function:** Set command refresh mode
- **Parameters:**
  - **mode: int.**
  - **1 - Always execute the latest command first.**
  - **0 - Execute instructions sequentially in the form of a queue.**
#### **2.6** `get_fresh_mode(self)`

- **function:** Query sports mode
#### **2.7** `get_robot_status(self)`

- **function:** Get robot status

### 3. MDI mode and operation

#### **3.1** `get_angles(self)`

- **function:** Get the angle of all joints.
- **Return value:**
  - **list: A float list of all angle.**
#### **3.2** `write_angle(self, joint_id, degree, speed)`

- **function:** Send the angle of a joint to robot arm.
- **Parameters:**
  - **joint_id: (int) 1 ~ 6**
  - **degree: (float) -150 ~ 150**
  - **speed : (int) 1 ~ 100**
#### **3.3** `write_angles(self, angles, speed)`

- **function:** Send the angles of all joints to robot arm.
- **Parameters:**
  - **angles: (list) A float list of all angle.**
  - **speed : (int) 1 ~ 100**
#### **3.4** `get_coords(self)`

- **function:** Get the coordinates of all joints.
- **Return value:**
  - **list: A float list of all coordinates.**
#### **3.5** `write_coord(self, coord_id, coord, speed)`

- **function:** Send the coordinates of a joint to robot arm.
- **Parameters:**
  - **coord_id: (int) 1 ~ 6**
  - **coord: (float) -150 ~ 150**
  - **speed : (int) 1 ~ 100**
#### **3.6** `write_coords(self, coords, speed, mode)`

- **function:** Send the coordinates of all joints to robot arm.
- **Parameters:**
  - **coords: (list) A float list of all coordinates.**
  - **speed : (int) 1 ~ 100**
  - **mode: (int) 0 - normal, 1 - low, 2 - high**
#### **3.7** `pause(self)`

- **function:** Pause movement
#### **3.8** `is_paused(self)`

- **function:** Judge whether the manipulator pauses or not.
- **Return value:**
  - **1 - paused**
  - **0 - not paused**
  - **-1 - error**
#### **3.9** `resume(self)`

- **function:** Recovery movement
#### **3.10** `stop(self)`

- **function:** Stop moving
#### **3.11** `is_in_position(self, data, mode = 0)`

- **function:** Judge whether in the position.
- **Parameters:**
  - **data: A data list, angles or coords.**
  - **for myArm: angles len 7, coords len 6.**
  - **mode: 1 - coords, 0 - angles**
- **Return value:**
  - **1 - True**
  - **0 - False**
  - **-1 - Error**
#### **3.12** `is_moving(self)`

- **function:** Detect if the robot is moving
- **Return value:**
  - **0 - not moving**
  - **1 - is moving**
  - **-1 - error data**

### 4. JOG mode and operation

#### **4.1** `jog_angle(self, joint_id, direction, speed)`

- **function:** Jog control angle.
- **Parameters:**
  - **joint_id: int**
  - **for myArm: Joint id 1 - 7.**
  - **direction: 0 - decrease, 1 - increase**
  - **speed: int (0 - 100)**
#### **4.2** `jog_rpy(self, end_direction, direction, speed)`

- **function:** Rotate the end around a fixed axis in the base coordinate system
- **Parameters:**
  - **end_direction (int):  Roll, Pitch, Yaw (1-3)**
  - **direction (int): 1 - forward rotation, 0 - reverse rotation**
  - **speed (int): 1 ~ 100**
#### **4.3** `jog_coord(self, coord_id, direction, speed)`

- **function:** Jog control coord.
- **Parameters:**
  - **coord_id: int 1 ~ 6**
  - **direction: 0 - decrease, 1 - increase**
  - **speed: int (1 - 100)**
#### **4.4** `jog_increment(self, joint_id, increment, speed)`

- **function:** step mode
- **Parameters:**
  - **joint_id(int):**
  - **for myArm: Joint id 1 - 6.**
  - **increment(int): incremental**
  - **speed(int): int (0 - 100)**

### 5. Motor potentiometer control mode

#### **5.1** `get_encoder(self, joint_id)`

- **function:** Obtain the specified joint potential value.
- **Parameters:**
  - **joint_id: (int)**
  - **for myArm: Joint id 1 - 7.**
#### **5.2** `get_encoders(self)`

- **function:** Get the six joints of the manipulator
- **Return value:**
  - **The list of encoders**

### 6. Software joint limit

#### **6.1** `get_joint_min(self, joint_id)`

- **function:** Gets the minimum movement angle of the specified joint
- **Parameters:**
  - **joint_id:**
  - **for myArm: Joint id 1 - 7.**
- **Return value:**
  - **angle value(float)**
#### **6.2** `get_joint_max(self, joint_id)`

- **function:** Gets the maximum movement angle of the specified joint
- **Parameters:**
  - **joint_id:**
  - **for myArm: Joint id 1 - 7.**
- **Return value:**
  - **angle value(float)**
#### **6.3** `set_joint_min(self, joint_id, angle)`

- **function:** Set the joint minimum angle
- **Parameters:**
  - **joint_id: int.**
  - **for myArm: Joint id 1 - 7.**
  - **angle: 0 ~ 180**
#### **6.4** `set_joint_max(self, joint_id, angle)`

- **function:** Set the joint maximum angle
- **Parameters:**
  - **joint_id: int.**
  - **for myArm: Joint id 1 - 7.**
  - **angle: 0 ~ 180**

### 7. Servo control

#### **7.1** `is_servo_enable(self, servo_id)`

- **function:** To detect the connection state of a single joint
- **Parameters:**
  - **servo_id:**
  - **for myArm: Joint id 1 - 8.**
- **Return value:**
  - **0 - disable**
  - **1 - enable**
  - **-1 - error**
#### **7.2** `is_all_servo_enable(self)`

- **function:** Detect the connection status of all joints
- **Return value:**
  - **0 - disable**
  - **1 - enable**
  - **-1 - error**
#### **7.3** `set_servo_data(self, servo_id, data_id, value, mode)`

- **function:** Set the data parameters of the specified address of the steering gear
- **Parameters:**
  - **servo_id: Serial number of articulated steering gear.**
  - **for myArm: joint id 1 - 8**
  - **data_id: Data address.**
  - **value: 0 - 4096**
  - **mode: 0 - indicates that value is one byte(default), 1 - 1 represents a value of two bytes.**
#### **7.4** `get_servo_data(self, servo_id, data_id, mode)`

- **function:** Read the data parameter of the specified address of the steering gear.
- **Parameters:**
  - **servo_id: Serial number of articulated steering gear. 1 ~ 7**
  - **data_id: Data address.**
  - **mode: 0 - indicates that value is one byte(default), 1 - 1 represents a value of two bytes.**
- **Return value:**
  - **values 0 - 4096**
#### **7.5** `release_servo(self, servo_id, mode)`

- **function:** Power off designated servo
- **Parameters:**
  - **servo_id: int 1 ~ 8**
  - **mode: Default damping, set to 1, cancel damping**
#### **7.6** `focus_servo(self, servo_id)`

- **function:** Power on designated servo
- **Parameters:**
  - **servo_id: int 1 ~ 7**
#### **7.7** `get_servo_speeds(self)`

- **function:** Get the joint speed .
- **Return value:**
  - **speeds: list[float * 8] +- 3000 step/s**
#### **7.8** `get_servo_currents(self)`

- **function:** Get the joint current
- **Return value:**
  - **currents: list[float * 8] 0 ~ 3250**
#### **7.9** `get_servo_voltages(self)`

- **function:** Get the joint voltages
- **Return value:**
  - **voltages: list[float] voltage 0 ~ 240**
#### **7.10** `get_servo_status(self)`

- **function:** Get the joint status.
- **Return value:**
  - **status: list[int] 0 ~ 255**
  - **0 - normal,**
  - **other - error**
#### **7.11** `get_servo_temps(self)`

- **function:** Get joint temperature
- **Return value:**
  - **temperatures: list[float] 0 ~ 255**

### 8. Atom IO

#### **8.1** `set_digital_output(self, pin_no, pin_signal)`

- **function:** Set the terminal atom io status
- **Parameters:**
  - **pin_no     (int):**
  - **pin_signal (int): 0 / 1**
#### **8.2** `get_digital_input(self, pin_no)`

- **function:** Get the terminal atom io status
- **Return value:**

### 9. Atom Button

#### **9.1** `set_led_color(self, r = 0, g = 0, b = 0)`

- **function:** Set the light color on the top of the robot arm.
- **Parameters:**
  - **r (int): 0 ~ 255**
  - **g (int): 0 ~ 255**
  - **b (int): 0 ~ 255**
#### **9.2** `is_tool_btn_clicked(self)`

- **function:** Judge whether the button on the top of the robot arm is clicked or not.
- **Return value:**
  - **0 - not clicked**
  - **1 - is clicked**
  - **-1- error data**

### 10. Gripper API

#### **10.1** `set_gripper_enabled(self)`

- **function:** Enable gripper
#### **10.2** `get_gripper_value(self)`

- **function:** Get the value of gripper.
- **Return value:**
  - **gripper value (int)**
#### **10.3** `set_gripper_state(self, flag, speed)`

- **function:** Set gripper switch state
- **Parameters:**
  - **flag  (int): 0 - open, 1 - close, 254 - release**
  - **speed (int): 1 ~ 100**
#### **10.4** `set_gripper_value(self, gripper_value, speed)`

- **function:** Set gripper value
- **Parameters:**
  - **gripper_value (int): 0 ~ 100**
  - **speed (int): 1 ~ 100**
#### **10.5** `set_gripper_calibration(self)`

- **function:** Set the current position to zero, set current position value is `2048`.
#### **10.6** `is_gripper_moving(self)`

- **function:** Judge whether the gripper is moving or not
- **Return value:**
  - **0 - not moving**
  - **1 - is moving**
  - **-1- error data**

### 11. Cartesian space parameter setting

#### **11.1** `set_tool_reference(self, coords)`

- **function:** Set tool coordinate system
- **Parameters:**
  - **coords: a list of coords value(List[float]), [x(mm), y, z, rx(angle), ry, rz]**
#### **11.2** `get_tool_reference(self)`

- **function:** Get tool coordinate system
#### **11.3** `set_world_reference(self, coords)`

- **function:** Set the world coordinate system
- **Parameters:**
  - **coords: a list of coords value(List[float]), [x(mm), y, z, rx(angle), ry, rz]**
#### **11.4** `get_world_reference(self)`

- **function:** Get the world coordinate system
#### **11.5** `set_reference_frame(self, rftype)`

- **function:** Set the base coordinate system
- **Parameters:**
  - **rftype: 0 - base 1 - tool.**
#### **11.6** `get_reference_frame(self)`

- **function:** Get the base coordinate system
- **Return value:**
  - **0 - base 1 - tool.**
#### **11.7** `set_movement_type(self, move_type)`

- **function:** Set movement type
- **Parameters:**
  - **move_type: 1 - movel, 0 - moveJ**
#### **11.8** `get_movement_type(self)`

- **function:** Get movement type
- **Return value:**
  - **1 - movel, 0 - moveJ**
#### **11.9** `get_end_type(self)`

- **function:** Get end coordinate system
- **Return value:**
  - **0 - flange, 1 - tool**
#### **11.10** `set_end_type(self, mode)`

- **function:** Set end coordinate system
- **Parameters:**
  - **mode: int, 0 - flange, 1 - tool**

### 12. Basic IO Control

#### **12.1** `set_basic_output(self, pin_no, pin_signal)`

- **function:** Set the base IO output
- **Parameters:**
  - **pin_no: pin port number.**
  - **pin_signal: 0 / 1**
#### **12.2** `get_basic_input(self, pin_no)`

- **function:** Read the base IO output
- **Parameters:**
  - **pin_no: (int) pin port number.**

### 13. WLAN Setting

#### **13.1** `set_ssid_pwd(self, account: str, password: str)`

- **function:** Change connected wi-fi.
- **Parameters:**
  - **account: (str) new wi-fi account.**
  - **password: (str) new wi-fi password.**
#### **13.2** `get_ssid_pwd(self)`

- **function:** Get connected wi-fi account and password.
- **Return value:**
  - **(account, password)**
#### **13.3** `set_server_port(self, port)`

- **function:** Change the connection port of the server.
- **Parameters:**
  - **port: (int) The new connection port of the server.**
  
---

[← 上一页](1_download.md) | [下一页 →](6_example.md)