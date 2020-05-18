---
layout: default
title: Collision Object From Geometry
nav_order: 0
parent: MoveIt Utilities
grand_parent: Batagur Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**MoveIt Utilities**]({{ site.baseurl }}{% link docs/Batagur/Categories/MoveIt Utilities/MoveIt Utilities.md %})**:** Generates a [moveit_msgs/CollisionObject](http://docs.ros.org/api/moveit_msgs/html/msg/CollisionObject.html) message from Rhino Geometry.

## **Input Parameters**

**ID:** The unique identivier of the object (name used in MoveIt).

**Header:** A [std_msgs/Header](docs.ros.org/api/std_msgs/html/msg/Header.html) message used for interpreting the poses. *Optional*

**Geometrys:** The collision geometries as a list associated with the object.

## # **{{page.title}}**Output Parameters**

**CollisionObject:** A [moveit_msgs/CollisionObject](http://docs.ros.org/api/moveit_msgs/html/message) to add to the Planning Scene.

## **Usage**
