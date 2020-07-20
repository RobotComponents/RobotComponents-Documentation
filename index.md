---
layout: default
title: Home
nav_order: 0
description: "Department of Experimental and Digital Design and Construction (EDEK)"
permalink: /
---

# **Robot Components Documentation**

Robot Components is a Plugin for intuitive Robot Programming for ABB robots inside of Rhinos Grasshopper.

The plugin is an open source project initiated by the chair of [Experimental and Digital Design and Construction](https://edek.uni-kassel.de/) of the University of Kassel led by Prof. Eversmann. The technical development is initiated and executed by the research associates and student assistants who are listed [here](https://github.com/EDEK-UniKassel/RobotComponents/blob/master/AUTHORS.md).

RobotComponents uses the ABB PC SDK for real-time connection to ABB Robots, you can find the .dll used in this project here: [ABB developercenter](http://developercenter.robotstudio.com/landing)

## **Overview**

[**Code Generation Components**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** These components are used to generate the RAPID program and system modules for an ABB IRC5 robot controller which can be copied manually or uploaded and run by using [Controller Utility]({{ site.baseurl }}{% link docs/Controller Utility/index.md %}) components. Furthermore, movement instructions can be simulated visually in Rhino by using [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) components.

[**Controller Utility Components**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** These components are used to build up a real-time connection to an ABB IRC5 robot controller.

[**Deconstruct Components**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** These components are used to deconstruct [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components into their parameters.

[**Definitions Components**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** These components are used to define robots and robot tools which are needed for [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}).

[**Parameters Components**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** These components are used to maintain and store Data of [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components.

[**Simulation Components**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** These components are used to visually approximate the movement behavior of the robot before running the RAPID program and system modules on an ABB IRC5 robot controller.

[**Utility Components**]({{ site.baseurl }}{% link docs/Utility/index.md %})**:** These components support other component categories with extra functionality.

**NOTE:** By selecting **Documentation** from the right-click menu of any robot components component in grasshopper, the corresponding documentation page opens up in the browser.
