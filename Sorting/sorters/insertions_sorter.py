import time
from sorters.sorter import Sorter

class InsertionsSorter(Sorter):
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        for i in range(1, len(self.array)):
            key = self.array[i]

            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1], self.array[j] = self.array[j], key
                                
                j -= 1

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
