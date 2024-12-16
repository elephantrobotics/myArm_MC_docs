# ROS环境搭建

## 系统版本:
**树莓派版本自带Ubuntu(*V-20.04)系统,内置开发环境,无需搭建和管理,更新mc_embodied_kit_ros包即可。**
mc_embodied_kit_ros是大象机器人推出的适用于其MyArm M&C 具身人型复合套件系列桌面六轴机械臂的ROS1包。

ROS1项目地址: [https://github.com/elephantrobotics/mc_embodied_kit_ros/tree/main](https://github.com/elephantrobotics/mc_embodied_kit_ros/tree/main)

机械臂API驱动库地址: [https://github.com/elephantrobotics/pymycobot](https://github.com/elephantrobotics/pymycobot)

# 更新mc_embodied_kit_ros包
为了保证用户能及时使用最新的官方包，可以通过文件管理器进入/home/elephant/catkin_ws/src文件夹,打开控制台终端(快捷键 Ctrl+Alt+T)，输入以下命令进行更新：

```bash
# 克隆github上的代码
cd ~/catkin_ws/src
git clone https://github.com/elephantrobotics/mc_embodied_kit_ros.git # 在决定是否执行此命令之前，请查看下面的注意部分
cd ..     # 回到工作区
catkin_make # 在工作区中构建代码
source devel/setup.bash # 添加环境变量
```

**注意**：如果在/home/elephant/catkin_ws/src(相当于~/catkin_ws/src)目录下已经存在mc_embodied_kit_ros文件夹,则需要先删除原来的mc_embodied_kit_ros,然后再执行上述命令。 其中,目录路径中的er为系统的用户名。 如有不一致，请修改。

至此ROS1环境搭建完成。


---

[← 上一节](../5.1-BasedOnPythonDevelopmentAndUse/5_tracer_example.md) | [下一页 →](2_workcode.md)




