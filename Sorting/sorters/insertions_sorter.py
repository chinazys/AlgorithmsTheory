import time
from sorters.sorter import Sorter

class InsertionsSorter(Sorter):
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        for index in range(1, len(self.array)):
            curValue = self.array[index]
            curPosition = index

            while curPosition > 0 and self.array[curPosition - 1] > curValue:
                self.array[curPosition] = self.array[curPosition - 1]
                curPosition -= 1

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
