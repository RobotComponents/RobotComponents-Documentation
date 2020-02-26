---
layout: module
title: Scoring
id: m-a-005
summary: Compares numbers of a dataset with preferred number and derives a score from difference.
---

## Setup

Basic scoring:

* Set preferred number
  
* Compare preferred number to each number of a dataset by subtraction.
  
    The resulting subtracted number can be used as a score with high numbers as high score and low numbers as low score.

Absolute Values:

* If there is no difference between the distance of numbers smaller or higher than the preferred number, choose the absolute/positive value: 

    -1 has same distance to 0 as 1. Both can get the same value of 1, if it is not of importance.
  
Remapping Values:

* Mapping: Take the smallest and highest calculated numbers as minimum and maximum values. Define a new minimum and maximum value and map all numbers within this range:

    Mapped Number = Minimum New + (Number - Minimum Old) * (Maximum New - Maximum Old) / (Maximum New - Minimum New)

* Easing: With an easing function number can not only be mapped linearly. Functions can be i.e. f(1/number). A function can be drawn on a graph with the x-axis representing the calculated numbers and a y-axis representing the new values. By taking a value on the x-axis a value on the y-axis can be derived through the function.
(Easing functions are common in animation software and web development and [well documented](https://easings.net))

## Application

* Residential areas might need to be build close to the city center. The distance to the center can be calculated. A basic scoring would give close locations a low number and far away places a high number. Low numbers would represent good values.

* If high numbers would be needed as good values, the numbers can be remapped: A distance of 0m would get a score of 1 a distance of 3000m and above would  get a score of 0.

* If very close areas are preferred, an easing function such as a cubic-bezier could rate close number higher.

## Limitations
