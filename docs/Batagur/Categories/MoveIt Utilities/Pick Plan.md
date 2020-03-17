---
layout: default
title: Pick Plan
nav_order: 1
parent: MoveIt Utilities
grand_parent: Batagur Categories
has_toc: false
---

## Description

[MoveIt Utilities]({{ site.baseurl }}{% link docs/Batagur/Categories/MoveIt Utilities/MoveIt Utilities.md %}): Composes a [moveit_msgs/PickupGoal](http://docs.ros.org/api/moveit_msgs/html/action/Pickup.html){:target="_blank"} message.<br/>
The PickupGoal is part of the [moveit_msgs/Pickup](http://docs.ros.org/api/moveit_msgs/html/action/Pickup.html){:target="_blank"} Action.

## Input Parameter

**TargetName**: The name of the object to pick up (as known in the planning scene).

**EndEffector**: Which end-effector to be used for pickup. (By defualt it is "gripper")

**GroupName**: Which group should be used to plan for pickup.

**Grasps**: A list of possible [moveit_msgs/Grasp](http://docs.ros.org/api/moveit_msgs/html/msg/Grasp.html){:target="_blank"} to be used.

## Output Parameter

**PickupGoal**: An action for picking up an object as [moveit_msgs/PickupGoal](http://docs.ros.org/api/moveit_msgs/html/action/Pickup.html){:target="_blank"} message. 

**PickupActionGoal**: An action for picking up an object as [moveit_msgs/PickupGoal](http://docs.ros.org/api/moveit_msgs/html/action/Pickup.html){:target="_blank"} message with Header. This message is ready to be published onto the MoveIt Pickup Action Goal Topic.

**Type**: The Type of the Message. This is always "moveit_msgs/PickupGoal".

## Menu Items

**Execute Motion**: Execute Motion will start moving the robot without any permission or confirmation. Don´t use that with any physical Robot!

## Usage
The Pick Plan component should be used if you are planning to robotically manipulate (Pick & Place) an object in space. The Pick movement is split by MoveIt into 3 parts, Pregrasp / Approach / Retreat. These movement steps are called trajectory stages


