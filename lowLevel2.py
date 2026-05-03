from copy import deepcopy
import heapq
import math

import sys

from grid2 import *
from sortedcontainers import SortedList


class LowLevel:
    def __init__(self, grid: Grid, start_point, end_point):
        self.grid = grid
        self.start_point: Node = start_point
        self.end_point: Node = end_point

        self._nodes_expanded = 0
        # self._visited_nodes = {self.start_point: 0}

    def heuristic_fn(self, node: Node):  # Manhattan distance
        value = abs(self.end_point.row - node.row) + abs(self.end_point.col - node.col)
        # if node in self._visited_nodes:
        #     value *= 10**self._visited_nodes[node]
        return value

    def a_star(self):
        # [0] is total cost + heuristic, [1] is Node, [2] is total cost, [3] is list that contains parent node
        curr_node: list[Node | int | None] = [self.heuristic_fn(self.start_point), self.start_point, 0, None]
        open_nodes, closed_nodes = [], SortedList()
        while True:
            self._nodes_expanded += 1
            # if curr_node[1] in self._visited_nodes:
            #     self._visited_nodes[curr_node[1]] += 1
            # else:
            #     self._visited_nodes[curr_node[1]] = 1
            closed_nodes.add(curr_node[1])
            neighbours = self.grid.get_neighbours(curr_node[1])
            new_nodes = []
            for neighbour_node in neighbours:
                if neighbour_node in closed_nodes:
                    continue
                cost = self.grid.flat_tree_list[neighbour_node.row][neighbour_node.col]
                heapq.heappush(new_nodes, [self.heuristic_fn(neighbour_node) + curr_node[2] + cost,
                                neighbour_node, curr_node[2] + cost, curr_node])
            for node in new_nodes:
                heapq.heappush(open_nodes, node)
            try:
                next_node: list[Node | int | None] = heapq.heappop(open_nodes)
            except Exception:
                print('Nema rješenja!')
                sys.exit(1)
            if next_node[1] == self.end_point:
                return next_node
            curr_node = next_node

    def return_path(self):
        solution = self.a_star()
        curr_node = solution
        path = []
        while curr_node is not None:
            path.append(str(curr_node[1]))  # node je na indexu 1
            curr_node = curr_node[3]
        path.reverse()
        string = " --> ".join(path)
        return f'Total cost: {solution[2]}\nNodes expanded: {self._nodes_expanded}\n{string}'