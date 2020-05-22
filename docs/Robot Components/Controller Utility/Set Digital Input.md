---
layout: default
title: Set Digital Input
nav_order: 1
parent: Controller Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/index.md %})**:** This component changes the state of a defined digital input from an ABB IRC5 robot controller in Realtime.

Note: The Access Levels of the defined digital input needs to be set to “all” in the robot controller for this component to work.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/Get Controller.md %}) component.

**DI Name (N):** Defines the name of the digital input based on a string value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital output.

**State (S):** Defines the state that sould be set for the digital input based on a boolean value.

**Update (U):** If set to true, the state of the digital input will be changed in the robot controller. It is recommended to use of button for this input parameter. 

## **Output Parameters**

**Signal (S):** Outputs the signal of the defined digital input. The signal value can be casted to a boolean and integer parameter. 

## **Menu Items**

Through the right-click menu of the component the following options are availbale:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/index.md %})**:** Change the state of a defined digital input of an ABB IRC5 robot controller by using this component.