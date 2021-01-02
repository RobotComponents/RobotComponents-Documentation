---
layout: default
title: Path Generator
nav_order: 3
parent: Simulation Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Simulation**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** 
Generates and displays the movement path for a defined robot based on a list of [Actions]({{ site.baseurl }}{% link docs/Code Generation/index.md %}). It can be also used for visually simulating the robot movement inside of Rhino.

**Note:** Every [Action]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) except Move Actions will be ignored. The [Inverse Kinematics]({{ site.baseurl }}{% link docs/Simulation/Inverse Kinematics.md %}) component can be used to calculate the axis values for a specific [Joint Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %}). 

**EXPERIMENTAL:** This component does an estimation of the path and robot movements! The following limitations are known:
- It ignores speed data values.
- It ignores zone data (movement precision) values. 

## **Input Parameters**

[**Robot**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot.md %}) **(R):** Defines the robot.

[**Actions**]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) **(A):** Defines the movement path based on a list of ordered move instructions. A move instruction can be defined by using the [Move]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Move.md %}) component. **Note:** All Actions can be plugged into this input but will be ignored except for move instructions.

**Interpolations (I):** Defines the resolution per movement based on an integer value. This means that for every two movement targets additional targets are generated in between them based on the interpolations count. Increase this value to get a smoother animation. **Note:** This can dramatically decrease performance. For performance improvement use a button for the Update Input of this component and only recalculate the movement path when necessary.

**Animation Slider (AS):** Defines the current robot target which the Axis Values output is generated from based on a double input with range from 0 to 1. You can imagine this as sliding through the timeline of the animation.

**Display Path (DP):** Displays and generates the robot movement path in Rhino if set to true.

**Update (U):** Only if set to true, the robot movement path will be calculated. To increase improvement, only update the path when changes were made.

## **Output Parameters**

**Path (P):** Contains the robot movement path as a list with curves.

## **Variable Output Parameters**

Through the right-click menu of the component the following variable output parameters can be added:

**Robot End Plane (EP):** Contains the current robot end plane (TCP). 

**Robot End Planes (EPs):** Contains the robot end planes (TCPs) of the whole path as a list with planes. 

**[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJ):** Contains the current [Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}). 

**[Robot Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJs):** Contains the [Robot Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) of the whole path as a list with [Robot Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}).

**External Axis Planes (EAP):** Contains a list with the current posed external axis planes.

**[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Contains the current [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}).

**[External Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Contains the [External Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) of the whole path as a listh with [External Joint Positions]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %})

**Error Messages (E):** Contains all the error and warning messages that were collected during the path generation. 

## **Usage**

[**Simulation**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** Visualize the robot movement as animation in Rhino by using a slider with range 0.0 to 1.0 for the Animation Slider input parameter of this component.

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** 
Visualize the robot movement path inside of Rhino by setting the update input parameter of this component to true.


