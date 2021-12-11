---
layout: default
title: External Joint Position
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **External Joint Position** declaration. 

## **Constructors**

[**External Joint Position**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/External Joint Position.md %})

## **Deconstructors**

[**Deconstruct External Joint Position**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct External Joint Position.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs an {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from an {{page.title}} parameter.

**Cast <u>from</u>** a **Number parameter:** Constructs an {{page.title}} parameter from a number value. This number value will be used as the first external axis value. The other external axis values inside the {{page.title}} parameter will be set to `9E9` (undefined / not connected).

**Cast <u>from</u>** a **Text parameter:** Constructs an {{page.title}} parameter from a text. The user can define up to six external axis values as a text to construct an {{page.title}} parameter. For example, the text `1000, 500` will be casted to an {{page.title}} parameter with the first external axis value set to `1000` and the second external axis value set to `500`. All other external axis values inside this {{page.title}} parameter will be set to `9E9` (undefined / not connected). 

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 