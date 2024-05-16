# 通信
  我们的MyarmC650主要是采用的是 **话题（Topic）** 的方式进行通信  
   
   > 话题（Topic）是ROS最常用的通信机制之一、它基于发布者-订阅者模式，其中一个节点作为发布者（Publisher）发布消息，而其他节点作为订阅者（Subscriber）接收消息。发布者可以同时向多个订阅者发布消息，而订阅者可以从多个发布者接收消息。这种方式非常适用于需要实时数据更新的情况，例如传感器数据的处理和实时控制。  

首先在.py文件中创建一个Publisher，将我们的消息发布给MyarmC650   
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/publisher.jpg" alt="7.1.1-1" style="zoom:100%;" />   

接下来在工作空间打开终端,启动ROS：  
> roscore

再新建一个终端，输入：  
> soure devel/setup.bash  
> roslaunch myarm_c650 test.launch

打开rviz后再启动我们的 **test2.py** 文件  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/runpython2.jpg" alt="7.1.1-1" style="zoom:100%;" />   

再新建一个终端，输入：
> rosnode kill /joint_state_publisher_gui    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/kill1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

最后我们再打开一个新终端，输入：
> rqt_graph 

我们能看到节点的所有信息  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/publisher1.jpg" alt="7.1.1-1" style="zoom:100%;" /> 

MyarmC650是处于可以用手控制其运动的状态  
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch6.jpg" alt="7.1.1-1" style="zoom:100%;" /> 

---

[← 上一页](3_ROScode.md) | [下一节 →](../5.4-DevelopmentBasedOnCommunicationProtocolPackage/5.4.1-CommunicationDoc.md)