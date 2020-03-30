---
layout: default
title: Set Digital Output
nav_order: 3
parent: Controller Utility
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[Controller Utility]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/index.md %})**:** This component gets the signal of a defined digital output from an ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller:** Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the Get Controller component.

**DO Name:** Defines the name of the digital output based on a string value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital output.

## **Output Parameters**

**Signal:** Contains information on the signal of the defined digital output.

**State:** Contains the state of the digital output as boolean value.