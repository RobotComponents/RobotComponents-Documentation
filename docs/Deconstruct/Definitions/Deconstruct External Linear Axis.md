---
layout: default
title: Deconstruct External Linear Axis
nav_order: 1
parent: Definition Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruct**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** 
Deconstructs a [External Linear Axis]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Linear Axis.md %}) parameter into its parameters.

## **Input Parameters**

[**External Linear Axis**]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Linear Axis.md %}) **(ELA):**  Defines the [External Linear Axis]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Linear Axis.md %}) to be deconstructed.

## **Output Parameters**

**Name (N):** Contains the name of the external linear axis as string.

**Attachment Plane (AP):** Contains the attachment plane for the robot. 

**Axis (A):** Contains the Axis as vector.

**Axis Limits (AL):** Contains the Axis Limits as domain.

**Base Mesh (BM):** Contains the Mesh for the External Linear Axis Base.

**Link Mesh (LM):** Contains the Mesh for the External Linear Axis Link.

**Axis Logic Number (AL):** Contains the axis logic number. 

**Moves Robot (MR):** Specifies whether or not the External Linear Axis moves the Robot. 

