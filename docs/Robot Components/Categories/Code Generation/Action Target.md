---
layout: default
title: Action Target
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** This component defines an instruction to change the current robot tool of the ABB robot for RAPID base code generation.

## **Input Parameters**

**Name (N):** Defines the name of the target based on a string value. Each target name should be unique. The first letter shouldn’t be a number. Don’t use special characters.

**Plane (P):** Defines the target plane of the target based on one or a list of planes. Note: You can use a Flip Plane X or Flip Plane Y component to flip the plane.

**Reference Plane (RP):**

**Axis Configuration (AC):** Defines the axis configuration of the robot to reach the defined target plane based on an integer value. The range is 0 to 7. Read more on that topic here: Robot Configuration Data.

**External Axis Value A (EAa):**

**External Axis Value B (EAb):**

**External Axis Value C (EAc):**

**External Axis Value D (EAd):**

**External Axis Value E (EAe):**

**External Axis Value F (EAf):**

## **Output Parameters**

**Target (T):** Contains the defined target information as an Action for RAPID main code generation.

## **Menu Items**

TODO

## **Usage**

**Simulation:** Plug the Target output of this component into the Target input of the Inverse Kinematics component to get the robots axis values for the defined target.

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %})**:** Plug the Target output of this component into the Target input of the Action: Movement component to define a robot movement.