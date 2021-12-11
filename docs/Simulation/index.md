---
layout: default
title: Simulation Components
nav_order: 7
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Simulation components are used to visually approximate the movement behavior of the robot before running the RAPID main and base code on the robot controller.
To simulate the robot movement path all [Actions]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) from the [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) category 
can be plugged into the [Path Generator]({{ site.baseurl }}{% link docs/Simulation/Path Generator.md %})component which also generates 
corresponding axis values for every path position. To visualize the robot geometry inside of Rhino the [Forward Kinematics]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %}) component can be used by feeding in any axis values.

## **Components**

[**Forward Kinematics**]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %})**:** Computes the position of the end-effector of a defined ABB robot based on a set of given axis values. It can be also used for visualizing the robot mesh inside of Rhino.

[**Inverse Kinematics**]({{ site.baseurl }}{% link docs/Simulation/Inverse Kinematics.md %})**:** Computes the axis values for a defined ABB robot based on an Action: Target.

[**Path Generator**]({{ site.baseurl }}{% link docs/Simulation/Path Generator.md %})**:** Generates and displays the movement path for a defined ABB robot based on a list of Actions. It can be also used for visually simulating and animating the robot movement inside of Rhino by using the Forward Kinematics component.
