# 1、Emulation

We provide a number of **static and dynamic simulations** to interact with the MyarmM750.    

## 1.1 Static simulation
Static simulation here refers to the use of the sliding module in rviz to interact with the MyarmC650 in the simulation  
In the Workspace Open Terminal command line, enter:    
> roscore

> source devel/setup.bash   
> roslaunch myarm_m demo_rviz.launch  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch7.jpg" alt="7.1.1-1" style="zoom:100%;" />   

**After successfully running the launch file, the terminal will display:**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch3.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**At the same time, rviz will be opened to generate a simulation model of MyarmM750**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/launch4.jpg" alt="7.1.1-1" style="zoom:100%;" />  


## 1.2 Dynamic simulation
Dynamic simulation here refers to the interaction of the MyarmM750 in motion reality with the MyarmM750 in the simulation    

First of all, we need to connect the MyarmM750 robotic arm to our computer via a USB to TypeC cable and power it on    
Select the **Transponder** button and press the **OK** button
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/Myarm1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

Then the screen will be displayed:    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/Myarm2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

We can see that the arrow points to **"USB UART"**, then press the **"OK"** button, after entering **"NO"**, then press the **"Exit"** button, go back to the arrow pointing to **"USB UART"**, and then press the **"OK"** button, then **"OK"** will be displayed **"OK"**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/Myarm3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

#### At this time, our MyarmM750 has been successfully connected to the computer


Next, enter it in the Workspace Open Terminal command line:    
> source devel/setup.bash  
> roslaunch myarm_m demo_rviz.launch  


<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch7.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**After successfully running the launch file, the terminal will display:**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch3.jpg" alt="7.1.1-1" style="zoom:100%;" />    

The rviz file will also display normally
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch5.jpg" alt="7.1.1-1" style="zoom:100%;" />  


Open the project in VS code and find the **read_control.py** file myArm/myarm_m/scripts/read_control.py     

- Open the .py file, right-click, select "Run Python", and then click "Run Python file in the terminal"   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/runpython2.jpg" alt="7.1.1-1" style="zoom:100%;" />  
 

We can also continue to enter the following commands in the terminal in order to see the angle change of each joint of the MyarmM750:    
> rostopic echo /joint_state  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/topic1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

Next, we move the real-life MyarmM750 robotic arm with our hands, and the robotic arm in rviz will also follow:        
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download1/launch6.jpg" alt="7.1.1-1" style="zoom:100%;" />    

#### At this point, the interaction with the MyarmM750 robotic arm has been completed  


# 2. MyarmC650 controls the movement of MyarmM750
This function requires two robotic arms to be connected to our computer at the same time through USB, we need to distinguish how much each robotic arm is connected to our serial port, and create a new terminal:    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/tty.jpg" alt="7.1.1-1" style="zoom:100%;" />    

Press **TAB key**   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/tty1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

**How to distinguish the string slogans: connect a robotic arm and then enter "ls /dev/tty" to view the current string slogan, and when the robotic arm is not opened, connect another robotic arm and enter the command to view the string slogan**  

Create a terminal input in the workspace:   
> roscore  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/launch1.jpg" alt="7.1.1-1" style="zoom:100%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:100%;" />   

Create another terminal and enter:    
> source devel/setup.bash  
> roslaunch myarm_m combined_control.launch  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch.jpg" alt="7.1.1-1" style="zoom:100%;" />   

After starting the rviz emulation, open the .py file in the **myArm/myarm_m/scripts/combined_control.py** directory   

- Open the .py file, right-click, select "Run Python", and then click "Run Python file in the terminal"   

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedrunpython1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

At this time, we can use our hands to move the MyarmC650 robotic arm, the two robotic arms in the rivz follow the movement of the real-life MyarmC650, and at the same time, the MayrmM750 robotic arm in the real world will also follow the movement of the MyarmC650 (the gripping function can also move)    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch1.jpg" alt="7.1.1-1" style="zoom:100%;" />    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/combinedlaunch2.jpg" alt="7.1.1-1" style="zoom:100%;" />    

## At this point, the MyarmC650 control MyarmM750 function is fully realized

---

[← last page](1_download.md) | [next page →](3_ROScode.md)

