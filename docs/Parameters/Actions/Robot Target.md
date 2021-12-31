---
layout: default
title: Robot Target
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Robot Target** declaration. 

## **Constructors**

[**Robot Target**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Target.md %})

## **Deconstructors**

[**Deconstruct Robot Target**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Robot Target.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Target parameter. This is only possible if the created Target parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **Plane parameter:** Constructs a {{page.title}} parameter from a Plane parameter. This results a robot target with a position and orientation set from the given plane position and orientation. The axis configuration will be set to `0' and a default external joint position will be used.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Cast to the generic [Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. This plane defines the target plane in the work object coordinate system. 

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. This is point defines the coordinates of the target position in the work object coordinate system. 

**Cast <u>to</u>** an **[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) parameter:** Cast to the External Joint Position parameter that is definied for this Robot Target declaration.

## **Transformation methods**

This parameter does not support transformation methods.

## **Morphing methods**

This parameter does not support morphing methods.