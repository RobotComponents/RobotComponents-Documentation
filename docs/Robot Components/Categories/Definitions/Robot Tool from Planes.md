---
layout: default
title: Robot Tool from Planes
nav_order: 2
parent: Definitions
grand_parent: Robot Components Categories
---

## Description

Work in progess....

Definitions: This component defines a robot tool based on attachment and end-effector planes. It will be automatically registered in the RAPID base code of any RAPID Generator component.

## Input Parameter

Name: Defines the robot tool name base on a Panel or any other string value. This name must be unique and shouldn’t start with a number or use special characters.

Mesh: Defines the robot tool mesh based on a mesh.

Attachment Plane: Defines the attachment plane for the robot tool based on a plane input.

Effector Plane: Defines the effector plane for the robot tool based on a plane input.

## Output Parameter

Robot Tool: Contains the robot tool information.

Robot Tool Code: Contains the robot tool information as a string for the RAPID base code. More information on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.

## Usage

Definitions: Plug the Robot Tool output of this component into the Robot Tool input of a ABB_IRB-1200-7-0.7 or any other Robot Info component. The robot tool will be mounted to the mounting frame of the robot.

Code Generation: Plug the Robot Tool output of this component into the Robot Tool input of a Action: Set Robot Tool component to define an instruction for RAPID base code generation that defines the currently used robot tool
