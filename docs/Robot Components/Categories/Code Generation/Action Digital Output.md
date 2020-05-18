---
layout: default
title: Action Digital Output
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** This component defines an instruction to change the state of a digital output of the robot controller in RAPID code generation.

## **Input Parameters**

**Name (N):** Defines the name of the digital output based on a string value. This name should match with the name of the digital signal as it defined in the controller. 

**State (S):** Defines the state of the digital output that should be set based on a boolean value.

## **Output Parameters**

**Digital Output (DO):** Contains the instruction to change the state of a defined digital output as an Action for RAPID code generation.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Digital Output output of this component into the actions input of a [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/RAPID Generator.md %}) component to add a single instruction that waits for the signal of a defined digital input from the robot controller in the RAPID code.