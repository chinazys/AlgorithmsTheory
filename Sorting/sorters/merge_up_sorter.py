import time
from sorters.sorter import Sorter

class MergeUpSorter(Sorter):
    def _merge2sort(self, left_start, middle, right_end):
        left_iterator = left_start
        right_iterator = middle + 1

        sorted_part = []
        while left_iterator <= middle and right_iterator <= right_end:
            if self.array[left_iterator] <= self.array[right_iterator]: 
                sorted_part.append(self.array[left_iterator])
                left_iterator += 1
            else:
                sorted_part.append(self.array[right_iterator])
                right_iterator += 1
        
        if left_iterator <= middle:
            sorted_part += self.array[left_iterator : middle + 1] 
        if right_iterator <= right_end:
            sorted_part += self.array[right_iterator : right_end + 1]

        self.array[left_start : right_end + 1] = sorted_part

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        part_size = 1
        while part_size < len(self.array):
            for part_start in range(0, len(self.array) - part_size, part_size * 2):
                self._merge2sort(part_start, part_start + part_size - 1, min(len(self.array) - 1, part_start + 2 * part_size - 1))
            part_size *= 2

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
