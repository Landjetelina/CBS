from low_level import createMaze, grid, lowLevel
from typing import NamedTuple
from sortedcontainers import SortedList

class Colision(NamedTuple):
    a1: str  # agent 1
    a2: str  # agent 2
    v: grid.Node  # vertex
    t: int  # time
class Conflict(NamedTuple):
    a: str  # agent
    v: grid.Node
    t: int

class Node:
    def __init__(self, constraint_list, sol_dict):
        pass

class ConstraintTree:
    def __init__(self):
        pass