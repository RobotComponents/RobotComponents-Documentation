---
layout: default
title: Get Axis Values
nav_order: 2
parent: Controller Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** 
Gets the current robot axis values from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Controller Utility/Get Controller.md %}) component.

## **Output Parameters**

**[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJ):** Contains the current Robot Joint Position of the robot. In case multiple robots are connected to one controller (e.g. Multi Move) this parameter outputs a list with multiple Robot Joint Positions with a Robot Joint Position for each robot. 

**External Axis Values (EAV):** Contains a datatree of numbers with the current robot external axis values. For each mechanical unit the axis values are placed in a separate datatree branch. Since it is not possible to acces the axis logic number of the mechanical units in the controller, the axis values may not be placed in the correct order to work with the [Forward Kinematics]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %}) component. The user has to order the axis values to create an [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) for the [Forward Kinematics]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %}) component.

## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** The Axis Values output of this component can be plugged into the Axis Values input parameters of a [Forward Kinematics]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %}) component to visualize the robot geometry inside of Rhino.

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** The Internal and External Axis Values outputs of this component can be plugged into the Axis Values input parameters of a [Forward Kinematics]({{ site.baseurl }}{% link docs/Simulation/Forward Kinematics.md %}) component to calculate the robots end plane. That end plane could then be used to define a [Robot Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Target.md %}) for the RAPID program module generation.

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** The Internal and External Axis Values outputs of this component can be used to define a [Robot Joint Position]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Joint Position.md %}) or [External Joint Position]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/External Joint Position.md %}).
