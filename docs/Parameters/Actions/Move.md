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

**Cast <u>from</u>** a **[Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) parameter:** Construct a {{page.title}} parameter from a Joint Target parameter. This results a Move instruction with the default work object `wobj0`, the default zonedata value `z0` and the slowest predefined speeddata value `v5`. An empty robot tool and empty digital output will be set, and as movement type a `MoveAbsJ` instruction will be set. This casting method is typically used to directly use a Target parameter as input for the Move parameter of the Inverse Kinematics component. 

**Cast <u>from</u>** a **[Robot Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) parameter:** Construct a {{page.title}} parameter from a Robot Target parameter. This results a Move instruction with the default work object `wobj0`, the default zonedata value `z0` and the slowest predefined speeddata value `v5`. An empty robot tool and empty digital output will be set, and as movement type a `MoveAbsJ` instruction will be set. This casting method is typically used to directly use a Target parameter as input for the Move parameter of the Inverse Kinematics component. 

**Cast <u>from</u>** a **[Robot Joint Position]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Joint Position.md %}) parameter:** Constructs a {{page.title}} parameter from a Robot Joint Position parameter. This results a joint target with a default external joint position. This results a Move instruction with a joint target set with the given robot joint position and a default external joint position. The default work object `wobj0`, the default zonedata value `z0` and the slowest predefined speeddata value `v5` will be used. An empty robot tool and empty digital output will be set, and as movement type a `MoveAbsJ` instruction will be used. This casting method is typically used to directly use a Plane parameter as input for the Move parameter of the Inverse Kinematics component.

**Cast <u>from</u>** a **Plane parameter:** Constructs a {{page.title}} parameter from a Plane parameter. This results a Move instruction with a robot target position and orientation set from the given plane position and orientation. The axis configuration will be set to `0' and a default external joint position will be used. The default work object `wobj0`, the default zonedata value `z0` and the slowest predefined speeddata value `v5` will be used. An empty robot tool and empty digital output will be set, and as movement type a `MoveAbsJ` instruction will be used. This casting method is typically used to directly use a Plane parameter as input for the Move parameter of the Inverse Kinematics component.

**Cast <u>to</u>** an **[Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter:** Cast to the generic [Action]({{ site.baseurl }}{% link docs/Parameters/Actions/Action.md %}) parameter. 

**Cast <u>to</u>** a **[Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Target.md %}) parameter:** Cast to the Target parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Joint Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Joint Target.md %}) parameter:** Cast to the Joint Target parameter that is definied for this move instruction. This is only possible if a Joint Target was used to construct the Move parameter.

**Cast <u>to</u>** a **[Robot Target]({{ site.baseurl }}{% link docs/Parameters/Actions/Robot Target.md %}) parameter:** Cast to the Robot Target parameter that is definied for this move instruction. This is only possible if a Robot Target was used to construct the Move parameter.

**Cast <u>to</u>** a **Plane parameter:** Cast to the Plane parameter. Defines the target plane in the world coordinate system. In case an External Axis is attached to the work object, the position and orientation  are defined for external axis values set to zero. 

**Cast <u>to</u>** a **Point parameter:** Cast to the Point parameter. Defines the position of the target plane in the world coordinate system. In case an External Axis is attached to the work object, the position is defined for external axis values set to zero. 

**Cast <u>to</u>** a **[Speed Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Speed Data.md %}) parameter:** Cast to the Speed Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Zone Data]({{ site.baseurl }}{% link docs/Parameters/Actions/Zone Data.md %}) parameter:** Cast to the Zone Data parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Robot Tool]({{ site.baseurl }}{% link docs/Parameters/Definitions/Robot Tool.md %}) parameter:** Cast to the Robot Tool parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Work Object]({{ site.baseurl }}{% link docs/Parameters/Definitions/Work Object.md %}) parameter:** Cast to the Work Object parameter that is definied for this move instruction.

**Cast <u>to</u>** a **[Set Digital Output]({{ site.baseurl }}{% link docs/Parameters/Actions/Set Digital Output.md %}) parameter:** Cast to the Set Digital Output parameter that is definied for this move instruction.
