---
layout: default
title: Robot Target
nav_order: 1
parent: Declarative Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Declarative Action**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/index.md %})**:** Defines a robot target for a [Move]({{ site.baseurl }}{% link docs/Parameters/Actions/Move.md %}) component. 

## **Input Parameters**

**Name (N):**  Defines the name of the target based on a text value. Each target name needs to be unique or empty. The first letter should not be a number. Do not use special characters. The variables names will be updated based on the list or datatree structure this component generates.

**Plane (P):** Defines the target plane of the target based on one plane or a list of planes. The target plane has to be defined in the work object coordinate system. Note: You can use a [Flip Plane X]({{ site.baseurl }}{% link docs/Utility/Flip Plane X.md %}) or [Flip Plane Y]({{ site.baseurl }}{% link docs/Utility/Flip Plane Y.md %}) component to invert the plane.

**Axis Configuration (AC):** Defines the axis configuration of the robot to reach the defined target plane based on an integer value. The range is 0 to 7. Read more on the topic of Robot Configuration Data in the official ABB Rechnical reference manual for RAPID Instructions.

## **Variable Input Parameters**

Through the right-click menu of the component the following variable input parameters can be added:

**Reference Plane (RP):** If this input is used the target planes will be reoriented from this reference plane to the world XY-plane.

**[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Defines the current robot external axis values based on an [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) parameter. The default external axis values are set to 9e9. For ABB this means that the axis is not connected. Robot Components recognizes this value as undefined external axis value. If external axes are used and no external axis values are defined the closed position of the target plane to the external linear axis will be used as axis value in case of an external linear axis, and an axis value of 0 will be used in case an external rotational axis is used and no axis value is defined.

## **Output Parameters**

**[Robot Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Target.md %}) (SD):** Contains the defined robot target information for a robot movement instruction.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Robot Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Target.md %}) output parameter of this component into the Target input parameter of the [Move]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Move.md %}) component to set the target for a robot movement instruction. This will also add a target declaration to the RAPID Program module.
