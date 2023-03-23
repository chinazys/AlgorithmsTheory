class Sorter:
    def __init__(self):
        self.array = None
        self.execution_time = None
    def reinitialize(self, array):
        self.array = [value for value in array]
        self.execution_time = None
    def run(self):
        pass