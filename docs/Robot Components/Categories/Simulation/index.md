---
layout: default
title: Simulation
nav_order: 5
parent: Robot Components Categories
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Work in progress....

Simulation components are used to visually approximate the movement behavior of the robot before running the RAPID main and base code on the robot controller.

## Functionality

To simulate the robot movement path all Actions from Category: Code Generation can be simply plugged into the Path Generator component which also generates corresponding axis values for every path position. Note that every Action except Movement Actions will be ignored. The Inverse Kinematics component can be used additionally to calculate the axis values for a specific Target. To visualize the robot geometry inside of Rhino the Forward Kinematics component can be used by feeding in any axis values.

## **Usage**

Forward Kinematics: Computes the position of the end-effector of a defined ABB robot based on a set of given axis values. It can be also used for visualizing the robot mesh inside of Rhino.

Inverse Kinematics: Computes the axis values for a defined ABB robot based on an Action: Target.

Path Generator: Generates and displays the movement path for a defined ABB robot based on a list of Actions. It can be also used for visually simulating and animating the robot movement inside of Rhino by using the Forward Kinematics component.