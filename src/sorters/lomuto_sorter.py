import time
from sorters.sorter import Sorter

class LomutoSorter(Sorter):
    def _quicksort(self, left=0, right=None):
        if right is None:
            right = len(self.array) - 1

        if left >= right:
            return
        
        i = left
        for j in range (left + 1, right + 1):
            if self.array[j] < self.array[left]:
                i += 1
                self.array[j], self.array[i] = self.array[i], self.array[j]

        self.array[left], self.array[i] = self.array[i], self.array[left]

        self._quicksort(left, i - 1)
        self._quicksort(i + 1, right)

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        self._quicksort()

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
