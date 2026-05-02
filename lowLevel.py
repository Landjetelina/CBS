from copy import deepcopy

import math

from grid import *

class LowLevel:
    def __init__(self, grid: Grid, start_point: Node, end_point: Node):
        self.grid = grid
        self.start_point: Node = self.grid.flat_tree_list[start_point.row][start_point.column]
        self.end_point: Node = self.grid.flat_tree_list[end_point.row][end_point.column]

        self.nodes_expanded = 0
        self.visited_nodes = {self.start_point: 0}

    def heuristic_fn(self, node: Node):  # Manhattan distance
        value = abs(self.end_point.row - node.row) + abs(self.end_point.column - node.column)
        if node in self.visited_nodes:
            value *= 10**self.visited_nodes[node]
        return value

    def a_star(self):
        open_nodes = []
        # [0] is Node, [1] is total cost, [2] is total cost + heuristic, [3] is list that contains parent node
        curr_node: list[Node | int | None] = [self.start_point, 0, self.heuristic_fn(self.start_point), None]
        while True:
            self.nodes_expanded += 1
            if curr_node[0] in self.visited_nodes:
                self.visited_nodes[curr_node[0]] += 1
            else:
                self.visited_nodes[curr_node[0]] = 0

            new_nodes = [[node, curr_node[1] + node.cost, self.heuristic_fn(node) + curr_node[1] + node.cost, curr_node]
                         for node in curr_node[0].neighbours]
            open_nodes.extend(new_nodes)
            open_nodes.sort(key=lambda x: (x[2], x[0]))
            next_node: list[Node | int | Node] = open_nodes.pop(0)
            if next_node[0] == self.end_point:
                return next_node
            curr_node = next_node

    def return_path(self):
        solution = self.a_star()
        curr_node = solution
        string = ''
        while curr_node[3] is not None:
            string += f'{str(curr_node[0])[::-1]} >-- '
            curr_node = curr_node[3]
        string += str(curr_node[0])
        return f'Total cost: {solution[1]}\nNodes expanded: {self.nodes_expanded}\n{string[::-1]}'