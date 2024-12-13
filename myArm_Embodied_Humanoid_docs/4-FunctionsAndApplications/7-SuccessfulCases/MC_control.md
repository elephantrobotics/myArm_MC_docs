# C650控制M750程序案例

## 程序地址
> https://github.com/elephantrobotics/mc_embodied_kit_ros/blob/main/myarm_m/scripts/mc_embodied_control.py

首先我们需要将MyarmM750机械臂通过USB转typeC线连接到系统上，并给其通电  
通过按钮选中 **Transponder** 再按“OK”按钮
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

然后屏幕会显示  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

我们可以看到箭头指向 **“USB UART”** ，再按“OK”按钮，进入之后会显示 **“NO”**，再按 **“Exit”** 按钮，回到箭头指向 **“USB UART”** ，再按“OK”按钮，这时会显示 **“OK”**
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

首先我们需要将MyarmC650机械臂通过USB转typeC线连接到系统上，并给其通电  
通过按钮选中 **Transponder** 再按“OK”按钮  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

然后屏幕会显示  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

我们可以看到箭头指向 **“USB UART”** ，再按“OK”按钮，进入之后会显示 **“NO”**，再按 **“Exit”** 按钮，回到箭头指向 **“USB UART”** ，再按“OK”按钮，这时会显示 **“OK”**  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

#### 这时我们的MyarmM750 和 MyArmC650已经成功启动
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/MC_1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

此功能需要将四台机械臂通过USB的方式同时连接到系统上，我们要区分每台机械臂连接我们的串口是多少，新建终端：  

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/tty.jpg" alt="7.1.1-1" style="zoom:100%;" />    

按 **TAB键**  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/tty1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**如何区分串口号：先连接一台机械臂然后输入ls /dev/tty查看当前串口号，在不断开这一台机械臂的情况下，连接另一台机械臂，输入该指令查看四个机械臂的串口号** 
根据对应的串口号修改**mc_embodied_kit_ros/myarm_m/scripts/mc_embodied_control.py文件**中的串口号，如图：
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_serial.jpg" alt="7.1.1-1" style="zoom:100%;" />

在工作空间新建一个终端输入：  
> roscore  
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:100%;" />   

再新建一个终端，输入：   
> roslaunch myarm_m mc_embodied_control.launch  

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_rviz.jpg" alt="7.1.1-1" style="zoom:100%;" />   

启动rviz仿真之后，再打开一个新的Terminal，输入：
> rosrun myarm_m mc_embodied_control.py

即可实现MyarmC650控制MyarmM750的功能
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_rviz_2.jpg" alt="7.1.1-1" style="zoom:100%;" />    

此时，我们就能用手去运动MyarmC650机械臂，rivz中的两款机械臂都跟随现实中的MyarmC650运动，在此同时，现实中的MayrmM750机械臂也会跟随MyarmC650运动（夹抓功能也可以运动）  

<video src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_run.mp4" controls="controls" width="800" height="500"></video>


## 至此，MyarmC650控制MyarmM750的功能全部实现

### 以下为MyArm M&C 具身人型复合套件实现的具体案例视频

#### 收纳

<video src="../../resources/7-SuccessfulCases/收纳.mp4" controls="controls" width="800" height="500"></video>

#### 推椅子

<video src="../../resources/7-SuccessfulCases/推椅子.mp4" controls="controls" width="800" height="500"></video>


---