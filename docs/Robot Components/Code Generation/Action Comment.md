---
layout: default
title: Action Comment
nav_order: 1
parent: Code Generation Components
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Defines a single comment line in the RAPID program.

## **Input Parameters**

**Text (T):** Defines the content of the comment based on a string value.

## **Output Parameters**

**Comment (C):** Contains the defined comment text based on the Text input of this component as an Action for code generation.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Comment output of this component into the actions input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component to generate a single comment line in the RAPID code. The RAPID code contains the robot instructions such as target definitions, movement behavior etc. More on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.