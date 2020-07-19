---
layout: default
title: Wait for Digital Input
nav_order: 9
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/index.md %})**:** 
Contains the data of a **Wait for Digital Input** instruction.

## **Constructors**

[**Wait for Digital Input**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Wait for Digital Input.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **Boolean parameter:** Cast to the primitive Boolean parameter. The boolean defines the state of the Wait for Digital Input parameter.  