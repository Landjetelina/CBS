# Implementation of Conflict Based Search (CBS) algorithm for Multi Agent Path Finding (MAPF) problem

## CBS Algorithm
CBS is an algorithm that works on two levels, high level and low level. Low level finds individual solution for each agent with A* algorithm using Manhattan heuristic function. High level detects possible collisions and creates a constraint tree which is responsible for avoiding collisions. 
