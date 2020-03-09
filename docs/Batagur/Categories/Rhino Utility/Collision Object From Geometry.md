---
layout: default
title: Collision Object From Geometry
nav_order: 0
parent: Rhino Utility
grand_parent: Batagur Categories
has_toc: false
---

## Description

[Rhino Utility]({{ site.baseurl }}{% link docs/Batagur/Categories/Rhino Utility/Rhino Utility.md %}): Generates a [moveit_msgs/CollisionObject](http://docs.ros.org/api/moveit_msgs/html/msg/CollisionObject.html) message from Rhino Geometry.

## Input Parameter

**ID**: The unique identivier of the object (name used in MoveIt).

**Header**: A [std_msgs/Header](docs.ros.org/api/std_msgs/html/msg/Header.html) message used for interpreting the poses. *Optional*

**Geometrys**: The collision geometries as a list associated with the object.

## Output Parameter

**CollisionObject**: A [moveit_msgs/CollisionObject](http://docs.ros.org/api/moveit_msgs/html/message) to add to the Planning Scene.

## Usage
