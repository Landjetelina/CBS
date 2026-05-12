# Implementation of Conflict Based Search (CBS) algorithm for Multi Agent Path Finding (MAPF) problem

## CBS Algorithm
CBS is an algorithm that works on two levels, high level and low level. Low level finds individual solution for each agent with A* algorithm using Manhattan heuristic function. High level detects possible collisions and creates a constraint tree which is responsible for avoiding collisions. <br>
## Files
* `lowLevel.py` - contains logic responsible for implementation of low-level part of the algorithm, implements A\* algorithm and returns path from start point to the end point that is found 
* `highLevel.py` - class `ConstraintTree` inside this file calls low-level with generated constraints and searches for non-collision solution
* `grid.py` - object oriented class that handles generation of the map and enables finding neighbouring nodes
* `testExamples.py` - list of 9 pre-made test examples, user can easily use one of those and don't have to create its own 
* `animate.py` - responsible for creating user-friendly GUI that shows animated paths of agents at each step
* `createMaze.oy` - contains utility functions that allow easier creation of a maze
* `main.py` - main program that starts the CBS algorithm <br>
## Usage
1. Clone git repository
2. Create your own example inside `testExamples.py` or use one of the available
    
    <img width="427" height="95" alt="image" src="https://github.com/user-attachments/assets/1dec3a04-e406-459c-a9fa-b6a71e1ecea1" />
    <img width="515" height="155" alt="image" src="https://github.com/user-attachments/assets/bd4dbbd6-ba09-462b-a4bd-67651361f2af" />

3. Call function for creating an example in `main.py`

    <img width="326" height="193" alt="image" src="https://github.com/user-attachments/assets/0c5abfcf-4e3d-472e-b57e-1143bbe70386" />
## Results
Program outputs created grid, complete path and total cost for each agent. If there is no solution, program will throw an exception. For some examples algorithm needs too much time and the program won't finish. <br>  
### Example 2

<img width="586" height="483" alt="image" src="https://github.com/user-attachments/assets/5aac3f8b-9493-4a61-a9e4-b00c53bf2279" /><br>
*Solution of the example 2* <br>
<br>
Program also creates a GUI where agents are animated and user can view each step of the solution in discretisized moments. <br>
<br>
  <img width="677" height="659" alt="20260512-2049-22 7860119" src="https://github.com/user-attachments/assets/5f62abb1-6d9f-4000-ba36-895c41ff96d9" /><br>
*Animation of the example 2* <br>

### Example 1

  <img width="586" height="483" alt="image" src="https://github.com/user-attachments/assets/af12a601-5e43-4fe9-a1f8-11129b9fce55" /><br>
*Solution of the example 1* <br>

  <img width="677" height="659" alt="20260512-2055-33 7841748" src="https://github.com/user-attachments/assets/0fb58b06-ef09-42f5-8025-05ab5c0274b9" /><br>
*Animation of the example 1* <br>

### Example 6

  <img width="677" height="659" alt="20260512-2100-36 2960092 (2)" src="https://github.com/user-attachments/assets/64b6618c-bbaa-4a07-ba82-d6b53c657eaa" /><br>
*Animation of the example 6* <br>












   
