---
layout: module
title: Administration Land Use
summary: 
nav_order: 2
---

#### Positioning

Administrational buildings can be placed in relation to other land uses. But since, they are of high importance for the functionality of a city, their position can be decided before other land uses, but also in relation to them. This can be done manually or with assistance of [Force-based Distribution]().

#### Land Use Type for Land Use Distribution

Can be a profile for [Land Use Distribution]().

Possible evaluation criteria can be:

* [Slope](): 2-8%
  
* Keep away from industry, dump site, cemetry
  
  **Close** entities get **low** score (Combine [DistanceTo]() and [Scoring]() )

* Keep close to city center and sub centers
  
  **Close** entities get **high** score (Combine [DistanceTo](), [City Center](), [Sub Centers]() and [Scoring]())


Preferred proportion of land use coverage:

* 2-5%
  
* Area Consumption differs by building typology of residential land use.