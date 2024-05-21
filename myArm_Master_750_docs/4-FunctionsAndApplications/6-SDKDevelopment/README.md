# SDK Development Guide

## 1 Environment

The myArm C650 is developed and used on a PC. Since there is no built-in system in the robot arm, it is necessary to combine the robot arm with a PC during use. Please prepare a PC before use.

## 2 Development Environment

In order to meet the diverse application requirements of the robot in different scenarios, we have adapted the robot to multiple programming languages. So far, we have adapted the following mainstream programming languages, and we think you can use any of the following languages for development. Please be sure to follow the instructions exactly. Any missing steps may result in the corresponding language not working successfully. We wish you the best of luck with your robot.

| **If you wish to use one of the following programming languages, make sure that your robot is configured for USB/Wi-Fi mode in the Transponder section and that the connection is correct.** |
| :-------------------------------------------------------------------------------------------------------------|

- [6.1 Python](./6.1-BasedOnPythonDevelopmentAndUse/1_download.md)<br>
  If you wish to use one of the following programming languages, make sure that your robot is configured for USB/Wi-Fi mode in the Transponder section and that the connection is correct.。<br>
  
- [6.2 ROS1](./6.2-DevelopmentAndUseBasedOnROS1/1_download.md)<br>
  As an open-source robot operating system, ROS (Robot Operating System) provides unlimited possibilities for the development and control of robots. Our robot can be controlled in a modular way through the rich control functions of ROS. Whether it's joint control, path planning, or perceptual feedback, ROS provides tools and libraries to make the control process more flexible and efficient.</br>

- [6.3 Communication](./6.4-DevelopmentBasedOnCommunicationProtocolPackage/6.4.1-CommunicationDoc.md)<br>
  If you know anything about information theory, coding and robot communication functions, then you should understand that all communication stems from data transfer. To make it easier for you to operate your robot, we have opened up a communication protocol based on serial port communication. You can control the robot using the Serial Assistant or encapsulate it into any programming language with which you are familiar.

---

[← Previous chapter](../5-BasicFunctions/5.1-Minirobot/README.md) | [Next chapter →](../7-SuccessfulCases/7-SuccessfulCases.md)