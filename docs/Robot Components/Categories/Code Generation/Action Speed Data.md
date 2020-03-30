---
layout: default
title: Action Speed Data
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **Speed Data**

## **Description**

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Defines a speed data for a Movement or Absolute Joint Movement instruction.

## **Input Parameters**

**Name (N):** Defines the name of the speed data based on a string value. Each speed data name needs to be unique. The first letter shouldn’t be a number. Don’t use special characters.

**TCP Velocity (vTCP):** Defines the TCP moving velocity in mm/s as an integer value.

**ORI Velocity (vORI):** Defines the reorientation speed of the robot tool in degrees/s as an integer value.

**LEAX Velocity (vLEAX):** Defines the linear external axes moving velocity in mm/s as an integer value.

**REAX Velocity (vREAX):** Defines the external axes reorientation speed in degrees/s as an integer value.

## **Output Parameters**

**Speed Data (SD):** Contains the Speed Data instructions as Action for a Action: Movement.

## **Usage**

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Speed Data output of this component into the Speed Data input of the Action: Movement component to set the speed behavior of a robot movement instruction in the RAPID Main Code. This will also add a speeddata variable to the RAPID Main Code.