---
layout: default
title: Wait for Digital Input
nav_order: 4
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** 
Defines an instruction to wait for the signal of a Digital Input from the robot controller.

## **Input Parameters**

**Digital Input Name (N):** Defines the name of the digital input based on a text value.

**State (S):** Defines the state of the digital input that should be waited for.

## **Output Parameters**

[**Wait for Digital Input**]({{ site.baseurl }}{% link docs/Parameters/Actions/Wait for Digital Input.md %}) **(WDI):**  Contains the instruction to wait for the signal of a defined digital input from the robot controller.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the output of this component into the Actions input of a [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to add a instruction that waits for the signal of a defined digital input from the robot controller in the RAPID program module.
