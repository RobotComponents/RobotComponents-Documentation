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

[**Declarative Action**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/index.md %})**:** Defines a robot joint position for a [Joint Target]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Joint Target.md %}) component. 

## **Input Parameters**

**Robot Axis Value A (RA1):** Defines the position of robot axis 1 in degrees.

**Robot Axis Value B (RA2):** Defines the position of robot axis 2 in degrees.

**Robot Axis Value C (RA3):** Defines the position of robot axis 3 in degrees.

**Robot Axis Value D (RA4):** Defines the position of robot axis 4 in degrees.

**Robot Axis Value E (RA5):** Defines the position of robot axis 5 in degrees.

**Robot Axis Value F (RA6):** Defines the position of robot axis 6 in degrees.

## **Output Parameters**

**[Robot Joint Position]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Robot Joint Position.md %}) (SD):** Contains the robot joint position as action for a joint target declaration.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the [Robot Joint Position]({{ site.baseurl }}{% link docs/Robot Components/Parameters/Actions/Robot Joint Position.md %}) output parameter of this component into the Robot Joint Position input parameter of the [Joint Target]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/Declarative Actions/Joint Target.md %}) component.