# Course-Dependency-Graph

This repository automatically generates schedule dependency graphs (Flowchart for what courses are prerequisite to others) for all majors offered at UC Irvine.

There are two main parts to this project:

* Data Collection
* Graph Creation

Data Collection consists of a web crawler navigating the UCI catalogue and creating a dictionary of each class and its list of prerequisites.

Graph Creation consists of the creation of the data structure to model the dependency graph. Also makes use of the library networkx to create visualizations for the graphs.
