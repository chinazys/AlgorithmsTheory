import time
from sorters.sorter import Sorter

class LSDSorter(Sorter):
    def __init__(self, base):
        self.base = base
        super().__init__()
        
    def _counting_sort(self, place_value):
        min_value = self._get_min_value(place_value)
        offset = 0
        if min_value < 0:
            offset = 0 - min_value
        counts = [0] * (self.base + offset)
        sorted_array = [0] * len(self.array)

        for i in range(len(self.array)):
            counts_ind = self._get_digit(i, place_value) + offset
            counts[counts_ind] += 1

        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        for i in range(len(self.array)-1, -1, -1):
            counts_ind = self._get_digit(i, place_value) + offset
            position = counts[counts_ind]
            sorted_ind = position - 1
            sorted_array[sorted_ind] = self.array[i]
            counts[counts_ind] -= 1

        self.array[:] = sorted_array

    def _get_min_value(self, place_value):
        min_value = self._get_digit(0, place_value)
        for i in range(1, len(self.array)):
            element = self._get_digit(i, place_value)
            if element < min_value:
                min_value = element
        return min_value

    def _get_digit(self, ind, place_value):
        element = self.array[ind]
        digit = abs(element) // place_value % self.base
        return digit if element > 0 else -digit

    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()
        
        max_value = max(self.array)

        place_value = 1
        while max_value // place_value > 0:
            self._counting_sort(place_value)
            # print(self.array)
            place_value *= self.base

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9

if __name__ == "__main__":
    arrays = [[2022, 5, 398, 159, 16, 1223, 7], [2022, -5, 398, 159, 16, -1223, 7]]
    
    sorter = LSDSorter(10)
    sorter.reinitialize([2022, -5, 398, 159, 16, -1223, 7])
    sorter.run()