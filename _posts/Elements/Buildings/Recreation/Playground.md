---
layout: module
title: Playground
summary: 

---

## Recreational Land Use
Can be a subtype of [Recreational Land Use]().

## Location
 Its location can be placed within [Land Use Distribution](), but also manually assisted by [Evaluation Score]() or through i.e. [Force-based Distribution]().

* Can be located close to schools or public spaces as well as residential areas with consideration of noise.
  
  **Close** entities get **high** score (Combine [DistanceTo](), , [Pedestrian Streets](), [Car Streets]() and [Scoring]())

* Keep away from industry, dump sity or cemetry
  
  **Close** entities get **low** score (Combine [DistanceTo](), [City Center]() and [Scoring]() )
