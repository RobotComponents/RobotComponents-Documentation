---
layout: default
title: Move
nav_order: 7
parent: Action Parameters
grand_parent: Parameter Components
---

# **{{page.title}}**

## **Description**

[**Action Parameter**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** 
Contains the data of a **Move** instruction.

## **Constructors**

[**Move**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/Move.md %})

## **Deconstructors**

[**Deconstruct Movement**]({{ site.baseurl }}{% link docs/Deconstruct/Actions/Deconstruct Move.md %})

## **Casting methods**

**Cast <u>from</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Constructs a {{page.title}} parameter from a generic Action parameter. This is only possible if the created Action parameter was constructed from a {{page.title}} parameter.

**Cast <u>from</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Construct a {{page.title}} parameter from a Target parameter. This results a Move instruction with the default work object `wobj0`, the default zonedata value `z0` and the slowest predefined speeddata value `v5`. An empty robot tool and empty digital output will be set, and as movement type a `MoveAbsJ` instruction will be set. This casting method is typically used to directly use a Target parameter as input for the Move parameter of the Inverse Kinematics component. 

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Cast to the Target parameter that is definied for this move instruction.

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. Defines the target plane in the world coordinate system. In case an External Axis is attached to the work object, the position and orientation  are defined for external axis values set to zero. 

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. Defines the position of the target plane in the world coordinate system. In case an External Axis is attached to the work object, the position is defined for external axis values set to zero. 

**Cast <u>to</u>** a **[Speed Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Speed Data.md %}) parameter:** Cast to the Speed Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Zone Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Zone Data.md %}) parameter:** Cast to the Zone Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Robot Tool]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) parameter:** Cast to the Robot Tool parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Work Object]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) parameter:** Cast to the Work Object parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Set Digital Output]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Digital Output.md %}) parameter:** Cast to the Set Digital Output parameter that is definied for this move instruction.
