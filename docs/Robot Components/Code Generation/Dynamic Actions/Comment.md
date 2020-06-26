---
layout: default
title: Comment
nav_order: 2
parent: Dynamic Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Dynamic Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Dynamic Actions/index.md %})**:** Defines a single comment line in the RAPID program module.

## **Input Parameters**

**Text (T):** Defines the content of the comment based on a text value.

**Type (T):** Defines the type of the comment. Use `0` for adding a comment for instructions in the RPAID programm module. Use `1` for adding a comment for declarations in the RAPID program module. In case this input is left empty and an input is defined for the Text parameter, a value list will automatically be created. You can select `Instruction` or `Declaration` from the value list to define the desired Comment type. 

## **Output Parameters**

[**Comment**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Comment.md %}) **(C):** Contains the defined comment for the RAPID program module based on the text input of this component.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the [Comment]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Speed Data.md %}) output parameter of this component into the [Actions]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) input parameter of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component to generate a single comment line in the RAPID program module.