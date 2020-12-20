---
layout: default
title: Set Digital Output
nav_order: 6
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** 
Defines an instruction to change the state of a digital output of the robot controller.

## **Input Parameters**

**Name (N):** Defines the name of the digital output based on a text value. This name should match with the name of the digital signal as it defined in the robot controller. 

**State (S):** Defines the state of the digital output that should be set based on a boolean value.

## **Output Parameters**

[**Set Digital Output**]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Digital Output.md %}) **(SDO):** Contains the instruction to change the state of a defined digital output.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the output of this component into the actions input of a [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to add a single instruction to the RAPID program module that sets the state of a defined digital output in the robot controller.
