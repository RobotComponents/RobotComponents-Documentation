---
layout: default
title: Deconstruct Absolute Joint Movement
nav_order: 1
parent: Deconstruct
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Deconstruction**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Deconstructs an [Action: Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %}) component into its parameters.

## **Input Parameters**

**Absolute Joint Movement (AJM):** Defines the [Action: Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %}) to deconstruct.

## **Output Parameters**

**Name (N):** Contains the name of the joint target of the deconstructed movement as a string value. 

**Internal Axis Values (IAV):** Contains the internal axis values of the deconstructed movement as a list of numbers in degrees.

**External Axis Values (EAV):** Contains the external axis values of the deconstructed movement as a list of numbers in degrees.

**Speed Data (SD):** Contains the [Action: Speed Data]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Speed Data.md %}) of the deconstructed movement. 

**Movement Type (MT:** Contains information on the movement type of the deconstructed movement.

**Zone Data (Z):** Contains the [Action: Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Zone Data.md %}) of the deconstructed movement.

**Robot Tool (RT):** Contains the [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Categories/Definitions/Robot Tool from Planes.md %}) of the deconstructed movement.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**


