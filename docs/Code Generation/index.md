---
layout: default
title: Code Generation Components
nav_order: 3
has_children: true
has_toc: false
---

# **{{page.title}}**

## **Description**

Code Generation components are used to create the RAPID program and system modules for a virtual or physical ABB IRC5 robot controller. This is done by plugging a list of Actions into the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component, which generates the RAPID program module for the ABB IRC5 robot controller. 

The RAPID program module contains the robot instructions such as target definitions, movement behavior etc. More information on that topic can be found in the [Introduction to RAPID manual](http://dl.icdst.org/pdfs/files3/db9fddeb58803077290aa2538c54333d.pdf) or in the [Technical Reference Manual](https://library.e.abb.com/public/688894b98123f87bc1257cc50044e809/Technical%20reference%20manual_RAPID_3HAC16581-1_revJ_en.pdf) of ABB Robotics. 

The RAPID program module can be copied manually from the [RAPID Generator]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %}) component output to the controller or uploaded and run by using the [Remote Connection]({{ site.baseurl }}{% link docs/Controller Utility/Remote Connection.md %}) component from the [Controller Utility]({{ site.baseurl }}{% link docs/Controller Utility/index.md %}) category. 

## **Components**

[**Declarative Actions**]({{ site.baseurl }}{% link docs/Code Generation/Declarative Actions/index.md %})**:** Used to define declarations for the RAPID program module.

[**Instructive Actions**]({{ site.baseurl }}{% link docs/Code Generation/Instructive Actions/index.md %})**:** Used to define instructions for the RAPID program module.

[**Dynamic Actions**]({{ site.baseurl }}{% link docs/Code Generation/Dynamic Actions/index.md %})**:** Used to define either declarations or instructions for the RAPID program module.

[**RAPID Generator**]({{ site.baseurl }}{% link docs/Code Generation/RAPID Generator.md %})**:** Generates the RAPID program and system modules for the ABB IRC5 robot controller from a list of Actions.
