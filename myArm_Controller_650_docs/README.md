# myArm Controller 650
通用型6自由度机器人运动信息采集装置    

核心文档
---

本文档包含从产品简介、详细的技术参数到用户须知和首次安装指导的全面信息。我们将深入解释myArm C650机械臂的基础功能，提供软件开发指南，并展示成功的应用案例，帮助您了解如何将 myArm C650 有效整合进各种应用中。此外，我们还提供了丰富的支持与服务信息，确保您在遇到任何技术挑战时能够获得必要的帮助。
### gitbook-en
英文版本: https://docs.elephantrobotics.com/docs/myArm_Controller_650-en/
### gitbook-cn
中文版本: https://docs.elephantrobotics.com/docs/myArm_Controller_650-cn/

文档说明
---

根据您的需求以及 myArm C650 应用程序开发的专业水平，您可以选择从头到尾遵循该顺序，或将其用作独立参考。您可以随时使用左侧的侧边栏导航跳转到任何部分，全文共分为以下五大板块：

#### 产品信息
产品信息板块将为您提供机械臂的基本概述，包括设计意图、主要功能和应用场景，帮助您快速了解产品的基本特性和使用环境。此外，这一部分将详细介绍产品的应用实例和支持的扩展开发，为您提供必要的开发指南和资源。文末将给出相关购买链接和渠道，方便您进行购买。

#### 产品参数
产品参数部分将向您展示包括机器规格、控制核心参数、结构尺寸和电气特性等详细的技术规格，这些信息对于理解产品的技术标准和性能指标至关重要。此外，还将提供关于机械臂工作范围和精确度的笛卡尔坐标系信息，为想要进行精密操作的用户提供参考。

#### 功能与应用
功能与应用板块详细介绍了机械臂的基础功能和软件使用方法，包括系统使用说明和固件功能。软件开发指南提供了基于不同开发环境的指导，如Python和ROS，支持技术开发者进行应用扩展。通过展示成功的应用案例和提供配套资源，为您提供实践参考和必要的支持材料，以便更深入地了解和使用产品。

#### 支持与服务
支持与服务板块将为您提供全面的故障排除指南和购买后的服务信息，如保修和服务条款，帮助您在遇到问题时能够快速解决，并确保您了解购买后的权利和义务。此外，'关于我们'部分加强了用户对myArm 系列产品设计及制造商的了解，旨在建立信任和品牌忠诚。

#### 致谢
我们非常感谢您花时间阅读 myArm C650 用户手册。我们希望本文档能够帮助您更好地了解并有效使用这款机器人，从而激发您的创造力。如果您有任何疑问或需要进一步帮助，请随时联系我们的客户支持团队。我们期待看到您使用 myArm C650 完成创新项目，并欢迎您加入我们快速发展的开发者社区。


文档目录  
---
# Summary

- **产品信息**

  - [1. 产品简介](2-ProductInformation/1-ProductIntroduction/1-ProductIntroduction.md)
  - [2. 产品参数](2-ProductInformation/2-ProductParameters/README.md)
    - [2.1 机器规格参数](2-ProductInformation/2-ProductParameters/2.1-MachineSpecifications/2.1.1-MachineSpecifications.md)
    - [2.2 控制核心参数](2-ProductInformation/2-ProductParameters/2.2-ControlCoreParameters/2.2.1-ControlCoreParameter.md)
    - [2.3 结构尺寸参数](2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/2.3.1-StructureParameter.md)
      <!-- - [2.4 电气特性参数]() -->
      <!-- - [2.5 笛卡尔坐标系]() -->

- **基础设置**

  - [3 用户须知](3-BasicSettings/3-UserInstructions/README.md)
    - [3.1 安全须知](3-BasicSettings/3-UserInstructions/3.1-SafetyInstructions/1-SafetyInstruction.md)
    - [3.2 运输和储存](3-BasicSettings/3-UserInstructions/3.2-TransportAndStorage/1-TransportandStorage.md)
    - [3.3 维护和保养](3-BasicSettings/3-UserInstructions/3.3-MaintenanceAndCare/1-MaintenanceandCare.md)
    <!-- - [3.4 常见问题解决]() -->
  - [4 首次安装](3-BasicSettings/4-FirstTimeInstallation/4.1-ProductStandardList/4.1.1-List.md)
    - [4.1 产品标准清单](3-BasicSettings/4-FirstTimeInstallation/4.1-ProductStandardList/4.1.1-List.md)
    - [4.2 产品开箱指南](3-BasicSettings/4-FirstTimeInstallation/4.2-ProductUnboxingGuide/4.2.1-Unboxing.md)
    - [4.3 开机检测指南](3-BasicSettings/4-FirstTimeInstallation/4.3-PowerOnDetectionGuide/0_StartRobot.md)
      - [1 结构安装和固定](3-BasicSettings/4-FirstTimeInstallation/4.3-PowerOnDetectionGuide/1_StructuralInstallation.md)
      - [2 外部电缆连接](3-BasicSettings/4-FirstTimeInstallation/4.3-PowerOnDetectionGuide/2_ExternalCableConnection.md)
      - [3 开机状态显示](3-BasicSettings/4-FirstTimeInstallation/4.3-PowerOnDetectionGuide/3_PowerOnStatusDisplay.md)
          <!-- - [4 基本功能检测](3-BasicSettings/4-FirstTimeInstallation/4.3-PowerOnDetectionGuide/4_BasicFunctionDetection.md) -->
          <!-- - [4.4 安装视频教程]() -->

- **功能与应用**

  - [5 基础功能](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/README.md)
    - [5.1 系统（功能）使用说明](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/README.md)
      - [5.1.1 Minirobot](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/README.md)
        - [1 Minirobot 使用指南](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/5.1.1.1-MinirobotGuide.md)
        - [2 零位校准](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/5.1.1.2-calibrate.md)
        - [3 通信转发](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/5.1.1.3-transponder.md)
        - [4 状态信息](4-FunctionsAndApplications/5-BasicFunctions/5.1-SystemInstructionsForUse/5.1.1-Minirobot/5.1.1.4-information.md)

  <!-- - [5.2 软件使用说明]()  -->
  <!-- - [5.3 固件功能说明]() -->

  - [6 软件开发指南](4-FunctionsAndApplications/6-SDKDevelopment/README.md)
    - [6.1 基于 python 开发使用](4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/1_download.md)
      - [下载与环境搭建](4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/1_download.md>)
      - [API](4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.md>)
      - [相关案例](4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/6_example.md>)
    - [6.2 基于通信协议包开发](4-FunctionsAndApplications/6-SDKDevelopment/5.4-DevelopmentBasedOnCommunicationProtocolPackage/5.4.1-CommunicationDoc.md)
  
  <!-- - [6.2 基于 ROS1 开发使用]() -->
  <!-- - [6.3 基于 ROS2 开发使用]() -->

  - [7. 成功案例](4-FunctionsAndApplications/7-SuccessfulCases/7-SuccessfulCases.md)
    <!-- - [8. 配套资源]() -->
      <!-- - [8.1 产品资料]() -->
      <!-- - [8.2 产品图纸]() -->
      <!-- - [8.3 软件资料及源码]() -->
      <!-- - [8.4 系统资料]() -->
      <!-- - [8.5 宣传资料]() -->

- **支持与服务**

  - [8 关于我们](5-SupportAndService/5-SupportAndService.md)

- **致谢**
  - [致谢](6-Acknowledgments/6-Acknowledgments.md)