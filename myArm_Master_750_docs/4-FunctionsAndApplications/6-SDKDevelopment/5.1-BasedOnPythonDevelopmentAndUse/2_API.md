# API 使用说明

> API (Application Programming Interface), 也称为应用程序编程接口函数，是预定义的函数。使用以下函数接口时，请在开始时输入以下代码导入我们的 API 库，否则将无法成功运行

> M750 固件支持以下接口:
> - [摇操固件接口](#摇操固件接口)
> - [坐标固件接口](#坐标固件接口)

# 摇操固件接口

```python
from pymycobot import MyArmM 

# 示例
m750 = MyArmM("COM3")

# 获取所有关节的当前角度
angles = m750.get_joints_angle()
print(angles)

# 将关节 1 设置为 move 40，并将速度设置为 20
m750.set_joint_angle(1, 40, 20)
```
### 1. 查询机器人的状态

#### **1.1** `get_robot_modified_version(self)`
- **功能:** 获取机器人更正版本号
- **返回:**
  - **版本 (int): 机器人更正版本号**
  
#### **1.2** `get_robot_firmware_version(self)`
- **功能:** 获取机器人固件版本（主要版本和次要版本）
- **返回:**
  - **版本(int): 机器人主要固件版本**
  
#### **1.3** `get_robot_tool_modified_version(self)`
- **功能:** 获取机器人工具的修复版本

#### **1.4** `get_robot_tool_firmware_version(self)`
- **功能:** 获取机器人工具固件版本(末端Atom)

#### **1.5** `set_robot_err_check_state(self, status)`

- **功能:** 设置错误检测状态 您可以关闭错误检测，但除非必要，否则不要将其关闭
- **参数:**
  - **status** - int
    - 1 - 打开错误检测
    - 0 - 关闭错误检测
- **返回:** 无

#### **1.6** `get_robot_err_check_state(self)`

- **功能:** 读取错误检测状态
- **参数:** 无
- **返回:**
  - 1 - 错误检测打开
  - 0 - 错误检测关闭

#### **1.7** `get_robot_error_status(self)`

- **功能:** 获取机器人错误状态, 此接口返回在15s内
- **参数:** 无
- **返回:** 没有错误返回: [0,0,0,0,0,0,0,0],假设在第 1 节中报告了错误 1 和 3，它应该返回：[[1,3]，0,0,0,0,0,0,0,0]

#### **1.8** `get_robot_power_status(self)`

- **功能:** 获取机器人电源状态
- **参数:** 无
- **返回:**
  - 1 - 开机状态
  - 0 - 关机状态

#### **1.9** `set_robot_power_on(self)`

- **功能:** 将机器人设置为开机状态
- **参数:** 无
- **返回:** 无

#### **1.10** `set_robot_power_off(self)`

- **功能:** 将机器人设置为关机状态
- **参数:** 无
- **返回:** 无
- 
#### **1.11** `clear_robot_err(self)`

- **功能:** 清除机器人异常，忽略报错关节，继续运动
- **参数:** 无
- **返回:** 无

#### **1.12** `get_recv_queue_max_len(self)`

- **功能:** 读取接收指令队列总长度
- **参数:** 无
- **返回:** `(int)` 指令队列总长度，默认值`100`
  
#### **1.13** `set_recv_queue_max_len(self, max_len)`

- **功能:** 设置接收指令队列总长度
- **参数:** 
  - `max_len`: `(int)` 队列长度
- **返回:**  无
- 
#### **1.14** `clear_recv_queue(self)`

- **功能:** 清除接收指令队列
- **参数:** 无
- **返回:** 无

#### **1.15** `get_recv_queue_len(self)`
- **功能:** 读取接收指令队列当前长度
- **参数:** 无
- **返回:** 当前指令队列长度

### 2. 联合伺服控制

#### **2.1** `get_joint_angle(self, joint_id)`

- **功能:** 获取指定关节的当前角度，当得到的角度为 200 时，表示该关节没有通信
- **参数:**
  - **joint_id (int): 0 - 254**
- **返回:**
  - **angle (int)**
  - 
#### **2.2** `set_joint_angle(self, joint_id, angle, speed)`

- **功能:** 将各个关节设置为移动到目标角度
- **参数:**
  - `joint_id`: `(int)` 关节编号
  - `angle`: `(int)` 目标角度
  - `speed`: `(int)` 移动速度，取值范围 `1 - 100`

#### **2.3** `get_joints_angle(self)`

- **功能:** 获取所有关节的当前角度，如果其中一个角度为 200，则表示该关节没有通信
- **返回:** 
  - `angles` 返回一个浮点型的列表，表示所有关节的当前角度
  
#### **2.4** `set_joints_angle(self, angles, speed)`

- **功能:** 将所有关节设置为移动到目标角度
- **参数:**
  - `angles`: `(list[int])` 目标角度
  - `speed`: `(int)` 移动速度，取值范围 `1 - 100`
  
#### **2.5** `get_joints_coord(self)`

- **功能:** 获取坐标
- **返回:**
  - **list[float] * 6: x, y, z, rx, ry, rz** 
  - 
#### **2.6** `is_robot_moving(self)`

- **功能:** 查看机器人是否在移动
- **参数:** 无
- **返回**
    - 1 - 正在移动
    - 0 - 静止
  
#### **2.7** `stop_robot(self)`
- **功能:** 机器人停止移动

#### **2.8** `get_joints_max(self)`
- **功能:** 读取所有关节的最大角度
- 
#### **2.9** `get_joints_min(self)`
- **功能:** 读取所有关节的最小角度

### 3. 伺服电机控制

#### **3.1** `set_servo_calibrate(self, servo_id)`

- **功能:** 设置指定伺服电动机的零位
- **参数:**
  - **servo_id (int): 0 - 254**
  
#### **3.2** `get_servo_encoder(self, servo_id)`
- **功能:** 获取指定伺服电动机的当前编码器电位值
- **参数:**
  - **servo_id (int): 0 - 254**
- **返回:**
  - **encoder (int): 0-4095**
  
#### **3.3** `set_servo_encoder(self, servo_id, encoder, speed)`
- **功能:** 将单个电机运动设置为目标编码器电位值
- **参数:**
  - **servo_id: (int) 0 - 254**
  - **encoder: (int) 0 - 4095**
  - **speed: (int) 1 - 100**
  
#### **3.4** `get_servos_encoder(self)`
- **功能:** 获取多个伺服电机的电流编码器电位值

#### **3.5** `set_servos_encoder(self, positions, speed)`
- **功能:** 设置移动到目标的多个电机的编码器电位值
- **参数:**
  - **positions (list[int * 8]): 0 - 4095:**
  - **speed (int): 1 - 100:**
  
#### **3.6** `get_servos_speed(self)`
- **功能:** 获取多个伺服电机的当前移动速度

#### **3.7** `set_servos_encoder_drag(self, encoders, speeds)`
- **功能:** 将多个具有指定速度的伺服电机设置为目标编码器电位值
- **参数:**
  - **encoders (list[int * 8]): 0 - 4095:**
  - **speeds (list[int * 8]): -10000 - 10000:**
  
#### **3.8** `get_servos_encoder_drag(self)`
- **功能:** 读取所有伺服电机的当前编码器值和运行速度
- **返回:**
  - **encoders (list[int * 8]): 0-4095**
  - **speeds (list[int * 8]): 0-4095**
  
#### **3.9** `is_all_servos_enabled(self)`
- **功能:** 获取多个伺服电机的连接状态
- **返回:**
  - **status: list[int*8] 0: 连接失败 1: 连接成功**

#### **3.10** `get_servos_temp(self)`
- **功能:** 获取多个伺服电机的温度

#### **3.11** `get_servos_voltage(self)`
- **功能:** 获取多个伺服电机的电压

#### **3.12** `get_servos_current(self)`
- **功能:** 获取多个伺服电机的电流

#### **3.13** `get_servos_status(self)`
- **功能:** 获取多个伺服电机的所有状态

#### **3.14** `get_servos_protect_current(self)`
- **功能:** 获得多个伺服电机保护电流

#### **3.15** `set_servo_enabled(self, servo_id, state)`
- **功能:** 设置伺服电机扭矩开关
- **参数:**
  - **servo_id (int): 0-254 254-all**
  - **state: 0/1**
  - **1-focus**
  - **0-release**

### 4. 伺服电机系统参数修改

#### **4.1** `set_servo_p(self, servo_id, data)`
- **功能:** 设置指定伺服电动机的位置回路 P 的比例系数
- **参数:**
  - **servo_id (int): 0-254**
  - **data (int): 0-254**
  
#### **4.2** `get_servo_p(self, servo_id)`
- **功能:** 读取指定伺服电动机的位置回路 P 比例因子
- **参数:**
  - **servo_id (int): 0-254**
  
#### **4.3** `set_servo_d(self, servo_id, data)`
- **功能:** 设置指定伺服电动机的位置环 D 的比例系数
- **参数:**
  - **servo_id (int): 0-254**
  - **data (int): 0-254**
  
#### **4.4** `get_servo_d(self, servo_id)`
- **功能:** 读取指定伺服电动机的位置环 D 比例因子
- **参数:**
  - **servo_id (int): 0-254**
  
#### **4.5** `set_servo_i(self, servo_id, data)`
- **功能:** 设置指定伺服电动机的位置环 I 的比例系数
- **参数:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 254**
  
#### **4.6** `get_servo_i(self, servo_id)`
- **功能:** 读取指定伺服电动机的位置回路 I 比例因子

#### **4.7** `set_servo_cw(self, servo_id, data)`
- **功能:** 为指定的伺服电动机设置编码器的顺时针不敏感区
- **参数:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 32**
  
#### **4.8** `get_servo_cw(self, servo_id)`
- **功能:** 读取指定伺服电机的编码器顺时针不敏感区域
- **参数:**
  - **servo_id (int): 0 - 254**
  
#### **4.9** `set_servo_cww(self, servo_id, data)`
- **功能:** 为指定的伺服电机设置编码器的逆时针不敏感区
- **参数:**
  - **servo_id (int): 0 - 254**
  - **data (int): 0 - 32**
  
#### **4.10** `get_servo_cww(self, servo_id)`
- **功能:** 读取指定伺服电机的编码器的逆时针不敏感区域
- **参数:**
  - **servo_id (int): 0 - 254**
  
#### **4.11** `restore_servo_system_param(self, servo_id)`
- **功能:** 恢复伺服电机系统参数
- **参数:**
  - **servo_id: 0 - 255**
  
#### **4.12** `set_servo_system_data(self, servo_id, addr, data, mode)`
- **功能:** 为指定的伺服电动机设置系统参数
- **参数:**
  - **servo_id (int): 0 - 254:**
  - **addr (int):**
  - **data (int): 0 - 4096**
  - **mode (int): 1 - data 1byte. 2 - data 2byte**
  
#### **4.13** `get_servo_system_data(self, servo_id, addr, mode)`
- **功能:** 读取指定伺服电机的系统参数
- **参数:**
  - **servo_id (int): 0 - 254**
  - **addr (int):**
  - **mode (int): 1 - data 1byte. 2 - data 2byte**

### 5. 主控IO控制

#### **5.1** `set_master_out_io_state(self, pin_number, status = 1)`

- **功能:** 设置主机 IO 引脚状态
- **参数:**
  - **pin_number: 1 -6**
  - **status: 0/1; 0: low; 1: high. default: 1**
#### **5.2** `get_master_in_io_state(self, pin_number)`

- **功能:** 获取主机 I/O 引脚状态
- **参数:**
  - **pin_number (int): M750(1 -6)**
- **返回:**
  - **0 or 1. 1: high 0: low**

### 6. 末端 IO 控制

#### **6.1** `set_tool_out_io_state(self, io_number, status = 1)`
- **功能:** 设置 Atom 引脚状态
- **参数:**
  - **io_number (int): 1 - 2**
  - **status: 0 or 1; 0: 低; 1: 高. 默认: 1**
  
#### **6.2** `get_tool_in_io_state(self, pin)`
- **功能:** 获取 Atom 引脚状态
- **参数:**
  - **pin (int): pin**
- **返回:**
  - **0 or 1. 1: 高 0: 低**
  
#### **6.3** `set_tool_led_color(self, r, g, b)`
- **功能:** 设置 Atom LED 颜色
- **参数:**
  - **r: 0-255**
  - **g: 0-255**
  - **b: 0-255**
  
#### **6.4** `is_tool_btn_clicked(self)`
- **功能:** 获取末端按钮状态
- **返回:**
  - **int: 0/1, 1: 按下, 0: 未按下**

# 坐标固件接口
```python
from pymycobot import MyArmMControl 

# 示例
arm_control = MyArmMControl('COM3')

# 获取所有关节的当前角度
angles = arm_control.get_angles()
print(angles)

# 将关节 1 设置为 move 40，并将速度设置为 20
arm_control.write_angle(1, 40, 20)
```
### 1. 系统状态

#### **1.1** `get_robot_modify_version(self)`
- **功能:** 获取机器人更正版本号

#### **1.2** `get_robot_system_version(self)`
- **功能:** 获取机器人固件版本（主要版本和次要版本）

#### **1.3** `get_robot_tool_modify_version(self)`
- **功能:** 获取机器人工具的修复版本

#### **1.4** `get_robot_tool_system_version(self)`
- **功能:** 获取机器人工具主版本号

### 2. Overall Status

#### **2.1** `power_on(self)`
- **功能:** 机械臂开启电源

#### **2.2** `power_off(self)`
- **功能:** 机械臂关闭电源

#### **2.3** `is_powered_on(self)`
- **功能:** 控制核心连接状态查询
- **返回:**
  - **1 - 开机**
  - **0 - 关闭电源**
  - **-1 - 错误**
  
#### **2.4** `release_all_servos(self, data)`
- **功能:** 机器人关闭扭矩输出
- **参数:**
  - **data: 1 - 取消阻尼（默认值为阻尼）**
  
#### **2.5** `set_fresh_mode(self, mode)`
- **功能:** 设置命令刷新模式
- **参数:**
  - **mode: int.**
  - **1 - 始终先执行最新的命令.**
  - **0 - 以队列的形式按顺序执行指令。**
  
#### **2.6** `get_fresh_mode(self)`
- **功能:** 查询运动模式

#### **2.7** `get_robot_status(self)`
- **功能:** 获取机器人状态

### 3. MDI mode and operation

#### **3.1** `get_angles(self)`
- **功能:** 获取所有关节的角度。
- **返回:**
  - **list: 所有角度的浮点型.**
  
#### **3.2** `write_angle(self, joint_id, degree, speed)`
- **功能:** 将关节的角度发送到机械臂。
- **参数:**
  - **joint_id: (int) 1 ~ 6**
  - **degree: (float) -150 ~ 150**
  - **speed : (int) 1 ~ 100**
  
#### **3.3** `write_angles(self, angles, speed)`
- **功能:** 将所有关节的角度发送到机械臂。
- **参数:**
  - **angles: (list) 所有角度的浮点列表。**
  - **speed : (int) 1 ~ 100**
  
#### **3.4** `get_coords(self)`
- **功能:** 获取所有关节的坐标。
- **返回:**
  - **list: 所有坐标的 float 列表。**
  
#### **3.5** `write_coord(self, coord_id, coord, speed)`
- **功能:** 将关节的坐标发送到机器人手臂。
- **参数:**
  - **coord_id: (int) 1 ~ 6**
  - **coord: (float) -150 ~ 150**
  - **speed : (int) 1 ~ 100**
  
#### **3.6** `write_coords(self, coords, speed, mode)`
- **功能:** 将所有关节的坐标发送到机械臂。
- **参数:**
  - **coords: (list) 所有坐标列表。**
  - **speed : (int) 1 ~ 100**
  
#### **3.7** `pause(self)`
- **功能:** 暂停移动

#### **3.8** `is_paused(self)`
- **功能:** 判断机械手是否暂停。
- **返回:**
  - **1 - paused**
  - **0 - not paused**
  - **-1 - error**
  
#### **3.9** `resume(self)`
- **功能:** 恢复运动

#### **3.10** `stop(self)`
- **功能:** 停止移动

#### **3.11** `is_in_position(self, data, mode = 0)`
- **功能:** 判断是否处于该位置。
- **参数:**
  - **data: 数据列表、角度或坐标。**
  - **对于 myArm：angles len 7，coords len 6。**
  - **模式： 1 - 坐标， 0 - 角度**
- **返回:**
  - **1 - 到位**
  - **0 - 未到位**
  - **-1 - 错误**
  
#### **3.12** `is_moving(self)`
- **功能:** 检测机器人是否在移动
- **返回:**
  - **0 - 不处于运动状态**
  - **1 - 处于运动状态**
  - **-1 - 错误**

### 4. JOG mode and operation

#### **4.1** `jog_angle(self, joint_id, direction, speed)`
- **功能:** 点动控制角度。
- **参数:**
  - **joint_id: int**
  - **for myArm: Joint id 1 - 7.**
  - **direction: 0 - 减少, 1 - 增加**
  - **speed: int (0 - 100)**
  
#### **4.2** `jog_rpy(self, end_direction, direction, speed)`
- **功能:** 在基础坐标系中绕固定轴旋转端点
- **参数:**
  - **end_direction (int):  横滚、俯仰、偏航 （1-3）**
  - **direction (int): 1 - 正向旋转，0 - 反向旋转**
  - **speed (int): 1 ~ 100**
  
#### **4.3** `jog_coord(self, coord_id, direction, speed)`
- **功能:** 点动控制坐标。
- **参数:**
  - **coord_id: int 1 ~ 6**
  - **direction: 0 - 减少, 1 - 增加**
  - **speed: int (1 - 100)**
  
#### **4.4** `jog_increment(self, joint_id, increment, speed)`
- **功能:** 步进模式
- **参数:**
  - **joint_id(int):**
  - **for myArm: Joint id 1 - 6.**
  - **increment(int): 增量**
  - **speed(int): int (0 - 100)**

### 5. 电动电位器控制方式

#### **5.1** `get_encoder(self, joint_id)`
- **功能:** 获取指定的关节电位值。
- **参数:**
  - **joint_id: (int)**
  - **for myArm: Joint id 1 - 7.**
  
#### **5.2** `get_encoders(self)`
- **功能:** 获取纵器的 6 个关节
- **返回:**
  - **编码器列表**

### 6. 软件关节限制

#### **6.1** `get_joint_min(self, joint_id)`
- **功能:** 获取指定关节的最小移动角度
- **参数:**
  - **joint_id:**
  - **对于 myArm：关节 ID 1 - 7。**
- **返回:**
  - **angle value(float)**
  - 
#### **6.2** `get_joint_max(self, joint_id)`
- **功能:** 获取指定关节的最大移动角度
- **参数:**
  - **joint_id:**
  - **for myArm: Joint id 1 - 7.**
- **返回:**
  - **angle value(float)**
  
#### **6.3** `set_joint_min(self, joint_id, angle)`
- **功能:** 设置关节最小角度
- **参数:**
  - **joint_id: int.**
  - **for myArm: Joint id 1 - 7.**
  - **angle: 0 ~ 180**
  
#### **6.4** `set_joint_max(self, joint_id, angle)`
- **功能:** 设置关节最大角度
- **参数:**
  - **joint_id: int.**
  - **for myArm: Joint id 1 - 7.**
  - **angle: 0 ~ 180**

### 7. 伺服控制

#### **7.1** `is_servo_enable(self, servo_id)`
- **功能:** 检测单个关节的连接状态
- **参数:**
  - **servo_id:**
  - **for myArm: Joint id 1 - 8.**
- **返回:**
  - **0 - 禁用**
  - **1 - 启用**
  - **-1 - 错误**
#### **7.2** `is_all_servo_enable(self)`
- **功能:** 检测所有关节的连接状态
- **返回:**
  - **0 - 禁用**
  - **1 - 启用**
  - **-1 - 错误**
  
#### **7.3** `set_servo_data(self, servo_id, data_id, value, mode)`
- **功能:** 设置舵机指定地址参数
- **参数:**
  - **servo_id: 舵机的序列号。**
  - **for myArm: joint id 1 - 8**
  - **data_id: 数据地址.**
  - **value: 0 - 4096**
  - **mode: 0 - 表示值为 1 个字节（默认），1 - 1 表示 2 个字节的值.**
  
#### **7.4** `get_servo_data(self, servo_id, data_id, mode)`
- **功能:** 读取舵机指定地址参数.
- **参数:**
  - **servo_id: 铰接式舵机的序列号。1 ~ 7**
  - **data_id: 数据地址。**
  - **mode: 0 - 表示值为 1 个字节（默认），1 - 1 表示 2 个字节的值.**
- **返回:**
  - **values 0 - 4096**
  
#### **7.5** `release_servo(self, servo_id, mode)`
- **功能:** 放松指定舵机
- **参数:**
  - **servo_id: int 1 ~ 8**
  - **mode: 默认阻尼，设置为 1 时，取消阻尼。**
  
#### **7.6** `focus_servo(self, servo_id)`
- **功能:** 锁定指定舵机
- **参数:**
  - **servo_id: int 1 ~ 7**
  
#### **7.7** `get_servo_speeds(self)`
- **功能:** 获取关节速度 。
- **返回:**
  - **speeds: list[float * 8] +- 3000 step/s**
  
#### **7.8** `get_servo_currents(self)`
- **功能:** 获取关节电流
- **返回:**
  - **currents: list[float * 8] 0 ~ 3250**
  
#### **7.9** `get_servo_voltages(self)`
- **功能:** 获取接头电压
- **返回:**
  - **voltages: list[float] voltage 0 ~ 240**
  
#### **7.10** `get_servo_status(self)`
- **功能:** 获取关节状态。
- **返回:**
  - **status: list[int] 0 ~ 255**
  - **0 - normal,**
  - **other - error**
  
#### **7.11** `get_servo_temps(self)`
- **功能:** 获取伺服电机温度
- **返回:**
  - **temperatures: list[float] 0 ~ 255**

### 8. Atom IO

#### **8.1** `set_digital_output(self, pin_no, pin_signal)`
- **功能:** 设置末端IO状态
- **参数:**
  - **pin_no     (int):**
  - **pin_signal (int): 0 / 1**
  
#### **8.2** `get_digital_input(self, pin_no)`
- **功能:** 获取末端IO状态
- **返回:**

### 9. Atom Button

#### **9.1** `set_led_color(self, r = 0, g = 0, b = 0)`
- **功能:** 设置末端颜色。
- **参数:**
  - **r (int): 0 ~ 255**
  - **g (int): 0 ~ 255**
  - **b (int): 0 ~ 255**
  
#### **9.2** `is_tool_btn_clicked(self)`
- **功能:** 判断机械臂顶部的按钮是否被点击。
- **返回:**
  - **0 - not clicked**
  - **1 - is clicked**
  - **-1- error data**

### 10. Gripper API

#### **10.1** `set_gripper_enabled(self)`
- **功能:** 启用夹爪

#### **10.2** `get_gripper_value(self)`
- **功能:** 获取夹爪角度值。
- **返回:**
  - **gripper value (int)**
  
#### **10.3** `set_gripper_state(self, flag, speed)`
- **功能:** 设置夹爪开关状态
- **参数:**
  - **flag  (int): 0 - 打开，1 - 关闭，254 - 释放**
  - **speed (int): 1 ~ 100**
  
#### **10.4** `set_gripper_value(self, gripper_value, speed)`
- **功能:** 设置夹持器值
- **参数:**
  - **gripper_value (int): 0 ~ 100**
  - **speed (int): 1 ~ 100**
  
#### **10.5** `set_gripper_calibration(self)`
- **功能:** 将当前位置设置为零，设置当前位置值为 '2048'。

#### **10.6** `is_gripper_moving(self)`
- **功能:** 判断夹爪是否移动
- **返回:**
  - **0 - not moving**
  - **1 - is moving**
  - **-1- error data**

### 11. Cartesian space parameter setting

#### **11.1** `set_tool_reference(self, coords)`
- **功能:** 设置工具坐标系
- **参数:**
  - **coords: 坐标值列表（List[float]）， [x（mm）， y， z， rx（angle）， ry， rz]**
  
#### **11.2** `get_tool_reference(self)`
- **功能:** 获取工具坐标系

#### **11.3** `set_world_reference(self, coords)`
- **功能:** 设置世界坐标系
- **参数:**
- **coords：坐标列表 value（List[float]）， [x（mm）， y， z， rx（angle）， ry， rz]**
  
#### **11.4** `get_world_reference(self)`
- **功能:** 获取世界坐标系

#### **11.5** `set_reference_frame(self, rftype)`
- **功能:** 设置基准坐标系
- **参数:**
  - **rftype: 0 - 底座 1 - 工具.**
  
#### **11.6** `get_reference_frame(self)`
- **功能:** 获取基本坐标系
- **返回:**
  - **0 - 底座 1 - 工具.**
  
#### **11.7** `set_movement_type(self, move_type)`
- **功能:** 设置移动类型
- **参数:**
  - **move_type: 1 - movel, 0 - moveJ**
  
#### **11.8** `get_movement_type(self)`
- **功能:** 获取移动类型
- **返回:**
  - **1 - movel, 0 - moveJ**
  
#### **11.9** `get_end_type(self)`
- **功能:** 获取终止坐标系
- **返回:**
  - **0 - 法兰, 1 - 工具**
  
#### **11.10** `set_end_type(self, mode)`
- **功能:** 设置终止坐标系
- **参数:**
  - **mode: int, 0 - 法兰, 1 - 工具**

### 12. 主控 IO 控制

#### **12.1** `set_basic_output(self, pin_no, pin_signal)`
- **功能:** 设置主控 IO 输出
- **参数:**
  - **pin_no: pin port number.**
  - **pin_signal: 0 / 1**
  
#### **12.2** `get_basic_input(self, pin_no)`
- **功能:** 读取主控 IO 输入
- **参数:**
  - **pin_no: (int) pin port number.**

### 13. WLAN 设置

#### **13.1** `set_ssid_pwd(self, account: str, password: str)`

- **功能:** 更改连接的 Wi-Fi.
- **参数:**
  - **account: (str) 新的 Wi-Fi 帐户.**
  - **password: (str) 新 Wi-Fi 密码.**
  
#### **13.2** `get_ssid_pwd(self)`
- **功能:** 获取连接的 Wi-Fi 帐户和密码。
- **返回:**
  - **(帐户, 密码)**
  
#### **13.3** `set_server_port(self, port)`
- **功能:** 更改服务器的连接端口。
- **参数:**
  - **port: (int) 服务器的新连接端口.**
  
---

[← 上一页](1_download.md) | [下一页 →](6_example.md)