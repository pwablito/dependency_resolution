import json
import src.graph as graph
import src.software as software


class InputFile:
    def __init__(self, filename):
        self.filename = filename

    def to_graph(self):
        data = json.load(open(self.filename))
        graph_obj = graph.Graph()
        for item in data:
            software_obj = software.Software(item['name'])
            for dep in item['dependencies']:
                software_obj.add_dependency(dep)
            graph_obj.add_software(software_obj)
        return graph_obj
