---
layout: default
title: Batagur Setup
nav_order: 5
has_children: true
has_toc: false
---

# **{{page.title}}**

The main functionality of the Grasshopper addin, Batagur is collision-free motion planning. For incorporating this and other functionality Batagur is connecting to [MoveIt](https://moveit.ros.org/){:target="_blank"}, an easy-to-use robotics platform for developing advanced applications. MoveIt is running inside [ROS](https://www.ros.org/){:target="_blank"} (Robot Operation Software) a flexible framework for writing robot software.<br/>
For connecting ROS with Grasshopper the package [Rosbridge](http://wiki.ros.org/rosbridge_suite){:target="_blank"} is used, a JSON API to ROS functionality for non-ROS programs.
Besides that, one easy way of setting up everything is installing everything on Ubuntu.<br/>
Therefore, setting up Batagur, ROS, MoveIt, Rosbridge and Ubuntu are required.<br/>
This tutorial will suggest one specific way of setting up these software packages, despite there are multiple different ways of doing it. 


![GH-ROS-workflow]({{ site.baseurl }}/assets/images/Batagur/GH-ROS-workflow_01.png){:class="img-responsive"}
This is a schematic communication workflow between ROS and Grasshopper.
