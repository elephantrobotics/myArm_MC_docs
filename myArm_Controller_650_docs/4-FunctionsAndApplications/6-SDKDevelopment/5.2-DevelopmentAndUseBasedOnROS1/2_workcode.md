# 一、仿真

我们提供一些 **静态仿真** 和 **动态仿真**， 用以和 MyarmC650 交互。  


## 1.1 静态仿真
这里的静态仿真是指：用rviz中的滑动模块与仿真中的MyarmC650交互  
在工作空间打开终端命令行中输入:  
> roscore

> source devel/setup.bash # 添加环境变量  
> roslaunch myarm_c650 test.launch  


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch2.jpg" alt="7.1.1-1" style="zoom:100%;" />   

**成功运行launch文件后，终端会显示：**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch3.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**同时会打开rviz，生成MyarmC650的仿真模型**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch4.jpg" alt="7.1.1-1" style="zoom:100%;" />  


## 1.2 动态仿真
这里的动态仿真是指：运动现实中的MyarmC650与仿真中的MyarmC650交互  

首先我们需要将MyarmC650机械臂通过USB转typeC线连接到我们的电脑上，并给其通电  
通过按钮选中 **Transponder** 再按“OK”按钮
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/Myarm1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

然后屏幕会显示  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/Myarm2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

我们可以看到箭头指向 **“USB UART”** ，再按“OK”按钮，进入之后会显示 **“NO”**，再按 **“Exit”** 按钮，回到箭头指向 **“USB UART”** ，再按“OK”按钮，这时会显示 **“OK”**
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/Myarm3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

#### 这时我们的MyarmC650已经成功连接上电脑


接下来在工作空间打开终端命令行中输入:  
> source devel/setup.bash # 添加环境变量  
> roslaunch myarm_c650 test.launch  


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch2.jpg" alt="7.1.1-1" style="zoom:100%;" />   

**成功运行launch文件后，终端会显示：**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch3.jpg" alt="7.1.1-1" style="zoom:100%;" />    

rviz文件也会正常显示
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch5.jpg" alt="7.1.1-1" style="zoom:100%;" />  


打开VS code中的项目，找到  myArm/myarm_c650/scripts/test.py 这个 **test.py** 文件  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/runpython1.jpg" alt="7.1.1-1" style="zoom:100%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/runpython2.jpg" alt="7.1.1-1" style="zoom:100%;" />  

在工作空间里再新建一个终端，输入下面指令，杀死节点：  
> rosnode kill /joint_state_publisher_gui   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/kill1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

我们也可以继续在终端输入下面的指令，以便查看MyarmC650每个关节的角度变化：  
> rostopic echo /joint_state  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/topic1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

接下来我们用手移动现实中的MyarmC650机械臂，rviz中的机械臂也会跟着运动：  
> rosnode kill /joint_state_publisher_gui   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch6.jpg" alt="7.1.1-1" style="zoom:100%;" />    

#### 至此与MyarmC650机械臂的交互已全部完成

# 二、MyarmC650控制MyarmM750运动
此功能需要将两台机械臂通过USB的方式同时连接到我们的电脑上，我们要区分每台机械臂连接我们的串口是多少，新建终端：  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/tty.jpg" alt="7.1.1-1" style="zoom:100%;" />    

按 **TAB键**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/tty1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**如何区分串口号：先连接一台机械臂然后输入ls /dev/tty查看当前串口号，在不断开这一台机械臂的情况下，连接另一台机械臂，输入该指令查看串口号**  

在工作空间新建一个终端输入：  
> roscore  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:100%;" />   

再新建一个终端，输入：  
> source devel/setup.bash
> roslaunch myarm_m combined_control.launch  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch.jpg" alt="7.1.1-1" style="zoom:100%;" />   

启动rviz仿真之后，再打开**myArm/myarm_m/scripts/combined_control.py** 路径下的.py文件   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedrunpython.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedrunpython1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

此时，我们就能用手去运动MyarmC650机械臂，rivz中的两款机械臂都跟随现实中的MyarmC650运动，在此同时，现实中的MayrmM750机械臂也会跟随MyarmC650运动（夹抓功能也可以运动）  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch2.jpg" alt="7.1.1-1" style="zoom:100%;" />    

## 至此，MyarmC650控制MyarmM750的功能全部实现