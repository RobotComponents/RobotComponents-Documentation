---
layout: default
title: Code
nav_order: 1
parent: Dynamic Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Dynamic Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Dynamic Actions/index.md %})**:**  This component defines manually an instruction or declaration for the RAPID program module.

## **Input Parameters**

**Text (T):** Defines the content of the code based on a string value. An introduction to RAPID Programming can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.

**Type (T):** Defines the type of the code. Use 0 for adding the code as instruction in the RPAID programm module. Use 1 for adding the code as declaration in the RAPID program module.

## **Output Parameters**

**Code (C):** Contains the defined RAPID code for the RAPID program module.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Code Line Output of this component into the Action Input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component to generate a single code line in the RAPID program module. 