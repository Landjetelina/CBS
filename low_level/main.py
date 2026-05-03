from lowLevel import *
from grid import *
import time
from low_level import createMaze

if __name__ == '__main__':
    start_time = time.time()
    n, start_point, end_point = 100, Node(0,0), Node(99,99)

    forbidden_nodes: list[Node] = [Node(0,1), Node(1,0)]
    # forbidden_nodes.extend(createMaze.create_snake(n))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(2, 2, 1, 99))

    grid = Grid(n, n, forbidden_nodes)
    print(grid)

    lowLevel = LowLevel(grid,start_point,end_point)
    solution = lowLevel.return_path()

    print(solution)
    print(f'Time elapsed: {time.time() - start_time:.3f}')


