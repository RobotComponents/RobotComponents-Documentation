---
layout: default
title: Absolute Joint Movement
nav_order: 6
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/index.md %})**:** 
Contains the data of an **Absolute Joint Movement** instruction. 

## **Constructors**

[**Absolute Joint Movement**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Instructive Actions/Absolute Joint Movement.md %})

## **Deconstructors**

[**Deconstruct Absolute Joint Movement**]({{ site.baseurl }}{% link docs/Robot Components/Deconstruct/Actions/Deconstruct Absolute Joint Movement.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter.   

**Cast <u>to</u>** a **[Speed Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Speed Data.md %}) parameter:** Cast to the Speed Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Zone Data]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Zone Data.md %}) parameter:** Cast to the Zone Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Robot Tool]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Definitions/Robot Tool.md %}) parameter:** Cast to the Robot Tool parameter that is definied for this move instruction.