---
layout: default
title: Controller Utility Components
nav_order: 2
has_children: true
# permalink: docs/utilities
has_toc: false
---

# **{{page.title}}**

## **Description**

Controller Utility components are used to build up a real-time connection to a virtual or real ABB IRC5 robot controller.

The [**Get Controller**]({{ site.baseurl }}{% link docs/Controller Utility/Get Controller.md %}) component can be used to easily build up and define a connection to an available virtual or real ABB IRC5 robot controller. 
Different pieces of information can then be extracted and updated using other components from this category. 
Also, the [**Remote Connection**]({{ site.baseurl }}{% link docs/Controller Utility/Remote Connection.md %}) component can be used to establish a remote connection with the defined controller which enables the user to upload an run RAPID code instantaneously.

## **Components**

[**Get Controller**]({{ site.baseurl }}{% link docs/Controller Utility/Get Controller.md %})**:** Connects to a virtual or real ABB IRC5 Controller to extract data from it.

[**Remote Connection**]({{ site.baseurl }}{% link docs/Controller Utility/Remote Connection.md %})**:** Establishes a remote connection with the controller to upload an run RAPID code directly on a virtual or real ABB IRC5 robot controller.

[**Get Axis Values**]({{ site.baseurl }}{% link docs/Controller Utility/Get Axis Values.md %})**:** Get the current robot axis values from the ABB IRC5 robot controller.

[**Get Plane**]({{ site.baseurl }}{% link docs/Controller Utility/Get Plane.md %})**:** Gets the position of a mechanical unit from the defined ABB IRC5 robot controller.

[**Get Digital Input**]({{ site.baseurl }}{% link docs/Controller Utility/Get Digital Input.md %})**:** Get the state of a defined digital input from the ABB IRC5 robot controller.

[**Get Digital Output**]({{ site.baseurl }}{% link docs/Controller Utility/Get Digital Output.md %})**:** Get the state of a defined digital output from an ABB IRC5 robot controller.

[**Set Digital Output**]({{ site.baseurl }}{% link docs/Controller Utility/Set Digital Output.md %})**:** Set the value of a defined digital output of the ABB IRC5 robot controller.

[**Set Digital Input**]({{ site.baseurl }}{% link docs/Controller Utility/Set Digital Input.md %})**:** Set the value of a defined digital input of the ABB IRC5 robot controller.
