import time
from sorters.sorter import Sorter

class CountingSorter(Sorter):
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        counts = [0 for i in range(max(self.array) + 1)]

        for value in self.array:
            counts[value] += 1

        for index in range(1, len(counts)):
            counts[index] += counts[index - 1]
    
        initial_array = [value for value in self.array]
        self.array = [0 for i in range(len(self.array))]
        for value in initial_array:
            index = counts[value] - 1
            self.array[index] = value
            counts[value] -= 1

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9