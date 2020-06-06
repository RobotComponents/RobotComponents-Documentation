---
layout: default
title: Get Plane
nav_order: 2
parent: Controller Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Controller Utility**]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/index.md %})**:** Gets the position of a mechanical unit from the defined ABB IRC5 robot controller.

## **Input Parameters**

**Robot Controller (RC):** Defines the ABB IRC5 robot controller. A virtual or real ABB IRC5 robot controller can be defined by using the [Get Controller]({{ site.baseurl }}{% link docs/Robot Components/Controller Utility/Get Controller.md %}) component.

**Coordinate System (CS)**: TODO

## **Output Parameters**

**Plane (P):** Contains the position of the mechanical unit as a plane.

**Name (N):** Contains the names of the mechanical units as a list of strings.
