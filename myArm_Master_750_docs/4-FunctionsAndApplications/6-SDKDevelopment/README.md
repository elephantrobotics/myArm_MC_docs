# SDK 开发指南

## 1 使用环境

myArm M750 是基于 PC 开发和使用的。由于机械臂内没有内置系统，因此在使用过程中需要机械臂和 PC 相结合。使用前请先准备好 PC。

## 2 开发环境

为了满足机器人在不同场景下的多样化应用需求，我们对机器人进行了多种编程语言的适配。到目前为止，我们已经适配了以下主流编程语言，我们认为您可以使用以下任何一种语言进行开发。请务必严格按照说明进行操作。任何遗漏的步骤都可能导致相应语言无法成功运行。祝您顺利使用机器人。

| **如果您希望使用以下编程语言， 请确保您的机器人已在应答器部分配置了 USB/Wi-Fi 模式，并确认连接正确。** |
| :------------------------------------------------------------------------------------------------------------- 

- [5.1 Python](./5.1-BasedOnPythonDevelopmentAndUse/1_download.md)<br>
  我们的机器人支持 Python，Python API 库的开发也日趋完善。机器人的关节角度、坐标、抓手和其他方面都可以通过 Python 进行控制。<br>

- [5.2 ROS1](./5.2-DevelopmentAndUseBasedOnROS1/1_download.md)<br>ROS（Robot Operating System）作为一个开源的机器人操作系统，为机器人的开发和控制提供了无限的可能性。我们的机器人可以通过ROS丰富的控制功能，通过模块化的方式对机器人进行控制。无论是关节控制、路径规划还是感知反馈，ROS都提供了相应的工具和库，使得控制过程更加灵活和高效。</br>

- [5.4 Communication](./5.4-DevelopmentBasedOnCommunicationProtocolPackage//5.4.1-CommunicationDoc.md)<br>
  如果您对信息论、编码和机器人通信功能有一定的了解，那么您就应该明白，所有的通信都源于数据传输。为了方便用户操作机器人，我们开放了基于串口通信的通信协议。您可以使用串口助手或将其封装到您熟悉的任何编程语言中来控制机器人。

---

[← 上一章](../5-BasicFunctions/5.1-Minirobot/README.md) | [下一章 →](../7-SuccessfulCases/7-SuccessfulCases.md)