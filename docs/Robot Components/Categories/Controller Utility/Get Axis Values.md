---
layout: default
title: Get Axis Values
nav_order: 2
parent: Controller Utility
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[Controller Utility]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/index.md %})**:** This component gets the current robot axis values from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller:** Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/Get Controller.md %}) component.

## **Output Parameters**

**Internal Axis Values:** Contains a list of doubles with the current robot internal axis values.

**External Axis Values:** Contains a list of doubles with the current robot external axis values.

## **Usage**

Simulation: The Axis Values output of this component can be plugged into the Axis Values input of a Forward Kinematics component to visualize the robot geometry inside of Rhino.

Code Generation: The Internal and External Axis Values outputs of this component can be plugged into the Axis Values input of a Forward Kinematics component to calculate the robots end plane. That end plane could then be used to define a Action: Target for RAPID main code generation.

