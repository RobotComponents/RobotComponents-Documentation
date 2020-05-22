---
layout: default
title: Action Target
nav_order: 1
parent: Code Generation Components
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** This component defines an instruction to change the current robot tool of the ABB robot for RAPID base code generation.

## **Input Parameters**

**Name (N):** Defines the name of the target based on a string value. Each target name should be unique. The first letter shouldn’t be a number. Don’t use special characters.

**Plane (P):** Defines the target plane of the target based on one or a list of planes. Note: You can use a Flip Plane X or Flip Plane Y component to flip the plane.

**Axis Configuration (AC):** Defines the axis configuration of the robot to reach the defined target plane based on an integer value. The range is 0 to 7. Read more on the topic of Robot Configuration Data in the official ABB Rechnical reference manual for RAPID Instructions.

## **Optional Input Parameters**

Through the right-click menu of the component additional inputs can be available:

**Reference Plane (RP):** TO DO

**External Axis Values:** Defines the current robot external axis values based on a list of doubles.

## **Output Parameters**

**Target (T):** Contains the defined target information as an Action for RAPID main code generation.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of this component.

## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Simulation/index.md %})**:** Plug the Target output of this component into the Target input of the Inverse Kinematics component to get the robots axis values for the defined target.

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Target output of this component into the Target input of the Action: Movement component to define a robot movement.