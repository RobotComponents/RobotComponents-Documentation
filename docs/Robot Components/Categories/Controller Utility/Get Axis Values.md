---
layout: default
title: Get Axis Values
nav_order: 3
parent: Controller Utility
grand_parent: Robot Components Categories
---

## Description

[Controller Utility]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/Controller Utility.md %}): This component gets the current robot axis values from an ABB IRC5 robot controller.

## Input Parameter

**Robot Controller**: Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/Get Controller.md %}) component.

## Output Parameter

**Internal Axis Values**: Contains a list of doubles with the current robot internal axis values.

**External Axis Values**: Contains a list of doubles with the current robot external axis values.

## Usage

Simulation: The Axis Values output of this component can be plugged into the Axis Values input of a Forward Kinematics component to visualize the robot geometry inside of Rhino.

Code Generation: The Internal and External Axis Values outputs of this component can be plugged into the Axis Values input of a Forward Kinematics component to calculate the robots end plane. That end plane could then be used to define a Action: Target for RAPID main code generation.

