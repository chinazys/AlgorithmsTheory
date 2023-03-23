import time
from sorters.sorter import Sorter

class SmoothSorter(Sorter):
    def _leonardo_numbers(num):
        a, b = 1, 1
        numbers = []
        while a <= num:
            numbers.append(a)
            a, b = b, a + b + 1
        return numbers

    def _restore_heap(lst, i, heap, leo_nums):
        current = len(heap) - 1
        k = heap[current]

        while current > 0:
            j = i - leo_nums[k]
            if (lst[j] > lst[i] and
                (k < 2 or lst[j] > lst[i-1] and lst[j] > lst[i-2])):
                lst[i], lst[j] = lst[j], lst[i]
                i = j
                current -= 1
                k = heap[current]
            else:
                break

        while k >= 2:
            t_r, k_r, t_l, k_l = SmoothSorter._get_child_trees(i, k, leo_nums)
            if lst[i] < lst[t_r] or lst[i] < lst[t_l]:
                if lst[t_r] > lst[t_l]:
                    lst[i], lst[t_r] = lst[t_r], lst[i]
                    i, k = t_r, k_r
                else:
                    lst[i], lst[t_l] = lst[t_l], lst[i]
                    i, k = t_l, k_l
            else:
                break

    def _get_child_trees(i, k, leo_nums):
        t_r, k_r = i - 1, k - 2
        t_l, k_l = t_r - leo_nums[k_r], k - 1
        return t_r, k_r, t_l, k_l


    def run(self):
        if self.array is None:
            raise Exception("Array was not set")
        
        time_start_ns = time.time_ns()

        leo_nums = SmoothSorter._leonardo_numbers(len(self.array))

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
            SmoothSorter._restore_heap(self.array, i, heap, leo_nums)

        for i in reversed(range(len(self.array))):
            if heap[-1] < 2:
                heap.pop()
            else:
                k = heap.pop()
                t_r, k_r, t_l, k_l = SmoothSorter._get_child_trees(i, k, leo_nums)
                heap.append(k_l)
                SmoothSorter._restore_heap(self.array, t_l, heap, leo_nums)
                heap.append(k_r)
                SmoothSorter._restore_heap(self.array, t_r, heap, leo_nums)
    
        self.execution_time = (time.time_ns() - time_start_ns) / 1e9