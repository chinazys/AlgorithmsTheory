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
from util.array_type_enums import ARRAY_RANDOM

VERIFICATION_ARRAY_LENGTH = 10
VERIFICATION_ARRAY_MIN = 0
VERIFICATION_ARRAY_MAX = 10

def _verify_sorter(sorter, array):
    sorter.reinitialize(array)
    sorter.run()
    return sorter.array
        
def verify_all_sorters():
    # sorters = [SelectionSorter(), HeapSorter(), LomutoSorter(), HoaresSorter(), BentleySorter(), MergeDownSorter(), MergeUpSorter(),]
    sorters = [LSDSorter(2), LSDSorter(10), LSDSorter(16), MSDSorter(2), MSDSorter(10), MSDSorter(16), HeapSorter(), BentleySorter(), Sorter()]

    verification_array = generate_array(ARRAY_RANDOM, VERIFICATION_ARRAY_LENGTH, min_array_value=VERIFICATION_ARRAY_MIN, max_array_value=VERIFICATION_ARRAY_MAX)
    print('Verification array:', verification_array)
    print('Sorted arrays:')
    for sorter in sorters:
        sorted_array = _verify_sorter(sorter, verification_array)
        print(sorted_array)