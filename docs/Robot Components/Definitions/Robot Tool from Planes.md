---
layout: default
title: Robot Tool from Planes
nav_order: 3
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** 
Defines a robot tool based on attachment and end-effector planes. It will be automatically registered in the RAPID system code of any [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component.

## **Input Parameters**

**Name (N):** Defines the robot tool name based on a string. This name must be unique and shouldn’t start with a number or use special characters.

**Mesh (M):** Defines the robot tool mesh.

**Attachment Plane (AP):** Defines the attachment plane for the robot tool based on a plane.

**Tool Plane (TP):** Defines the effector plane for the robot tool based on a plane.

## **Output Parameters**

**Robot Tool (RT):** Contains the robot tool information.

**Robot Tool Code (RTC):** Contains the robot tool infortmation as a string for the RAPID system code.

## **Usage**

[**Definitions**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:**  
Plug the Robot Tool output of this component into the Robot Tool input of a [Robot]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot.md %}) component. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Robot Tool output of this component into the Robot Tool input of a [Override Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Override Robot Tool.md %}) component.
