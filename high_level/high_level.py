import sys, os
from functools import total_ordering
import heapq as hp

sys.path.append(os.path.join(os.getcwd(), 'low_level'))

from low_level import createMaze, grid as grd, lowLevel
from typing import NamedTuple
from sortedcontainers import SortedList


class Constraint(NamedTuple):
    a: str  # agent
    v: grd.Node  # vertex
    t: int  # time


@total_ordering
class Node:
    # sol_dict = {agent: (path, total cost)}
    # sol_dict = {'a1': ([0,0, 0, 1,0, 1 ... 9,9, 18], 18),
    #             'a2': ([2,2, 0, 3,2, 1 ... 9,9, 14], 14)}
    def __init__(self, constraint_set: set[Constraint]=None, sol_dict: dict[str, list[tuple[grd.Node, int]]]=None, parent=None):
        self.constraint_set = constraint_set
        self.sol_dict = sol_dict
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def get_sic(self):
        return sum([item[1] for _, item in self.sol_dict.items()])

    def __lt__(self, other):
        return isinstance(other, Node) and self.get_sic() < other.get_sic()

class ConstraintTree:
    # agent_dict = {agent: (start Node, goal Node)}
    # agent_dict = {'a1': (0,0, 9,9),
    #               'a2': (2,2, 9,9)}
    def __init__(self, agent_dict: dict[str, tuple[Node,Node]], grid):
        self.root: Node = None
        self.agent_dict = agent_dict
        self.grid = grid


    def treeWalk(self):
        Node(set(), {agent: (path[0], path[1]) for agent, path in self.agent_dict.items()})
        open_nodes_hp: list[Node] = []
        hp.heappush(open_nodes_hp, self.root)
        while open_nodes_hp:
            curr_node = open_nodes_hp.pop(0)

            dict_of_path_sets = {agent: set(path) for agent, path in curr_node.sol_dict.items()}
            items = dict_of_path_sets.items()
            for a1, path_set1 in items:
                for a2, path_set2 in items:
                    conflicts = path_set1 & path_set2
                    if not conflicts:
                        return curr_node.sol_dict
                    conflicts = list(conflicts)[:2]

                    left_child, right_child = Node(), Node()
                    left_child.constraint_set = curr_node.constraint_set | Constraint(a1, grd.Node(conflicts[0]))
                    # left_child.sol_dict = c
                    # lowLevel.LowLevel())
