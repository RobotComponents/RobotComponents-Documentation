---
layout: default
title: Catkin Workspace
nav_order: 1
parent: Batagur Setup
has_toc: false
---

# **{{page.title}}**

ROS code needs to be set up in a Catkin Workspace. A Workspace is basically a set of directories in which a related ROS code lives.
For Batagur you have to store there some information about the Robots.<br/>
RobotComponents provides you with some example files for your Workspace. This example files are required if you want to run the Batagur Grasshopper example files.
 
Catkin is a ROS build system and included by default when ROS is installed. Catkin is used by ROS to generate libraries, executable programs, generated scripts, exported interfaces that other code can use.<br/>
It´s not required to know more details about catkin, but more information can be found [here](http://wiki.ros.org/catkin){:target="_blank"}.

## **Creating a Workspace**
Running this command line code will create a workspace folder and initialize it:<br/>
`mkdir -p ~/catkin_ws/src`<br/>
`cd ~/catkin_ws/`<br/>
`catkin_make`<br/>

The `catkin_make` command created extra folders within your workspace.<br/>
The catkin_make command created extra folders within your workspace, e.g. _build_ and _devel_. While build holds libraries and executable programs devel holds the setup bash file (_setup.bash_). To call workspace programs form your terminal you need to tell your terminal how. The _setup.bash_ file is doing that for you. You could source it each time you open a new terminal by calling<br/>
`source devel/setup.bash`<br/>
or you add some lines of text at the end of your _.bashrc_ file which is located at the home/user directory. Open the file in a text editor and add:<br/>
`source ~/catkin_ws/devel/setup.bash`<br/>
If you followed the ROS installation you added already the ROS _setup.bash_ file to it. Therefore, a text line `source /opt/ros/melodic/setup.bash` should be added already.<br/>
If you can not find the _.bashrc_ file, Ubuntu might hide it. You have to enable _show hidden files_.
If you want to have more insides you could have a look [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace){:target="_blank"}.

## **Example Files for Batagur**
You can find [here](https://github.com/EDEK-UniKassel/Batagur-ROS-Workspace){:target="_blank"}, the files for your ROS workspace.
You need to have git installed to follow the installation instructions. 


