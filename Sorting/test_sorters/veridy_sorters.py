from sorters.insertions_sorter import InsertionsSorter
from sorters.selection_sorter import SelectionSorter
from sorters.bubble_sorter import BubbleSorter
from sorters.counting_sorter import CountingSorter
from sorters.heap_sorter import HeapSorter
from sorters.smooth_sorter import SmoothSorter
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
    sorters = [InsertionsSorter(), SelectionSorter(), BubbleSorter(), CountingSorter(), HeapSorter(), SmoothSorter()]

    verification_array = generate_array(ARRAY_RANDOM, VERIFICATION_ARRAY_LENGTH, min_array_value=VERIFICATION_ARRAY_MIN, max_array_value=VERIFICATION_ARRAY_MAX)
    print('Verification array:', verification_array)
    print('Sorted arrays:')
    for sorter in sorters:
        sorted_array = _verify_sorter(sorter, verification_array)
        print(sorted_array)