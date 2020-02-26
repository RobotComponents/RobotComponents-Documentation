---
layout: module
title: Sport Facility
summary: 

---

## Recreational Land Use
Can be a subtype of [Recreational Land Use]().

## Location
 Its location can be placed within [Land Use Distribution](), but also manually assisted by [Evaluation Score]() or through i.e. [Force-based Distribution](). Depending on the sport type, a specific shape of the sport field should be considered.

* Can be located close to schools or public spaces. Residential areas are also favourable, but noise should be considered.
  
  **Close** entities get **high** score (Combine [DistanceTo](), , [Pedestrian Streets](), [Car Streets]() and [Scoring]())

* Keep away from industry, dump sity or cemetry
  
  **Close** entities get **low** score (Combine [DistanceTo](), [City Center]() and [Scoring]() )
