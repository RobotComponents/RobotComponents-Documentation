---
layout: default
title: Speed Data
nav_order: 3
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/index.md %})**:** 
Contains the data of a **Speed Data** declaration. 

## **Constructors**

[**Speed Data**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/Speed Data.md %})

## **Deconstructors**

[**Deconstruct Speed Data**]({{ site.baseurl }}{% link docs/Robot Components/Deconstruct/Actions/Deconstruct Speed Data.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **Number parameter:**  Constructs a {{page.title}} parameter from a primitive Number parameter. The number value will be round off to the nearest predefined speeddata value by ABB. Predefined speeddata values are `5`, `10`, `20`, `30`, `40`, `50`, `60`, `80`, `100`, `150`, `200`, `300`, `400`, `500`, `600`, `800`, `1000`, `1500`, `2000`, `2500`, `3000`, `4000`, `5000`, `6000` or `7000`. For example, the number value `98` will be casted to the predefined speedata variable `v100`. 

**Cast <u>from</u>** a **Text parameter:**  Constructs a {{page.title}} parameter from a primitive Text parameter. Only text values are allowed that start with a `v` followed by a predefined speeddata number. Allowed predefined speeddata text values are `v5`, `v10, `v20`, `v30`, `v40`, `v50`, `v60`, `v80`, `v100`, `v150`, `v200`, `v300`, `v400`, `v500`, `v600`, `v800`, `v1000`, `v1500`, `v2000`, `v2500`, `v3000`, `v4000`, `v5000`, `v6000` or `v7000`.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Action.md %}) parameter. 
