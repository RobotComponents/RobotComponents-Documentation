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

[**Declarative Action**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/index.md %})**:** 
Defines the external joint position for a [Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) component.

## **Input Parameters**

**External Axis Value A (EAa):** Defines the position of external logical axis A. The default axis value is set to `9E9` (undefined / not connected). 

**External Axis Value B (EAb):** Defines the position of external logical axis B. The default axis value is set to `9E9` (undefined / not connected). 

## **Variable Input Parameters**

**External Axis Value C (EAc):** Defines the position of external logical axis C. The default axis value is set to `9E9` (undefined / not connected). 

**External Axis Value D (EAd):** Defines the position of external logical axis D. The default axis value is set to `9E9` (undefined / not connected). 

**External Axis Value E (EAe):** Defines the position of external logical axis E. The default axis value is set to `9E9` (undefined / not connected). 

**External Axis Value F (EAf):** Defines the position of external logical axis F. The default axis value is set to `9E9` (undefined / not connected). 

## **Output Parameters**

**[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Contains the external joint position as Action for a Joint Target declaration.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) output parameter of this component into the External Joint Position input parameter of the [Joint Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %}) component.
