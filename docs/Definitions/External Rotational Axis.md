---
layout: default
title: External Rotational Axis
nav_order: 7
parent: Definition Components
grand_parent: Robot Components Categories
---

# **{{page.title}}**

## **Description**

[**Definition**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** 
Defines a custom external rotational axis.

## **Input Parameters**

**Name (N):** Defines the name of the external rotational axis as string.

**Axis Plane (AP):** Defines the axis plane as plane.

**Axis Limits (AL):** Defines the axis limits as list of domains.

**Base Mesh (BM):** Defines the mesh of the external rotational axis base.

**Link Mesh (LM):** Defines the mesh of the external rotational axis link.

## **Variable Input Parameters**

Through the right-click menu of the component the following variable input parameters can be added:

**Axis Logic Number (AL):** Defines the axis logic number of the External Rotational Axis. By default this value is set to `-1`. For that case the axis logic number will be assigned automatically when a new Robot is constructed based on the list order of all attached external axes. The user can overwrite this value by using this Axis Logic Number input parameter. Allowed text values are `A`, `B`, `C`, `D`, `E` and `F`. Lower case text values are also allowed. 

**Moves Robot (MR)**: Defines if the External Rotatioanl Axis moves a Robot. For an External Rotational Axis the default value is set to `False`. 

## **Output Parameters**

[**External Rotational Axis**]({{ site.baseurl }}{% link docs/Parameters/Definitions/External Rotational Axis.md %}) **(ERA):** Contains the External Rotational Axis information.

## **Usage**

**Note:** You can use the Quarternion to Plane component to define the axis plane from the Base Frame data that is defined in controller configuration. The position and orientation of the axis plane has to match with the Base Frame that is defined in the configuration file of the virtual or physical controller. 

[**Definitions**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** Plug the External Rotational Axis output parameter of this component into the External Rotational Axis input parameter of a [Robot]({{ site.baseurl }}{% link docs/Definitions/Robot.md %}) component. The robot will be attached to the External Linear Axis.
