import numpy as np
import time
import linecache
from save_to_output_file import save_to_output_file

class PolyphaseSorter:
    file_line_pointers = [0, 0, 0, 0]
    file_sizes = [0, 0, 1]
    file_sorted_heights = [1, 1, 1, 0]
    file_start_pointers = [0, 0, 0, 0]

    def _fill_files_sizes(self):
        while True:
            next_num = self.file_sizes[0] + self.file_sizes[1] + self.file_sizes[2]
            if next_num < self.input_array_size:
                self.file_sizes = [self.file_sizes[1], self.file_sizes[2], next_num]
            else:
                self.file_sizes.append(0)
                break

    def __init__(self, input_filename, input_array_size, files_quantity=4):
        self.partition_size = files_quantity - 1
        self.input_array_size = input_array_size

        unsorted_file = open(input_filename, 'r')

        self._fill_files_sizes()
        buffer = []
        file_shift_index = 0
        self.array = []
        for line in unsorted_file.readlines():
            buffer.append(int(line))
            self.array.append(int(line))
            if len(buffer) >= self.file_sizes[file_shift_index % self.partition_size]:                
                file = open(str(file_shift_index % self.partition_size), "ab")
                np.savetxt(file, buffer, fmt='%1.0f')
                file.close()
                
                buffer = []
                file_shift_index += 1

        file = open(str(self.partition_size), "ab")
        np.savetxt(file, [], fmt='%1.0f')
        file.close()

        unsorted_file.close()
        
    def run(self, output_filename):
        time_start_ns = time.time_ns()

        next = self._move_to_file(3)
        next = self._move_to_file(next)
        save_to_output_file(output_filename, self.array)

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9

    def _get_min_file_metadata(self, exclude_file_index):
        cur_min_value = 1e9
        cur_min_layer_cnt = 1e9
        
        for file_index in range(0, 4):
            if file_index == exclude_file_index:
                continue

            file_min = int(linecache.getline(str(file_index), self.file_start_pointers[file_index] + self.file_line_pointers[file_index] + 1))
            cur_layer_cnt = int(self.file_line_pointers[file_index] / self.file_sorted_heights[file_index])

            if cur_layer_cnt < cur_min_layer_cnt:
                cur_min_value = file_min
                min_index = file_index
                cur_min_layer_cnt = cur_layer_cnt 
                continue
            if cur_min_value > file_min and cur_layer_cnt <= cur_min_layer_cnt:
                cur_min_value = file_min
                min_index = file_index
                cur_min_layer_cnt = cur_layer_cnt

        return min_index, cur_min_value

    def _move_to_file(self, target_file_index):
        heights_sum = 0
        for i in range(0, 4):
            heights_sum += self.file_sorted_heights[i]

        self.file_sorted_heights[target_file_index] = heights_sum
        target_file = open(str(target_file_index), "ab")

        while True:
            min_file_index, min_file_value = self._get_min_file_metadata(target_file_index)
            self.file_line_pointers[min_file_index] += 1

            np.savetxt(target_file, [min_file_value], fmt='%1.0f')
            self.file_sizes[target_file_index] += 1

            if self.file_start_pointers[min_file_index] + self.file_line_pointers[min_file_index] >= self.file_sizes[min_file_index]:
                np.savetxt(str(min_file_index), [], fmt="%1.0f")
                self.file_sizes[min_file_index] = 0
                self.file_start_pointers = [v for v in self.file_line_pointers]
                self.file_line_pointers = [0, 0, 0, 0]
                self.file_sorted_heights[min_file_index] = 0
                target_file.close()
                return min_file_index

# 1. Постановка задачи
# 2. Условия єксперимента
# 3. Результаты работы
# 4. Выводы

ARRAY_SIZE = 3136
INPUT_FILENAME = 'unsorted.csv'
OUTPUT_FILENAME = 'sorted.csv'

unsorted_array = np.arange(ARRAY_SIZE)
np.random.shuffle(unsorted_array)
np.savetxt(INPUT_FILENAME, unsorted_array, fmt = '%1.0f')

polyphase_sorter = PolyphaseSorter(INPUT_FILENAME, ARRAY_SIZE)
polyphase_sorter.run(OUTPUT_FILENAME)

print("Execution time:", polyphase_sorter.execution_time)