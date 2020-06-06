---
layout: default
title: Deconstruct Movement
nav_order: 4
parent: Action Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Robot Components/Utility/index.md %})**:** 
Deconstructs a [Movement]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Move.md %}) into its parameters.

## **Input Parameters**

**Move (M):** Defines the [Movement]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Move.md %}) to be deconstructed.

## **Output Parameters**

**Target (T):** Contains the target of the deconstructed move component.

**Speed Data (SD):** Contains the [Speed Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Speed Data.md %}) of the deconstructed move component.

**Movement Type (MT):** Contains information on the movement type of the deconstructed move component.

**Zone Data (Z):** Contains the [Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) of the deconstructed move component.

**Robot Tool (RT):** Contains the [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) of the deconstructed move component.

**Work Object (WO):** Contains the [Work Object]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Work Object.md %}) of the deconstructed move component.
 
**Digital Output (DO):** Contains the [Digital Output]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Set Digital Output.md %}) of the deconstructed move component.