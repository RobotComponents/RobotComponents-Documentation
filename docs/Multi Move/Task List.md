---
layout: default
title: Task List
nav_order: 1
parent: Multi Move Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Multi Move Action**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** 
Defines a collection that specifies several RAPID program tasks.

## **Input Parameters**

**Name (N):** Defines the variable name of the collection with tasks based on a text value. Each name needs to be unique. The first letter should not be a number. Do not use special characters.

[**Task List**]({{ site.baseurl }}{% link docs/Parameters/Actions/Task List.md %}) **(TL):** 

## **Output Parameters**

[**Task List**]({{ site.baseurl }}{% link docs/Parameters/Actions/Task List.md %}) **(TL):** Contains the data of a Task List declaration. 

## **Usage**

[**Multi Move**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** Plug the [Task List]({{ site.baseurl }}{% link docs/Parameters/Actions/Task List.md %}) output parameter of this component into the Task List input parameter of the [Wait Sync Task]({{ site.baseurl }}{% link docs/Multi Move/Wait Sync Task.md %}) and/or [Sync Move On]({{ site.baseurl }}{% link docs/Multi Move/Sync Move On.md %}) component to set the RAPID program tasks for these Multi Move synchronization points. This will also add the Task List declaration to the RAPID Program module.

