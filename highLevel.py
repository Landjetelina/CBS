import sys, os
from functools import total_ordering
import heapq as hp
from itertools import combinations
from lowLevel import Constraint

sys.path.append(os.path.join(os.getcwd(), 'low_level'))
import grid as grd
import lowLevel


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
        while open_nodes_hp:
            curr_node = open_nodes_hp.pop(0)
            dict_of_path_sets = dict()
            for agent, path in curr_node.sol_dict.items():
                if path:
                    dict_of_path_sets[agent] = set(path)
            agents_list = list(dict_of_path_sets.keys())

            found_conflict = False
            for a1, a2 in combinations(agents_list, 2):
                path_set1, path_set2 = dict_of_path_sets[a1], dict_of_path_sets[a2]
                v_confls = path_set1 & path_set2   # vertex conflicts
                swap_confl_left, swap_confl_right = None, None
                if not v_confls:
                    # no vertex conflict detected, checks swap conflict
                    path_list1 = sorted(list(path_set1), key=lambda x: x[1])
                    path_list2 = sorted(list(path_set2), key=lambda x: x[1])
                    for i in range(len(path_list1)-1):
                        if len(path_list2)-1 == i:  # path2 is shorter than path1, we got to an end and found no conflicts
                            break
                        start_p1, next_p1 = path_list1[i], path_list1[i+1]
                        start_p2, next_p2 = path_list2[i], path_list2[i+1]
                        if start_p1[0] == next_p2[0] and next_p1[0] == start_p2[0]:
                            swap_confl_left = next_p1
                            swap_confl_right = next_p2
                            break
                    if not swap_confl_left and not swap_confl_right:
                        continue
                found_conflict = True
                curr_node.left_child, curr_node.right_child = Node(), Node()

                if v_confls:
                    v_confl = list(v_confls)[0]
                    curr_node.left_child.constraint_set = curr_node.constraint_set | {Constraint(a1, *v_confl)}
                    curr_node.right_child.constraint_set = curr_node.constraint_set | {Constraint(a2, *v_confl)}
                else:
                    curr_node.left_child.constraint_set = curr_node.constraint_set | {Constraint(a1, *swap_confl_left)}
                    curr_node.right_child.constraint_set = curr_node.constraint_set | {Constraint(a2, *swap_confl_right)}

                curr_node.left_child.sol_dict = {a: path for a, points in self.agent_dict.items()
                                        if (path := self.low_level.return_path(*points, curr_node.left_child.constraint_set, a))}
                hp.heappush(open_nodes_hp, curr_node.left_child)

                curr_node.right_child.sol_dict = {a: path for a, points in self.agent_dict.items()
                                        if (path := self.low_level.return_path(*points, curr_node.right_child.constraint_set, a))}
                hp.heappush(open_nodes_hp, curr_node.right_child)

            if not found_conflict and len(curr_node.sol_dict.values()) == len(self.agent_dict.values()):
                return curr_node.sol_dict
