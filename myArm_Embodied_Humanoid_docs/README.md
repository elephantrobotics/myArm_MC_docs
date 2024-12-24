# myArm M&C Embodied Human Composite Kit
Universal Intelligent Six Degree of Freedom Robotic Arm

Core Document
---

This document contains comprehensive information from product introduction and detailed technical specifications to user notes and initial installation instructions. We will explain in depth the basic functions of the myArm M&C Embodied Human Composite arm, provide a software development guide, and showcase successful application cases to help you understand how to effectively integrate the myArm M&C Embodied Human Composite Suite into a variety of applications. In addition, we provide a wealth of support and service information to ensure that you can get the necessary help in any technical challenge.
### gitbook-en
English Version: https://docs.elephantrobotics.com/docs/myarm-MC-embodied-en/
### gitbook-cn
Chinese Version: https://docs.elephantrobotics.com/docs/myarm-MC-embodied-cn/

Document Overview
---

Based on your needs and the professional level of myArm M750 application development, you can choose to follow this sequence from start to finish or use it as an independent reference. You can navigate to any section using the sidebar navigation on the left at any time. The document is divided into the following five major sections:

#### Product Information
The Product Information section provides you with a basic overview of the robotic arm, including design intent, key features, and application scenarios, helping you quickly understand the basic characteristics and usage environment of the product. Additionally, this section will detail application examples and supported extension development, providing you with necessary development guidelines and resources. Relevant purchase links and channels will be provided at the end for your convenience.

#### Product Parameters
The Product Parameters section will showcase detailed technical specifications including machine specifications, control core parameters, structural dimensions, and electrical characteristics, which are crucial for understanding the technical standards and performance indicators of the product. Additionally, Cartesian coordinate system information regarding the robotic arm's working range and precision will be provided as a reference for users who require precise operations.

#### Features and Applications
The Features and Applications section elaborates on the basic functionalities of the robotic arm and software usage methods, including system usage instructions and firmware functionalities. The software development guide provides guidance based on different development environments such as Python and ROS, supporting technical developers in application extensions. By showcasing successful application cases and providing supporting resources, we aim to offer practical references and necessary support materials for you to better understand and utilize the product.

#### Support and Services
The Support and Services section will provide you with comprehensive troubleshooting guides and post-purchase service information such as warranty and service terms, helping you quickly resolve issues and ensuring you understand your rights and obligations after purchase. Additionally, the 'About Us' section enhances users' understanding of the design and manufacturer of the myArm series products, aiming to build trust and brand loyalty.

#### Acknowledgments
We appreciate you taking the time to read the myArm M&C Embodied Human Composite Kit user manual. We hope that this document will help you better understand and use this robot effectively, thereby stimulating your creativity. If you have any questions or need further assistance, please feel free to contact our customer support team. We look forward to seeing you complete innovative projects with the myArm M&C Embodied Human Composite Kit and welcome you to our rapidly growing developer community.

# Summary

## Product Information

  - [1 Product Introduction](2-ProductInformation/1-ProductIntroduction/1-ProductIntroduction.md)
  - [2 Product Specifications](2-ProductInformation/2-ProductParameters/2-ProductParameters.md)

## Initial Setup

  - [3 User Instructions](3-BasicSettings/3-UserInstructions/3-UserInstructions.md)
  - [4 Initial Installation](3-BasicSettings/4-FirstTimeInstallation/4-FirstTimeInstallation.md)

## Features and Applications

  - [5 Basic Function](4-FunctionsAndApplications/5-BasicFunctions/README.md)
    - [5.1 MyArm750-Minirobot](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.1-MinirobotGuide.md)
      - [1 Minirobot User Guide](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.1-MinirobotGuide.md)
      - [2 Drag-and-drop teaching](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.2-maincontrol.md)
      - [3 Zero Calibrate](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.3-calibrate.md)
      - [4 Communication Transponder](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.4-transponder.md)
      - [5 Status Information](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.5-information.md)
      - [6 Burn Function](4-FunctionsAndApplications/5-BasicFunctions/5.1-M750-Minirobot/5.1.6-flash.md)
    - [5.2 MyArm C650 Minirobot](4-FunctionsAndApplications/5-BasicFunctions/5.2-C650-Minirobot/README.md)
      - [1 Minirobot User Guide](4-FunctionsAndApplications/5-BasicFunctions/5.2-C650-Minirobot/5.2.1-MinirobotGuide.md)
      - [2 Zero Calibrate](4-FunctionsAndApplications/5-BasicFunctions/5.2-C650-Minirobot/5.2.2-calibrate.md)
      - [3 Communication Transponder](4-FunctionsAndApplications/5-BasicFunctions/5.2-C650-Minirobot/5.2.3-transponder.md)
      - [4 Status Information](4-FunctionsAndApplications/5-BasicFunctions/5.2-C650-Minirobot/5.2.4-information.md)
    - [5.3 Tracer car remote control function](4-FunctionsAndApplications/5-BasicFunctions/5.3-TracerCarRemoteControlFunction/tracerremotecontrol.md)

  - [6 Software Development Guide](4-FunctionsAndApplications/6-SDKDevelopment/README.md)
    - [6.1 Python](4-FunctionsAndApplications/6-SDKDevelopment/6.1-BasedOnPythonDevelopmentAndUse/1_download.md)
      - [API](4-FunctionsAndApplications/6-SDKDevelopment/6.1-BasedOnPythonDevelopmentAndUse/2_API.md)
      - [Related Examples](4-FunctionsAndApplications/6-SDKDevelopment/6.1-BasedOnPythonDevelopmentAndUse/6_example.md)
      - [Tracer Car API](4-FunctionsAndApplications/6-SDKDevelopment/6.1-BasedOnPythonDevelopmentAndUse/4_tracer_API.md)
      - [Tracer Motion Control Case](4-FunctionsAndApplications/6-SDKDevelopment/6.1-BasedOnPythonDevelopmentAndUse/5_tracer_example.md)
    - [6.2 ROS1](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/1_download.md)
      - [ROS workspace code and usage](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/2_workcode.md)
      - [Common ROS tool commands](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/3_ROScode.md)
      - [ROS architecture and communication](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/4_communication.md)
      - [Tracer Keyboard Control](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/5_tracer_keyboard_control.md)
      - [Radar Mapping and Navigation](4-FunctionsAndApplications/6-SDKDevelopment/6.2-DevelopmentAndUseBasedOnROS1/6_tracer_map_navigation.md)

    - [6.3 ROS2](4-FunctionsAndApplications/6-SDKDevelopment/6.3-DevelopmentAndUseBasedOnROS2/1_download.md)
      - [ROS workspace code and usage](4-FunctionsAndApplications/6-SDKDevelopment/6.3-DevelopmentAndUseBasedOnROS2/2_workcode.md)
      - [Common ROS tool commands](4-FunctionsAndApplications/6-SDKDevelopment/6.3-DevelopmentAndUseBasedOnROS2/3_ROScode.md)
      - [ROS architecture and communication](4-FunctionsAndApplications/6-SDKDevelopment/6.3-DevelopmentAndUseBasedOnROS2/4_communication.md)

    - [6.4 Communication Packages](4-FunctionsAndApplications/6-SDKDevelopment/5.4-DevelopmentBasedOnCommunicationProtocolPackage/5.4.1-M750-CommunicationDoc.md)
      - [1 MyArm M750](4-FunctionsAndApplications/6-SDKDevelopment/6.4-DevelopmentBasedOnCommunicationProtocolPackage/6.4.1-M750-CommunicationDoc.md)
      - [ 2 MyArm C650](4-FunctionsAndApplications/6-SDKDevelopment/6.4-DevelopmentBasedOnCommunicationProtocolPackage/6.4.2-C650-CommunicationDoc.md)
      - [ 3 Tracer Mobile Chassis](4-FunctionsAndApplications/6-SDKDevelopment/6.4-DevelopmentBasedOnCommunicationProtocolPackage/6.4.3-Tracer-CommunicationDoc.md)

    
  - [7 Successful Cases](4-FunctionsAndApplications/7-SuccessfulCases/7-SuccessfulCases.md)
    * [1 myarm mc remote operation case](4-FunctionsAndApplications/7-SuccessfulCases/7.1-demo_add.md)
    * [2 Keyboard control case](4-FunctionsAndApplications/7-SuccessfulCases/key.md)
    * [3 Palletizing and handling case](4-FunctionsAndApplications/7-SuccessfulCases/coords.md)


## Support and Services

  - [8 About Us](5-SupportAndService/5-SupportAndService.md)

## Acknowledgments

  - [9 Acknowledgments](6-Acknowledgments/6-Acknowledgments.md)


 
