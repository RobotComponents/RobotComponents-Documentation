---
layout: default
title: Action Wait for Digital Input
nav_order: 1
parent: Code Generation
grand_parent: Robot Components Categories
has_toc: false
---

# **{{page.title}}**

## **Description**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** This component defines an instruction to wait for the signal of a Digital Input from the robot controller in RAPID main code generation.

## **Input Parameters**

**Digital Input Name (N):** Defines the name of the digital input based on a string value.

**State (S):** Defines the state of the digital input that should be waited for.

## **Output Parameters**

**Wait for Digital Input (WDI):** Contains the instruction to wait for the signal of a defined digital input from the robot controller as an Action for RAPID main code generation.

## **Menu Items**

Through the right-click menu of the component the following options are available:

**Documentation:** Opens the documentation page of the component in your browser.

## **Usage**

[**Code Generation**]({{ site.baseurl }}{% link docs/Robot Components/Code Generation/index.md %})**:** Plug the Digital Output output of this component into the Actions input of a RAPID Generator component to add a single instruction that waits for the signal of a defined digital input from the robot controller in the RAPID main code.