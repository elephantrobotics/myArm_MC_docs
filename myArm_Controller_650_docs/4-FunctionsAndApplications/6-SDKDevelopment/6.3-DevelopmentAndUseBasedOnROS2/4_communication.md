# correspondence
  Our MyarmC650 mainly uses a **Topic** method for communication    
   
   > Topic is one of the most commonly used communication mechanisms in ROS, which is based on the publisher-subscriber model, in which one node publishes messages as publishers and other nodes receive messages as subscribers. A publisher can publish messages to multiple subscribers at the same time, and subscribers can receive messages from multiple publishers. This approach is ideal for situations that require real-time data updates, such as processing and real-time control of sensor data.    

Start by creating a Publisher in the .py file to post our message to the MyarmC650     
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/ros2publisher.jpg" alt="7.1.1-1" style="zoom:100%;" />   

Next, open the terminal in the workspace and start ROS2:    
> colcon build 
  
> soure install/setup.bash  
> ros2 launch myarm_c650 test.launch.py

Open RVIZ2 and then launch our **test.py** file    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/runpython2.jpg" alt="7.1.1-1" style="zoom:100%;" />   

Create another terminal and enter:  
> ros2 node list  
> ps aux | grep joint_state_publisher  
> kill 32695  #Kill the string of randomly generated numbers    

<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/ros2kill1.jpg" alt="7.1.1-1" style="zoom:100%;" />   

Finally, we open a new terminal and enter:  
> rqt_graph 

We can see all the information about the node    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.3 -DevelopmentAndUseBasedOnROS2/1_download/ros2rqt_graph.jpg" alt="7.1.1-1" style="zoom:100%;" />   

The MyarmC650 is also in a state where it can be manually moved    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/launch6.jpg" alt="7.1.1-1" style="zoom:100%;" /> 

---

[← last page](3_ROScode.md) | [next section →](../6.4-DevelopmentBasedOnCommunicationProtocolPackage/6.4.1-CommunicationDoc.md)