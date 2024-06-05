# 一、仿真

我们提供一些 **静态仿真** 和 **动态仿真**， 用以和 MyarmC650 交互。  


## 1.1 静态仿真
这里的静态仿真是指：用rviz2中的滑动模块与仿真中的MyarmC650交互  
在工作空间打开终端命令行中输入:  
> colcon build  

再新建一个终端输入：  
> source install/setup.bash # 添加环境变量  
> ros2 launch myarm_c650 test.launch.py  


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/colcon.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/colcon2.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/colcon1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/launch.py3.jpg" alt="7.1.1-1" style="zoom:100%;" />   

**成功运行launch.py文件后，终端会显示：**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/launch.py.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**同时会打开rviz2，生成MyarmC650的仿真模型**

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
> colcon build  
> source install/setup.bash # 添加环境变量  
> ros2 launch myarm_c650 test.launch.py  


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/colcon.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/colcon2.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/launch.py3.jpg" alt="7.1.1-1" style="zoom:100%;" />   

**成功运行launch.py文件后，终端会显示：**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/launch.py.jpg" alt="7.1.1-1" style="zoom:100%;" />    

rviz2文件也会正常显示
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch5.jpg" alt="7.1.1-1" style="zoom:100%;" />  


打开VS code中的项目，找到  myArm/myarm_c650/myarm_c650/test.py 这个 **test.py** 文件  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/runpy1.jpg" alt="7.1.1-1" style="zoom:100%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/runpy3.jpg" alt="7.1.1-1" style="zoom:100%;" />  

在工作空间里再新建一个终端，输入下面指令，先查看正在运行的节点，再查看**joint_state_publisher**节点的PID 最后kill这个节点生成的数字串： 
> ros2 node list  
> ps aux | grep joint_state_publisher   
>  kill 32695  #这串数字是随即生成的,每次生成的数字串都不一样  
   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/ros2kill1.jpg" alt="7.1.1-1" style="zoom:100%;" />    


接下来我们用手移动现实中的MyarmC650机械臂，rviz中的机械臂也会跟着运动：  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch6.jpg" alt="7.1.1-1" style="zoom:100%;" />    

#### 至此与MyarmC650机械臂的交互已全部完成



---

[← 上一页](1_download.md) | [下一页 →](3_ROScode.md)