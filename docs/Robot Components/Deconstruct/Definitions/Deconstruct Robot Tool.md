---
layout: default
title: Deconstruct Robot Tool
nav_order: 2
parent: Definition Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Utility**]({{ site.baseurl }}{% link docs/Robot Components/Utility/index.md %})**:**
Deconstructs a [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) into its parameters.

## **Input Parameters**

**Robot Tool (RT):** Defines the [Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) to deconstruct.

## **Output Parameters**

**Name (N):** Contains the robot tool name as a string value.

**Mesh (M):** Contains the robot tool mesh as a mesh.

**Attachment Plane (AP):** Contains the attachment plane of the robot tool as a plane.

**Tool Plane (TP):** Contains the effector plane of the robot tool as a plane.
