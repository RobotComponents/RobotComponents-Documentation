---
layout: default
title: Get Digital Input
nav_order: 3
parent: Controller Utility
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/index.md %})**:** This component gets the signal of a defined digital input from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/Get Controller.md %}) component.

**DI Name (N):** Defines the name of the digital input based on a string value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital input.

## **Output Parameters**

**Signal (S):** Contains the signal of the defined digital input. The signal value can be casted to a boolean and integer parameter. 

## **Menu Items**

Through the right-click menu of the component the following options are availbale:

**Documentation:** Opens the documentation page of the component in your browser.
