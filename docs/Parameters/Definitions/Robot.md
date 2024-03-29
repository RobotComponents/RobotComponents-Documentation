---
layout: default
title: Robot
nav_order: 2
parent: Definition Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Definition Parameter**]({{ site.baseurl }}{% link docs/Parameters/Definitions/index.md %})**:** 
Contains the data of a **Robot**.

## **Constructors**

[**Robot**]({{ site.baseurl }}{% link docs/Definitions/Robot.md %})

## **Deconstructors**

[**Deconstruct Robot**]({{ site.baseurl }}{% link docs/Deconstruct/Definitions/Deconstruct Robot.md %})

## **Casting methods**

**Cast <u>from</u>** a **Mechanical Unit parameter:** Constructs an {{page.title}} parameter from a Mechanical Unit parameter. This is only possible if the {{page.title}} parameter was constructed from a Robot parameter.

**Cast <u>to</u>** a **Mechanical Unit parameter:** Cast to the Mechanical Unit parameter.

**Cast <u>to</u>** a **Robot Tool parameter:** Cast to the Robot Tool parameter. Defines the Robot Tool that is attached to the robot. 

## **Transformation methods**

Transformation methods are implemented for this parameter. It will transform all geometric properties of the {{page.title}} inlcuding the attached External Axes that move the {{page.title}}. External Axes that do not move the {{page.title}} will not be transformed. 

## **Morphing methods**

This parameter does not support morphing methods.