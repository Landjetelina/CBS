import random
from grid import *

def create_forbidden_grid(row_start=None, row_end=None, column_start=None, column_end=None):
    lista = []
    for i in range(row_start, row_end+1):
        for ii in range(column_start, column_end+1):
            lista.append(Node(i, ii))
    return lista

def create_complex_maze(n):
    forbidden = []
    for r in range(2, n - 2, 2):
        if (r // 2) % 2 == 0:
            for c in range(0, n - 2):
                forbidden.append(Node(r, c))
        else:
            for c in range(2, n):
                forbidden.append(Node(r, c))
    return forbidden

def create_random_forest(n, start_point, end_point, density=0.3):
    forbidden = []
    for r in range(n):
        for c in range(n):
            if random.random() < density:
                # Don't put an obstacle on the start or the end!
                if Node(r, c) != start_point and Node(r, c) != end_point:
                    forbidden.append(Node(r, c))
    return forbidden

def create_snake(n):
    forbidden_nodes = []
    for i in range(n):
        if i % 4 == 1:
            forbidden_nodes.extend(create_forbidden_grid(i, i, 0, n - 2))
        if i % 4 == 3:
            forbidden_nodes.extend(create_forbidden_grid(i, i, 1, n - 1))
    return forbidden_nodes


