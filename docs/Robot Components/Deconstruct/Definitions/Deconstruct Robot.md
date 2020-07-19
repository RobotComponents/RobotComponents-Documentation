---
layout: default
title: Deconstruct Robot
nav_order: 2
parent: Definition Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruct**]({{ site.baseurl }}{% link docs/Robot Components/Deconstruct/index.md %})**:** 
Deconstructs a [Robot]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot.md %}) into its parameters.

## **Input Parameters**

[**Robot**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot.md %}) **(R):** Defines the [Robot]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot.md %}) to deconstruct.

## **Output Parameters**

**Name (N):** Contains the robot name as a string value.

**Mesh (M):** Contains the robot mesh as a list of meshes. For a six-axis robot, this would make regularly a list of seven meshes. One mesh for the robot base and an additional mesh for every robot axis.

**Axis Planes (AP):** Contains the robot axis planes as a list of planes. The count of this list should be equal to the count of the axis limits list.

**Axis Limits (AL):** Contains the robot axis limits as a list of intervals. The count of this list should be equal to the count of the axis planes list.

**Position Plane (PP):** Contains the position plane of the robot as a plane. In the case if an external linear axes is moving the robot. The position plane is location of the robot when the external axes values are zero. 

**Mounting Frame (MF):** Contains the mounting frame of the robot tool as a plane. The mounting frame is the frame any robot tool is attached to.

[**Robot Tool**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) **(RT):** Contains the [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) of the deconstructed robot. 

[**External Axes**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/External Axis.md %}) **(EA):** Contains the [External Axis]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/External Axis.md %}) of the robot.

