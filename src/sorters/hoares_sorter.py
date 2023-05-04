import time
from sorters.sorter import Sorter

class HoaresSorter(Sorter):
    def _quicksort(self, left=0, right=None):
        if right is None:
            right = len(self.array) - 1
        
        if left >= right:
            return
        
        pivot = self.array[left]
        i = left
        j = right + 1

        while True:
            while True:
                i += 1
                if i > right or self.array[i] >= pivot:
                    break
            while True:
                j -= 1
                if self.array[j] <= pivot:
                    break

            if i > j:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]
        
        self.array[left], self.array[j] = self.array[j], self.array[left]
        self._quicksort(left, j - 1)
        self._quicksort(j + 1, right)

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        self._quicksort()

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9