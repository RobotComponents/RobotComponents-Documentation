---
layout: default
title: External Linear Axis
nav_order: 6
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** 
Defines a custom external linear axis.

## **Input Parameters**

**Name (N):** Defines the name of the external linear axis as string.

**Attachment Plane (AP):** Defines the attachment plane for the robot. Overrides the robot position plane.

**Axis (A):** Defines the Axis as vector.

**Axis Limits (AL):** Defines the Axis Limits as list of domains.

**Base Mesh (BM):** Defines the Mesh for the External Linear Axis Base.

**Link Mesh (LM):** Defines the Mesh for the External Linear Axis Link.

## **Output Parameters**

**External Linear Axis (ELA):** Contains the External Linear Axis information.

## **Usage**

[**Definitions**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** Plug the External Linear Axis output of this component into the External Linear Axis input of a [Robot]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot.md %}) component. The robot will be attached to the External Linear Axis.
