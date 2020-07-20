---
layout: default
title: Target
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Target** declaration. 

## **Constructors**

[**Robot Target**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Target.md %})

[**Joint Target**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %})

## **Deconstructors**

[**Deconstruct Robot Target**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Robot Target.md %})

[**Deconstruct Joint Target**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Joint Target.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. This plane defines the target plane in the work object coordinate system. 

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. This is point defines the coordinates of the target position in the work object coordinate system. 
