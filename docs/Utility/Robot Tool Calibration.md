---
layout: default
title: Robot Tool Calibration
nav_order: 2
parent: Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Utility/index.md %})**:** EXPERIMENTAL! Calculates the robot tool center point (TCP) from given joint positions. At least four different joint positions need to be declared.

## **Input Parameters**

[**Robot**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot.md %}) **(R):** Defines the robot based on a robot parameter. Provide the robot that you use for your tool calibration. 

**[Robot Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJ):** Defines the robot joint positions.

**[External Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Defines the external axis joint positions. By default empty external joint positions will be used with all external joint positions set to `9E9` (undefined / not connected). 

## **Output Parameters**

**TCP (P):** Contains the calibrated tool center point (TCP) as a point.

**Errors (E):** Contains the maximum calibration errors in x-, y- and z-direction as a vector.

## **Usage**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** Jog the robot to at least four different positions with the tool tip located at the same location. Feed these joint positions to this component and it will result the calibrated tool center point. The [Get Controller]({{ site.baseurl }}{% link docs/Controller Utility/Get Controller.md %}) component and [Get Axis Values]({{ site.baseurl }}{% link docs/Controller Utility/Get Axis Values.md %}) component can be used to obtain these joint positions inside Grasshopper.