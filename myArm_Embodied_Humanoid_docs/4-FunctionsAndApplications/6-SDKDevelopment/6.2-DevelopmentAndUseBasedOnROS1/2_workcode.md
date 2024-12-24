# 1. Simulation

We provide **static simulation** and **dynamic simulation** to interact with MyArm M&C Embodied Human Composite Kit.

## 1.1 Static Simulation
Static simulation refers to interacting with the MyArm M&C Embodied Human Composite Kit in simulation using the slider module in RViz.  
In the workspace, open the terminal and enter the following commands:  
> source devel/setup.bash # Add environment variables  
> roslaunch myarm_m mc_embodied_control.launch  

**This will open RViz and generate the simulation model of the Myarm M&C Embodied Kit.**

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/mc_launch2.jpg" alt="7.1.1-1" style="zoom:100%;" />  

## 1.2 Dynamic Simulation
Dynamic simulation refers to the interaction between the real-world Myarm M&C Embodied Kit and its simulation counterpart.  

First, connect the MyarmM750 robotic arm to the system using a USB-to-Type-C cable and power it on.  
Select **Transponder** using the buttons and press the "OK" button.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

Then the screen will display the following:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

You will see the arrow pointing to **"USB UART"**. Press "OK," and it will show **"NO"**. Press the **"Exit"** button to return to the screen where the arrow points to **"USB UART"**. Press "OK" again, and it will display **"OK"**.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarm3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

Repeat the same steps for the MyarmC650 robotic arm. Connect it via USB-to-Type-C cable, power it on, select **Transponder**, and follow the on-screen prompts:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc1.jpg" alt="7.1.1-1" style="zoom:50%;" />  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc2.jpg" alt="7.1.1-1" style="zoom:50%;" />  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/2_download1/Myarmc3.jpg" alt="7.1.1-1" style="zoom:50%;" />  

#### At this point, MyarmM750 and MyarmC650 have successfully started.
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/MC_1.jpg" alt="7.1.1-1" style="zoom:100%;" />  

This function requires connecting four robotic arms to the system simultaneously via USB. Identify the serial port for each arm by following these steps:  

1. 1. Connect a robot arm and run the `ls /dev/tty` command on the terminal to check the current serial port.  
2. Without disconnecting the first arm, connect another arm and run the command again to identify all four ports.  

Update the corresponding serial ports in the `mc_embodied_kit_ros/myarm_m/scripts/mc_embodied_control.py` file as shown below:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_serial.jpg" alt="7.1.1-1" style="zoom:100%;" />  

To start the system, open a terminal and run:  
> roscore  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:100%;" />  

Open another terminal and run:  
> roslaunch myarm_m mc_embodied_control.launch  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_rviz.jpg" alt="7.1.1-1" style="zoom:100%;" />  

Once the RViz simulation starts, open another terminal and run:  
> rosrun myarm_m mc_embodied_control.py  

You can now use MyarmC650 to control MyarmM750.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/mc_rviz_2.jpg" alt="7.1.1-1" style="zoom:100%;" />  

At this point, you can move the MyarmC650 with your hand. Both simulated arms in RViz and the physical MyarmM750 will follow the movements (including gripper functionality).  

## At this point, MyarmC650 controlling MyarmM750 is fully implemented.

## 1.3 Starting the Camera Node
### 1.3.1 First, open a terminal and run:
```bash
sudo apt-get update

sudo apt-get install ros-noetic-usb-cam
```
### 1.3.2 Then, open another terminal and run:
```bash
cd mc_embodied_kit_ros

catkin_make

source devel/setup.bash

roslaunch my_camera usb_cam.launch
```
#### After running these commands, you can view the camera feeds:
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/pic_1.jpg" alt="7.1.1-1" style="zoom:100%;" /> <img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/pic_2.jpg" alt="7.1.1-1" style="zoom:100%;" /> ```

---

[← last page](1_download.md) | [next page →](3_ROScode.md)

