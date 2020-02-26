---
layout: default
title: Get Digital Input
nav_order: 4
---

## Description

[Controller Utility]({{ site.baseurl }}{% link docs/Robot Components/Categories/Controller Utility/index.md %}): This component gets the signal of a defined digital input from an ABB IRC5 robot controller.

Note: The Access Levels of the defined digital input needs to be set to “all” in the robot controller for this component to work.

## Input Parameter

**Robot Controller**: Defines the ABB IRC5 robot controller that is connected to. A virtual or real ABB IRC5 robot controller can be defined by using the Get Controller component.

**DI Name**: Defines the name of the digital input based on a string value. This needs to be the same name that is defined in the ABB IRC5 robot controller for the digital input.

## Output Parameter

**Signal Value**: Contains information on the signal of the defined digital input.

**State**: Contains the state of the digital output signal as boolean value.
