---
layout: module
title: Line Segment Network Analysis
image: line-segment-network-analysis-1.png
summary: This module is mainly used for street analysis, since streets can be divided into line segments. They serve as the main connection between places of cities. Some emerged from natural movement patterns, others are imposed constructions such as the Manhattan grid. Similar to human relations, where some persons have more contacts than others, street segments are differently integrated in the street system. They can be analysed through network theories such as i.e. Space Syntax. The more connections a street segment has the higher the chances for more activities on it, since more people might take this path. With different analysis settings it is possible to recognise main transportation arteries, public meeting points or remote areas.
---

## Setup

* **Segment Network**

  To analyse segment networks, they need to be available as line drawings with lines and each line connecting to at least one other line of the network. In Space Syntax i.e. street networks are analysed by drawing Axial maps. Since streets are not always straight, axial maps try to simplify them by drawing the longest possible axis onto a street segment. All axes together form the Axial map. Streets available through resources such as OpenStreetMap are not axial maps and might not serve as a useable base for good analysis.
  (The DeCodingSpaces Toolbox provides utilities to create simplified maps of segment networks)

* **Segment Weighting**

  Not every segment has the same properties. Segments have different lengths. It is a factor that influences how long travelling takes. Furthermore, in Space Syntax research on street networks the angle between segments is considered, since people tend to take straight paths instead of walking around corners. If one walks on a perfect grid from the point north-east towards south-west, one might rather take straight paths than always turning corners.
  Additionally cyclists or pedestrians prefer other streets than car drivers, sometimes looking for more attractive paths or safer roads. Or streets at point of interest are used more frequently. Segments with good properties can, therefore, get additional positive weights.

* **Origin and Destination**

  Navigation systems recommend us the shortest, most economic or fastest path from one point to another. This shortest path calculation is commonly used and only needs one origin and one destination. By analysing a whole segment network it is furthermore interesting to run this calculation from one origin to all other possible destinations in a predefined **radius** and even from all possible origins to all other destinations. This gives additional insights on the characteristics of a segment network.

## Application

* **Shortest Path**

  Commonly used calculation to find best path between two points, depending on the segment weighting. One possible use case could be the fastest way from a water tank towards a tap.

* **Transportation arteries**

  Betweenness centrality is a calculation method in network theories that quantifies the number of times a street segment is taken along the shortest path between two other street segments [Street Analysis - Movement Through](). By analysing the street network with this method for all origins and destinations within a radius, main transportation routes become visible. The radius influences which mode of transportation is visible. Pedestrians walk rather short distances, a radius of 400m might be suitable. Cyclists take longer distances such as 700m. Car owners can have no limit in radius and the results might show highways as arteries.

* **Activity hotspots**

  Closeness centrality is a calculation method in network theories that is the average length of the shortest path from one street segment to all other segments in the network. Thus the more central a segment is, the closer it is to all other nodes. The analysis allows to trace specific hotspots of a city [Street Analysis - Movement To](). These segments are most probably more frequently visited and therefore more active.

* **Combination with segment generation**

  Besides analysing existing street networks, the analysis can be combined with generative street networks. It allows to measure the performance of different generated scenarios as well as assists in assigning land uses along the streets. For example, well integrated street segments might server better for commercial purposes.

## Limitations

* Imprecisions in line drawings lead to failures in calculations.

* For street networks, a thorough analysis needs a good base drawing including bridges and tunnels.

* Choosing a too small frame of analysis might lead to wrong conclusions of an area. A thumb rule is, to draw double the size of an analysed area.

* Field research might show other results than desk analysis has shown. It is recommended to have a degree of distrust on the results and get to know the analysis methods in more depth.

* Additional criteria such as temporary and permanent point of interests, quality of streets and others influence the use of streets. Human activities are defined through more aspects than streets, such as dynamic internet communication, which can lead to unexpected overuse of street segments, too.
