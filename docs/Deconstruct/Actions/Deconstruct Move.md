---
layout: default
title: Deconstruct Move
nav_order: 5
parent: Action Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruct**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** 
Deconstructs a [Move]({{ site.baseurl }}{% link docs/Parameters/Actions/Move.md %}) into its parameters.

## **Input Parameters**

[**Move**]({{ site.baseurl }}{% link docs/Parameters/Actions/Move.md %}) **(M):** Defines the [Move]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Move.md %}) to be deconstructed.

## **Output Parameters**

**Movement Type (MT):** Contains information on the movement type of the deconstructed move component.

[**Target**]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) **(T):** Contains the target of the deconstructed move component.

[**Speed Data**]({{ site.baseurl }}{% link docs/Parameters/Actions/Speed Data.md %}) **(SD):** Contains the [Speed Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Speed Data.md %}) of the deconstructed move component.

**Time (TI):** Contains information on the movement time of the deconstructed move component in seconds. If the value is positive, this overwrites the defined speeddata value to obtain the desired movement time.

[**Zone Data**]({{ site.baseurl }}{% link docs/Parameters/Actions/Zone Data.md %}) **(ZD):** Contains the [Zone Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Zone Data.md %}) of the deconstructed move component.

[**Robot Tool**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) **(RT):** Contains the [Robot Tool]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) of the deconstructed move component.

[**Work Object**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) **(WO):** Contains the [Work Object]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) of the deconstructed move component.
 
[**Set Digital Output**]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Digital Output.md %}) **(DO):** Contains the [Digital Output]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Digital Output.md %}) of the deconstructed move component.
