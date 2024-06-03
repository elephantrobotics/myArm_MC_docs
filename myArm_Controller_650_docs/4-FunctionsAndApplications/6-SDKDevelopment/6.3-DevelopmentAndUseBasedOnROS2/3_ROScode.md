# Basic tool

In this chapter, you will learn about the common command tools of ROS2.

# 1 Topics

ROS2 breaks complex systems down into many modular nodes. Topics are a vital element of the ROS graph that act as a bus for nodes to exchange messages. Topics are one of the main ways in which data is moved between nodes and therefore between different parts of the system.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

- **topics help**
> ros2 topics -h

- **Start turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key  


- **Node Relationship Diagram**
> rqt_graph

- **Learn about topic-related commands**
> ros2 topics -h

- **topics list**
> ros2 topic list  
> ros2 topic list -t # Display the corresponding message type

- **View topic content**
> ros2 topic echo <topic_name>  
> ros2 topic echo /turtle1/cmd_vel  

- **Display topic-related information, type**
> ros2 topic info <topic_name>  
> \# Output /turtle1/cmd_vel topic related information  
> ros2 topic info /turtle1/cmd_vel

- **Display interface related information**
> ros2 interface show <msg_type>  
> \# Output geometry_msgs/msg/Twist interface related information  
> ros2 interface show geometry_msgs/msg/Twist

- **Issue an order**
> ros2 topic pub \<topic_name\> \<msg_type\> \<args\>   
> \# Issue speed command  
> ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"  
> \# Issue speed commands at a certain frequency    
> ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"  


# 2 Nodes

Each node in ROS should be responsible for a single, module purpose (e.g. one node for controlling wheel motors, one node for controlling a laser range-finder, etc). Each node can send and receive data to other nodes via topics, services, actions, or parameters. A full robotic system is comprised of many nodes working in concert. In ROS 2, a single executable (C++ program, Python program, etc.) can contain one or more nodes.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)


- **nodes help**
> ros2 nodes -h

- **Start turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key

- **View the node list**
> ros2 node list

- **View Node Relationship Diagram**
> rqt_graph

- **Remapping**
> ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle  
> ros2 node list  

- **View node information**
> ros2 node info \<node_name\>  
> ros2 node info /my_turtle  


# 3 Services

Services are another method of communication for nodes in the ROS graph. Services are based on a call-and-response model, versus topics’ publisher-subscriber model. While topics allow nodes to subscribe to data streams and get continual updates, services only provide data when they are specifically called by a client.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)  

- **services help**
> ros2 service -h

- **Start turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key

- **View the service list**
> ros2 service list  
> \# Display service list and message type  
> ros2 service list -t

- **View the message types received by the service**
> ros2 service type \<service_name\>  
> ros2 service type /clear

- **Find services that use a certain message type**
> ros2 service find \<type_name\>  
> ros2 service find std_srvs/srv/Empty  

- **View Service Message Type Definitions**
> ros2 interface show \<type_name\>.srv  
> ros2 interface show std_srvs/srv/Empty.srv

- **Call the service command to clear the walking track**
> ros2 service call \<service_name\> \<service_type\>  
> ros2 service call /clear std_srvs/srv/Empty

- **Spawn a new turtle**
> ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'turtle2'}"  

# 4 Parameters

A parameter is a configuration value of a node. You can think of parameters as node settings. A node can store parameters as integers, floats, booleans, strings, and lists. In ROS 2, each node maintains its own parameters. For more background on parameters, please see the concept document.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html)  

- **parameters help**
> ros2 param -h

- **Start turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key

- **View service list**
> ros2 param list

- **Get the parameter value**
> ros2 param get \<node_name\> \<parameter_name\>   
> ros2 param get /turtlesim background_g

- **Set parameter values**
> ros2 param set \<node_name\> \<parameter_name\> \<value\>  
> ros2 param set /turtlesim background_r 150

- **Export parameter values**
> ros2 param dump \<node_name\>  
> ros2 param dump /turtlesim

- **Import parameters independently**
> ros2 param load \<node_name\> \<parameter_file\>  
> ros2 param load /turtlesim ./turtlesim.yaml

- **Start the node and import parameters at the same time**
> ros2 run \<package_name\> \<executable_name\> --ros-args --params-file \<file_name\>  
> ros2 run turtlesim turtlesim_node --ros-args --params-file ./turtlesim.yaml  

# 5 Actions

Actions are one of the communication types in ROS 2 and are intended for long running tasks. They consist of three parts: a goal, feedback, and a result.

Actions are built on topics and services. Their functionality is similar to services, except actions are preemptable (you can cancel them while executing). They also provide steady feedback, as opposed to services which return a single response.

Actions use a client-server model, similar to the publisher-subscriber model (described in the topics tutorial). An “action client” node sends a goal to an “action server” node that acknowledges the goal and returns a stream of feedback and a result.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)  

- **action help**
> ros2 action -h

- **Start turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key

Press G|B|V|C|D|E|R|T to achieve rotation, press F to cancel

- **View the server and client of the node action**
> ros2 node info /turtlesim

- **View action list**
> ros2 action list  
> ros2 action list -t # show action type

- **view action info**
> ros2 action info \<action\>  
> ros2 action info /turtle1/rotate_absolute

- **View action message content**
> ros2 interface show turtlesim/action/RotateAbsolute

- **Send action target information**
> ros2 action send_goal \<action_name\> \<action_type\>  
> ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"  
> \# With feedback information  
> ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 0}" --feedback


# 6 RQt

RQt is a graphical user interface framework that implements various tools and interfaces in the form of plugins. One can run all the existing GUI tools as dockable windows within RQt! The tools can still run in a traditional standalone method, but RQt makes it easier to manage all the various windows in a single screen layout.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Concepts/About-RQt.html)  

You can run any RQt tools/plugins easily by:  
> rqt

- **rqt help**
> rqt -h

- **tart turtlesim and keyboard control**
> ros2 run turtlesim turtlesim_node  
> ros2 run turtlesim turtle_teleop_key

- Action Type Browser: / Plugins -> Actions ->Action Type Browser

- parameter reconfiguration: / Plugins -> configuration ->Parameter Reconfigure

- Node grap: /Node Graph

- control steering: /Plugins -> Robot Tools -> Robot Steering

- service invocation: /Plugins -> Services -> Service Caller

- Service Type Browser: Plugins -> Services -> Service Type Browser

- message release: Plugins -> Topics -> Message Publisher

- Message Type Browser: Plugins -> Topics -> Message Type Browser

- topic list: Plugins -> Topics -> Topic Monitor

- draw a graph: Plugins -> Visualization -> Plot

- **View logs: rqt_console**
> ros2 run rqt_console rqt_console  
> ros2 run turtlesim turtlesim_node  
> ros2 topic pub -r 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}"  


# 7 TF2

tf2 is the transform library, which lets the user keep track of multiple coordinate frames over time. tf2 maintains the relationship between coordinate frames in a tree structure buffered in time and lets the user transform points, vectors, etc. between any two coordinate frames at any desired point in time.

Specific reference: [Official Tutorials](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html)  

Let’s start by installing the demo package and its dependencies.  
> sudo apt-get install ros-foxy-turtle-tf2-py ros-foxy-tf2-tools ros-foxy-tf-transformations

- **follow**

- **launch starts 2 little turtles, the first little turtle automatically follows the second one**
> ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py

- **Control the movement of the first little turtle through the keyboard**
> ros2 run turtlesim turtle_teleop_key

- **View TF tree**
> ros2 run tf2_tools view_frames.py  
> evince frames.pdf

- **View the relationship between two coordinate systems**
> ros2 run tf2_ros tf2_echo [reference_frame] [target_frame]  
> ros2 run tf2_ros tf2_echo turtle2 turtle1

- **View TF relationships on rviz**
> ros2 run rviz2 rviz2 -d $(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz




# 8、Introduction to the URDF  

- Unified Robot Description Format，The Unified Robot Description Format, or URDF for short. The urdf feature pack in ROS contains a C++ parser for URDF, and URDF files describe the robot model in XML format.  
- URDF cannot be used on its own and needs to be combined with Rviz2 or Gazebo, URDF is just a file that needs to be rendered as a graphical robot model in Rviz2 or Gazebo.  

### 8.1 urdf file description  

Code examples:  
Only some of the codes are screenshotted for display:    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/urdf1.jpg" alt="7.1.1-1" style="zoom:100%;" />    
<img src="../../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2 -DevelopmentAndUseBasedOnROS1/1_download/urdf2.jpg" alt="7.1.1-1" style="zoom:100%;" />  


- **Install dependent libraries**
> sudo apt install ros-foxy-joint-state-publisher-gui ros-foxy-joint-state-publisher  
> sudo apt install ros-foxy-xacro

- **Download the source code**
> cd ~/dev_ws  
> git clone -b ros2 https://github.com/ros/urdf_tutorial.git src/urdf_tutorial

- **Compiling the source code**
> colcon build --packages-select urdf_tutorial

- **Running the example**
> ros2 launch urdf_tutorial display.launch.py model:=urdf/01-myfirst.urdf



---

[← last page](2_workcode.md) | [next page →](4_communication.md)