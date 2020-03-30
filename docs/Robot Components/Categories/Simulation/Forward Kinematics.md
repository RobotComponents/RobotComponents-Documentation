---
layout: default
title: Forward Kinematics
nav_order: 1
parent: Simulation
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

Work in progress....

Simulation: This component computes the position of the end-effector of a defined ABB robot based on a set of given axis values. It can be also used for visualizing the robot mesh inside of Rhino.

## **Input Parameters**

Robot Info: Defines the robot based on a Robot Info component.

Internal Axis Values: Defines the current robot internal axis values based on a list of doubles.

External Axis Values: Defines the current robot external axis values based on a list of doubles.

## **Output Parameters**

Robot Mesh: Contains the robot mesh information which is displayed inside of Rhino. Note: Display errors can be fixed by creating a rectangle around and above the robot inside of Rhino like shown here.

End Plane: Contains the plane information about the robot’s end-effector.

## **Usage**

Simulation: Visualize a defined robot based on a given list of internal and external axis values. The robot mesh will be colored red if any axis values are invalid. Note: Display errors can be fixed by creating a rectangle that contains the robot and is placed above it inside of Rhino like shown here.

Code Generation: Plug the End Plane output of this component into the Plane input of the Action: Target component to define a robot target.
