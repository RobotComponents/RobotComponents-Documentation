---
layout: default
title: Path Generator
nav_order: 3
parent: Simulation
grand_parent: Robot Components Categories
---

## Description

Work in progess....

EXPERIMENTAL

Simulation: This component generates and displays the movement path for a defined robot based on a list of Actions. It can be also used for visually simulating the robot movement inside of Rhino.

## Input Parameter

Robot Info: Defines the robot based on a Robot Info component.

Actions: Defines the movement path based on a list of ordered movement instructions. A movement instruction can be defined by using the Action: Movement component. Note: All Actions can be plugged into this input but will be ignored except for movement instructions.

Interpolations: Defines the resolution per movement based on an integer value. This means that for every two movement targets additional targets are generated in between them based on the interpolations count. Increase this value to get a smoother animation. Note: This can dramatically decrease performance. For performance improvement use a button for the Update Input of this component and only recalculate the movement path when necessary.

Animation Slider: Defines the current robot target which the Axis Values output is generated from based on a double input with range from 0 to 1. You can imagine this as sliding through the timeline of the animation.

Display Path: Displays and generates the robot movement path in Rhino if set to true.

Display Names: Display the movement target names if set to true.

Update: Only if set to true, the robot movement path will be calculated. To increase improvement, only update the path when changes were made.

## Output Parameter

Target: Contains the current robot target.

Internal Axis Values: Contains the current robot internal axis values as a list of doubles.

External Axis Values: Contains the current robot external axis values as a list of doubles.

Movement Path: Contains the robot movement path as a curve.

## Usage

Simulation: Plug the Axis Values output of this component into the Axis Values input of the Forward Kinematics component. Visualize the robot movement as animation in Rhino by using a slider with range 0.0 to 1.0 for the Animation Slider input of this component.

General: Visualize the robot movement path inside of Rhino by setting the Update input of this component to true.
