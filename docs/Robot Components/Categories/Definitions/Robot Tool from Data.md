---
layout: default
title: Robot Tool from Data
nav_order: 2
parent: Definitions
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

Work in progress....

Definitions: This component defines a robot tool based on translation and rotation values. It will be automatically registered in the RAPID base code of any RAPID Generator component.

## **Input Parameters**

**Name (N):** Defines the robot tool name base on a Panel or any other string value. This name must be unique and shouldn’t start with a number or use special characters.

**Mesh (M):** Defines the robot tool mesh based on a mesh.

**Translation X (TX):** Defines the X Translation of the robot tool effector based on a double value.

**Translation Y (TY):** Defines the Y Translation of the robot tool effector based on a double value.

**Translation Z (TZ):** Defines the Z Translation of the robot tool effector based on a double value.

**Rotation X (RX):** Defines the X Rotation of the robot tool effector based on a double value.

**Rotation Y (RY):** Defines the Y Rotation of the robot tool effector based on a double value.

**Rotation Z (RZ):** Defines the Z Rotation of the robot tool effector based on a double value.

## **Output Parameters**

**Robot Tool (RT):** Contains the robot tool information.

**Robot Tool Code (RTC):** Contains the robot tool information as a string for the RAPID base code. More information on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.

## **Usage**

Definitions: Plug the Robot Tool output of this component into the Robot Tool input of a ABB_IRB-1200-7-0.7 or any other Robot Info component. The robot tool will be mounted to the mounting frame of the robot.

Code Generation: Plug the Robot Tool output of this component into the Robot Tool input of a Action: Set Robot Tool component to define an instruction for RAPID base code generation that defines the currently used robot tool.
