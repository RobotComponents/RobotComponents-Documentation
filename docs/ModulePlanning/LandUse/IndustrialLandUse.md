---
layout: module
title: Industrial Land Use
summary: 
nav_order: 2
---
## Land Use Type for Land Use Distribution

Can be a profile for [Land Use Distribution]().

Possible evaluation criteria can be:

* [Slope](): 5-10%
  
* Keep away from city center, residential, education and health areas
  
  **Close** entities get **low** score (Combine [DistanceTo](), [City Center]() and [Scoring]() )

* Keep close to primary roads, distribution facilities
  
  **Close** entities get **high** score (Combine [DistanceTo]() and [Scoring]())

* Because of polluting industries consider [Wind direction]()

Preferred proportion of land use coverage:

* 5-10%