---
layout: default
title: Work Object
nav_order: 8
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/index.md %})**:** 
Defines a work object. 

## **Input Parameters**

**Name (N):** Defines the work object name based on a text value. This name must be unique and shouldn't start with a number or use special characters.

**Plane (WP):** Defines the work objects plane. In case you attach and external axis to the work object you have to defined the work object plane relative to the axis plane. 

**External Rotational Axis (ERA):** Defines the external rotational axis of the work object. A custom external rotational axis can be created by using the
[External Rotational Axis]({{ site.baseurl }}{% link docs/Robot Components/Definitions/External Rotational Axis.md %}) component. This input parameter is optional. By default this input parameter is empty and a fixed work object will be created. In case an external rotational axis is attacted to the work object a movable work object will be created. 

## **Output Parameters**

[**Work Object**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Work Object.md %}) **(WO):** Contains the work object information.

## **Usage**

**Note:** You can use the Quarternion to Plane component to define the work object plane from calibration data. 

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the [Work Object]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Work Object.md %}) output parameter of this component into the Work Object input parameter of the [Move]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Move.md %}) component to set a work object of a robot movement instruction. This will also add a work object data to the RAPID System module.