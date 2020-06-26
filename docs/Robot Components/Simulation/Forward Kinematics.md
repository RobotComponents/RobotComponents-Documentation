---
layout: default
title: Forward Kinematics
nav_order: 2
parent: Simulation Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Simulation/index.md %})**:** 
Computes the position of the end-effector of a defined ABB robot based on a set of given axis values. 

## **Input Parameters**

[**Robot**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot.md %}) **(R):** Defines the robot based on a robot parameter. A custom robot can be created by using the [Robot]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot.md %}) component.

**Internal Axis Values (IAV):** Defines the robot internal axis values based on a list of numbers.

**External Axis Values (EAV):** Defines the robot external axis values based on a list of numbers.

## **Output Parameters**

**Posed Meshes (PM):** Contains the posed robot and external axis meshes.

**End Plane (EP):** Contains the robot's tool center point plane.

**External Axis Planes (EAP):** Contains a list with all external axis planes.

## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Simulation/index.md %})**:** 
Visualize a robot based on a given list of internal and external axis values. 
The robot mesh will be colored red if any axis values are invalid. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** 
Plug the End Plane output parameter of this component into the Plane input parameter of the [Target]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/Target.md %}) component.
