import select
from pywin.idle import PyParse
from scipy.sparse import coo

class Node:
    def __init__(self, row, column):
        self.row = row
        self.col = column
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False
    def __lt__(self, other):
        if isinstance(other, Node):
            if self.row > other.row:
                return True
            if self.row == other.row and self.col > other.col:
                return True
            return False
        return False
    def __str__(self):
        return f'{self.row},{self.col}'




class Grid:
    def __init__(self, row, column, forbidden_nodes=None, weight=1):
        self.row = row  # number of grid rows
        self.column = column  # number of grid columns
        self.forbidden_nodes:list[Node] = sorted(forbidden_nodes)  # represents an obstacle

        self.flat_tree_list = [[weight if (i, j) not in self.forbidden_nodes
                                else None for i in range(self.column) ] for j in range(self.row)]
    def set_weight(self, i, j, cost):
        self.flat_tree_list[i][j] = cost

    def get_neighbours(self, node: Node):
        i, j = node.row, node.col
        if not self.flat_tree_list[i][j]:
            return None
        if i > 0 and self.flat_tree_list[i-1][j]:
            yield Node(i - 1, j)
        if j > 0 and self.flat_tree_list[i][j-1]:
            yield Node(i, j - 1)
        yield Node(i, j)
        if j+1 < self.column and self.flat_tree_list[i][j+1]:
            yield Node(i, j + 1)
        if i+1 < self.row and self.flat_tree_list[i+1][j]:
            yield Node(i + 1, j)

    def __str__(self):
        string = ''
        for i in range(self.row):
            for j in range(self.column):
                if not self.flat_tree_list[i][j]:
                    string += f'{'---':^5}  '
                else:
                    string += f'{f"{i},{j}":^5}  '
            string += '\n'
        return string

    # Grid 3x3 with forbidden (1,1)
        # +y --->
    # +x  0,0  1,0  2,0
    #  |  0,1  ---  2,1
    #  |  0,2  1,2  2,2
    #  V
