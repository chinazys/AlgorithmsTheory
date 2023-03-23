import time
from sorters.sorter import Sorter

class SmoothSorter(Sorter):
    def _leonardo_numbers(num):
        if num < 2:
            return 1
        return SmoothSorter._leonardo_numbers(num - 1) + SmoothSorter._leonardo_numbers(num - 2) + 1
    
    def _heapify(array, start, end):
        i = start
        j = 0
        k = 0

        while k < end - start + 1:
            if k & 0xAAAAAAAA:
                j = j + i
                i = i >> 1
            else:
                i = i + j
                j = j >> 1

            k = k + 1

        while i > 0:
            j = j >> 1
            k = i + j

            while k < end:
                if array[k] > array[k - i]:
                    break
                array[k], array[k - i] = array[k - i], array[k]
                k = k + i

            i = j


    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        p = len(self.array) - 1
        q = p
        r = 0
        while p > 0:
            if (r & 0x03) == 0:
                SmoothSorter._heapify(self.array, r, q)
    
            if SmoothSorter._leonardo_numbers(r) == p:
                r = r + 1
            else:
                r = r - 1
                q = q - SmoothSorter._leonardo_numbers(r)
                SmoothSorter._heapify(self.array, r, q)
                q = r - 1
                r = r + 1
    
            self.array[0], self.array[p] = self.array[p], self.array[0]
            p = p - 1
    
        for i in range(len(self.array) - 1):
            j = i + 1
            while j > 0 and self.array[j] < self.array[j - 1]:
                self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                j = j - 1
    
        self.execution_time = (time.time_ns() - time_start_ns) / 1e9