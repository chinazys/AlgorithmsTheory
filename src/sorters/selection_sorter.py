import time
from sorters.sorter import Sorter

class SelectionSorter(Sorter):
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        for i in range(len(self.array) - 1):
            min_index = i
            
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
