import time
from sorters.sorter import Sorter

class BubbleSorter(Sorter):
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        for i in range(len(self.array) - 1) :
            flag = False

            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[j + 1] : 
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    flag = True

            if not flag:
                break
        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
