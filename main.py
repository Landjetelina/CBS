import time


from sys import path
from high_level.high_level import *
from low_level.lowLevel import *
from low_level.grid import *
from low_level import createMaze, lowLevel

if __name__ == '__main__':
    start_time = time.time()
    n, agent_dict = 5, {'a1': (Node(0,0), Node(4,4)), 'a2': (Node(4,4), Node(0,0)),
                        'a3': (Node(0,4), Node(4,0)), 'a4': (Node(4,0), Node(0,4))}

    forbidden_nodes: list[Node] = [Node(1,1), Node(1,0), Node(0,3), Node(3,2)]
    forbidden_nodes = []
    # forbidden_nodes.extend(createMaze.create_snake(n))
    # forbidden_nodes.extend(createMaze.create_forbidden_grid(0, 3, 3, 3))

    grid = Grid(n, n, forbidden_nodes)
    print(grid)

    sol_dict = ConstraintTree(agent_dict, grid).treeWalk()
    #
    for agent, path in sol_dict.items():
        print(f'{agent}\n{20*'-'}')
        print(lowLevel.LowLevel.path2str(path, nodes_expanded=path[1]) + '\n')
    print(f'{20*'='}\nTime elapsed: {time.time() - start_time:.3f}')

    print(0)


