---
layout: default
title: Action Group
nav_order: 1
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of any [Action Group]({{ site.baseurl }}{% link docs/Parameters/Actions/Action Group.md %}). 

## **Constructors**

[**Group Actions**]({{ site.baseurl }}{% link docs/Utility/Group Actions.md %})

## **Deconstructors**

[**Ungroup Actions**]({{ site.baseurl }}{% link docs/Utility/Ungroup Actions.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **Geometry Group parameter:** Constructs a {{page.title}} parameter from a Geometry Group parameter. This is only possible if the objects within the Geometry Group parameter are Action types.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

## **Transformation methods**

This parameter does not support transformation methods.

## **Morphing methods**

This parameter does not support morphing methods.