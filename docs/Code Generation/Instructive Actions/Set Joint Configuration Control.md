---
layout: default
title: Set Joint Configuration Control
nav_order: 5
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** Defines an instruction to activate or deactivate joint configuration control for all following `MoveJ` move instructions.

## **Input Parameters**

**Is Active (A):** Defines if the joint configuration control is active based on a boolean value.

## **Output Parameters**

[**Set Joint Configuration Control**]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Auto Axis Configurator.md %}) **(SJCC):** Contains an instruction to activate or deactivate joint configuration control for all following `MoveJ` move instructions.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the output paramter of this component into the Actions input parameter of the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to add an instruction to the RAPID program module that activates or deactivates joint configuration control.
