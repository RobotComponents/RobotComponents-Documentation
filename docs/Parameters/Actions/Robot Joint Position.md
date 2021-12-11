---
layout: default
title: Robot Joint Position
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Robot Joint Position** declaration. 

## **Constructors**

[**Robot Joint Position**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Joint Position.md %})

## **Deconstructors**

[**Deconstruct Robot Joint Position**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Robot Joint Position.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **Text parameter:** Constructs an {{page.title}} parameter from a text. The user can define the six axis values as a text to construct a {{page.title}} parameter. The axis values has to be separated by a comma. For example, the text `10, 25, 10.9, -45, 25, -24.9` will be casted to a {{page.title}} parameter with the first axis value set to `10`, the second axis value set to `25` and so forth. If less then six axis values are defined the missing axis values will be set to `0`. 

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 
