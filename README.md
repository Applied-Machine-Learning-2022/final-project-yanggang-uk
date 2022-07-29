[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8127851&assignment_repo_type=AssignmentRepo)
<!--
Name of your teams' final project
-->
# snap-that-cat
## [National Action Council for Minorities in Engineering(NACME)](https://www.nacme.org) Google Applied Machine Learning Intensive (AMLI) at the `University_of_Kentucky`

<!--
List all of the members who developed the project and
link to each members respective GitHub profile
-->
Developed by:
- [Jeffery Millan](https://github.com/jmillan736) - `University_of_California_Berkeley`
- [Bria Reed](https://github.com/briareed47) - `Cornell_University`
- [Jose Salazar](https://github.com/JSalazar026) - `University_of_California_San_Diego`
- [Brenton Figures-Mormon](https://github.com/SkullNightMegaFan) - `George_Mason_University`


## Description
Problem: Trying to solve network congestion in smart cities

Smart cities more than ever have many, devices that are connected to the internet to improve citizen's quality of life. Through all of these devices being connected to internet is going to soak up the city's bandwith and result in slower or non working speeds. For example, a person that is nearby a sensor that is collecting data would then pick up that data unknowningly through their daily routine and through their daily routines drop off that data at gateway that will then upload the data to the cloud. While this itself could possibly work as we expand our network and greater capacity for devices the introduction of a smart city would make this impossible. A smart city has features to collect and spread information, which will enhance the lives of residents. Some of the devices that are connected within smart cities are a real time tracking locator for buses and train stations, cleaning robots(roombas), map kiosks, trash cans, etc. With all of these devices on the same wifi networks, the network is going to be inefficient and hardly worth using. Since much of the data that is being transported is time sensitive and high priority, this will result in time inefficient data. For this project, we propose for low priority data to be transported through the general public's devices bluetooth and local network. This low priority data would be sent and collected through devices moving throughout the city. We will be using the General Conv type of General Neural Networks to figure out the best way to transform data by bus routes and pedestrians throughout all of the devices within a smart city.

## Usage instructions
1. Import the imgkit package (https://pypi.org/project/imgkit/)
2. Import the chromedriver package (https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver)
3. Install networkx
4. Install peartree
5. Install osmnx
6. Install numpy
7. Install random
8. Install folium==0.11.0
9. Install imgkit==1.0.2
10. Install selenium==3.141.0

##Summary of Tools
We used pytorch to turn the end result data that was in Dr.Baker and his cohorts model. We transformed the data from a networks.multigraph object into a torch_geometric.data.Data object. This was done so we could pass the data into a suitable format for our GNN. See below for more detail about the torch_geometric object.
https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html

Our usage of Graphical Neural Networks was due to us using the prevoius iteration of this research project's data points. We used a torch_geometric.data.Data object as we were dealing with scalars points on a geographical points. The last paper created graph nodes of the optimal gateway placement. Using this data, we wanted to then find a target metric of 90% coverage for the city of Louisville.


https://ieeexplore.ieee.org/abstract/document/9415579?casa_token=meb9lMbqx_kAAAAA:OeLaM7aHmm6AiqqnrKZ6-a--7juGicj7rm0DD3oCQHv5HhvOE9ktgN3rf_kndmICu55Tv0Jy6Yw

Our Power Point Presentation of our work. 
https://docs.google.com/presentation/d/1pRuu5iETSQJIYwGXK6PNHz9Pci0nvsP35FzWiCAXKoQ/edit#slide=id.p
Below will be the speaker notes that add some additional perspective on the project. 

"The internet is a wonderful and amazing thing that allows us to connect to each other from thousands of miles away. Of course, we all know how annoying it is to be disconnected from the internet. Now most of the time maybe you just need to reset your router or maybe disconnect from the network. 
These aren’t the situations that we’re aiming to solve. If you have ever been to a packed sports game or in the middle of a super busy city like New York you’ll know that sometimes you may run into network congestion. Which is a really academic way of saying that too many people are using the network at the same time." 

Smart cities are normal cities that use internet of things devices think of cleaning devices, map kiosks, and even your real time bus tracker to help make you and I’s life easier. Additionally, smart cities use many sensors and gateways to help manage the abundance of data that is tracked by a living breathing city

"According to the United Nations World Urbanization Prospects report that 55% of the world lives in urban areas and 68% of the world’s population by 2050. That’s well within our lifetime, folks. We are not just looking at a problem that can happen, one that very may well be if we are not proactive about it."

"Basically now smart devices around the city such as kiosk don't need to send information from the cloud every minute and can route information to buses that send that information to gateways relieving stress on the network and prioritizing other information"

"So how do graphs come into play for our machine learning model? We’ve seen multiple different neural networks take in different types of inputs in this class: We saw convolutional neural networks take in images, neural networks that just take in DataFrames, but never have we seen them take a graph as input. How is our ML model going to process a graph? Well, we make use of specialized neural networks, called graph neural networks. Graph neural networks take in graphs as an input, and trains and makes predictions based off of the information found in the nodes and edges of the graph. Graph neural networks can make three types of predictions: they can make node-level predictions, where graphs will make predictions about a specific node or object in the graph based on the surrounding nodes and edges, they can make edge-level predictions, where graphs will make predictions about the type of relationship between two objects in a graph, or they can make graph level predictions, where it predicts something about the entire graph. In our specific use-case, we want to make a node level prediction to determine how many gateways we want to have in the city, and where we want them."

"In our project we mentioned the ability to route data from device to device. Think of point of interest as essentially hot spots that have frequent or high amounts of traffic on regular intervals. A wonderful example of this would be your local Starbucks where it’s always frantic during the morning rush. Now point of interest can also include one time events that have huge amounts of traffic like a sports game, music concerts or even a pokemon go raid. These places events are important as they drastically change the routes and ability to route data. If you have a 30,000 people at a concert Saturday night that’s going to affect our ability to route data through users resulting in a less effective data delivery."

