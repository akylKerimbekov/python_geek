from random import randint
from sorting import Sorting, BubbleSorting, SelectionSorting
from searching import Searching, BinarySearching
from random import choice

unsorted_list = [randint(1, 100) for _ in range(10)]
print(unsorted_list)

sorting = Sorting(BubbleSorting())
bubble_sorted_list = sorting.process(unsorted_list)
print(bubble_sorted_list)

sorting.strategy = SelectionSorting()
selected_sorted_list = sorting.process(unsorted_list)
print(selected_sorted_list)

element = choice(unsorted_list)
searching_context = Searching(BinarySearching())
searching_context.process(selected_sorted_list, element)