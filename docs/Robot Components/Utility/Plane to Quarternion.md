---
layout: default
title: Plane to Quaternion
nav_order: 2
parent: Utility Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Robot Components/Utility/index.md %})**:** 
Converts a plane to quaternion values.

## **Input Parameters**

Plane (P): Defines the plane to be converted.

Reference Plane (RP): Defines the reference plane for the conversion.

## **Output Parameters**

**Coord X (X):** Contains the x-coordinate of the plane origin as number.

**Coord Y (Y):** Contains the y-coordinate of the plane origin as number.

**Coord Z (Z):** Contains the z-coordinate of the plane origin as number.

**Quaternion A (A):** Contains the real part of the quaternion as number.

**Quaternion B (B):** Contains the first imaginary coefficient of the quaternion as number.

**Quaternion C (C):** Contains the second imaginary coefficient of the quaternion as number.

**Quaternion D (D):** Contains the third imaginary coefficient of the quaternion as number.

**String (STR):** Contains the quaternion in string format to be used in RAPID Code.
