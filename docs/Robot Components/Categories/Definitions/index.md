---
layout: default
title: Definitions
nav_order: 4
parent: Robot Components Categories
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Work in progress....

Definition components are used to define robots and robot tools for Code Generation and Simulation.

## **Functionality**

ABB_IRB-1200-7-0.7 or any other Robot Info components are needed for different components from Code Generation and Simulation such as RAPID Generator or Inverse Kinematics and Forward Kinematics. If a specific robot tool is required it can be defined by using the Robot Tool From Data or Robot Tool From Planes component from this category. The Robot Tool output must then be plugged into the ABB_IRB-1200-7-0.7 or any other Robot Info component which is used for Code Generation and Simulation. It will be automatically registered in the RAPID base code of any RAPID Generator component

## **Usage**

Robot Info: Defines a robot which is needed for Code Generation and Simulation

ABB_IRB-1200-7-0.7: An ABB IRB 1200-7/7.0 Robot Info preset component.

Robot Tool From Data: Defines a robot tool based on translation and rotation values.

Robot Tool From Planes: Generates a robot tool based on attachment and effector planes.