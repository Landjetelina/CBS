import random as rnd

import createMaze
from highLevel import *
from grid import *

# ================ CREATE YOUR OWN EXAMPLE: =====================
def create_example():
    n, agent_dict, forbidden_nodes, grid = None, None, None, None
    return n, agent_dict, forbidden_nodes, grid

def create_example_1():
    # simple example from the book, grid 4x4 two agents
    n = 4
    agent_dict = {'a1': (Node(0,1), Node(3,2)), 'a2': (Node(1,0), Node(2,3))}
    forbidden_nodes = [Node(0,0), Node(0,3), Node(3,0), Node(3,3)]
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
    # 2 agents, tests swap collision and if agent can wait to avoid collision
    n = 5
    agent_dict = {'a1': (Node(0,0), Node(0,4)), 'a2': (Node(1,2), Node(0,0))}
    forbidden_nodes = [Node(2, 2)]
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 3, 4))
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_4():
    # random chaos!!! grid = 20x20, 10 agents
    n, k, a = 20, 40, 10  # grid, obstacles, agents
    agents = [f'a{i}' for i in range(1, a+1)]
    agent_dict = dict()
    for a in agents:
        start_p, end_p = None, None
        while start_p == end_p:
            start_p = rnd.randint(0, n-1), rnd.randint(0, n-1)
            end_p = rnd.randint(0, n-1), rnd.randint(0, n-1)
        agent_dict[a] = (Node(*start_p), Node(*end_p))

    forbidden_nodes = set()
    points = list(agent_dict.values())
    for i in range(k):
        obstacle = Node(rnd.randint(0, n-1), rnd.randint(0, n-1))
        if obstacle in [node for pair in points for node in pair]:
            i -= 1
        else:
            forbidden_nodes.add(obstacle)
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid


def create_example_5():
    # 4 agents, corner swap, huge empty grid = 100x100
    n = 100
    agent_dict = {'a1': (Node(0,0), Node(99,99)), 'a2': (Node(99,99), Node(0,0)),
                  'a3': (Node(0,99), Node(99,0)), 'a4': (Node(99,0), Node(0,99))}
    forbidden_nodes = []
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_6():
    # 4 agents, each tries to go to the center of the map, grid = 6x6
    n = 6
    agent_dict = {'a1': (Node(0,0), Node(3,3)), 'a2': (Node(5,5), Node(2,2)),
                  'a3': (Node(0,5), Node(3,2)), 'a4': (Node(5,0), Node(2,3))}
    forbidden_nodes = [Node(1,4),Node(1,5),Node(1,0),Node(1,1),Node(4,0),Node(4,1),Node(4,4),Node(4,5)]
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_7():
    # 2 agents, tests swap collision and if agents can go backwards to avoid collision
    n = 6
    agent_dict = {'a1': (Node(0,3), Node(0,5)), 'a2': (Node(0,4), Node(0,0))}
    forbidden_nodes = [Node(2, 2)]
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 3, 5))
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_8():
    # 3 agents, tests swap collision and if agents can go backwards to avoid collision
    n = 10
    agent_dict = {'a1': (Node(0,3), Node(0,9)), 'a2': (Node(0,4), Node(0,0)), 'a3': (Node(0,0), Node(0,9))}
    forbidden_nodes = [Node(2, 2), Node(2,5)]
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 3, 4))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(1, 1, 6, 9))
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_9():
    # 3 agents, cross map
    n = 5
    agent_dict = {'a1': (Node(0,2), Node(4,2)), 'a2': (Node(4,2), Node(0,2)),
                  'a3': (Node(2,0), Node(2,4))} # ,'a4': (Node(2,4), Node(2,0))
    forbidden_nodes = []
    forbidden_nodes.extend(createMaze.create_forbidden_grid(0, 1, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(0, 1, 3, 4))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(3, 4, 0, 1))
    forbidden_nodes.extend(createMaze.create_forbidden_grid(3, 4, 3, 4))

    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid

def create_example_10():
    # 4 agents, each tries to go to the opposite corner, grid = 3x3
    n = 3
    agent_dict = {'a1': (Node(0,0), Node(2,2)), 'a2': (Node(2,2), Node(0,0)),
                  'a3': (Node(0,2), Node(2,0)), 'a4': (Node(2,0), Node(0,2))}
    forbidden_nodes = []
    grid = Grid(n, n, forbidden_nodes)
    return n, agent_dict, forbidden_nodes, grid




