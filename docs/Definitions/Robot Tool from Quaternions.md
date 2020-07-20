---
layout: default
title: Robot Tool from Quaternions
nav_order: 5
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** 
Defines a robot tool based on quaternion values. It will be automatically registered in the RAPID system code of any [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component.

## **Input Parameters**

**Name (N):** Defines the robot tool name based on a string. This name must be unique and shouldn't start with a number or use special characters.

**Mesh (M):** Defines the robot tool mesh.

**Attachment Plane (AP):** Defines the attachment plane for the robot tool based on a plane.

**Coord X (X):** Defines the x coordinate of the tool center point as number.

**Coord Y (Y):** Defines the y coordinate of the tool center point as number.

**Coord Z (Z):** Defines the z coordinate of the tool center point as number.

**Quaternion A (A):** Defines the real part of the quaternion as number.

**Quaternion B (B):** Defines the first imaginary coefficient of the quaternion as number.

**Quaternion C (C):** Defines the second imaginary coefficient of the quaternion as number.

**Quaternion D (D):** Defines the third imaginary coefficient of the quaternion as number.

## **Output Parameters**

[**Robot Tool**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) **(RT):** Contains the robot tool information.

## **Usage**

[**Definitions**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** Plug the Robot Tool output parameter of this component into the Robot Tool input parameter of a [Robot]({{ site.baseurl }}{% link docs/Definitions/Robot.md %}) component. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the Robot Tool output parameter of this component into the Robot Tool input parameter of a [Override Robot Tool]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Override Robot Tool.md %}) component.
