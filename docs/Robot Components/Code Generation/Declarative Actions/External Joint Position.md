---
layout: default
title: External Joint Position
nav_order: 6
parent: Declarative Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Declarative Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/index.md %})**:** 
Defines the external joint position for a [Joint Target]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Joint Target.md %}) component. 

## **Input Parameters**

**External Axis Value A (EAa):** Defines the first external axis value.

**External Axis Value B (EAb):** Defines the second external axis value.

**External Axis Value C (EAc):** Defines the third external axis value.

**External Axis Value D (EAd):** Defines the fourth external axis value.

**External Axis Value E (EAe):** Defines the fifth external axis value.

**External Axis Value F (EAf):** Defines the sixth external axis value.

## **Output Parameters**

**[External Joint Position]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/External Joint Position.md %}) (SD):** Contains the external joint position as action for a joint target declaration.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the [External Joint Position]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/External Joint Position.md %}) output parameter of this component into the External Joint Position input parameter of the [Joint Target]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/Joint Target.md %}) component.