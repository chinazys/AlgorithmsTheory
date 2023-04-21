from queue import PriorityQueue
import numpy as np
import time

class BalancedMultiwaySorter:
    def __init__(self, input_filename, buffer_size, files_quantity):
        self.partition_size = int(files_quantity / 2)

        unsorted_file = open(input_filename, 'r')
        self.buffer_size = buffer_size
        self.input_array_size = 0

        buffer = []
        file_shift_index = 0
        for line in unsorted_file.readlines():
            self.input_array_size += 1
            buffer.append(int(line))
            if len(buffer) >= self.buffer_size:
                buffer = sorted(buffer)
                
                file = open(str(file_shift_index % self.partition_size), "ab")
                np.savetxt(file, buffer, fmt='%1.0f')
                file.close()
                
                buffer = []
                file_shift_index += 1

        for i in range(self.partition_size):
            file = open(str(i + self.partition_size), "ab")
            np.savetxt(file, [], fmt='%1.0f')
            file.close()

        unsorted_file.close()

    def _move_layer(self, move_to_right, layer_height):
        if move_to_right:
            first_source_file_index = 0
            first_target_file_index = self.partition_size
        else:
            first_source_file_index = self.partition_size
            first_target_file_index = 0

        source_files = [] 
        for i in range(first_source_file_index, first_source_file_index + self.partition_size):
            source_files.append(open(str(i), "r"))

        transfered_values_cnt = 0
        while transfered_values_cnt < self.input_array_size:
            for target_file_index in range(first_target_file_index, first_target_file_index + self.partition_size):
                if transfered_values_cnt >= self.input_array_size:
                    break

                target_file = open(str(target_file_index), "ab")

                merger_queue = PriorityQueue()
                iterators_state = []
                for i in range(self.partition_size):
                    try:
                        merger_queue.put((int(source_files[i].readline()), i))
                        iterators_state.append(1)
                    except:
                        iterators_state.append(0)
                
                while not merger_queue.empty():
                    (value, file_index) = merger_queue.get()
                    np.savetxt(target_file, [int(value)], fmt='%1.0f')
                    transfered_values_cnt += 1
                    if iterators_state[file_index] < layer_height:
                        try:
                            merger_queue.put((int(source_files[file_index].readline()), file_index))
                            iterators_state[file_index] += 1
                        except:
                            pass
                
                target_file.close()

        for i in range(self.partition_size):
            source_files[i].close()
        
        for i in range(first_source_file_index, first_source_file_index + self.partition_size):
            np.savetxt(str(i), [], fmt='%1.0f')

    def run(self, output_filename):
        time_start_ns = time.time_ns()

        current_layer_height = self.buffer_size

        move_to_right = True
        while current_layer_height * self.partition_size < self.input_array_size:
            self._move_layer(move_to_right, current_layer_height)
            current_layer_height *= self.partition_size
            move_to_right = not move_to_right
        self._move_layer(move_to_right, self.input_array_size)

        if move_to_right:
            sorted_file_index = self.partition_size
        else:
            sorted_file_index = 0
        sorted_file = open(str(sorted_file_index), "r")

        output_file = open(output_filename, "ab")
        for line in sorted_file.readlines():
            np.savetxt(output_file, [int(line)], fmt='%1.0f')
        output_file.close()

        sorted_file.close()
        np.savetxt(str(sorted_file_index), [], fmt='%1.0f')

        self.execution_time = (time.time_ns() - time_start_ns) / 1e9

ARRAY_SIZE = 100
BUFFER_SIZE = 10
FILES_QUANTITY = 6
INPUT_FILENAME = 'unsorted.csv'
OUTPUT_FILENAME = 'sorted.csv'

unsorted_array = np.arange(ARRAY_SIZE)
np.random.shuffle(unsorted_array)
np.savetxt(INPUT_FILENAME, unsorted_array, fmt = '%1.0f')

balanced_multiway_sorter = BalancedMultiwaySorter(INPUT_FILENAME, BUFFER_SIZE, FILES_QUANTITY)
balanced_multiway_sorter.run(OUTPUT_FILENAME)
print(balanced_multiway_sorter.execution_time)