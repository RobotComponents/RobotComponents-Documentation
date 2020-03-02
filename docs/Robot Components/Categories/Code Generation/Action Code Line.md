---
layout: default
title: Action Code Line
nav_order: 9
parent: Code Generation
grand_parent: RC Categories
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): This component defines manually an instruction for RAPID main code generation.

## Input Parameter

**Code**: Defines the content of the code line based on a string value. An introduction to RAPID Programming can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.

## Output Parameter

**Code Line**: Contains the defined RAPID code robot instructions as an Action for code generation.

## Usage

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): Plug the Code Line Output of this component into the Action Input of the RAPID Generator component to generate a single code line in the RAPID main code. The RAPID main code contains the robot instructions such as target definitions, movement behavior etc. More on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.