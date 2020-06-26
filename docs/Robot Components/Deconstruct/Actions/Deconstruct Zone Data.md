---
layout: default
title: Deconstruct Zone Data
nav_order: 3
parent: Action Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Robot Components/Utility/index.md %})**:** 
Deconstructs a [Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) into its parameters. 

## **Input Parameters**

[**Zone Data**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) **(ZD):** Defines [Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) to be deconstructed.

## **Output Parameters**

**Name (N):** Contains the zone data variable name. 

**Fine Point (FP):** Contains the boolean that defines whether the movement is to terminate as a stop point (fine point) or as a fly-by point. 

**Path Zone TCP (pzTCP):** Contains the size (the radius) of the TCP zone in mm. 

**Path Zone Orientation (pzORI):** Contains the zone size (the radius) for the tool reorientation. The size is defined as the distance of the TCP from the programmed point in mm.

**Path Zone External Axes (pzEA):** Contains the zone size (the radius) for external axes. The size is defined as the distance of the TCP from the programmed point in mm.

**Zone Orientation (zORI):** Contains the zone size for the tool reorientation in degrees. If the robot is holding the work object, this means an angle of rotation for the work object.

**Zone External Linear Axes (zELA):** Contains the zone size for linear external axes in mm.

**Zone External Rotational Axes (zERA):** Contains the zone size for rotating external axes in degrees.

