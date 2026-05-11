from high_level.high_level import *
from low_level.lowLevel import *
from low_level.grid import *


def create_example_1():
    # 2 agents, tests swap collision and if agent can wait to avoid collision
    n = 5
    agent_dict = {'a1': (Node(0,0), Node(0,4)), 'a2': (Node(1,2), Node(0,0))}
    forbidden_nodes = [Node(2, 2)]
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 3, 4))
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_2():
    # 4 agents, each tries to go to the opposite corner, grid = 5x5
    n = 5
    agent_dict = {'a1': (Node(0,0), Node(4,4)), 'a2': (Node(4,4), Node(0,0)),
                  'a3': (Node(0,4), Node(4,0)), 'a4': (Node(4,0), Node(0,4))}
    forbidden_nodes = []
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_3():
    # 4 agents, each tries to go to the opposite corner, grid = 3x3
    n = 3
    agent_dict = {'a1': (Node(0,0), Node(2,2)), 'a2': (Node(2,2), Node(0,0)),
                  'a3': (Node(0,2), Node(2,0)), 'a4': (Node(2,0), Node(0,2))}
    forbidden_nodes = []
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_4():
    # 4 agents, each tries to go to the center of the map, grid = 6x6
    n = 6
    agent_dict = {'a1': (Node(0,0), Node(3,3)), 'a2': (Node(5,5), Node(2,2)),
                  'a3': (Node(0,5), Node(3,2)), 'a4': (Node(5,0), Node(2,3))}
    forbidden_nodes = [Node(1,4),Node(1,5),Node(1,0),Node(1,1),Node(4,0),Node(4,1),Node(4,4),Node(4,5)]
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_5():
    # 4 agents, corner swap, huge empty grid = 100x100
    n = 100
    agent_dict = {'a1': (Node(0,0), Node(99,99)), 'a2': (Node(99,99), Node(0,0))}
                  # 'a3': (Node(0,99), Node(99,0)), 'a4': (Node(99,0), Node(0,99))}
    forbidden_nodes = []
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid