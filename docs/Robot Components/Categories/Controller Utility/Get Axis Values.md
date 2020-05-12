---
layout: default
title: Get Axis Values
nav_order: 2
parent: Controller Utility
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/index.md %})**:** This component gets the current robot axis values from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/Get Controller.md %}) component.

## **Output Parameters**

**Internal Axis Values (IAV):** Contains a list of doubles with the current robot internal axis values.

**External Axis Values (EAV):** Contains a list of doubles with the current robot external axis values.


## **Menu Items**

Through the right-click menu of the component additional options are availbale:

**Documentation:** Opens the documentation page of this component.


## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Simulation/index.md %})**:** The Axis Values output of this component can be plugged into the Axis Values input of a Forward Kinematics component to visualize the robot geometry inside of Rhino.

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** The Internal and External Axis Values outputs of this component can be plugged into the Axis Values input of a Forward Kinematics component to calculate the robots end plane. That end plane could then be used to define a Action: Target for RAPID main code generation.

