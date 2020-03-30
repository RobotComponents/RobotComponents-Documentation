---
layout: default
title: Action Comment
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **Comment**

## Description

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): Defines a single comment line in the RAPID program.

## **Input Parameters**

**Text (T):** Defines the content of the comment based on a string value.

## **Output Parameters**

**Comment (C):** Contains the defined comment text based on the Text input of this component as an Action for code generation.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): Plug the Comment output of this component into the actions input of the [RAPID generator component]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/RAPID Generator.md %}) to generate a single comment line in the RAPID code. The RAPID code contains the robot instructions such as target definitions, movement behavior etc. More on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.