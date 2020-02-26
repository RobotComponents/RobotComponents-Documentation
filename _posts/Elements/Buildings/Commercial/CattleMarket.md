---
layout: module
title: Cattle Market
summary: 

---

## Commercial Land Use
Can be a subtype of [Commercial Land Use]() and influences its density.

* Area Requirement per plot: 5,000-13,000 sqm
* Goats and sheeps need around 4 sqm per animal
* Donkey and horse need around 5 sqm per animal

## Location
A cattle market needs space. Its location can be placed within [Land Use Distribution](), but also manually assisted by [Evaluation Score]() or through i.e. [Force-based Distribution](). Assisted with the [Boundary]() module, a site can be defined that is considering the context.
  
* Keep away from residential areas or city center
  
  **Close** entities get **low** score (Combine [DistanceTo]() and [Scoring]() )

* Keep close to primary roads, agricultural service locations and sites
  
  **Close** entities get **high** score (Combine [DistanceTo]() and [Scoring]())
  