---
layout: module
title: Commercial Land Use
summary: 
nav_order: 2

---

## Land Use Type for Land Use Distribution

Can be a profile for [Land Use Distribution]().

Possible evaluation criteria can be:

* [Slope](): Preferable 2-8%, Allowable 2-15%
  
* Keep away from dump site and cemetry
  
  **Close** entities get **low** score (Combine [DistanceTo]() and [Scoring]() )

* Keep close to primary roads and city center
  
  **Close** entities get **high** score (Combine [DistanceTo](), , [Pedestrian Streets](), [City Center](), [Sub Centers]() and [Scoring]())

Preferred proportion of land use coverage:

* 3-7%
  
* Area Consumption differs by building typology.