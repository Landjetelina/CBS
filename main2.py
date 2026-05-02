import lowLevel
from lowLevel2 import *
from grid2 import *
import time

def create_forbidden_nodes(row_start=None, row_end=None, column_start=None, column_end=None):
    lista = []
    for i in range(row_start, row_end+1):
        for ii in range(column_start, column_end+1):
            lista.append((i, ii))
    return lista

if __name__ == '__main__':
    start_time = time.time()
    N = 30
    forbidden_nodes = []
    # for i in range(N):
    #     if i % 4 == 1:
    #         forbidden_nodes.extend(create_forbidden_nodes(0,N-2,i,i,))
    #     if i % 4 == 3:
    #         forbidden_nodes.extend(create_forbidden_nodes(1,N-1,i,i))

    grid = Grid(N, N, forbidden_nodes)
    print(grid)

    lowLevel = LowLevel(grid, (0, 0), (29,29))
    solution = lowLevel.return_path()
    print(solution)
    end_time = time.time()
    print(f'Time elapsed: {end_time - start_time:.3f}')


