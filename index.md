---
layout: default
title: Home
nav_order: 0
description: "Department of Experimental and Digital Design and Construction (EDEK)"
permalink: /
---

# **Robot Components Documentation**

Robot Components is a plugin for intuitive robot programming for ABB robots inside of Rhinoceros Grasshopper. Robot Components offers a wide set of tools to create toolpaths, simulate robotic motion and generate RAPID code within Grasshopper. Some of the main features include:

- 30+ predefined ABB robot models
- Possibility to add your own robot models
- Support for external axes (both linear and rotational)
- Possibility to define custom strategies for all external axis values
- Support for work objects (including movable work objects)
- Efficient forward and inverse kinematics
- Possibility to add your own custom code lines
- Real-time connection with IRC5 controllers
- Robot Components API to develop your custom components using either Python or C# (w.i.p, documentation coming soon)

# **Getting Started**

You can download the latest release directly from our [Github release page](https://github.com/RobotComponents/RobotComponents/releases) and from [Food4Rhino](https://www.food4rhino.com/app/robot-components). Unzip the downloaded archive and copy all files in the Grasshopper Components folder (in GH, File > Special Folders > Components Folder). Make sure that all the files are unblocked (right-click on the file and select Properties from the menu. Click Unblock on the General tab). Restart Rhino and you are ready to go!

In case you want to use the components from the Controller Utility section you additionally have to install [Robot Studio](https://new.abb.com/products/robotics/robotstudio) or the ABB Robot Communication Runtime (you can download it by clicking [here](https://github.com/RobotComponents/RobotComponents/raw/master/Utility/ABB%20Robot%20Communication%20Runtime%207.0.zip)). The current release is built and tested against the ABB PC SDK version 2020.1 (ABB Robot Communication Runtime 7.0). We do not guarantee that the Controller Utility components work with older versions of the ABB Robot Communucation Runtime. Please contact us if you have problems with establishing a real-time connection from Grasshopper.

You can find a collection of example files demonstrating the main features of Robot Components on our [Github page](https://github.com/RobotComponents/RobotComponents) and on [Food4Rhino](https://www.food4rhino.com/app/robot-components). The documentation website of the API is coming soon.

For easy sharing of the download link and the documentation (with e.g. students) you can also use our [linktree](https://linktr.ee/RobotComponents).

# **Overview of the components**

[**Code Generation Components**]({{ site.baseurl }}{% link docs/Code Generation/index.md %})**:** These components are used to generate the RAPID program and system modules for an ABB IRC5 robot controller which can be copied manually or uploaded and run by using [Controller Utility]({{ site.baseurl }}{% link docs/Controller Utility/index.md %}) components. Furthermore, movement instructions can be simulated visually in Rhino by using [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) components.

[**Controller Utility Components**]({{ site.baseurl }}{% link docs/Controller Utility/index.md %})**:** These components are used to build up a real-time connection to an ABB IRC5 robot controller.

[**Deconstruct Components**]({{ site.baseurl }}{% link docs/Deconstruct/index.md %})**:** These components are used to deconstruct [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components into their parameters.

[**Definitions Components**]({{ site.baseurl }}{% link docs/Definitions/index.md %})**:** These components are used to define robots and robot tools which are needed for [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Simulation]({{ site.baseurl }}{% link docs/Simulation/index.md %}).

[**Parameters Components**]({{ site.baseurl }}{% link docs/Parameters/Actions/index.md %})**:** These components are used to maintain and store Data of [Code Generation]({{ site.baseurl }}{% link docs/Code Generation/index.md %}) and [Definitions]({{ site.baseurl }}{% link docs/Definitions/index.md %}) components.

[**Simulation Components**]({{ site.baseurl }}{% link docs/Simulation/index.md %})**:** These components are used to visually approximate the movement behavior of the robot before running the RAPID program and system modules on an ABB IRC5 robot controller.

[**Utility Components**]({{ site.baseurl }}{% link docs/Utility/index.md %})**:** These components support other component categories with extra functionality.

**NOTE:** By selecting **Documentation** from the right-click menu of any robot components component in grasshopper, the corresponding documentation page opens up in the browser.

# **Credits**

The plugin is an open source project initiated by the chair of [Experimental and Digital Design and Construction](https://edek.uni-kassel.de/) of the University of Kassel led by Prof. Eversmann. The technical development is initiated and executed by the research associates and student assistants who are listed [here](https://github.com/RobotComponents/RobotComponents/blob/master/AUTHORS.md).

RobotComponents uses the ABB PC SDK for real-time connection to ABB Robots, you can find the .dll used in this project here: [ABB developercenter](http://developercenter.robotstudio.com/landing). 

We would like to acknowledge [Jose Luis Garcia del Castillo](https://github.com/garciadelcastillo) and [Vicente Soler](https://github.com/visose) for making their Grasshopper plugins [RobotExMachina](https://github.com/RobotExMachina) and [Robots](https://github.com/visose/Robots) available. Even our approach is different it was helpful for us to see how you implemented certain functionalities and approached certain issues. 

# **License**

Robot Components

Copyright (c) 2018-2020 [The Robot Components authors and / or their affiliations](https://github.com/RobotComponents/RobotComponents/blob/master/AUTHORS.md)

Robot Components is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3.0 as published by the Free Software Foundation. 

Robot Components is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Robot Components; If not, see <http://www.gnu.org/licenses/>.

@license GPL-3.0 <https://www.gnu.org/licenses/gpl.html>

