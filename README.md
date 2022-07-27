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

Smart cities more than ever have many, devices that are connected to the internet to improve citizen's quality of life. Through all of these devices being connected to internet is going to soak up the city's bandwith and result in slower or non working speeds. While this itself could possibly work as we expand our network and greater capacity for devices the introduction of a smart city would make this impossible. A smart city has features to collect and spread information, which will enhance the lives of residents. Some of the devices that are connected within smart cities are a real time tracking locator for buses and train stations, cleaning robots(roombas), map kiosks, trash cans, etc. With all of these devices on the same wifi networks, the network is going to be inefficient and hardly worth using. Since much of the data that is being transported is time sensitive and high priority, this will result in time inefficient data. For this project, we propose for low priority data to be transported through the general public's devices bluetooth and local network. This low priority data would be sent and collected through devices moving throughout the city. We will be using the General Conv type of General Neural Networks to figure out the best way to transform data by bus routes and pedestrians throughout all of the devices within a smart city.



##
For example, a person that is nearby a sensor that is collecting data would then pick up that data unknowningly through their daily routine and through their daily routines drop off that data at gateway that will then upload the data to the cloud.
<!--
Give a short description on what your project accomplishes and what tools is uses. In addition, you can drop screenshots directly into your README file to add them to your README. Take these from your presentations.
-->

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
