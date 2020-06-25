---
layout: default
title: Deconstruct Absolute Joint Movement
nav_order: 5
parent: Action Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruction**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** 
Deconstructs an [Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Absolute Joint Movement.md %}) component into its parameters.

## **Input Parameters**

**Absolute Joint Movement (AJM):** Defines the [Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Absolute Joint Movement.md %}) to be deconstructed.

## **Output Parameters**

**Name (N):** Contains the name of the joint target of the deconstructed movement as a string value. 

**Internal Axis Values (IAV):** Contains the internal axis values of the deconstructed movement as a list of numbers in degrees.

**External Axis Values (EAV):** Contains the external axis values of the deconstructed movement as a list of numbers in degrees.

**Speed Data (SD):** Contains the [Speed Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Speed Data.md %}) of the deconstructed movement. 

**Movement Type (MT:** Contains information on the movement type of the deconstructed movement.

**Zone Data (Z):** Contains the [Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) of the deconstructed movement.

**Robot Tool (RT):** Contains the [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) of the deconstructed movement.

## **Usage**


