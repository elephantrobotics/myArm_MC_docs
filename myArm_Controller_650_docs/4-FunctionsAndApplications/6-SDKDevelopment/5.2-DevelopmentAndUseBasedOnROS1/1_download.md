# Myarm C650 version:
## Install different versions of ubuntu in Linux
### 1 Virtual machine installation

Go to [Official website](https://www.virtualbox.org/wiki/Downloads) to download the virtual machine Viltul albox or go to [the official website ](https://www.vmware.com/products/desktop-hypervisor.html)download the virtual machine Wimwal  

Of course, if you already have your virtual machine, you can skip that step.    
We chose to download the Virtual box because it is free.  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/box.png" alt="7.1.1-1" style="zoom:0%;" />
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/installbox.gif" alt="7.1.1-1" style="zoom:0%;" />

### 2 Create a new virtual machine
#### 2.1 Create a virtual machine

**In Control, select New**  
Enter the name of the VM and the location where the VM is stored, select the VM type as Linux, and select the ubuntu 64-bit version to proceed to the next step.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-1.jpg" alt="7.1.1-1" style="zoom:0%;" />

Configure the memory size according to your needs and proceed to the next step.    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-4.jpg" alt="7.1.1-1" style="zoom:0%;" />

Select **Create virtual hard disk** now to create it.   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-5.jpg" alt="7.1.1-1" style="zoom:0%;" />

Select **VDI** for Virtual Hard Disk Type and proceed to the next step.   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-6.jpg" alt="7.1.1-1" style="zoom:0%;" />

Allocate the size of the virtual hard disk, since the ubuntu system needs to be installed, and it will also operate in the system, it is recommended that the size should not be less than 20G.     
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-7.jpg" alt="7.1.1-1" style="zoom:0%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-8.jpg" alt="7.1.1-1" style="zoom:0%;" />

#### 2.2 Import the Ubuntu system
##### 2.2.1 Download the Ubuntu system

Please choose the Ubuntu version according to your needs to install it.   
Note: ROS2 requires version 20.04 to be downloaded.       
> [16.04 version](https://releases.ubuntu.com/16.04.7/)  
> [18.04 version](https://releases.ubuntu.com/18.04.6/)  
> [20.04 version](https://old-releases.ubuntu.com/releases/20.04.3/)

**The installation method and process are the same for all three versions, and version 18.04 is used as an example for installation**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/u-1.jpg" alt="7.1.1-1" style="zoom:0%;" />  

After the download is completed, there is a file as shown in the figure:    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/u-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  

##### 2.2.2 Import Ubuntu to the virtual machine

Locate the previously installed virtual machine in the virtual box, go to **Settings**, and assign a disc to the controller in **Storage**：  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/ros-1.jpg" alt="7.1.1-1" style="zoom:0%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/vbox-3.jpg" alt="7.1.1-1" style="zoom:0%;" />  
Then open the virtual machine for ubuntu installation and click start.    

##### 2.2.3 ubuntu installation

Wait for the system to boot, enter the **Welcome** interface, select "Chinese (Simplified)", and click the "Install Ubuntu" button；
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-1.jpg" alt="7.1.1-1" style="zoom:0%;" />  

Click “Continue” button;  
  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  

Select the "Clear entire disk and install Ubuntu" option, and click the "Install Now" button;  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-3.jpg" alt="7.1.1-1" style="zoom:0%;" />  

Click the "Continue" button in the pop-up dialog box;  
  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-4.jpg" alt="7.1.1-1" style="zoom:98%;" />   

Set a geographic position and click the “Continue” button;  
  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-5.jpg" alt="7.1.1-1" style="zoom:0%;" />  

Set a user name and password, and click the “Continue” button;  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-6.jpg" alt="7.1.1-1" style="zoom:0%;" />   

Enter the system installation interface, and wait patiently;   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-7.jpg" alt="7.1.1-1" style="zoom:100%;" />    

After installation is complete, click the "Restart now" button in the pop-up dialog box to complete the installation.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/uit-8.jpg" alt="7.1.1-1" style="zoom:155%;" />

# 1 ROS Environment building  
## 1.1 Installing ROS  
Building a basic development environment requires the installation of the robot operating system (short for ROS), MoveIt and a git version manager. The installation methods and procedures are described respectively below.   

### 1.1.1 Selecting a version
There is a one-to-one relationship between ROS and ubuntu. Different versions of ubuntu correspond to different versions of ROS. The reference website is as follows: http://wiki.ros.org/Distributions  
- Here are the ROS versions supported by Ubuntu:
  - Ubuntu 16.04 / ROS Kinetic  
  - Ubuntu 18.04 / ROS Melodic  
  - Ubuntu 20.04 / ROS Noetic  

**Install the ROS version corresponding to the Ubuntu version you have installed.**  

If the versions are different, the downloading will fail. The system we choose here is Ubuntu 18.04, so the corresponding ROS version is ROS Melodic.  
  - NOTE: At present, we do not provide any reference for installing ROS in windows. If necessary, refer to https://www.ros.org/install/  
  
### 1.1.2 Installing ROS
#### 1 Adding a software source  
There is no ROS software source in the software source list of Ubuntu itself, so you need to Configure the ROS software source into the software list repository first, and then download ROS. Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command:  
- official source:
    > sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'  

- If the download speed is slow, it is recommended to select a nearby mirror source to replace the above command. For example, Tsinghua University is:  
    > sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'  

Here you will be asked to input a user password. Just input the user password set when Ubuntu is installed.  

####  2 Setting a key
**Configuring a public key**. This step is to let the system confirm that our path is safe, so that there is no problem in downloading the file. Otherwise it will be deleted immediately after downloading:  
   > sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654  

The execution result is displayed as follows:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/install-ros-2.jpg" alt="7.1.1-1" style="zoom:155%;" />  

#### 3 Installation
After adding a new software source, you need to update the software source list. Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command:  
> sudo apt-get update  

Execute **Installing ROS**. Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command according to your Ubuntu version:  

> \# Ubuntu 16.04  
> sudo apt install ros-kinetic-desktop-full    
> \# Ubuntu 18.04  
> sudo apt install ros-melodic-desktop-full  
> \# Ubuntu 20.04  
> sudo apt install ros-noetic-desktop-full

It is recommended to install the complete ROS here to prevent the lack of libraries and dependencies.  

**The installation process takes a long time, so please wait with patience.**  

 - If the following error message appears on the console terminal during the installation process, you need to replace the software source list in /etc/apt/sources.list.  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/ros-2.jpg" alt="7.1.1-1" style="zoom:155%;" />  

 - Open a console terminal (shortcut key:Ctrl+Alt+T),enter the following command:  
> sudo gedit /etc/apt/sources.list  

 - Replace all the official repositories in **sources.list** with the following Alibaba Cloud repositories:  

**Ubuntu 16.04 version：**

deb http://mirrors.aliyun.com/ubuntu/ xenial main   
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main  

deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main  

deb http://mirrors.aliyun.com/ubuntu/ xenial universe  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe  
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe  

deb http://mirrors.aliyun.com/ubuntu/ xenial-security main  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main  
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe  
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe  


**Ubuntu 18.04 version：**

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse  


**Ubuntu 20.04 version：**

deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse  

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse  

- After the configuration is complete, the contents of the sources.list file are as follows, click Save and Exit.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/ros-4.jpg" alt="7.1.1-1" style="zoom:155%;" />  

- To update the list of software sources, enter in the console terminal:  
> sudo apt-get update  

- Enter the instructions to install ROS in the console terminal:  
> \# Ubuntu 16.04  
> sudo apt install ros-kinetic-desktop-full  
> \# Ubuntu 18.04  
> sudo apt install ros-melodic-desktop-full  
> \# Ubuntu 20.04  
> sudo apt install ros-noetic-desktop-full  

**The installation process takes a long time, so please wait with patience.**  

#### 4 Configuring the ROS environment to the system  
rosdep allows you to easily install the source codes you want to compile, or the system dependencies required by some ROS core components. Execute the following commands in sequence in the terminal, and open a console terminal (shortcut key: Ctrl+Alt+T).

If your system does not have rosdep installed, use the command sudo apt install python-rosdep to install it.

If the system of the Ubuntu installed by you is version 20.04, use the command sudo apt install python3-rosdep to it install. After completion, execute the rosdep initialization command.  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/install-ros-4.jpg" alt="7.1.1-1" style="zoom:155%;" />  

**initialize rosdep:** 
> sudo rosdep init

If the following error message appears:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/ros-3.jpg" alt="7.1.1-1" style="zoom:155%;" />  

**Solution**: Modify the hosts file and enter the following command in the console terminal:  
> sudo gedit /etc/hosts  

At the end of the file content, add the IP addresses of the following two URLs to access:  
> 199.232.28.133 raw.githubusercontent.com  
> 151.101.228.133 raw.github.com  

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/ros-6.jpg" alt="7.1.1-1" style="zoom:155%;" />  

After the modification is complete, execute in the console terminal:

> sudo rosdep init  

> rosdep update  

After the initialization is completed, in order to avoid re-validating the ROS function path every time the terminal window is closed, we can **set the path to an environment variable**, so that each time you open a new terminal, the ROS function path will automatically take effect. Execute the following commands in sequence in the terminal, and open a console terminal (shortcut key: Ctrl+Alt+T):

#### 5 Set up the ros environment
- Bash  
Execute the following commands:  
> \# Ubuntu 16.04  
> echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc  
> \# Ubuntu 18.04  
> echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc  
> \# Ubuntu 20.04  
> echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc  
> source ~/.bashrc  

- Zsh
If you replace bash with zsh, then:

> \# Ubuntu16.04  
> echo "source /opt/ros/kinetic/setup.bash" >> ~/.zshrc  
> \## Ubuntu18.04  
> echo "source /opt/ros/melodic/setup.bash" >> ~/.zshrc  
> \## Ubuntu20.04  
> echo "source /opt/ros/noetic/setup.bash" >> ~/.zshrc  
> source ~/.zshrc  

#### 6 Installing a ROS extra dependency
Input the following command in the terminal to install a ROS extra dependency, and open a console terminal (shortcut key: Ctrl+Alt+T):  
> sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential  

If your Unbutu system is version 20.04, please execute the following command to install:  
> sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential  

> \# Ubuntu 16.04  
> sudo apt install ros-kinetic-joint-state-publisher-gui  
> \# Ubuntu 18.04   
> sudo apt install ros-melodic-joint-state-publisher-gui  
> \# Ubuntu 20.04   
> sudo apt install ros-noetic-joint-state-publisher-gui  

### 1.1.3 Verifying ROS
The startup of the ROS system requires a ROS Master, that is, a node manager. We can input the roscore command in the terminal to start the ROS Master.

To verify whether ROS has been installed successfully, open a console terminal (shortcut key: Ctrl+Alt+T) and execute the following command in the terminal:  
> roscore  

When the following interface is displayed, it means that ROS has been installed successfully.  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/install-ros-3.jpg" alt="7.1.1-1" style="zoom:155%;" />  

The roscore command starts a node manager, which is used for node management. In a ros system, there is and only one node manager, which is the prerequisite for the operation of the ros node, so before executing the start of the ros node, roscore needs to be executed in the first step.  

For more detailed installation instructions, you can refer to the official installation instructions by visiting the website: http://wiki.ros.org/ROS/Installation  


## 1.2 MoveIt Installation
MoveIt is the composition of a series of function packages for movement operations in ros, mainly including motion planning, collision detection, kinematics, 3D perception, operation control and other functions.  

### 1.2.1 Updating the software source list
Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window to update the software source list:
> sudo apt-get update

### 1.2.2 Installing MoveIt
Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window to execute the installation of MoveIt:

> \# Ubuntu16.04  
> sudo apt-get install ros-kinetic-moveit  
> \# Ubuntu 18.04  
> sudo apt-get install ros-melodic-moveit  
> \# Ubuntu20.04  
> sudo apt-get install ros-noetic-moveit  


## 1.3 git Installation
### 1.3.1 Adding a software source
Add the software source for installing git to the software source list of ubuntu, open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window:
>sudo add-apt-repository ppa:git-core/ppa

### 1.3.2 Updating the software source list
Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window to update the software source list:
> sudo apt-get update

### 1.3.3 Installing git
Open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window to execute the installation of git:
> sudo apt-get install git

### 1.3.4 Verifying git
Read the git version, open a console terminal (shortcut key: Ctrl+Alt+T) and input the following command on the terminal window:
> git --version

The git version number can be displayed in the terminal as follows, that is, the installation is successful.

><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/git.jpg" alt="7.1.1-1" style="zoom:100%;" />

### 1.3.5 Use
During the subsequent downloading of the ros package, you need to use git. For the use of git, refer to the following link:   
https://git-scm.com/book/zh/v2    
https://www.runoob.com/git/git-tutorial.html


# 2 MyarmC650 Installation

The MyarmC650 is a ROS package launched by ElephantRobotics that adapts to its desktop six-axis robotic arm Myarm series.  

Project Address: https://github.com/elephantrobotics/mycobot_ros/tree/myarm-c650

## 2.1 precondition

Before installing the package, make sure you have a ROS workspace.    
Here we give a sample command to **create a workspace**,The default is catkin_ws, Open a console terminal (Ctrl+Alt+T),On the command line, enter the following command:  

>mkdir -p ~/catkin_ws/src  # Create folders  
>cd ~/catkin_ws/src        # Go to the folder  
>catkin_init_workspace     # Initialize the current directory into a ROS workspace    
>cd ..                     # Return to the parent directory  
>catkin_make               # Build the code in the workspace

**Once created, a folder will be generated**    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/2_download_en/workplace.jpg" alt="7.1.1-1" style="zoom:0%;" /> 

**Add the environment for the workspace**  
Bash  
The official default ROS1 workspace is catkin_ws.    
> \# Ubuntu 16.04    
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc  

> \# Ubuntu 18.04  
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

> \# Ubuntu 20.04  
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

> source ~/.bashrc  

## 2.2 Installation

**NOTE：**

This package relies on ROS and MoveIT, make sure to install ROS and MoveIT successfully before use.  
The interaction between this package and the real robotic arm relies on the PythonApi - pymycobot  
The API project locations are:[https://github.com/elephantrobotics/pymycobot](https://github.com/elephantrobotics/pymycobot)  

Quick Installation:pip install pymycobot --upgrade

When executing the Pip Instale Pimicobo-Uprad command, if the following error message appears:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/ros-5.jpg" alt="7.1.1-1" style="zoom:0%;" />   

Enter the following command to install pip when prompted:  

> sudo apt install python-pip
>
>> If your Ubuntu system is version 20.04, run the sudo apt install python3-pip installation pip installation and run the terminal again after the installation is complete    
>>
>> pip install pymycobot --upgrade
>
>> The installation method depends on Git, so make sure you have Git installed on your computer.  

The official default ROS1 workspace is catkin_ws.    

**Open the terminal:**
> cd ~/catkin_ws/src  # Go to the src folder in your workspace    
> git clone https://github.com/elephantrobotics/mycobot_ros.git     # Clone the code on github  
> cd ..       # Return to the workspace    
> catkin_make # Build the code in the workspace    
> cd ..  
> source devel/setup.bash # Add environment variables  

## **At this point, the environment construction is partially completed**

### For the subsequent programming, we also need to download one VS code
#### Here we will choose the most convenient method: **Installing in Ubuntu Software [Easy & Convenient]**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vs1.jpg" alt="7.1.1-1" style="zoom:0%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vs2.png" alt="7.1.1-1" style="zoom:0%;" />   

**After installation, we also need to install the python environment**  
To run a python file, click on the left extension (ctrl+shift+X) - search for python, download and install        
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/python2.jpg" alt="7.1.1-1" style="zoom:0%;" />     
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/python.jpg" alt="7.1.1-1" style="zoom:0%;" />      

After installation, you can click on the upper left file, select New File, select the file type as Python, write your own Python code, and then click Run in the upper menu bar    

# 3 A brief introduction and use of RVIZ

rviz is a 3D visualization platform in ROS, which can realize the graphical display of external information on the one hand, and release control information to objects through rviz, so as to realize the monitoring and control of the robot.    
## 3.1 Introduction to the installation and interface of RVIZ  
When installing ROS, if the full installation is performed, RVIZ is already installed, you can directly try to run it; If it is not fully installed, you can install rviz separately:    
> - **\#Ubuntu16.04**
> - sudo apt-get install ros-kinetic-rviz

> - **\#Ubuntu18.04**  
> - sudo apt-get install ros-melodic-rviz

> - **\#Ubuntu20.04**  
> - sudo apt-get install ros-noetic-rviz  

After the installation is completed, please open a new terminal (shortcut Ctrl+Alt+T) and enter the following command:    
> roscore

Then open a new terminal (shortcut Ctrl+Alt+T) and enter the command to open rviz :   

> rosrun rviz rviz  

or
> rviz  

Open RVIZ and display the following interface:  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/rviz1.jpg" alt="7.1.1-1" style="zoom:0%;" />   

### 3.1.1 Introduction to each area

- On the left is a list of monitors, which are things that draw something in the 3D world and may have some options available in the display list.  
- At the top is the toolbar, which allows the user to select a tool with a variety of functions with various function buttons  
- The middle part is the 3D view: it is the main screen where you can view various data in 3D. The background color, fixed frame, mesh, etc. of the 3D view can be set in detail in the Global Options and Grid items displayed on the left.  
- The lower part is the time display area, including the system time and ROS time.  
- On the right is the observation angle setting area, which can be set to different observation angles.  

We only give a rough introduction in this part, if you want to know more details, you can go to [User Guide ](http://wiki.ros.org/rviz/UserGuide)to review.

---

[← last section](../5.1-BasedOnPythonDevelopmentAndUse/6_example.md) | [next page →](2_workcode.md)




