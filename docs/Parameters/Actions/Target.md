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

**Cast <u>from</u>** a **[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) parameter:** Constructs a {{page.title}} parameter from a Robot Joint Position parameter. This results a joint target with a default external joint position.

**Cast <u>from</u>** a **Plane parameter:** Constructs a {{page.title}} parameter from a Plane parameter. This results a robot target with a position and orientation set from the given plane position and orientation. The axis configuration will be set to `0' and a default external joint position will be used. 

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) parameter:** Cast to the Joint Target parameter. This is only possible if a Joint Target was used to construct the Target parameter.

**Cast <u>to</u>** a **[Robot Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Target.md %}) parameter:** Cast to the Robot Target parameter. This is only possible if a Robot Target was used to construct the Target parameter.

**Cast <u>to</u>** an **[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) parameter:** Cast to the External Joint Position parameter that is definied for this Target declaration.
