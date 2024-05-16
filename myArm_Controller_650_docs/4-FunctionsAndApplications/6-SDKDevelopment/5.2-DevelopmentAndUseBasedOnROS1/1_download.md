# Myarm C650版本:
## 在Linux中安装不同版本的ubuntu系统
### 1 虚拟机安装

前往[官方网站](https://www.virtualbox.org/wiki/Downloads)下载虚拟机Virtual Box 或者前往[官方网站](https://www.vmware.com/products/desktop-hypervisor.html)下载虚拟机 VM ware

当然，如果您已经拥有您的虚拟机，您可以跳过该步骤。  
我们选择下载Virtual box，因为它是免费的。

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/box.png" alt="7.1.1-1" style="zoom:0%;" />
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/box2.gif" alt="7.1.1-1" style="zoom:0%;" />

### 2 新建虚拟机
#### 2.1 创建虚拟机

**在控制中选择新建**  
输入虚拟机名称和虚拟机存放的位置，选择虚拟机类型为Linux，选择ubuntu64位版本，进行下一步。
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-1.jpg" alt="7.1.1-1" style="zoom:0%;" />

按照自己的需求配置内存大小，进行下一步。  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-4.jpg" alt="7.1.1-1" style="zoom:0%;" />

选择现在**创建虚拟硬盘**，进行创建。   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-5.jpg" alt="7.1.1-1" style="zoom:0%;" />

虚拟硬盘类型选择**VDI**类型，进行下一步。  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-6.jpg" alt="7.1.1-1" style="zoom:0%;" />

分配虚拟硬盘大小，由于需要安装ubuntu系统，而且还会在该系统中进行操作，建议大小不要低于20G。   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-7.jpg" alt="7.1.1-1" style="zoom:0%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-8.jpg" alt="7.1.1-1" style="zoom:0%;" />

#### 2.2 导入ubuntu系统
##### 2.2.1 下载ubuntu系统。

请根据自己的需要选择ubuntu版本进行安装

注意： ROS2需要下载20.04版本。  
> [16.04版本](https://releases.ubuntu.com/16.04.7/)  
> [18.04版本](https://releases.ubuntu.com/18.04.6/)  
> [20.04版本](https://old-releases.ubuntu.com/releases/20.04.3/)

**三种版本的安装方法和过程都是相同的，这里以18.04版本作为例子进行安装**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/u-1.jpg" alt="7.1.1-1" style="zoom:0%;" />  

下载完成后有如图文件：  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/u-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  

##### 2.2.2 导入ubuntu到虚拟机中

在Virtual box中找到之前安装的虚拟机，进入**设置**，并在**存储**中给控制器分配光盘：
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vbox4.jpg" alt="7.1.1-1" style="zoom:0%;" />  
然后打开虚拟机进行ubuntu安装，并点击启动。  

##### 2.2.3 ubuntu安装

等待系统启动，进入**欢迎**界面，选中“中文（简体）”，并点击“安装 Ubuntu”按钮；
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-1.jpg" alt="7.1.1-1" style="zoom:0%;" />  

点击“继续”按钮；  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-2.jpg" alt="7.1.1-1" style="zoom:0%;" />  

选中“清除整个磁盘并安装 Ubuntu”选项，点击“现在安装”按钮；
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-3.jpg" alt="7.1.1-1" style="zoom:0%;" />  

在弹出的对话框中点击“继续”按钮；  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-4.jpg" alt="7.1.1-1" style="zoom:98%;" />   

设置地理位置，点击“继续”按钮；  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-5.jpg" alt="7.1.1-1" style="zoom:0%;" />  

设置用户名和密码，点击“继续”按钮；  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-6.jpg" alt="7.1.1-1" style="zoom:0%;" />   

进入系统安装界面，请耐心等待；  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-7.jpg" alt="7.1.1-1" style="zoom:100%;" />    

待安装完成，在弹出的对话框中，点击“现在重启”按钮，完成安装。  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/uit-8.jpg" alt="7.1.1-1" style="zoom:155%;" />




##  一、配置Linux清华镜像源
### 1.1介绍

我们在下载很多基础的工具请求的基本上是国外的服务器，这对于国内用户来说，无疑是非常糟糕的体验，其下载速度慢、请求失败往往成为很多刚入门Linux的小白最大的困扰。
不过好在国内有着稳定高速且免费的镜像网站，我们可以通过修改系统配置文件来享受这些优秀的网站资源。

>清华源：https://pypi.tuna.tsinghua.edu.cn/simple/  
>阿里云：https://mirrors.aliyun.com/pypi/simple  
>中科大：https://pypi.mirrors.ustc.edu.cn/simple/

### 1.2 开始配置

这里我以 Ubuntu 20.04为例阿里云来配置

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/yun.jpg" alt="7.1.1-1" style="zoom:0%;" />

## 二、ROS安装
### 2.1 添加ros环境源
> sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main"> /etc/apt/sources.list.d/ros-latest.list'

### 2.2 添加密钥
> sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

### 2.3 安装ROS（注意ubuntu版本）
> sudo apt update
>sudo apt install ros-noetic-desktop-full

### 2.4 初始化rosdep
> sudo rosdep init && rosdep update
>
>##### 自带的可能会出现错误。可以使用大神基于 rosdep 源码写的rosdepc。
>>sudo pip install rosdepc  
>##### 没有pip可以试试pip3  
>>sudo pip3 install rosdepc  
>##### pip3没有选择安装  
>>sudo apt-get install python3-pip  
>>sudo pip install rosdepc

### 2.5 再次初始化
> sudo rosdepc init  
>rosdepc update

### 2.6 配置环境变量
> echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc  
>source ~/.bashrc

### 2.7 安装 rosinstall
> sudo apt install python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

### 2.8 测试ROS（打开三个终端窗口）
第一个窗口运行 roscore
> roscore
>
>><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/roscore.jpg" alt="7.1.1-1" style="zoom:0%;" />

第二个终端窗口，输入：

> rosrun turtlesim turtlesim_node  
>当出现有一个海龟的窗口，证明运行成功了
>><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/rosrun1.jpg" alt="7.1.1-1" style="zoom:0%;" />

打开第三个终端窗口，输入：
> rosrun turtlesim turtle_teleop_key  
>出现这样的提示后，我们用鼠标聚焦第三个终端窗口，便可以通过按下 ↑ ↓ ← →键来对小海龟进行控制。
>><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/rosrun3.jpg" alt="7.1.1-1" style="zoom:0%;" />  
>><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/rosrun2.jpg" alt="7.1.1-1" style="zoom:100%;" />

## 安装完成

到了这里，恭喜你已经完成了ROS的安装、配置且运行。

祝你日后的 ROS 学习也更加畅通无阻！

## 三、MoveIt安装
MoveIt 是 ros 中一系列移动操作的功能包的组成，主要包含运动规划，碰撞检测，运动学，3D 感知，操作控制等功能。

### 3.1 更新软件源列表

打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令，以更新软件源列表：
> sudo apt-get update

### 3.2 安装 MoveIt

打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令，执行 MoveIt 的安装：
> sudo apt-get install ros-noetic-moveit

## 四、 git 安装
### 4.1 添加软件源
将 git 安装的软件源添加到 ubuntu 的软件源列表中，打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令：
>sudo add-apt-repository ppa:git-core/ppa

### 4.2 更新软件源列表
打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令，以更新软件源列表：
> sudo apt-get update

### 4.3 安装 git
打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令，执行 git 的安装：
> sudo apt-get install git

### 4.4 验证安装
读取 git 版本，打开一个控制台终端(快捷键Ctrl+Alt+T)，在终端窗口输入以下命令：
> git --version

在终端中可以显示 git 版本号，如下，即为安装成功
><img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/git.jpg" alt="7.1.1-1" style="zoom:100%;" />

### 4.5 使用

在后续下载 ros 包需要用到git，git 的使用可以参考下面链接：  
https://git-scm.com/book/zh/v2    
https://www.runoob.com/git/git-tutorial.html


## MyarmC650 安装

MyarmC650 是 ElephantRobotics 推出的，适配旗下桌面型六轴机械臂 Myarm系列 的ROS 包。

项目地址：https://github.com/elephantrobotics/mycobot_ros/tree/myarm-c650

### 5.1 前提

在安装包之前，请保证拥有 ros 工作空间。  
这里我们给出**创建工作空间**的样例命令，默认为catkin_ws, 打开一个控制台终端(快捷键Ctrl+Alt+T)，在命令行输入以下命令：

>mkdir -p ~/catkin_ws/src  # 创建文件夹  
>cd ~/catkin_ws/src        # 进入文件夹  
>catkin_init_workspace     # 把当前目录初始化为一个ROS工作空间  
>cd ..                     # 返回上级目录  
>catkin_make               # 构建工作区中的代码

**创建好之后会生成一个文件夹**    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/catkin.jpg" alt="7.1.1-1" style="zoom:0%;" /> 

**添加工作空间的环境**  
Bash  
官方默认的 ROS1 工作区是 catkin_ws。  
###### Ubuntu 16.04  
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc  

###### Ubuntu 18.04  
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

###### Ubuntu 20.04  
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

source ~/.bashrc  

### 5.2 安装

**NOTE：**

本包依赖于ROS和MoveIT，使用前确保以成功安装ROS和MoveIT。  
本包与真实机械臂的交互依赖于PythonApi - pymycobot  
Api项目地为：[https://github.com/elephantrobotics/pymycobot](https://github.com/elephantrobotics/pymycobot)  

快速安装：pip install pymycobot --upgrade

执行pip install pymycobot --upgrade命令时，若出现如下图错误提示：  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/ros-5.jpg" alt="7.1.1-1" style="zoom:0%;" />   

根据提示输入以下命令安装pip

> sudo apt install python-pip
>
>> 如果你的Ubuntu系统是20.04版本，请执行命令sudo apt install python3-pip安装pip pip安装完成后，终端再次执行  
>>
>> pip install pymycobot --upgrade
>
>> 安装方式依赖于Git，请确保电脑中已安装Git。

官方默认的 ROS1 工作区是 catkin_ws。  

**打开终端：**
> cd ~/catkin_ws/src  # 进入工作区的src文件夹中  
> git clone https://github.com/elephantrobotics/mycobot_ros.git     # 克隆github上的代码  
> cd ..       # 返回工作区  
> catkin_make # 构建工作区中的代码  
> cd ..  
> source devel/setup.bash # 添加环境变量  

## **至此，环境搭建部分完成**

### 为了后续的编程，我们还需要下载一个 VS code
#### 这里我们就选择最方便的一种方法： **在Ubuntu Software中安装【简单、方便】**  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vs1.jpg" alt="7.1.1-1" style="zoom:0%;" />   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/vs2.png" alt="7.1.1-1" style="zoom:0%;" />   

**安装好之后，我们还需要安装一下python环境**  
要想运行python文件很简单，点击左边扩展(ctrl+shift+X)--搜索python，下载安装即可      
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/python2.jpg" alt="7.1.1-1" style="zoom:0%;" />     
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/python.jpg" alt="7.1.1-1" style="zoom:0%;" />      

安装好后就可以点击左上文件，选择新建文件，选择文件类型为python，编写自己的python代码，然后点击上方菜单栏的运行就可以  

# rviz的简单介绍及使用

rviz是ROS中一款三维可视化平台，一方面能够实现对外部信息的图形化显示，另外还可以通过 rviz 给对象发布控制信息，从而实现对机器人的监测与控制。  
1 rviz的安装及界面简介  
在安装ros时，如果执行的完全安装，rviz已经安装好了,您可以直接尝试运行；如果没有完全安装，可单独安装rviz:  
> - **Ubuntu16.04**
> - sudo apt-get install ros-kinetic-rviz

> - **Ubuntu18.04**  
> - sudo apt-get install ros-melodic-rviz

> - **Ubuntu20.04**  
> - sudo apt-get install ros-noetic-rviz  

安装完成后，请先打开一个新的终端(快捷键Ctrl+Alt+T),输入如下指令：  
> roscore

然后再打开一个一个新的终端(快捷键Ctrl+Alt+T)输入命令打开rviz  

> rosrun rviz rviz 或 rviz

打开rviz,显示如下界面：  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/rviz1.jpg" alt="7.1.1-1" style="zoom:0%;" />   

### 1.1 各个区域介绍

- 左侧为显示器列表，显示器是在3D世界中绘制某些内容的东西，并且可能在显示列表中具有一些可用的选项。
- 上方是工具栏，允许用户用各种功能按键选择多种功能的工具
- 中间部分为3D视图: 它是可以用三维方式查看各种数据的主屏幕。3D视图的背景颜色、固定框架、网格等可以在左侧显示的全局选项（Global Options）和网格（Grid）项目中进行详细设置。
- 下方为时间显示区域，包括系统时间和ROS时间等。
- 右侧为观测视角设置区域，可以设置不同的观测视角。

本部分我们只进行粗略的介绍，如果您想了解更多详细的内容，可以前往[用户指南](http://wiki.ros.org/rviz/UserGuide)进行查看。






