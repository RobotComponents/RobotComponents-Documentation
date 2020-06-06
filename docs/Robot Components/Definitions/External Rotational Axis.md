---
layout: default
title: External Rotational Axis
nav_order: 7
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** 
Defines a custom external rotational axis.

## **Input Parameters**

**Name (N):** Defines the name of the external rotational axis as string.

**Axis Plane (AP):** Defines the axis plane as plane.

**Axis Limits (AL):** Defines the axis limits as list of domains.

**Base Mesh (BM):** Defines the mesh of the external rotational axis base.

**Link Mesh (LM):** Defines the mesh of the external rotational axis link.

## **Output Parameters**

**External Rotational Axis (ERA):** Contains the External Rotational Axis information.

## **Usage**

[**Definitions**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** Plug the External Rotational Axis output of this component into the External Rotational Axis input of a [Robot]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot.md %}) component. The robot will be attached to the External Linear Axis.
