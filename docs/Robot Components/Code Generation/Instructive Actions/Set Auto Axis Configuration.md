---
layout: default
title: Set Auto Axis Configuration
nav_order: 5
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/index.md %})**:** Defines an instruction to activate or deactivate auto axis configuration for all following instructions.

## **Input Parameters**

**Is Active (A):** Defines if the axis configuration of the robot is set automatically based on a boolean value.

## **Output Parameters**

[**Set Auto Axis Configuration**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Set Auto Axis Configurator.md %}) **(SAAC):** Contains an instruction to activate or deactivate auto axis configuration for all following instructions.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the output paramter of this component into the Actions input parameter of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component to add an instruction to the RAPID program module that activates or deactivates auto axis configuration.