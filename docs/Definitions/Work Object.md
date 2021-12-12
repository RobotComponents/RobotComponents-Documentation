---
layout: default
title: Work Object
nav_order: 8
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** 
Defines a work object. 

## **Input Parameters**

**Name (N):** Defines the work object name based on a text value. This name must be unique and shouldn't start with a number or use special characters.

**Plane (WP):** Defines the work objects plane. In case you attach and external axis to the work object you have to defined the work object plane relative to the axis plane. 

[**External Axis**]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Axis.md %}) **(EA):** Defines the external axis of the work object. A custom external axis can be created by using the [External Rotational Axis]({{ site.baseurl }}{% link docs/Definitions/External Rotational Axis.md %}) or [External Linear Axis]({{ site.baseurl }}{% link docs/Definitions/External Linear Axis.md %}) component. This input parameter is optional. By default this input parameter is empty and a fixed work object will be created. In case an external axis is attacted to the work object a movable work object will be created. An external axis that moves a Robot cannot be attached to a Work Object. 

## **Output Parameters**

[**Work Object**]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) **(WO):** Contains the work object information.

## **Usage**

**Note:** You can use the Quarternion to Plane component to define the work object plane from calibration data. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Work Object]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) output parameter of this component into the Work Object input parameter of the [Move]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Move.md %}) component to set a work object of a robot movement instruction. This will also add a work object data to the RAPID System module.
