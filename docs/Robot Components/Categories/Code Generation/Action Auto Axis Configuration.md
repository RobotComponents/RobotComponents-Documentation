---
layout: default
title: Action Auto Axis Configuration
nav_order: 8
parent: Code Generation
grand_parent: RC Categories
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): Defines an instruction to set the axis configuration of the robot automatically in RAPID main code generation.

## Input Parameter

**is Active**: Defines if the axis configuration of the robot is set automatically based on a boolean value.

## Output Parameter

**Auto Axis Config**: Contains an instruction to sets or unset the auto axis configuration for the robot as an Action for RAPID main code generation.

## Usage

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/Code Generation.md %}): Plug the Auto Axis Config output of this component into the Actions input of the RAPID Generator component to define an instruction that sets or unsets the auto axis configuration for the robot in RAPID main code.