---
layout: strategy
title: Resourcity
team: Bitar Julien, Constien Anja & Elshani Diellza
video: https://vimeo.com/383250024
---

#### Concept

Ethiopia´s population is growing in a very fast pace (National Planning Commission, 2016). Many people want to live in the cities to step into the modern life. All these people need resources to survive. The concept of the Resourcity – metabolism city for Ethiopia deals with the challenge on how to keep the people next to their resources while at the same time connect them to the modern society with an ‘urbanised live-style’ with technological and educational facilities. This adaptation should empower the Ethiopian culture and the circumstances of the current city but also serve as a living proof of integrating the usage of resources, education and technologies in a metabolistic, (self-sufficient) and sustainable way. The city is designed with parametric design methods. The programs allow simulate three different scenarios as an output. For each scenario further are simulated three growth stages (+2/5/10.000) inhabitants.

#### Process

Our whole planning-strategy is based on an iterative process where one step is decided but after further planning steps can be re-decided. To find out what might be the best strategy to apply a concept to a site, the site first has to be analysed. Elements of the analysis are the topography, the existing land-uses and the street-network. To have a framed extend of the site we first selected a centre point of the existing settlement and from that centre-point created a radius to have a border of the site. In this radius we could reveal the strategy for the site. The strategy used for the Resourcity starts with revealing the potential resources of the place. The spatial definition of the resources is the pull factor for the new settlers in the town, which will have the biggest impact to the urban form and its gradual development.

Firstly to define the boundary and location of these resources, water was considered as a supporting factor and a resource in itself. We analysed the rain water streams in the 5 km radius and have located the points where water will be naturally collected. The rainwater collection ponds were simulated through topography analysis. Out of all points, the ones which collect water the most, without disturbing existing settlements were used as water ponds for the natural resources. This information lead to the definition of the location of the resources and their boundary.
Having located the natural water ponds, we forecasted a certain area of three resources covering the needs of the 10. 000 population scenario. This should ensure that all resources have quick and efficient access to water, leading to a self-sufficient city in terms of resources.

The final resource areas were defined after some modifications, based on the topography, street network as well as existing settlements.

In regards to the street network, our approach was based on conserving the existing structure, and so we followed the pattern of the current streets while optimizing it, not only for the future settlers, but for the most efficient way of resources transportation as well.

The landuse-distribution was based on different scenarios of the priorisation of the people towards different resources. Different groups of interest were allocated to the city by an urban generative model which takes into consideration the street network accessibility.With C#, a scripting language in Grasshopper for Rhino the basic land uses such as housing, public facilities, mixed use and processing units were simulated.

After subtracting the resource surfaces from the whole surface, we subtracted the existing settlements too, since another Grasshopper definition was used to densify them.

People and functions were distributed using an attracitivy map as a tool. The first attractivity map – in order to place 1000 people; was created by taking into consideration the distance of a plot to the existing settlement and the resource.

Afterwards, there were defined four profiles of groups of people with different interests in resources.

Group A is oriented more in Agroforestry
Group B is oriented in Industry
Group C in Agriculture
Group D is interested equally in every resource.

In addition, all the groups are tended to locate near the existing settlements too.
In the next iterations, despite housing; public facilities, mixed use, and processing units were added which were also considered as attractors and resources for new comers.

As a next step the street network was adapted. The city-blocks were automatically created by the street-network. The structure was evaluated in between and eventually was adapted. The same Grasshopper definition helped us to show the growth of the city.

After distributing a certain number of housing, facilities and treatment blocks the loop was stopped to see the growing stages of the Resourcity.