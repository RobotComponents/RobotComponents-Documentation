---
layout: default
title: Robot Joint Position
nav_order: 5
parent: Declarative Actions
grand_parent: Code Generation Components
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Declarative Action**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/index.md %})**:** Defines a robot joint position for a [Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) component. 

## **Input Parameters**

**Name (N):**  Defines the name of the joint position based on a text value. Each joint position name needs to be unique or empty. The first letter should not be a number. Do not use special characters. The variables names will be updated based on the list or datatree structure this component generates.

**Robot Joint Position 1 (RJ1):** Defines the position of robot axis 1 in degrees.

**Robot Joint Position 2 (RJ2):** Defines the position of robot axis 2 in degrees.

**Robot Joint Position 3 (RJ3):** Defines the position of robot axis 3 in degrees.

**Robot Joint Position 4 (RJ4):** Defines the position of robot axis 4 in degrees.

**Robot Joint Position 5 (RJ5):** Defines the position of robot axis 5 in degrees.

**Robot Joint Position 6 (RJ6):** Defines the position of robot axis 6 in degrees.

## **Output Parameters**

**[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) (RJ):** Contains the robot joint position as action for a joint target declaration.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** Plug the [Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) output parameter of this component into the Robot Joint Position input parameter of the [Joint Target]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/Joint Target.md %}) component.
