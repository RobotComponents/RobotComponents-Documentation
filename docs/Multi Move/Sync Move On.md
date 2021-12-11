---
layout: default
title: Sync Move On
nav_order: 3
parent: Multi Move Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Multi Move Action**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** 
Defines an instruction that starts a sequence of synchronized movements.

## **Input Parameters**

**Sync ID (ID):** Defines the variable name of the synchronization point (syncident) based on a text value. Each name needs to be unique. The first letter should not be a number. Do not use special characters.

[**Task List**]({{ site.baseurl }}{% link docs/Parameters/Actions/Task List.md %}) **(TL):** Defines the program tasks that should meet in the synchronization point.

## **Output Parameters**

[**Sync Move On**]({{ site.baseurl }}{% link docs/Parameters/Actions/Sync Move On.md %}) **(SMON):** Contains the data of a Sync Move On instruction.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Sync Move On]({{ site.baseurl }}{% link docs/Parameters/Actions/Sync Move On.md %}) output of this component into the Actions input of the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component to define a Sync Move On instruction in the RAPID program module. 
