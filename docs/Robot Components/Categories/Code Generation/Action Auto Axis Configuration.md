---
layout: default
title: Action Auto Axis Configuration
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation:**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Defines an instruction to set the axis configuration of the robot automatically in RAPID code generation.

## **Input Parameters**

**is Active (A):** Defines if the axis configuration of the robot is set automatically based on a boolean value.

## **Output Parameters**

**Auto Axis Config (AAC):** Contains an instruction to sets or unset the auto axis configuration for the robot as an action for RAPID code generation.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Auto Axis Config output of this component into the actions input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/RAPID Generator.md %}) component to define an instruction that sets or unsets the auto axis configuration for the robot in RAPID main code.