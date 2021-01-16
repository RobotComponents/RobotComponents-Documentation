---
layout: default
title: Set Linear Configuration Control
nav_order: 5
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** Defines an instruction to activate or deactivate linear configuration control for all following `MoveJ` move instructions.

## **Input Parameters**

**Is Active (A):** Defines if the linear configuration control is active based on a boolean value.

## **Output Parameters**

[**Set Linear Configuration Control**]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Auto Axis Configurator.md %}) **(SJCC):** Contains an instruction to activate or deactivate linear configuration control for all following `MoveJ` move instructions.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the output paramter of this component into the Actions input parameter of the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to add an instruction to the RAPID program module that activates or deactivates linear configuration control.
