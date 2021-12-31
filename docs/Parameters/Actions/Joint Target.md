---
layout: default
title: Joint Target
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Joint Target** declaration. 

## **Constructors**

[**Joint Target**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %})

## **Casting methods**

[**Deconstruct Joint Target**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Joint Target.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Target parameter. This is only possible if the created Target parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) parameter:** Constructs a {{page.title}} parameter from a Robot Joint Position parameter. This results a joint target with a default external joint position.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Cast to the generic [Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) parameter:** Cast to the Robot Joint Position parameter that is definied for this Joint Target declaration.

**Cast <u>to</u>** an **[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) parameter:** Cast to the External Joint Position parameter that is definied for this Joint Target declaration.

## **Transformation methods**

This parameter does not support transformation methods.

## **Morphing methods**

This parameter does not support morphing methods.