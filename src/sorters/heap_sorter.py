import time
from sorters.sorter import Sorter

class HeapSorter(Sorter):
    def _max_heapify(array, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and array[left] > array[i]:
            largest = left
        else:
            largest = i
            
        if right < n and array[right] > array[largest]:
            largest = right
            
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            HeapSorter._max_heapify(array, n, largest)

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()
    

        for i in range(len(self.array), -1,-1):
            HeapSorter._max_heapify(self.array, len(self.array), i)
            
        for i in range(len(self.array) - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            HeapSorter._max_heapify(self.array, i, 0)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
