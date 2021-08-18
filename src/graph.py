import src.error as error
import src.queue as queue


class Node:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, node):
        self.dependencies.append(node)

    def __str__(self):
        if len(self.dependencies):
            return "{} -> ({})".format(self.name, [dependency.__str__() for dependency in self.dependencies])
        return self.name


class Graph:
    def __init__(self):
        self.nodes = []

    def get_node(self, software_name):
        for node in self.nodes:
            if node.name == software_name:
                return node
        return None

    def add_software(self, software):
        new_node = self.get_node(software.name)
        if not new_node:
            new_node = Node(software.name)
        for dependency_name in software.dependency_names:
            dependency_node = self.get_node(dependency_name)
            if not dependency_node:
                dependency_node = Node(dependency_name)
                self.nodes.append(dependency_node)
            new_node.add_dependency(dependency_node)
        self.nodes.append(new_node)

    def resolve(self, name):
        node = self.get_node(name)
        if not node:
            raise error.SoftwareNotFoundError(name)
        for name in self.get_install_order(node):
            print(name)

    def add_node_to_queue(self, node, queue_obj, parents):
        if node.name in parents:
            raise error.CircularDependencyError
        for dependency in node.dependencies:
            new_parents = parents.copy()
            new_parents.append(node.name)
            self.add_node_to_queue(dependency, queue_obj, new_parents)
        if not queue_obj.has(node.name):
            queue_obj.enqueue(node.name)

    def get_install_order(self, node):
        install_queue = queue.Queue()
        self.add_node_to_queue(node, install_queue, [])
        return install_queue.queue
