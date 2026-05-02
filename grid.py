from functools import total_ordering

from sklearn import neighbors


class Node:
    def __init__(self, row, column, cost=1, neighbours=None):
        if neighbours is None:
            neighbours = []
        self.row: int = row
        self.column: int = column
        self.cost = cost  # cost function for robot to go to this square

        self.neighbours: list[Node] | None = neighbours  # node list depicting available moves for robot
        self.heuristic = None
    def __str__(self):
        return f'{self.row},{self.column}'

    def __hash__(self):
        return hash((self.row, self.column))
    @total_ordering
    def __eq__(self, other):  # equal if they have the same row and column number
        if isinstance(other, Node):
            return self.row == other.row and self.column == other.column
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            if self.row > other.row:
                return True
            if self.row == other.row and self.column > other.column:
                return True
            return False
        return False



class Grid:
    def __init__(self, row, column, forbidden_nodes=None):
        self.row = row  # number of grid rows
        self.column = column  # number of grid columns
        self.forbidden_nodes:list['Node'] | None = sorted(forbidden_nodes)  # represents an obstacle

        self.flat_tree_list = []
        for i in range(self.row):
            self.flat_tree_list.append([Node(i, j) for j in range(self.column)])

        self.root: Node = self.flat_tree_list[0][0]


        # iterates through flat_tree_list and adds neighbouring nodes for each node
        for i in range(self.row):
            for j in range(0, self.column):
                node: Node = self.flat_tree_list[i][j]
                if self.forbidden_nodes is not None and node in self.forbidden_nodes: # skips forbidden nodes
                    continue
                node.neighbours.append(node)  # node is also his own neighbour, this represents waiting in the same node
                if i-1 >= 0 and self.flat_tree_list[i-1][j] not in self.forbidden_nodes: # checks if it's first row and upper node doesn't exist
                    node.neighbours.append(self.flat_tree_list[i-1][j])
                if j-1 >= 0 and self.flat_tree_list[i][j-1] not in self.forbidden_nodes: # checks if it's first column and left node doesn't exist
                    node.neighbours.append(self.flat_tree_list[i][j-1])
                if i+1 < self.row and self.flat_tree_list[i+1][j] not in self.forbidden_nodes: # checks if it's last row and lower node doesn't exist
                    node.neighbours.append(self.flat_tree_list[i+1][j])
                if j+1 < self.column and self.flat_tree_list[i][j+1] not in self.forbidden_nodes: # checks if it's last column and right node doesn't exist
                    node.neighbours.append(self.flat_tree_list[i][j+1])

    def __str__(self):
        string = ''
        for row in self.flat_tree_list:
            for node in row:
                if node in self.forbidden_nodes:
                    string += f'{'---':^5}  '
                else:
                    string += f'{f"{node.row},{node.column}":^5}  '
            string += '\n'
        return string

    # Grid 3x3 with forbidden (1,1)
        # +y --->
    # +x  0,0  1,0  2,0
    #  |  0,1  ---  2,1
    #  |  0,2  1,2  2,2
    #  V
