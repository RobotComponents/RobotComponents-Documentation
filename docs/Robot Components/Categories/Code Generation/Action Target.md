---
layout: default
title: Action Target
nav_order: 2
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): This component defines an instruction to change the current robot tool of the ABB robot for RAPID base code generation.

## Input Parameter

**Name**: Defines the name of the target based on a string value. Each target name should be unique. The first letter shouldn’t be a number. Don’t use special characters.

**Plane**: Defines the target plane of the target based on one or a list of planes. Note: You can use a Flip Plane X or Flip Plane Y component to flip the plane.

**Axis Configuration**: Defines the axis configuration of the robot to reach the defined target plane based on an integer value. The range is 0 to 7. Read more on that topic here: Robot Configuration Data.

## Output Parameter

**Target**: Contains the defined target information as an Action for RAPID main code generation.

## Usage

Simulation: Plug the Target output of this component into the Target input of the Inverse Kinematics component to get the robots axis values for the defined target.

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): Plug the Target output of this component into the Target input of the Action: Movement component to define a robot movement.