---
layout: default
title: Definition Components
nav_order: 6
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Work in progress....

Definition components are used to define robots and robot tools for Code Generation and Simulation.

## **Functionality**

ABB_IRB-1200-7-0.7 or any other Robot Info components are needed for different components from Code Generation and Simulation such as RAPID Generator or Inverse Kinematics and Forward Kinematics. If a specific robot tool is required it can be defined by using the Robot Tool From Data or Robot Tool From Planes component from this category. The Robot Tool output must then be plugged into the ABB_IRB-1200-7-0.7 or any other Robot Info component which is used for Code Generation and Simulation. It will be automatically registered in the RAPID base code of any RAPID Generator component

## **Usage**

[**External Linear Axis**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/External Linear Axis.md %})**:** ...

[**External Rotational Axis**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/External Rotational Axis.md %})**:** ...

[**Robot Info Presets**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot Info Presets.md %})**:** ...

[**Robot Info**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot Info.md %})**:** Defines a robot which is needed for Code Generation and Simulation. 

[**Robot Tool From Planes**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot Tool from Planes.md %})**:** ...

[**Robot Tool Quaternion**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Robot Tool from Quaternion Data.md %})**:** ...

[**Work Object**]({{ site.baseurl }}{% link docs/Robot Components/Definitions/Work Object.md %})**:** ...