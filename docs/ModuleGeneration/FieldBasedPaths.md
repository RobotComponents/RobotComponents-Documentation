---
layout: module
title: Field-based Paths
image: field-based-paths-1.png
summary: Paths grow in the direction of an underlying vector field similar to a magnetic field. The resulting paths are not always straight and more comparable to naturally grown streets.
---

## Setup

* Provide a vector field or derive date from grey-scale image.

* Set starting point from where street should grow.

## Application

Field-based paths are i.e. used in [CityEngine](https://www.youtube.com/watch?v=min5Cz587hw).
By changing the direction 90° perpendicular segments can start from paths. Combining multiple field-based paths, grid-like structures can be created, but the grid deforms and orients itself to the field.

The underlying vector field can be derived i.e. from the terrain, resulting paths might take the steepest path.

## Limitations

* Difficult to control destination of paths.
