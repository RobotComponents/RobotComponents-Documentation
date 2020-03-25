---
layout: default
title: Action Digital Input
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

## Description

[Code Generation]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): This component defines an instruction to wait for the signal of a Digital Input from the robot controller in RAPID main code generation.

## Input Parameter

**DI Name**: Defines the name of the digital input based on a string value.

**State**: Defines the state of the digital input that should be waited for.

## Output Parameter

**Wait DI**: Contains the instruction to wait for the signal of a defined digital input from the robot controller as an Action for RAPID main code generation.

## Usage

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Categories/Code Generation/index.md %}): Plug the Digital Output output of this component into the Actions input of a RAPID Generator component to add a single instruction that waits for the signal of a defined digital input from the robot controller in the RAPID main code.