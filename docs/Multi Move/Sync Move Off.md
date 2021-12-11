---
layout: default
title: Sync Move Off
nav_order: 7
parent: Multi Move Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**


[**Multi Move Action**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** 
Defines an instruction that ends a sequence of synchronized movements.

## **Input Parameters**

**Sync ID (ID):** Defines the variable name of the synchronization point (syncident) based on a text value. Each name needs to be unique. The first letter should not be a number. Do not use special characters.

## **Output Parameters**

[**Sync Move Off**]({{ site.baseurl }}{% link docs/Parameters/Actions/Sync Move Off.md %}) **(SMOFF):** Contains the data of a Sync Move Off instruction.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Sync Move Off]({{ site.baseurl }}{% link docs/Parameters/Actions/Sync Move Off.md %}) output of this component into the Actions input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to define a Sync Move Off instruction in the RAPID program module.

