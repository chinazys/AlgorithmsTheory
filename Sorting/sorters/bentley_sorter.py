import time
from sorters.sorter import Sorter
import random

class BentleySorter(Sorter):
    def _partition(self, left, right):
        t = left
        i = left
        j = right
        pivot = self.array[left]

        while i <= j:
            if self.array[i] < pivot:
                self.array[t], self.array[i] = self.array[i], self.array[t]
                t += 1
                i += 1
            elif self.array[i] > pivot:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                j -= 1
            else:
                i += 1
            
        return t, j
    def _quicksort(self, l=0, r=None):
        if r is None:
            r = len(self.array) - 1
        
        if l >= r: 
            return
        k = random.randint(l, r)
        self.array[k], self.array[l] = self.array[l], self.array[k]
        
        t, j = self._partition(l, r)
        self._quicksort(l, t - 1)
        self._quicksort(j + 1, r)  

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        self._quicksort()

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9