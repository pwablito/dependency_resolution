class Software:
    def __init__(self, name):
        self.name = name
        self.dependency_names = set()

    def add_dependency(self, name):
        self.dependency_names.add(name)

    def __str__(self):
        return self.name
