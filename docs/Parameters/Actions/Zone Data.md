---
layout: default
title: Zone Data
nav_order: 2
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Zone Data** declaration. 

## **Constructors**

[**Zone Data**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Zone Data.md %})

## **Deconstructors**

[**Deconstruct Zone Data**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Zone Data.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** an **Integer parameter:** Constructs a {{page.title}} parameter from a primitive Integer parameter. The integer value will be round off to the nearest predefined zonedata value by ABB. Predefined zonedata values are `-1`, `0`, `1`, `5`, `10`, `15`, `20`, `30`, `40`, `50`, `60`, `80`, `100`, `150` and `200`. For example, the integer value `9` will be casted to the predefined zonedata variable `z10`. If the value equals `-1` the precision is interpreted as `fine`.


**Cast <u>from</u>** a **Number parameter:** Constructs a {{page.title}} parameter from a primitive Number parameter. The number value will be round off to the nearest predefined zonedata value by ABB. Predefined zonedata values are `-1`, `0`, `1`, `5`, `10`, `15`, `20`, `30`, `40`, `50`, `60`, `80`, `100`, `150` and `200`. For example, the number value `9` will be casted to the predefined zonedata variable `z10`. If the value equals `-1` the precision is interpreted as `fine`.

**Cast <u>from</u>** a **Text parameter:**  Constructs {{page.title}} parameter from a primitive Text parameter. Only text values are allowed that start with a `z` followed by a predefined zonedata number. Allowed predefined zonedata text values are `fine`, `z0`, `z1`, `z5`, `z10`, `z15`, `z20`, `z30`, `z40`, `z50`, `z60`, `z80`, `z100`, `z150` and `z200`.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 
