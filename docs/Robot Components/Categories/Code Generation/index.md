---
layout: default
title: Code Generation
nav_order: 1
parent: Robot Components Categories
has_children: true
has_toc: false
---

# **Code Generation**

## **Description**

Code Generation components are used to generate the RAPID program and system Code for a virtual or real ABB IRC5 robot controller.

## **Functionality**

All Action components can be plugged into the Code Generator component which generates the RAPID program and system code for the ABB IRC5 robot controller. The RAPID program and system code can be copied manually to the controller or uploaded and run by using the Remote Connection component from Category: Controller Utility.

## **Usage**

[**Action: Set Robot Tool**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Set Robot Tool.md %})**:** Defines an instruction to change the current robot tool of the ABB robot for RAPID base code generation.

[**Action: Target**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Target.md %})**:** Defines a target for an Action: Movement or Inverse Kinematics component.

[**Action: Absolute Joint Movement**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %})**:** Defines an aboslute joint movement instruction for simulation and RAPID code generation.

[**Action: Movement**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Movement.md %})**:** Defines a linear or nonlinear movement instruction for simulation and RAPID code generation.

[**Action: Speed Data**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Speed Data.md %})**:** Defines a speed data for an Action: Movement.

[**Action: Timer**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Timer.md %})**:** Defines an instruction to wait a given amount of time between two other robot instructions in RAPID code generation.

[**Action: Digital Output**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Digital Output.md %})**:** Defines an instruction to change the state of a digital output of the robot controller for RAPID code generation.

[**Action: Wait for Digital Input**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Wait for Digital Input.md %})**:** Defines an instruction to wait for the signal of a Digital Input from the robot controller in RAPID code generation.

[**Action: Auto Axis Configuration**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Auto Axis Configuration.md %})**:** Defines an instruction to set the axis configuration of the robot automatically for RAPID code generation.

[**Action: Code Line**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Code Line.md %})**:** Defines manually an instruction for RAPID code generation.

[**Action: Comment**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Comment.md %})**:** Defines a comment for RAPID code generation.

[**RAPID Generator**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/RAPID Generator.md %})**:** Generates the RAPID program and system code for the ABB IRC5 robot controller from a list of Actions.