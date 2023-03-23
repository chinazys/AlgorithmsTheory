from sorters.insertions_sorter import InsertionsSorter
from sorters.selection_sorter import SelectionSorter
from sorters.bubble_sorter import BubbleSorter
from sorters.counting_sorter import CountingSorter
from sorters.heap_sorter import HeapSorter
from sorters.smooth_sorter import SmoothSorter
from util.array_generator import generate_array

NUMBER_OF_MEASURES = 50

def _measure_sorter(sorter, array):
    sorter.reinitialize(array)
    sorter.run()
    return sorter.execution_time
        
def measure_all_sorters(array_type, min_length, max_length):
    n_measures = []
    t_measures = [[], [], [], [], [],[]]
    sorters = [InsertionsSorter(), SelectionSorter(), BubbleSorter(), CountingSorter(), HeapSorter(), SmoothSorter()]

    cur_length = min_length
    step =  max(1, int((max_length - min_length) / (NUMBER_OF_MEASURES - 1)))
    
    while cur_length <= max_length:
        array = generate_array(array_type, cur_length)
        
        n_measures.append(cur_length)
        
        for i, sorter in enumerate(sorters):
            t_measures[i].append(_measure_sorter(sorter, array))

        cur_length += step

    return (n_measures, t_measures)