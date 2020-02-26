---
layout: strategy
title: Afrofuturism
team: Dario Corral, Natalia Kopeikina & Subhashree Nath
video: https://vimeo.com/383250413
---

#### Concept

The studio objective was to “create an adaptable model for the self-sufficient and livable rural town”, where the goals to achieve were:

+ Food Sovereignty
+ Resource-efficient water and waste-water infrastructure
+ Integrating renewable energy system
+ Attractive town where people want to move to and stay
+ Vibrant public spaces for fostering social interaction and integration
+ Healthy town encouraging non-motorized traffic, integrating nature and alleviating pollution 

The main aim of the studio was to develop an adaptable and flexible spatial planning strategy that can be used to develop the different rural areas in Ethiopia, as is the agenda mentioned in Ethiopia’s Growth Transformation Plan II.

The design part of the project is preceded by a thorough study of two Ethiopian rural settlements, Olomkomi, and Addis Alem, as well as two Thuringia rural settlements: Hilburbhausen and Zella-Mehlis. This helped develop a sense of social context for which we are designing and the infrastructural upgrades foreseeable from the Northern counterparts in Thuringia. The spatial modeling and growth analysis has been done with parametric urban development analysis and simulations, through Rhino and Grasshopper.

To provide a contextual basis, the town of Wurer was selected where the designed development strategy was to be tested. The following sections present the contextual analysis and the derivation of the specific goals based on it.

#### Process

Post contextual analysis and development of design guidelines and goals, implementation of design
included the following five main steps, which used Grasshopper and C# script:

+ Street network development
+ Developing tool for parcellation of land according to different diet scenarios
+ Developing Accessibility tool for function distribution
+ Growth simulation of the urban system
+ Visualization of results

**Street Network Development**
As revealed in the topography and water analysis of Wurer, the residential plateaus and the existing street network, correspond to water movement. This gave us a cue to use the Water Flow Analysis for developing the street network system. According to that analysis, we proposed the street network that will expand as the population grows from 2000 to 10,000 people. As mentioned earlier, the design considers a majorly pedestrian street network with Emergency Vehicular Access and only a few selected streets are for motorised vehicular access. This street network forms the basis for the street network centrality and accessibility analysis, which along with the accessibility tool, helps in population and functional distribution.

**Developing Plot Parcellation Tool**
The next major step in developing the initial growth scenario of 2000 was the densification of existing residential areas within the plateaus. This is one of the land management strategy, where land usage is first maximized in the already developed residential areas and once it reaches its optimum capacity, only then new land is occupied.
The plot sizes for land redistribution is based on diet choice. Considering the balanced option of Mixed Diet involving both plant and meat consumption, it was decided to divide the residential plateaus into plots of sizes between 0.5 -0.7 ha. The snippet tool, Divde by Area based equal plot division algorithm, developed was used to achieve this.
Along with the manual selection of most populated existing settlemet, results from Centrality and Accessibility Analysis helped in selecting the residential plateaus to develop first.

**Developing Accessibility Tool**
It is established that pedestrian accessibility is one of the key aspects of successful cities. Hence, a principle of function distribution was developed according to the daily, weekly or monthly accessibility requirements. This was respectively translated to radii of 400, 800, 1200; which is equal to 5, 10- and 15-minutes walking distance.
Applying the Accessibility Tool:
+ Select the residential plateaus parcellated in Section 3.2 and from each land plot offset circles of radius 400m for functions required daily.
+ Zone where most of the radii intersect gives us the most accessible location to assign functions. This will be referred to as the “Popularity Factor”, which is also used as a criterion for growth simulations.
+ The steps are repeated for circles of radii 800m and 1200m.

**Growth Simulation**
As the studio brief required us to design a flexible system which can adapt to the growing population without losing on the initially planned characteristics, a C# code was developed which simulated the growth of the urban system as the population grows from 2000 and eventually, stops at 10,000. Three principles of growth were established related to the growing population: agriculture, social facilities, and agro-processing units. A relation between these was developed such that a change in the population input would cause the town to grow further. The relation used was population attract agriculture and social facilities, but the industry is located on
the places with the least population outside of the development area. 

**Visualisation**
Based on the above steps, plans are generated which show the correlation between attractively and functional distribution. Thus, a code was developed to describe the proportional distribution of each function in every land plot and stimulate its growth.