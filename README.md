# Course-Dependency-Graph

This repository automatically generates schedule dependency graphs (Flowchart for what courses are prerequisite to others) for all majors offered at UC Irvine.

There are two main parts to this project:

* Data Collection
* Graph Creation

Data Collection consists of a web crawler navigating the UCI catalogue and creating a dictionary of each class and its list of prerequisites.

Graph Creation consists of the creation of the data structure to model the dependency graph. Also makes use of the library networkx to create visualizations for the graphs.


Possible Expansion:
Rewrite the graph visualization in d3.js using force directed graph. Electrostatic force will push nodes apart and edges will act as springs that pull them together. This will make the graph layout much nicer and also adds opportunities for interactive visualization.
