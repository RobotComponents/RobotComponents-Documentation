---
layout: default
title: Home
nav_order: 0
description: "Robot Components"
permalink: /
---

# **Robot Components Documentation**

Robot Components is a plugin for intuitive robot programming for ABB robots inside of Rhinoceros Grasshopper. Robot Components offers a wide set of tools to create toolpaths, simulate robotic motion and generate RAPID code within Grasshopper. Some of the main features include:

- 40+ predefined ABB robot models
- Possibility to add your own robot models
- Support for external axes (both linear and rotational)
- Possibility to define custom strategies for all external axis values
- Support for work objects (including movable work objects)
- Efficient forward and inverse kinematics
- Possibility to add your own custom code lines
- Real-time connection with IRC5 and OmniCore controllers
- [Robot Components API](https://robotcomponents.github.io/RobotComponents-API-Documentation/index.html) to develop your custom components using either Python or C#

# **Getting Started**
If you use Rhino 7 or higher you can install Robot Components via the package manager. For other versions, you can download the latest release directly from the GitHub [releases page](https://github.com/RobotComponents/RobotComponents/releases) or [Food4Rhino](https://www.food4rhino.com/app/robot-components). Unzip the downloaded archive and copy all files in the Grasshopper Components folder (in GH, File > Special Folders > Components Folder). Make sure that all the files are unblocked (right-click on the file and select Properties from the menu. Click Unblock on the General tab). Restart Rhino and you are ready to go! 

In case you want to use the components from the Controller Utility section you additionally have to install [Robot Studio](https://new.abb.com/products/robotics/robotstudio) or the ABB Robot Communication Runtime (you can download it by clicking [here](https://github.com/RobotComponents/RobotComponents/raw/main/Utility/ABB%20Communication%20Runtime/ABB%20Robot%20Communication%20Runtime%202024.1.zip)). The latest release is built and tested against the ABB PC SDK version 2024.1 (ABB Robot Communication Runtime 2024.1). We do not guarantee that the Controller Utility components work with older versions of the ABB Robot Communication Runtime. Besides that, the components from the Controller Utility section are only supported on Windows operating systems. Please contact us if you have problems with establishing a real-time connection from Grasshopper.

You can find a collection of example files demonstrating the main features of Robot Components in this repository in the folder [Example Files](https://github.com/RobotComponents/RobotComponents/tree/master/ExampleFiles). You can find the Grasshopper documentation website [here](https://robotcomponents.github.io/RobotComponents-Documentation/). The documentation website of the API [here](https://robotcomponents.github.io/RobotComponents-API-Documentation/index.html).

For easy sharing of the download link and the documentation (with e.g. students) you can also use our [linktree](https://linktr.ee/RobotComponents).

# **Overview of the components**

[**Code Generation Components**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** These components are used to generate the RAPID program and system modules for an ABB IRC5 robot controller which can be copied manually or uploaded and run by using [Controller Utility]({{ site.baseurl }}{% link docs/Controller Utility/index.md %}) components. Furthermore, movement instructions can be simulated visually in Rhino by using [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) components.

[**Controller Utility Components**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** These components are used to build up a real-time connection to an ABB IRC5 robot controller.

[**Deconstruct Components**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** These components are used to deconstruct [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components into their parameters.

[**Definitions Components**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** These components are used to define robots and robot tools which are needed for [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}).

[**Multi Move Components**]({{ site.baseurl }}{% link docs/Multi Move/index.md %})**:** These components are used to create RAPID programs for Multi Move tasks. Multi Move components are an extension of the components in the [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) category and need to be combined with other [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) components to create a Multi Move program.

[**Parameters Components**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** These components are used to maintain and store Data of [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components.

[**Simulation Components**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** These components are used to visually approximate the movement behavior of the robot before running the RAPID program and system modules on an ABB IRC5 robot controller.

[**Utility Components**]({{ site.baseurl }}{% link docs/Utility/index.md %})**:** These components support other component categories with extra functionality.

**NOTE:** By selecting **Documentation** from the right-click menu of any robot components component in Grasshopper, the corresponding documentation page opens up in the browser.

# **Credits**

Robot Components is an open-source project that was initiated by the chair of [Experimental and Digital Design and Construction of the University of Kassel](https://www.uni-kassel.de/fb06/institute/architektur/fachgebiete/experimentelles-und-digitales-entwerfen-und-konstruieren/home). The plugin is currently further developed and maintained by [Arjen Deetman](http://www.arjendeetman.nl). All developers and contributors are listed [here](https://github.com/RobotComponents/RobotComponents/blob/master/AUTHORS.md).

Robot Components uses the ABB PC SDK for real-time connection to ABB Robots, you can find the .dll used in this project here: [ABB developercenter](http://developercenter.robotstudio.com/landing). 

Robot Components uses the OPW kinematics solver as described in the paper ['_An Analytical Solution of the Inverse Kinematics Problem of Industrial Serial Manipulators with an Ortho-parallel Basis and a Spherical Wrist_'](https://www.researchgate.net/publication/264212870_An_Analytical_Solution_of_the_Inverse_Kinematics_Problem_of_Industrial_Serial_Manipulators_with_an_Ortho-parallel_Basis_and_a_Spherical_Wrist) by Mathias Brandstötter, Arthur Angerer, and Michael Hofbaur.

We would like to acknowledge [Jose Luis Garcia del Castillo](https://github.com/garciadelcastillo) and [Vicente Soler](https://github.com/visose) for making their Grasshopper plugins [RobotExMachina](https://github.com/RobotExMachina) and [Robots](https://github.com/visose/Robots) available. Even though our approach is different it was helpful for us to see how you implemented certain functionalities and approached certain issues. 

# **License**

Copyright (c) 2018-2020 EDEK Uni Kassel\
Copyright (c) 2020-2024 Arjen Deetman

Robot Components is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3.0 as published by the Free Software Foundation. 

Robot Components is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Robot Components; If not, see <http://www.gnu.org/licenses/>.

@license GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.html>

