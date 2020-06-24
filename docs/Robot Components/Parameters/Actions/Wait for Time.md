---
layout: default
title: Wait for Time
nav_order: 7
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/index.md %})**:** 
Contains the data of a **Wait for Time** instruction.

## **Constructors**

[**Wait for Time**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Wait for Time.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **Number parameter:** Construct a {{page.title}} parameter from a primitive Numer parameter.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **Number parameter:** Cast to the primitive Number parameter. The number defines the wait time of the Wait for Time instruction.  