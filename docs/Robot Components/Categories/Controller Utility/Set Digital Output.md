---
layout: default
title: Set Digital Output
nav_order: 3
parent: Controller Utility
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/index.md %})**:** This component changes the state of a defined digital output from an ABB IRC5 robot controller in Realtime.

Note: The Access Levels of the defined digital input needs to be set to “all” in the robot controller for this component to work.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the Get Controller component.

**DI Name (N):** Defines the name of the digital output based on a string value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital output.

**State (S):** Defines the state that sould be set for the digital input based on a boolean value.

**Update (U):** If set to true, the state of the digital output will be changed in the robot controller.

## **Output Parameters**

**Signal (S):** Outputs the signal of the defined digital output. The signal value can be casted to a boolean and integer parameter. 

## **Menu Items**

TODO...

## **Usage**

**General:** Change the state of a defined digital output of an ABB IRC5 robot controller by using this component.