---
layout: default
title: Get Controller
nav_order: 4
has_toc: true
---

# Description

Controller Utility: This component is used to connect to a virtual or real ABB IRC5 robot controller and extract data from it.

# Input Parameter

Update: Defines if the connection to the ABB IRC5 robot controller will be constantly updated based on a boolean value. This is needed for real-time communication.

# Output Parameter

Robot Controller: Contains information about the connected ABB IRC5 Controller.

# Usage

Controller Utility: This component is used to get different information from a virtual or real ABB IRC5 robot controller. The Robot Controller output of this component can be plugged into the Robot Controller input of following components: Get Axis Values, Get Digital Input, Get Digital Output, Remote Connection.