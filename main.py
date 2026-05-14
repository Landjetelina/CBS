import time
import testExamples
from highLevel import *
from lowLevel import *

from animate import MultiAgentAnimator


def convert_paths(sol_dict):
    paths = {}
    for agent, solution in sol_dict.items():
        path = solution
        converted = []
        for state in path:
            node = state[0]
            converted.append((node.row, node.col))
        paths[agent] = converted
    return paths

if __name__ == '__main__':
    start_time = time.time()

    # =========== CHANGE TEST EXAMPLE HERE: ==============================
    n, agent_dict, forbidden_nodes, grid = testExamples.create_example_10()
    # ====================================================================

    print(grid)
    constr_tree = ConstraintTree(agent_dict, grid)
    sol_dict = constr_tree.treeWalk()
    for agent, path in sol_dict.items():
        print(f'{agent}\n{"-"*20}')
        print(LowLevel.path2str(path, nodes_expanded=path[1]))
        print()

    print(f'{"="*20}')
    print(f'Nodes expanded: {constr_tree.nodes_expanded}')
    print(f'Time elapsed: {time.time() - start_time:.3f}')

    # Animation
    paths = convert_paths(sol_dict)
    animator = MultiAgentAnimator(
        paths=paths,
        grid_size=n,
        forbidden_nodes=forbidden_nodes
    )
    animator.show()