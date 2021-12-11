---
layout: default
title: Wait Sync Task
nav_order: 7
parent: Multi Move Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Multi Move Action**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** 
Defines an instruction to synchronize several program tasks at a special point in each program.

## **Input Parameters**

**Sync ID (ID):** Defines the variable name of the synchronization point (syncident) based on a text value. Each name needs to be unique. The first letter should not be a number. Do not use special characters.

[**Task List**]({{ site.baseurl }}{% link docs/Parameters/Actions/Task List.md %}) **(TL):** Defines the program tasks that should meet in the synchronization point.

**In Position (IP):** Defines whether or not the robot and external axes must have come to a standstill in its synchronization point.


## **Output Parameters**

[**Wait Sync Task**]({{ site.baseurl }}{% link docs/Parameters/Actions/Wait Sync Task.md %}) **(WST):** Contains the data of a Wait Sync Task instruction.

## **Usage**

Work in progress..

