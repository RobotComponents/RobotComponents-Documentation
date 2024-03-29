---
layout: default
title: Multi Move Components
nav_order: 5
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Multi Move components are used to create RAPID declarations and instructions for a virtual or physical ABB IRC5 robot controller. These components are an extension of the [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) category and need to be combined with other [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) components to create a Multi Move program. This is done by plugging a list of Actions into the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component, which generates the RAPID program module for the ABB IRC5 robot controller. For each Multi Move task a seperate program module has to be generated by constructing for each task a list with Actions. In case synchronized movements are used the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component will automatically assign synchronization IDs to the movements that are located between the [Sync Move On]({{ site.baseurl }}{% link docs/Multi Move/Sync Move On.md %}) and [Sync Move Off]({{ site.baseurl }}{% link docs/Multi Move/Sync Move Off.md %}) instructions.

## **Components**

[**Task List**]({{ site.baseurl }}{% link docs/Multi Move/Task List.md %})**:** Defines a collection that specifies several RAPID program tasks.

[**Wait Sync Task**]({{ site.baseurl }}{% link docs/Multi Move/Wait Sync Task.md %})**:** Defines an instruction to synchronize several program tasks at a special point in each program.

[**Sync Move On**]({{ site.baseurl }}{% link docs/Multi Move/Sync Move On.md %})**:** Defines an instruction that starts a sequence of synchronized movements.

[**Sync Move Off**]({{ site.baseurl }}{% link docs/Multi Move/Sync Move Off.md %})**:** Defines an instruction that ends a sequence of synchronized movements.




