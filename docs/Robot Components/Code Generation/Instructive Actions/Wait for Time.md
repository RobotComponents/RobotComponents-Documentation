---
layout: default
title: Wait for Time
nav_order: 3
parent: Instructive Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Instructive Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/index.md %})**:** 
Defines an instruction to wait a given amount of time between two other RAPID instructions.

## **Input Parameters**

**Duration (D):** Defines the duration in seconds based on a number value.

## **Output Parameters**

**Timer (T):** Contains the wait instruction.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** The Timer output of this component can be plugged into the actions input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/RAPID Generator.md %}) component to add a wait instruction to the RAPID program module.