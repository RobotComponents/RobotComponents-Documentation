---
layout: default
title: Deconstruct Joint Target
nav_order: 2
parent: Action Deconstructors
grand_parent: Deconstruct Components
---

# **{{page.title}}**

## **Description**

[**Deconstruct**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** 
Deconstructs a [Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) into its parameters.

## **Input Parameters**

[**Robot Target**]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Target.md %}) **(RT):** Defines the [Robot Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Robot Target.md %}) to be deconstructed.

## **Output Parameters**

**Name (N):** Contains the variable name of the deconstructed Joint Target.

**[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJ):** Contains the [Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) of the deconstructed Joint Target.

**[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Contains the [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) of the deconstructed Joint Target.
