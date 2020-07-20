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

[**Dynamic Action**]({{ site.baseurl }}{% link docs/Code Generation/Dynamic Actions/index.md %})**:**  This component defines manually an instruction or declaration for a RAPID program module.

## **Input Parameters**

**Text (T):** Defines the content of the code line based on a text value.

**Type (T):** Defines the type of the code line. Use `0` for adding a code line as instruction in the RPAID program module. Use `1` for adding a code line as declaration in the RAPID program module. In case this input is left empty and an input is defined for the Text parameter, a value list will automatically be created. You can select `Instruction` or `Declaration` from the value list to define the desired Code Line type. 

## **Output Parameters**

[**Code**]({{ site.baseurl }}{% link docs/Parameters/Actions/Code Line.md %}) **(C):** Contains the defined RAPID code for the RAPID program module.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Code Line]({{ site.baseurl }}{% link docs/Parameters/Actions/Code Line.md %}) output parameter of this component into the [Actions]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) input parameter of the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to generate a custom single code line in the RAPID program module. 
