# Factory Firmware Introduction

The MyArm C650 version comes with the miniRoboflow application software developed independently by Elephant Robotics. Functions such as drag-and-drop teaching, communication forwarding, status checking and zero calibration can be achieved through simple push-button interaction.

The user interface of the built-in software is simple and easy to use. The communication forwarding function allows you to control the robot using a variety of programming languages and development environments, making robot control easy.

## miniRoboFlow

**miniRoboFlow** It has four main chapters:

- [**Guidelines for use**](5.1.1-MinirobotGuide.md)
  - Minirobot is an application that controls the MyArm robotic arm through a combination of 3 buttons on the base of the arm and an on-screen display. (It features communication forwarding, zero calibration, and status information), which facilitates the operator's interaction with and proper use of the elephant robot.
- [**Zero Calibration**](5.1.2-calibrate.md)
  - Calibrating the arm is a prerequisite for precise control of the arm, while setting the joint zeros and initialising the motor potentials are essential for subsequent advanced development.
- [**communications redirection**](5.1.3-transponder.md)
  - For microcontroller robotic arms, the timeliness of communication is critical. For this type of robotic arm, we often send control commands to the **M5Stack-basic** at the bottom. Through communication forwarding, the end-effector analyses the commands and then executes the target action. Currently, the **MyArm C650** has one communication method: **Serial port**.
- [**status message**](5.1.4-information.md)
  - Status information is a detection function that utilises the connection status of the motors and **Atom** in the robotic arm. With this function, users can easily troubleshoot equipment. During the link test, the connection status of the robotic arm devices can be seen, including the connection of the **Server**. In microcontroller devices, M5Stack-basic displays its current firmware version.

---

[← Previous chapter](../../../3-BasicSettings/4-FirstTimeInstallation/4-FirstTimeInstallation.md) | [Next chapter →](../../6-SDKDevelopment/README.md)