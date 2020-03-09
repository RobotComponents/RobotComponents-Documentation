---
layout: default
title: ROS Environment
nav_order: 0
parent: Batagur Setup
has_toc: false
---

## Ubuntu Installation
One easy, convenient way of installing [Ubuntu](https://ubuntu.com/){:target="_blank"} on the same machine Rhino/Grasshopper is running is to set up a Virtual Machine. Recommended is [VMware Player](https://www.vmware.com/products/workstation-player.html){:target="_blank"} because there are known issues with ROS with VirtualBox. For non-commercial use, VMware is for free. Batagur is developed with [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/){:target="_blank"} which will work fine with the ROS version we need.<br/>
The installation should be easy and straight forward.

## ROS Installation
If you have Ubuntu running and not confident in using the terminal it is highly recommended [learning the basics](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview){:target="_blank"}. Even if Batagur will work fine with the absolute minimum use of Ubuntu/ROS/MoveIt and the terminal for installing and for debugging the basics are extremely useful.
For the installation, follow [these](http://wiki.ros.org/melodic/Installation/Ubuntu){:target="_blank"} instructions. It is recommended to install the Desktop-Full configuration which comes with useful tools for our desired setup.<br/>
You can check if ROS workes, when you type in <br/>
`roscore`<br/>
and there is no error message appearing.
It should look more like this.<br/>
![roscore]({{ site.baseurl }}/assets/images/Batagur/roscore_01.png){:class="img-responsive"}

To understand what ROS is and how it works you can follow the [start guide](http://wiki.ros.org/ROS/StartGuide){:target="_blank"}.

## MoveIt Installation
For installing MoveIt follow the official instructions which you can find [here](https://moveit.ros.org/install/){:target="_blank"}.

## Rosbrige Installation
The connecting ROS to other non-ROS programs you need to install Rosbridge.
You can find the instruction [here](http://wiki.ros.org/rosbridge_suite){:target="_blank"} in the Installation section. It´s a one-line command.<br/>
_Note: If you followed this instruction your `<rosdistro>` is melodic. Therefore, the command should be:_<br/>
`sudo apt-get install ros-melodic-rosbridge-server`
To test Rosbridge work, start the server with the command:
`roslaunch rosbridge_server rosbridge_websocket.launch`