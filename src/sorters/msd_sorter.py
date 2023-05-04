import time
from sorters.sorter import Sorter

class MSDSorter(Sorter):
    def __init__(self, base):
        self.base = base
        super().__init__()

    def _get_number_of_digits(self, number):
        res = 0
        while number > 0:
            res += 1
            number //= self.base
        return res

    def _bucket_sort(self, array, place):
        if place < 1:
            return array
        
        if len(array) <= 1:
            return array

        buckets = []
        minimum = self._get_min_value(array, place)

        offset = 0
        if minimum < 0:
            offset = 0 - minimum

        for i in range(self.base + offset):
            buckets.append([])

        for index, num in enumerate(array):
            bucket_index = self._get_digit(array, index, place) + offset
            buckets[bucket_index].append(num)
        
        sorted_index = 0
        for bucket in buckets:
            sorted_bucket = self._bucket_sort(bucket, place // self.base)
            for num in sorted_bucket:
                array[sorted_index] = num
                sorted_index += 1

        return array
    
    def _get_min_value(self, array, place_value):
        min_value = self._get_digit(array, 0, place_value)
        for i in range(1, len(array)):
            element = self._get_digit(array, i, place_value)
            if element < min_value:
                min_value = element
        return min_value

    def _get_digit(self, array, ind, place_value):
        element = array[ind]
        digit = abs(element) // place_value % self.base
        return digit if element > 0 else -digit
    
    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        maximum = max(self.array)
        place = self.base ** (self._get_number_of_digits(maximum) - 1)
        self._bucket_sort(self.array, place)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9

if __name__ == "__main__":
    arrays = [[2022, 5, 398, 159, 16, 1223, 7], [2022, -5, 398, 159, 16, -1223, 7]]
    
    sorter = MSDSorter(10)
    sorter.reinitialize([2022, -5, 398, 159, 16, -1223, 7])
    sorter.run()

    print(sorter.array)