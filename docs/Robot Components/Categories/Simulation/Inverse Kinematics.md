---
layout: default
title: Inverse Kinematics
nav_order: 2
parent: Simulation
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

Work in progress....

Simulation: This component computes the axis values for a defined ABB robot based on an Action: Target.

## **Input Parameters**

Target: Defines the robot target. A target can be generated by using an Action: Target component.

Robot Info: Defines the robot based on a Robot Info component.

## **Output Parameters**

Internal Axis Values: Contains the robot internal axis values as a list of doubles.

External Axis Values: Contains the robot external axis values as a list of doubles.

## **Usage**

Simulation: Plug the Internal and External Axis Values outputs of this component into the Internal and External Axis Values inputs of the Forward Kinematics component to generate an end-plane for an Action: Target or to visualize the robot mesh inside of Rhino.