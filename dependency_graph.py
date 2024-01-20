'''
create a graph to map out the required dependencies
'''


class Node:
    def __init__(self, file_name: str, dependencies: [str]):
        self.file_name = file_name
        self.dependencies = dependencies

    # this isn't good enough
    def check_cycle(self, file: 'Node') -> bool:
        return (file in self.dependencies) and (self in file.dependencies)
