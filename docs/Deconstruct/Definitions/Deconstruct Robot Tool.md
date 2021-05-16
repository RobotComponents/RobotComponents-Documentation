---
layout: default
title: Deconstruct Robot Tool
nav_order: 2
parent: Definition Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruct**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** 
Deconstructs a [Robot Tool]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) into its parameters.

## **Input Parameters**

[**Robot Tool**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) **(RT):** Defines the [Robot Tool]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) to deconstruct.

## **Output Parameters**

**Name (N):** Contains the robot tool name as a string value.

**Mesh (M):** Contains the robot tool mesh as a mesh.

**Attachment Plane (AP):** Contains the attachment plane of the robot tool as a plane.

**Tool Plane (TP):** Contains the effector plane of the robot tool as a plane.

**Mass (M):** Contains the weight of the tool load in kg as a number.

**Center of Gravity (CG):** Contains the position and orientation of the center of gravity of the tool load as a plane.

**Moment of Intertia (MI):** Contains the moment of inertia of the tool load in kgm2 as a vector.