---
layout: default
title: Action Comment
nav_order: 10
parent: Code Generation
grand_parent: RC Categories
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): Defines a single comment line in RAPID Main Code.

## Input Parameter

**Text**: Defines the content of the comment based on a string value.

## Output Parameter

**Comment**: Contains the defined comment text based on the Text input of this component as an Action for code generation.

## Usage

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): Plug the Comment output of this component into the Actions input of the RAPID Generator component to generate a single comment line in the RAPID main code. The RAPID main code contains the robot instructions such as target definitions, movement behavior etc. More on that topic can be found here: Introduction to RAPID or in the Technial Reference Manual of ABB Robotics.