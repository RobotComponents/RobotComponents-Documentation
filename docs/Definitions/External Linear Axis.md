---
layout: default
title: External Linear Axis
nav_order: 6
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** 
Defines a custom external linear axis.

## **Input Parameters**

**Name (N):** Defines the name of the external linear axis as a text value.

**Attachment Plane (AP):** Defines the attachment plane for the robot. This overrides the robot position plane.

**Axis (A):** Defines the axis movement direction as a vector.

**Axis Limits (AL):** Defines the Axis Limits as a domain.

**Base Mesh (BM):** Defines the Mesh for the External Linear Axis Base.

**Link Mesh (LM):** Defines the Mesh for the External Linear Axis Link.

## **Output Parameters**

[**External Linear Axis**]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Linear Axis.md %}) **(ELA):** Contains the External Linear Axis information.

## **Usage**

**Note:** You can use the Quarternion to Plane component to define the attachement plane from the Base Frame data that is defined in controller configuration. The position and orientation of the attachment plane has to match with the Base Frame that is defined in the configuration file of the virtual or physical controller. 

[**Definitions**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** Plug the External Linear Axis output parameter of this component into the External Linear Axis input parameter of a [Robot]({{ site.baseurl }}{% link docs/Definitions/Robot.md %}) component. The robot will be attached to the External Linear Axis.
