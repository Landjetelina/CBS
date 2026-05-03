import random

from lowLevel2 import *
from grid2 import *
import time

def create_forbidden_nodes(row_start=None, row_end=None, column_start=None, column_end=None):
    lista = []
    for i in range(row_start, row_end+1):
        for ii in range(column_start, column_end+1):
            lista.append((i, ii))
    return lista

def create_complex_maze(n):
    forbidden = []
    # Stvara horizontalne zidove svaka 2 reda
    for r in range(2, n - 2, 2):
        if (r // 2) % 2 == 0:
            # Zid s rupom na desnoj strani
            for c in range(0, n - 2):
                forbidden.append((r, c))
        else:
            # Zid s rupom na lijevoj strani
            for c in range(2, n):
                forbidden.append((r, c))
    return forbidden

def create_random_forest(n, start_point, end_point, density=0.3):
    forbidden = []
    for r in range(n):
        for c in range(n):
            if random.random() < density:
                # Nemoj staviti zid na start ili kraj
                if Node(r, c) != start_point and Node(r, c) != end_point:
                    forbidden.append((r, c))
    return forbidden
def create_snake(n):
    forbidden_nodes = []
    for i in range(n):
        if i % 4 == 1:
            forbidden_nodes.extend(create_forbidden_nodes(i,i,0,n-2))
        if i % 4 == 3:
            forbidden_nodes.extend(create_forbidden_nodes(i,i,1,n-1))
    return forbidden_nodes

if __name__ == '__main__':
    start_time = time.time()
    n, start_point, end_point = 10, Node(0, 0), Node(9, 9)
    forbidden_nodes = []

    forbidden_nodes.extend(create_random_forest(n, start_point, end_point))
    forbidden_nodes.extend(create_snake(n))

    grid = Grid(n, n, forbidden_nodes)
    print(grid)

    lowLevel = LowLevel(grid,start_point,end_point)
    solution = lowLevel.return_path()
    print(solution)
    end_time = time.time()
    print(f'Time elapsed: {end_time - start_time:.3f}')


