---
layout: default
title: External Axis
nav_order: 3
parent: Definition Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Definition Parameter**]({{ site.baseurl }}{% link docs/Parameters/Definitions/index.md %})**:** 
Contains the data of an **External Axis**.

## **Constructors**

[**External Linear Axis**]({{ site.baseurl }}{% link docs/Definitions/External Linear Axis.md %})

[**External Rotational Axis**]({{ site.baseurl }}{% link docs/Definitions/External Rotational Axis.md %})

## **Deconstructors**

[**Deconstruct External Linear Axis**]({{ site.baseurl }}{% link docs/Deconstruct/Definitions/Deconstruct External Linear Axis.md %})

[**Deconstruct External Rotational Axis**]({{ site.baseurl }}{% link docs/Deconstruct/Definitions/Deconstruct External Rotational Axis.md %})

## **Casting methods**

**Cast <u>from</u>** an **External Linear Axis parameter:** Constructs an {{page.title}} parameter from an External Linear Axis parameter. 

**Cast <u>from</u>** an **External Rotational Axis parameter:** Constructs an {{page.title}} parameter from an External Rotational Axis parameter. 

**Cast <u>to</u>** an **External Linear Axis parameter:** Cast to the External Linear Axis parameter. This is only possible if the {{page.title}} parameter was constructed from an External Linear Axis parameter.

**Cast <u>to</u>** an **External Rotational Axis parameter:** Casts to the External Rotational Axis parameter. This is only possible if the {{page.title}} parameter was constructed from an External Rotational Axis parameter.

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. Defines the position and orientation of the attachment plane of the {{page.title}}. The plane is given in for an external joint position of 0.

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. Defines the position of the attachment plane of the {{page.title}}. The position is given in for an external joint position value of 0.

**Cast <u>to</u>** a **Vector parameter:** Cast to the Vector parameter. Defines the movement direction of the of the {{page.title}} in case it is an External Linear Axis. Defines the rotation axis in case it is an External Rotattional Axis.

**Cast <u>to</u>** a **Domain parameter:** Cast to the Domain parameter. Defines the axis limit of the {{page.title}}.

**Cast <u>to</u>** a **Boolean parameter:** Cast to the Boolean parameter. Defines if the {{page.title}} moves a robot. 

**Cast <u>to</u>** a **Number parameter:** Cast to the Number parameter. Defines if the logic number of the {{page.title}}.

## **Transformation methods**

Transformation methods are implemented for this parameter. It will transform all geometric properties of the {{page.title}}.

## **Morphing methods**

This parameter does not support morphing methods.