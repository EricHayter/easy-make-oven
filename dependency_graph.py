'''
create a graph to map out the required dependencies
'''


class Node:
    def __init__(self, file_name: str, dependencies: ['Node']):
        self.file_name = file_name
        self.dependencies = dependencies

    def get_dependencies(self):
        return self.dependencies


def check_cycle(start_node: Node, visited=[]):
    if start_node in visited:  # already visited
        return True
    visited.append(start_node)
    for node in start_node.get_dependencies():
        if check_cycle(node, visited):
            return True
    return False

# might want to add function to find islands
