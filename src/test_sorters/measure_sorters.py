from sorters.sorter import Sorter
from sorters.bubble_sorter import BubbleSorter
from sorters.insertions_sorter import InsertionsSorter
from sorters.selection_sorter import SelectionSorter
from sorters.counting_sorter import CountingSorter
from sorters.heap_sorter import HeapSorter
from sorters.smooth_sorter import SmoothSorter 
from sorters.lomuto_sorter import LomutoSorter
from sorters.hoares_sorter import HoaresSorter
from sorters.bentley_sorter import BentleySorter
from sorters.merge_down_sorter import MergeDownSorter
from sorters.merge_up_sorter import MergeUpSorter
from sorters.lsd_sorter import LSDSorter
from sorters.msd_sorter import MSDSorter
from util.array_generator import generate_array

NUMBER_OF_MEASURES = 25

def _measure_sorter(sorter, array):
    sorter.reinitialize(array)
    sorter.run()
    return sorter.execution_time
        
def measure_all_sorters(array_type, min_length, max_length):
    n_measures = []
    t_measures = [[], [], [], [], [], [], [], [], []]
    #sorters = [SelectionSorter(), HeapSorter(), LomutoSorter(), HoaresSorter(), BentleySorter(), MergeDownSorter(), MergeUpSorter()]
    sorters = [LSDSorter(2), LSDSorter(10), LSDSorter(16), MSDSorter(2), MSDSorter(10), MSDSorter(16), HeapSorter(), BentleySorter(), Sorter()]
    
    cur_length = min_length
    step =  max(1, int((max_length - min_length) / (NUMBER_OF_MEASURES - 1)))
    
    while cur_length <= max_length:
        array = generate_array(array_type, cur_length)
        
        n_measures.append(cur_length)
        
        for i, sorter in enumerate(sorters):
            t_measures[i].append(_measure_sorter(sorter, array))

        cur_length += step

    return (n_measures, t_measures)