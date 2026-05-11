import sys, os
from typing import NamedTuple


sys.path.append(os.path.join(os.getcwd(), 'low_level'))
from low_level.grid import *
from sortedcontainers import SortedList

class Constraint(NamedTuple):
    a: str  # agent
    v: Node  # vertex
    t: int  # time

class LowLevel:
    def __init__(self, grid: Grid):
        self.grid = grid

        self._nodes_expanded = 0


    def a_star(self, start_point, end_point, constraints=None, agent=None):
        def heuristic_fn(node: Node):  # Manhattan distance
            value = abs(end_point.row - node.row) + abs(end_point.col - node.col)
            return value

        # [0] g_n = total cost + heuristic, [1] is current node (Node), [2] is total cost, [3] is list that contains parent node
        curr_node: list[Node | int | None] = [0+heuristic_fn(start_point), start_point, 0, None]
        open_nodes_list, open_nodes_set, closed_nodes_set = SortedList(), set(), set()
        while True:
            self._nodes_expanded += 1
            closed_nodes_set.add(curr_node[1])
            # iterator that contains at most 5 neighbouring nodes (upper, left, itself, right, lower)
            neighbours = self.grid.get_neighbours(curr_node[1])
            new_nodes = []  # isn't neccessary, put for debugging purposes, neighbours could be appended directly to an open nodes list
            for neighbour_node in neighbours:
                if neighbour_node in closed_nodes_set: # node is already visited
                    continue
                cost = self.grid.flat_tree_list[neighbour_node.row][neighbour_node.col]
                total_cost = curr_node[2] + cost
                if constraints and Constraint(agent, neighbour_node, total_cost) in constraints:
                    continue
                # adds neighbouring node with additional info to heap. Node with the lowest g_n is on top of the heap
                # if two nodes have the same g_n, priority has the one with higher row rank, then higher column rank
                new_nodes.append([heuristic_fn(neighbour_node) + curr_node[2] + cost,
                                neighbour_node, total_cost, curr_node])
            for node in new_nodes:
                if node[1] not in open_nodes_set:
                    open_nodes_list.add(node)
                    open_nodes_set.add(node[1])
            if not open_nodes_list:  # if heap becomes empty, it means that we have visited every available node and couldn't find solution
                return None
            next_node = open_nodes_list.pop(0)
            if next_node[1] == end_point:  # checks if the goal is found
                return next_node
            curr_node = next_node

    # returns a solution of A*
    def return_path(self, start_node: Node, end_node: Node, constraints=None, agent=None):
        curr_node = self.a_star(start_node, end_node, constraints, agent)
        if not curr_node:
            return None
        path, total_cost = [], curr_node[2]
        while curr_node is not None:
            path.append((curr_node[1], curr_node[2]))  # node is at index 1, cost is at index 2
            curr_node = curr_node[3]  # next node is parent node
        path.reverse()  # path should be reversed in order to go from start to finish
        return path #, self._nodes_expanded

    @staticmethod
    def path2str(path, nodes_expanded=None):
        total_cost = path[-1][1]
        path = [f'{str(node[0])} {node[1]}' for node in path]
        str_path = " --> ".join(path)
        if total_cost:
            return f'Total cost: {total_cost}\nNodes expanded: {nodes_expanded}\n{str_path}'
        else:
            return str_path