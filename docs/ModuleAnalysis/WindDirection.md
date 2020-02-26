---
layout: module
title: Wind Direction
nav_order: 1
---
# Wind Direction

Wind direction data is required.

* Wind can blow in all directions but with different intensity.

* By simplifying the wind directions as a circle, it can be subdivided into equal parts. Each part represents another vector as a sky direction.

A vector, i.e. from a polluting industry to a healthcare center, can be compared to the wind direction data to find out, how strong wind blows in the direction.

* To figure out the wind intensity in the direction of the vector, the angle between the vector and each wind direction is calculated. The intensity of the two smallest angles is taken and combined by proportional average: 

    intensity = ( intensity1 * ( angle1 ) / ( angle1 + angle2 ) + intensity2 * ( angle2 ) / ( angle1 + angle2 ) ) / 2

* Furthermore, since polluted air is not carried indefinitely, a falloff function can be added through [Scoring](). Starting from the industrial site the intensity is as high as the wind direction. Going away from it, the intensity slowly decreases until it reaches 0 at a far distance.
