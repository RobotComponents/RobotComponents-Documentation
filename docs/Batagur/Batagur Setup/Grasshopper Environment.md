---
layout: default
title: Grasshopper Environment
nav_order: 2
parent: Batagur Setup
has_toc: false
---

## Bengesht WebSocket communication
For setting up communication between Grasshopper and ROS we use rosbridge on the ROS side and Batagur on the Grasshopper side.<br/>
[Bengesht](https://github.com/behrooz-tahanzadeh/Bengesht){:target="_blank"} is a open-source Grasshopper addin by Behrooz Tahanzadeh.
One of its functionality is handle (send/receive) communication with a server over WebSocket protocol.<br/>
Simply download the .gha File from [Food4Rhino](https://www.food4rhino.com/app/bengesht){:target="_blank"} and install it as any other Grasshopper addin.

Furthermore, it is recommended getting the complementary Userobjects for Bengesht, called [ROS.GH](https://github.com/behrooz-tahanzadeh/ROS.GH){:target="_blank"}. ROS.GH is a set of the open-source parser and developed to simplify the generation of RosBridge messages.

A simple setup of Bengesht components can be seen in this picture below.<br/>
![bangasht setup]({{ site.baseurl }}/assets/images/Batagur/bengesht_connection_01.png){:class="img-responsive"}

The "subscriber" part of the definition consists out of a "WebSocket Client Start" and a "WebSocket Client Receiver" component. The Websocket ip-address and a port (default rosbridge post is 9090) need to be defined, as well as, an initial message stating the ROS-Topic to subscribe to. The "WebSocket Client Receiver" component then receives all the messages published at this topic and outputs it as a string in Grasshopper.

The "publisher" part of this example consists out of a "WebSocket Client Start" component and a "WebSocket Client Sender" component. The Sender takes the created WebSocket object and a string and publishes it.

That rosbridge works well, the messages have to follow the [rosbridge-protocol](https://github.com/RobotWebTools/rosbridge_suite/blob/develop/ROSBRIDGE_PROTOCOL.md){:target="_blank"}. ROS.GH helps with that.

## Batagur setup
For installing Batagur you [download](https://github.com/EDEK-UniKassel){:target="_blank"} the .gha and the associated .dll´s and drop that into your Grasshopper Libraries folder. The .ghuser files should be placed in the dedicated UserObjects folder.<br/>

## Usefull knowlage and tools
If you want to know more about what is going on with JSON. [This](https://www.json.org/json-en.html){:target="_blank"} might be useful.<br/>
For more convenience working in Grasshopper with JSON, there are useful addins, like [JSwan](https://www.food4rhino.com/app/jswan){:target="_blank"} and [ghJSON](https://mathrioshka.ru/ghjson){:target="_blank"} (both of them are opensource: [JSwan](https://github.com/Mathrioshka/ghJSON){:target="_blank"} / [ghJSON](https://github.com/andrewheumann/jswan){:target="_blank"}).