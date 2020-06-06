---
layout: default
title: Flip Plane X
nav_order: 1
parent: Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Robot Components/Utility/index.md %})**:** 
Flips a plane by setting its x-Axis negativ.

## **Input Parameters**

**Plane (P):** Defines the plane or a list of planes to flip.

## **Output Parameters**

**Plane (P):** Outputs all input planes flipped.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** 
Plug the Plane output of this component into the Plane input of the [Target]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/Target.md %}) component. 
Since be default grasshopper planes are facing the wrong direction when working with robot components, this component makes life easier.
