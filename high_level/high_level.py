import sys, os
from functools import total_ordering
import heapq as hp
from itertools import combinations

from low_level.lowLevel import Constraint

sys.path.append(os.path.join(os.getcwd(), 'low_level'))

from low_level import createMaze, grid as grd, lowLevel

@total_ordering
class Node:
    # sol_dict = {agent: (path, total cost)}
    # sol_dict = {'a1': ([0,0, 0, 1,0, 1 ... 9,9, 18]),
    #             'a2': ([2,2, 0, 3,2, 1 ... 9,9, 14])}
    def __init__(self, constraint_set: set[Constraint]=None, sol_dict: dict[str, list[tuple[grd.Node, int]]]=None, parent=None):
        self.constraint_set = constraint_set
        self.sol_dict = sol_dict
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def get_sic(self):
        return sum([item[1][-1] for _, item in self.sol_dict.items()])

    def __lt__(self, other):
        return isinstance(other, Node) and self.get_sic() < other.get_sic()

class ConstraintTree:
    # agent_dict = {agent: (start Node, goal Node)}
    # agent_dict = {'a1': (0,0, 9,9),
    #               'a2': (2,2, 9,9)}
    def __init__(self, agent_dict: dict[str, tuple[Node,Node]], grid):
        self.root: Node = None
        self.agent_dict = agent_dict
        self.low_level = lowLevel.LowLevel(grid)


    def treeWalk(self):
        self.root = Node(set())
        self.root.sol_dict = {a:self.low_level.return_path(*points) for a, points in self.agent_dict.items()}
        open_nodes_hp: list[Node] = [self.root]
        solution = None
        while open_nodes_hp:
            curr_node = open_nodes_hp.pop(0)

            dict_of_path_sets = {agent: set(path) for agent, path in curr_node.sol_dict.items()}
            agents_list = list(dict_of_path_sets.keys())


            found_conflict = False
            for a1, a2 in combinations(agents_list, 2):
                path_set1, path_set2 = dict_of_path_sets[a1], dict_of_path_sets[a2]
                conflicts = path_set1 & path_set2
                if not conflicts:
                    continue
                found_conflict = True
                conflict = list(conflicts)[0]

                curr_node.left_child, curr_node.right_child = Node(), Node()
                curr_node.left_child.constraint_set = curr_node.constraint_set | {Constraint(a1, *conflict)}
                curr_node.left_child.sol_dict = {a: path
                                       for a, points in self.agent_dict.items()
                                        if (path := self.low_level.return_path(*points, curr_node.left_child.constraint_set, a))}
                hp.heappush(open_nodes_hp, curr_node.left_child)

                curr_node.right_child.constraint_set = curr_node.constraint_set | {Constraint(a2, *conflict)}
                curr_node.right_child.sol_dict = {a: path
                                       for a, points in self.agent_dict.items()
                                       if (path := self.low_level.return_path(*points, curr_node.right_child.constraint_set, a))}
                hp.heappush(open_nodes_hp, curr_node.right_child)
            if not found_conflict:
                # return curr_node.sol_dict
                solution = curr_node.sol_dict
        return solution
