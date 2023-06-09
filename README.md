# Directed Weighted Graph python (Ex3)

## **Motivation:**
At this assignment we were asked to Implement data structures of directed and weighted graphs in python language.
In the previous assigment we used Java launguage and now we using python language in order to compare results and performance between this two launguage.

* For more details and results of the comparison 
[click here](https://github.com/JosefMamo12/Ex3/wiki/Comparison).

Therefore we build function based on algorithms like - **isConnected**, **tsp**, **shortest path**(returns list of the route),**shortest path distance**(returns the length in double) and **centner** who based on algorithms like **Dijkstra** and **DFS**.

At this assignment we used **dicitionary as data structures**, in order to handle the vertice of the graph. And we added nested dictionary to handle the edges of the graph.

The motivation to use this data structures was because its unordered collection, changeable and do not allow duplicates. but mainly because its based on HashMap (who used in our code in Java) who can search elemnts in **complexity of O(1)** by using key and value. 

## Project Structure

**NodeData** - Simple class to define a node in the graph object.

**DiGraph** - Main class of the directed weighted graph object which implement the GraphInterface interface

**GraphAlgo** - Main graph which implements GraphAlgoInterface where we implement all algorithms that we can use on the graph.

**GraphDraw** - Using pygame to show the graphic of the graph.

**Tests** - Check out two main classes (DiGraph, GraphAlgo)

* you can find more details of the functions [here](https://github.com/JosefMamo12/Ex3/wiki/Classes).

## GUI
![](https://github.com/JosefMamo12/Ex3/blob/master/Images/gui%20exsplanation.jpeg)
