import heapq
import sys
from grid import *
from sortedcontainers import SortedList


class LowLevel:
    def __init__(self, grid: Grid, start_point, end_point):
        self.grid = grid
        self.start_point: Node = start_point
        self.end_point: Node = end_point

        self._nodes_expanded = 0

    def heuristic_fn(self, node: Node):  # Manhattan distance
        value = abs(self.end_point.row - node.row) + abs(self.end_point.col - node.col)
        return value

    def a_star(self):
        # [0] g_n = total cost + heuristic, [1] is current node (Node), [2] is total cost, [3] is list that contains parent node
        curr_node: list[Node | int | None] = [0+self.heuristic_fn(self.start_point), self.start_point, 0, None]
        open_nodes, closed_nodes = [], SortedList()
        while True:
            self._nodes_expanded += 1
            closed_nodes.add(curr_node[1])
            # iterator that contains at most 5 neighbouring nodes (upper, left, itself, right, lower)
            neighbours = self.grid.get_neighbours(curr_node[1])
            new_nodes = []  # isn't neccessary, put for debugging purposes, neighbours could be appended directly in open nodes list
            for neighbour_node in neighbours:
                if neighbour_node in closed_nodes:  # node is already visited
                    continue
                cost = self.grid.flat_tree_list[neighbour_node.row][neighbour_node.col]
                # adds neighbouring node with additional info to heap. Node with the lowest g_n is on top of the heap
                # if two nodes have the same g_n, priority has the one with higher row rank, then higher column rank
                heapq.heappush(new_nodes, [self.heuristic_fn(neighbour_node) + curr_node[2] + cost,
                                neighbour_node, curr_node[2] + cost, curr_node])
            for node in new_nodes:
                heapq.heappush(open_nodes, node)
            try:
                next_node: list[Node | int | None] = heapq.heappop(open_nodes)
            except IndexError: # if heap becomes empty, it means that we have visited every available node and couldn't find solution
                print('Nema rješenja!')
                sys.exit(1)
            if next_node[1] == self.end_point:  # checks if the goal is found
                return next_node
            curr_node = next_node

    # returns a solution of A*
    def return_path(self):
        curr_node = self.a_star()
        path, total_cost = [], curr_node[2]
        while curr_node is not None:
            path.append(curr_node[1])  # node is at index 1
            curr_node = curr_node[3]  # next node is parent node
        path.reverse()  # path should be reversed in order to go from start to finish
        return path, total_cost

    def path2str(self, path, total_cost=None):
        path = [str(node) for node in path]
        string = " --> ".join(path)
        if total_cost:
            return f'Total cost: {total_cost}\nNodes expanded: {self._nodes_expanded}\n{string}'
        else:
            return string