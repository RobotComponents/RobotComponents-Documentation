---
layout: strategy
title: Radius City
team: Ayah Al-Sabbagh, Bastiaan Woudenberg & Xuanyu Li
video: https://vimeo.com/281793824
---

#### Concept

In this project, our group took the challenge to create a framework for a future city in Ethiopia which roughly fits 10.000 people. We approached this challenge with the idea of designing a radial city that could improve certain factors which are currently disregarded in the present urban situation in Ethiopia. The main focus in this project lies on what we call ‘justified urbanization’. This is an idea that takes into consideration that when you consume agricultural land you have to increase the efficiency of the remaining land to keep demand and supply balanced.

#### Process

RADIUS is a widely adaptable model which could be adapted into different geographical situations and social environments. However when applying RADIUS, one should adapt it to the surroundings and regard the local qualities when developing.

The model simulates the development and includes certain parameters that predict different final outcomes according to different pull factors. According to these pull factors we shaped different scenarios and benchmarked the different metabolisms on their performance in different aspects. Which scenario has the best performance if it comes down to gathering rainwater and how is the ratio agriculture area/residential area? Which scenario performs best in limiting the needed water infrastructure?

To start using the model you need to analyse the surroundings and define small streets and pathways. Following this the software Grasshopper creates the city but it needs you to follow the next five steps:

1. Decide where to place your centre point, which should be set on the best possible location. This location can be a combination between different factors. First off it is important to define the highest elevation areas of the surroundings. If these high elevated areas contain an intersection between two existing road structures then the centre point should be placed on this location. In case there is no existing intersection then place the point can either be placed on the highest elevated point of the main road where the distance to a nearby water body is the smallest. Finally, it there are no water bodies in the direct environment than simply place the point on the highest elevated point of the main road.
2. Decide on the placement of your catchment areas. It is important that they are located on the point where they gather the highest amount of rainwater. Also think about the size your rainwater reservoir needs to be to house the needed amount of water.
3. Define the centre area size. This depends on the amenities which it needs to facilitate which again depends on the amount of people the city needs to house.
4. Define the depth you want your street blocks to be and define which range your plot sizes should be. Consider that the maximum size of a privately owned plot is 250 m2.
5. Decide which density each tier should have depending on which phase they are in. The range can be based on various considerations but should at least differ enough per tier to create spatial contrast between the tiers.
6. Put in your pull factors to simulate the possible growth of your city and create different growth scenarios.

Following these steps the Grasshopper model will do the rest. It will create the street network by connecting the existing streets and pathways with the centre area in the shortest way possible thus creating the radials of the city. Then it creates secondary streets by offsetting lines with a fixed difference from the centre area which extend perpendicular along the radial streets and connect when they meet with the perpendicular line from the opposite radial. Then it will create street blocks by offsetting the street network. Next, it will fill the street blocks with the manual defined plot sizes and enclose them with a backroad. Finally it will simulate the growth by creating buildings which are randomly placed on the plot but don´t intersect with the core sanitation unit.
When applying the radial city model to Wurer, there are certain specific elements which have to be regarded. Especially the surrounding existing residential strips which are, like small islands, embedded in their surroundings. These strips form little green oases and are considered as areas of great quality and therefore should be preserved. The model therefore takes these strips in consideration and integrates them by adapting the street network to their boundaries.