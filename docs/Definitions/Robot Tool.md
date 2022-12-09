---
layout: default
title: Robot Tool
nav_order: 3
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** 
Defines a robot tool based on attachment and end-effector planes. It will be automatically registered in the RAPID system code of any [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component.

## **Input Parameters**

**Name (N):** Defines the robot tool name based on a string. This name must be unique and shouldn’t start with a number or use special characters.

**Mesh (M):** Defines the robot tool mesh.

**Attachment Plane (AP):** Defines the attachment plane for the robot tool based on a plane.

**Tool Plane (TP):** Defines the effector plane for the robot tool based on a plane.

## **Variable Input Parameters**

Through the right-click menu of the component the following variable input parameters can be added:

**Mass (M):** Defines the weight of the tool load in kg. The default value is set to 0.001 kg.

**Center of Gravity (CG):** Defines the position and orientation of the center of gravity of the tool load based on a plane. The default position is set to (0, 0, 0.001), and the default quaternion orientation is set to (1, 0, 0, 0).

**Moment of Intertia (MI):** Defines the moment of inertia of the tool load in kgm2. The default value is set to (0, 0, 0). 

## **Output Parameters**

[**Robot Tool**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) **(RT):** Contains the robot tool information.

## **Usage**

[**Definitions**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:**  
Plug the Robot Tool output of this component into the Robot Tool input of a [Robot]({{ site.baseurl }}{% link docs/Definitions/Robot.md %}) component. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the Robot Tool output of this component into the Robot Tool input of a [Override Robot Tool]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Override Robot Tool.md %}) component.
