# Implementation of Conflict Based Search (CBS) algorithm for Multi Agent Path Finding (MAPF) problem

## CBS Algorithm
CBS is an algorithm that works on two levels, high level and low level. Low level finds individual solution for each agent with A* algorithm using Manhattan heuristic function. High level detects possible collisions and creates a constraint tree which is responsible for avoiding collisions. <br>
## Files
*`lowLevel.py` - contains logic responsible for implementation of low-level part of the algorithm, implements A\* algorithm and returns path from start point to the end point that is found
*`highLevel.py` - class `ConstraintTree` inside this file calls low-level with generated constraints and searches for non-collision solution
*`grid.py` - object oriented class that handles generation of the map and enables finding neighbouring nodes
*`testExamples.py` - list of 9 pre-made test examples, user can easily use one of those and don't have to create its own 
*`animate.py` - responsible for creating user-friendly GUI that shows animated paths of agents at each step
*`createMaze.oy` - contains utility functions that allow easier creation of a maze
*`main.py` - main program that starts the CBS algorithm
