# ROS Environment Setup

## System Version:
**The Raspberry Pi version comes with a built-in Ubuntu (*V-20.04) system and a pre-installed development environment, eliminating the need for setup and management. Simply update the `mc_embodied_kit_ros` package.**
The `mc_embodied_kit_ros` package is a ROS1 package developed by Elephant Robotics for their MyArm M&C humanoid composite kit series, a desktop six-axis robotic arm.

ROS1 Project Repository: [https://github.com/elephantrobotics/mc_embodied_kit_ros/tree/main](https://github.com/elephantrobotics/mc_embodied_kit_ros/tree/main)

Robotic Arm API Driver Library: [https://github.com/elephantrobotics/pymycobot](https://github.com/elephantrobotics/pymycobot)

# Updating the `mc_embodied_kit_ros` Package
To ensure users can access the latest official packages promptly, navigate to the `/home/elephant/catkin_ws/src` folder using the file manager. Open the terminal (shortcut: `Ctrl+Alt+T`) and enter the following commands to update:

```bash
# Clone the repository from GitHub
cd ~/catkin_ws/src
git clone https://github.com/elephantrobotics/mc_embodied_kit_ros.git # Check the note below before executing this command
cd ..     # Return to the workspace
catkin_make # Build the code in the workspace
source devel/setup.bash # Add environment variables
```
**Note**: If the mc_embodied_kit_ros folder already exists in the /home/elephant/catkin_ws/src directory (equivalent to ~/catkin_ws/src), you need to delete the existing mc_embodied_kit_ros folder before executing the above commands. Note that the username in the directory path, elephant, corresponds to the system's username. If it differs, please modify accordingly.

With this, the ROS1 environment setup is complete.



---

[← last section](../6.1-BasedOnPythonDevelopmentAndUse/1_download.md) | [next page →](2_workcode.md)




