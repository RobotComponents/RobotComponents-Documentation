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

**Name (N):** Defines the name of the joint position based on a text value. Each joint position name needs to be unique or empty. The first letter should not be a number. Do not use special characters. The variables names will be updated based on the list or datatree structure this component generates.

**External Joint Position A (EJa):** Defines the position of external logical axis A in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

**External Joint Position B (EJb):** Defines the position of external logical axis B in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

## **Variable Input Parameters**

**External Joint Position C (EJc):** Defines the position of external logical axis C in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

**External Joint Position D (EJd):** Defines the position of external logical axis D in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

**External Joint Position E (EJe):** Defines the position of external logical axis E in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

**External Joint Position F (EJf):** Defines the position of external logical axis F in degrees or mm. The default axis value is set to `9E9` (undefined / not connected). 

## **Output Parameters**

**[External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) (EJ):** Contains the external joint position as Action for a Joint Target declaration.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [External Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/External Joint Position.md %}) output parameter of this component into the External Joint Position input parameter of the [Joint Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %}) component.
