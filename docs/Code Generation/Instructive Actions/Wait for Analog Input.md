---
layout: default
title: Wait for Analog Input
nav_order: 4
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** 
Defines an instruction to wait for the signal of an Analog Input from the robot controller.

## **Input Parameters**

**Analog Input Name (N):** Defines the name of the analog input based on a text value.

**Value (V):** Defines the value of the analog input that should be waited for.

**Inequality Symbol (IS):** Defines the inequality symbol to describe if the instruction waits until the value is less than or greater than the defined signal value. Use `0` for less than and `1` for greater than. In case this input is left empty and inputs are defined for the other parameters, a value list will automatically be created. You can select `LT` or `GT` from the value list to define the desired inequality symbol.

## **Output Parameters**

[**Wait for Analog Input**]({{ site.baseurl }}{% link docs/Parameters/Actions/Wait for Analog Input.md %}) **(WAI):**  Contains the instruction to wait for the signal of a defined analog input from the robot controller.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the output of this component into the Actions input of a [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to add a instruction that waits for the signal of a defined analog input from the robot controller in the RAPID program module.
