import time
from sorters.sorter import Sorter

class MergeDownSorter(Sorter):
    def _merge_down_sort(array):
        if len(array) < 2:
            return
        
        middle = len(array) // 2
        left_part = array[:middle]
        right_part = array[middle:]

        MergeDownSorter._merge_down_sort(left_part)
        MergeDownSorter._merge_down_sort(right_part)

        left_iterator = 0
        right_iterator = 0
        common_iterator = 0
        
        while left_iterator < len(left_part) and right_iterator < len(right_part):
            if left_part[left_iterator] <= right_part[right_iterator]:
                array[common_iterator] = left_part[left_iterator]
                left_iterator += 1
            else:
                array[common_iterator] = right_part[right_iterator]
                right_iterator += 1
            common_iterator += 1

        if left_iterator < len(left_part):
            array[common_iterator:] = left_part[left_iterator:] 
        if right_iterator < len(right_part):
            array[common_iterator:] = right_part[right_iterator:] 

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        MergeDownSorter._merge_down_sort(self.array)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9
