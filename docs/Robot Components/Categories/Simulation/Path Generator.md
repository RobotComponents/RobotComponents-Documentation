---
layout: default
title: Path Generator
nav_order: 3
parent: Simulation
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

Work in progress....

EXPERIMENTAL: This component does an estimation of the path and robot movements!

Simulation: This component generates and displays the movement path for a defined robot based on a list of Actions. It can be also used for visually simulating the robot movement inside of Rhino.

## **Input Parameters**

**Robot Info (RI):** Defines the robot based on a Robot Info component.

**Actions (A):** Defines the movement path based on a list of ordered movement instructions. A movement instruction can be defined by using the Action: Movement component. Note: All Actions can be plugged into this input but will be ignored except for movement instructions.

**Interpolations (I):** Defines the resolution per movement based on an integer value. This means that for every two movement targets additional targets are generated in between them based on the interpolations count. Increase this value to get a smoother animation. Note: This can dramatically decrease performance. For performance improvement use a button for the Update Input of this component and only recalculate the movement path when necessary.

**Animation Slider (AS):** Defines the current robot target which the Axis Values output is generated from based on a double input with range from 0 to 1. You can imagine this as sliding through the timeline of the animation.

**Display Path (DP):** Displays and generates the robot movement path in Rhino if set to true.

**Update (U):** Only if set to true, the robot movement path will be calculated. To increase improvement, only update the path when changes were made.

## **Output Parameters**

**Plane (P):** Contains the current robot end plane. 

**Internal Axis Values (IAV):** Contains the current robot internal axis values as a list of numbers.

**External Axis Values (EAV):** Contains the current robot external axis values as a list of numbers.

**Movement Paths (P):** Contains the robot movement path as a list with curves.

## **Menu Items**

TODO

## **Usage**

Simulation: Plug the Axis Values output of this component into the Axis Values input of the Forward Kinematics component. Visualize the robot movement as animation in Rhino by using a slider with range 0.0 to 1.0 for the Animation Slider input of this component.

General: Visualize the robot movement path inside of Rhino by setting the Update input of this component to true.
