---
layout: default
title: Work Object
nav_order: 7
parent: Definition Parameters
grand_parent: Parameter Components
---


# **{{page.title}}**

## **Description**

[**Definition Parameter**]({{ site.baseurl }}{% link docs/Parameters/Definitions/index.md %})**:** 
Contains the data of a **Work Object**.

## **Constructors**

[**Work Object**]({{ site.baseurl }}{% link docs/Definitions/Work Object.md %})

## **Deconstructors**

[**Deconstruct Work Object**]({{ site.baseurl }}{% link docs/Deconstruct/Definitions/Deconstruct Work Object.md %})

## **Casting methods**

**Cast <u>to</u>** a **External Axis parameter:** Cast to an External Axis parameter. Defines the External Axes that is attached to the work object. This parameter is empty when no External Axis is attached to the work object. 

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. Defines the plane of the work object in the world coordinate system. In case an External Axis is attached to the work object, the position and orientation are defined for external axis values set to zero. 

**Cast <u>to</u>** a **Point parameter:** Cast to the Point Parameter. Defines the point of the work object in the world coordinate system In case an External Axis is attached to the work object, the position and orientation is defined for external axis values set to zero. 

## **Transformation methods**

This parameter does not support transformation methods.

## **Morphing methods**

This parameter does not support morphing methods.
