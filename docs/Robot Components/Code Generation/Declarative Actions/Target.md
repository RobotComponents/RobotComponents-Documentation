---
layout: default
title: Target
nav_order: 1
parent: Declarative Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Declarative Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/index.md %})**:** Defines the target for a [Move]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Move.md %}) component.

## **Input Parameters**

**Name (N):** Defines the name of the target based on a text value. Each target name should be unique. The first letter shouldn’t be a number. Don’t use special characters.

**Plane (P):** Defines the target plane of the target based on one plane or a list of planes. The target plane has to be defined in the work object coordinate system. Note: You can use a Flip Plane X or Flip Plane Y component to flip the plane.

**Axis Configuration (AC):** Defines the axis configuration of the robot to reach the defined target plane based on an integer value. The range is 0 to 7. Read more on the topic of Robot Configuration Data in the official ABB Rechnical reference manual for RAPID Instructions.

## **Variable Input Parameters**

Through the right-click menu of the component additional inputs can be available:

**Reference Plane (RP):** If this input is used the target planes will be reoriented from this reference plane to the world XY-plane. This a variable input parameter that can be accessed and enabled through the right-click menu of the component. 

**External Axis Values:** Defines the current robot external axis values based on number values. The default external axis value is set to `9e9`. For ABB this means that the axis is not connected. Robot Components recognizes this value as undefined external axis value. If external axes are used and no external axis values are defined the closed position of the target plane to the external linear axis will be used as axis value in case of an external linear axis, and an axis value of `0' will be used in case an external rotational axis is used and no axis value is defined. This a variable input parameter that can be accessed and enabled through the right-click menu of the component. 

## **Output Parameters**

**[Target]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Target.md %}) (T):** Contains the defined target information as action for a robot movement instruction.

## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Simulation/index.md %})**:** Plug the [Target]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Target.md %}) output parameter of this component into the target input parameter of the [Inverse Kinematics]({{ site.baseurl }}{% link docs/Robot Components/Simulation/Inverse Kinematics.md %}) component to get the robots axis values for the defined target.

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the [Target]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Target.md %}) output parameter of this component into the Target input parameter of the [Move]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Move.md %}) component to set the target of a robot movement instruction. This will also add a target declaration to the RAPID Program module.