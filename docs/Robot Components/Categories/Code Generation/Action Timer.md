---
layout: default
title: Action Timer
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** This component defines an instruction to wait a given amount of time between two other robot instructions.

## **Input Parameters**

**Duration (D):** Defines the duration in seconds based on a number value.

## **Output Parameters**

**Timer (T):** Contains the wait instruction as an action for RAPID code generation.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** The Timer output of this component can be plugged into the actions input of the RAPID Generator component to add a wait instruction in the RAPID main code that defines an amount of time until the next instruction is executed.