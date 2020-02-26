---
layout: module
title: Slicing Tree
image: slicing-tree-1.png
summary: Subdivides boundary polygons in tree like structure. Useful to create orthogonal parcels on a street blocks.

---

## Setup

* Needs a boundary polygon as input. The algorithm slices through the middle of the polygon on the longest edge, creating two new polygons. The step is repeated up until the minimal parcel width is reached.

## Application

* Parcellating street blocks.

## Limitations

* Only width or depth, but not size of parcels can be controlled.

* Restriction to orthogonal forms
