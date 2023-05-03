import time

class Sorter:
    def __init__(self):
        self.array = None
        self.execution_time = None
    def reinitialize(self, array):
        self.array = [value for value in array]
        self.execution_time = None
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        self.array = sorted(self.array)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9