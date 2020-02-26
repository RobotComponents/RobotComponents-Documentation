---
layout: default
title: Action Timer
nav_order: 5
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): This component defines an instruction to wait a given amount of time between two other robot instructions in RAPID main code generation.

## Input Parameter

**Duration**: Defines the duration in seconds based on a double value.

## Output Parameter

**Timer**: Contains the wait instruction as an Action for RAPID main code generation.

## Usage

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): The Timer output of this component can be plugged into the Actions input of the RAPID Generator component to add a wait instruction in the RAPID main code that defines an amount of time until the next instruction is executed.