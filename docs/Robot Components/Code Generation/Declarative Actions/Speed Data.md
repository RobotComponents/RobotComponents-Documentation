---
layout: default
title: Speed Data
nav_order: 2
parent: Declarative Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Declarative Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/index.md %})**:** 
Defines the speed data for a [Move]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Move.md %}) or [Absolute Joint Movement]({{ site.baseurl }}{link docs/Robot Components/Parameters/Actions/Absolute Joint Movement.md %}) component. The Speed data is used to specify the velocity at which both the robot and the external axes move. 

## **Input Parameters**

**Name (N):** Defines the name of the speed data based on a string value. Each speed data name needs to be unique. The first letter shouldn’t be a number. Don’t use special characters.

**TCP Velocity (vTCP):** Defines the velocity of the tool center point (TCP) in mm/s as a number value.

**ORI Velocity (vORI):** Defines the reorientation velocity of the robot tool in degrees/s as a number value.

**LEAX Velocity (vLEAX):** Defines the linear external axes velocity in mm/s as a number value.

**REAX Velocity (vREAX):** Defines the external axes reorientation velocity in degrees/s as a number value.

## **Output Parameters**

**Speed Data (SD):** Contains the Speed Data as action for a robot movement instruction.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Speed Data output of this component into the Speed Data input of the [Move]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Move.md %}) or [Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Absolute Joint Movement.md %}) component to set the speed behavior of the robot movement instruction. This will also add a speeddata declaration to the RAPID program module.