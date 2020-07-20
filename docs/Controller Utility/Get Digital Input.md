---
layout: default
title: Get Digital Input
nav_order: 3
parent: Controller Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** 
Gets the signal of a defined digital input from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Controller Utility/Get Controller.md %}) component.

**DI Name (N):** Defines the name of the digital input based on a text value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital input.

## **Output Parameters**

**Signal (S):** Contains the signal of the defined digital input. The signal value can be casted to a boolean and integer parameter. 