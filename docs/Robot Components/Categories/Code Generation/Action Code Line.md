---
layout: default
title: Action Code Line
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** This component defines manually an instruction for RAPID code generation.

## **Input Parameters**

**Code (C):** Defines the content of the code line based on a string value. An introduction to RAPID Programming can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.

## **Output Parameters**

**Code Line (CL):** Contains the defined RAPID code robot instructions as an Action for code generation.

## **Menu Items**

Through the right-click menu of the component additional options are availbale:

**Documentation:** Opens the documentation page of this component.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Code Line Output of this component into the Action Input of the [RAPID generator component]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/RAPID Generator.md %}) to generate a single code line in the RAPID main code. The RAPID code contains the robot instructions such as target definitions, movement behavior etc. More on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.