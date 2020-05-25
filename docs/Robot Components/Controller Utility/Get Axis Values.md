---
layout: default
title: Get Axis Values
nav_order: 2
parent: Controller Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/index.md %})**:** This component gets the current robot axis values from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/Get Controller.md %}) component.

## **Output Parameters**

**Internal Axis Values (IAV):** Contains a datatree of doubles with the current robot internal axis values. In case if multiple robots are connected to one controller a separate branch is made for each robot.

**External Axis Values (EAV):** Contains a datatree of doubles with the current robot external axis values. For every mechanical unit the axis values are placed in a separate datatree branch. Since it is not possible to acces the axis logic number of the mechanical units in the controller, the axis values may not be placed in the correct order to work with the [Forward Kinematics]({{ site.baseurl }}{% link docs/Robot Components/Simulation/Forward Kinematics.md %}) component. In that case the user has to re-order the axis values and / or flatten it to a list. 


## **Menu Items**

Through the right-click menu of the component additional options are available:

**Documentation:** Opens the documentation page of this component.


## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Robot Components/Simulation/index.md %})**:** The Axis Values output of this component can be plugged into the Axis Values input of a Forward Kinematics component to visualize the robot geometry inside of Rhino.

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** The Internal and External Axis Values outputs of this component can be plugged into the Axis Values input of a Forward Kinematics component to calculate the robots end plane. That end plane could then be used to define a Action: Target for RAPID main code generation.

