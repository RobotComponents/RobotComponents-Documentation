---
layout: default
title: Action Zone Data
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Defines a zone data for a [Action: Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Movement.md %}) or [Action: Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %}) instruction. Zone data is used to specify how (precise) a position is to be terminated. 

## **Input Parameters**

**Name (N):** The zone data variable name. Each zone data name needs to be unique. The first letter shouldn’t be a number. Don’t use special characters.

**Fine Point (FP):** A boolean that defines whether the movement is to terminate as a stop point (fine point) or as a fly-by point. 

**Path Zone TCP (pzTCP):** The size (the radius) of the TCP zone in mm. 

**Path Zone Orientation (pzORI):** The zone size (the radius) for the tool reorientation. The size is defined as the distance of the TCP from the programmed point in mm.

**Path Zone ExternalAxes (pzEA):** The zone size (the radius) for external axes. The size is defined as the distance of the TCP from the programmed point in mm.

**Zone Orientation (zORI):** The zone size for the tool reorientation in degrees. If the robot is holding the work object, this means an angle of rotation for the work object.

**Zone External Linear Axes (zELA):** The zone size for linear external axes in mm.

**Zone External Rotational Axes (zERA):** The zone size for rotating external axes in degrees.

## **Output Parameters**

**Zone Data (ZD):** Contains the Zone Data instructions as action for an [Action: Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Movement.md %}) or [Action: Absolute Joint Movement]({{ site.baseurl }}{link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %}) instruction.

## **Menu Items**

Through the right-click menu of the component additional options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Zone Data output of this component into the Zone Data input of the [Action: Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Movement.md %}) or [Action: Absolute Joint Movement]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Action Absolute Joint Movement.md %}) component to set the precision of the movement instruction in the RAPID Program code. This will also add a zonedata variable to the RAPID Program module.