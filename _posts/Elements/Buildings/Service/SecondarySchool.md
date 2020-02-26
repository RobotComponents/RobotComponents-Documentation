---
layout: module
title: Secondary School
summary: 

---

# Education
Can be a subtype of [Education]().

* Area Requirement for 1st to 4th grade: 30,000-60,000 sqm

* Keep away noisy, distracting areas such as industry or commerce

  **Close** entities get **low** score (Combine [DistanceTo]() and [Scoring]() )

* Keep close residential areas (less than 3-5km)
  
  **Close** entities get **high** score (Combine [DistanceTo](), , [Cycling Streets]() and [Scoring]() )

* Prefer less sloppy areas, not vulnerable to [Flood]() and [Wind]()
  
  