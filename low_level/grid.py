from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, row, column):
        self.row = row
        self.col = column
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False
    def __hash__(self):
        return hash((self.row, self.col))
    # nodes that have higher row value and higher column value will have priority
    def __lt__(self, other):
        if isinstance(other, Node):
            if self.row > other.row:
                return True
            if self.row == other.row and self.col > other.col:
                return True
        return False
    def __str__(self):
        return f'{self.row},{self.col}'


class Grid:
    def __init__(self, row, column, forbidden_nodes=None, weight=1):
        self.row = row  # number of grid rows
        self.column = column  # number of grid columns
        self.forbidden_nodes:list[Node] = sorted(forbidden_nodes)  # represents an obstacle

        # contains node weights
        self.flat_tree_list = [[weight if (i, j) not in self.forbidden_nodes
                                else None for i in range(self.column) ] for j in range(self.row)]
    def set_weight(self, i, j, cost):
        self.flat_tree_list[i][j] = cost


    # returns neighbouring nodes
    def get_neighbours(self, node: Node):
        i, j = node.row, node.col
        if not self.flat_tree_list[i][j]:  # obstacle
            return None
        if i > 0 and self.flat_tree_list[i-1][j]:  # adds upper neighbour
            yield Node(i - 1, j)
        if j > 0 and self.flat_tree_list[i][j-1]:  # adds left neighbour
            yield Node(i, j - 1)
        yield Node(i, j)   # adds itself as neighbour, represents agent wait
        if j+1 < self.column and self.flat_tree_list[i][j+1]:  # adds right neighbour
            yield Node(i, j + 1)
        if i+1 < self.row and self.flat_tree_list[i+1][j]:   # adds lower neighbour
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
