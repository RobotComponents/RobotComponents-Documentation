---
layout: default
title: External Linear Axis
nav_order: 4
parent: Definition Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Definition Parameter**]({{ site.baseurl }}{% link docs/Parameters/Definitions/index.md %})**:** 
Contains the data of an **External Linear Axis**.

## **Constructors**

[**External Rotational Axis**]({{ site.baseurl }}{% link docs/Definitions/External Linear Axis.md %})

## **Deconstructors**

[**Deconstruct External Rotational Axis**]({{ site.baseurl }}{% link docs/Deconstruct/Definitions/Deconstruct External Linear Axis.md %})

## **Casting methods**

**Cast <u>from</u>** a **Mechanical Unit parameter:** Constructs an {{page.title}} parameter from a Mechanical Unit parameter. This is only possible if the {{page.title}} parameter was constructed from a External Linear Axis parameter.

**Cast <u>from</u>** an **External Axis parameter:** Constructs an {{page.title}} parameter from a generic External Axis parameter. This is only possible if the {{page.title}} parameter was constructed from an {{page.title}} parameter.

**Cast <u>to</u>** a **Mechanical Unit parameter:** Cast to the Mechanical Unit parameter.

**Cast <u>to</u>** a **Curve parameter:** Cast to the Curve parameter. This curves defines the movement direction of the External Linear Axis. The curve goes through the origin of the attachment plane and has a domain that is equal to the axis limit. The length of the domain is equal to the length of the curve. 

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. Defines the position and orientation of the attachment plane of the {{page.title}}. The plane is given in for an external joint position of 0.

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. Defines the position of the attachment plane of the {{page.title}}. The position is given in for an external joint position value of 0.

**Cast <u>to</u>** a **Vector parameter:** Cast to the Vector parameter. Defines the rotation axis of the {{page.title}}.

**Cast <u>to</u>** a **Domain parameter:** Cast to the Domain parameter. Defines the axis limit of the {{page.title}}.

**Cast <u>to</u>** a **Boolean parameter:** Cast to the Boolean parameter. Defines if the {{page.title}} moves a robot. 

**Cast <u>to</u>** a **Number parameter:** Cast to the Number parameter. Defines if the logic number of the {{page.title}}.

## **Transformation methods**

Transformation methods are implemented for this parameter. It will transform all geometric properties of the {{page.title}}.

## **Morphing methods**

This parameter does not support morphing methods.

