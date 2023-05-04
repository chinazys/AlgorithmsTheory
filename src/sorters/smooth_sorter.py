import time
from sorters.sorter import Sorter

class SmoothSorter(Sorter):
    def _leonardo_numbers(num):
        preprev, prev = 1, 1
        numbers = []
        while preprev <= num:
            numbers.append(preprev)
            preprev, prev = prev, preprev + prev + 1
        return numbers

    def _restore_heap(array, i, heap, leonardo_numbers):
        current = len(heap) - 1
        k = heap[current]

        while current > 0:
            j = i - leonardo_numbers[k]
            if (array[j] > array[i] and
                (k < 2 or array[j] > array[i-1] and array[j] > array[i-2])):
                array[i], array[j] = array[j], array[i]
                i = j
                current -= 1
                k = heap[current]
            else:
                break

        while k >= 2:
            t_right, k_right, t_left, k_left = SmoothSorter._get_child_trees(i, k, leonardo_numbers)
            if array[i] < array[t_right] or array[i] < array[t_left]:
                if array[t_right] > array[t_left]:
                    array[i], array[t_right] = array[t_right], array[i]
                    i, k = t_right, k_right
                else:
                    array[i], array[t_left] = array[t_left], array[i]
                    i, k = t_left, k_left
            else:
                break

    def _get_child_trees(i, k, leonardo_numbers):
        t_right, k_right = i - 1, k - 2
        t_left, k_left = t_right - leonardo_numbers[k_right], k - 1
        return t_right, k_right, t_left, k_left


    def run(self):
        if self.array is None:
            raise Exception("Array was not set")

        time_start_ns = time.time_ns()

        leonardo_numbers = SmoothSorter._leonardo_numbers(len(self.array))

        heap = []

        for i in range(len(self.array)):
            if len(heap) >= 2 and heap[-2] == heap[-1] + 1:
                heap.pop()
                heap[-1] += 1
            else:
                if len(heap) >= 1 and heap[-1] == 1:
                    heap.append(0)
                else:
                    heap.append(1)
            SmoothSorter._restore_heap(self.array, i, heap, leonardo_numbers)

        for i in reversed(range(len(self.array))):
            if heap[-1] < 2:
                heap.pop()
            else:
                k = heap.pop()
                t_right, k_right, t_left, k_left = SmoothSorter._get_child_trees(i, k, leonardo_numbers)
                heap.append(k_left)
                SmoothSorter._restore_heap(self.array, t_left, heap, leonardo_numbers)
                heap.append(k_right)
                SmoothSorter._restore_heap(self.array, t_right, heap, leonardo_numbers)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9