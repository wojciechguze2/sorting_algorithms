import sys
import time
from random import randint

from sorting_algorithms import Sort
import threading

threading.stack_size(64 * 64 * 2048 * 16)
sys.setrecursionlimit(10000000)


def generate(input_list: list, sorting_algorithm, sorting_algorithm_name: str) -> dict:
    start_timer = time.perf_counter()
    sorting_algorithm(input_list)
    end_timer = time.perf_counter()

    time_elapsed = end_timer - start_timer

    return {
        'sorting_algorithm_name': sorting_algorithm_name,
        'time_elapsed': time_elapsed,
        'list_length': len(input_list)
    }


sorting_algorithms = Sort()
list_of_numbers = [randint(0, 100) for _ in range(10000)]


def run_insertion_sort_test():
    print(generate(list_of_numbers, sorting_algorithms.insertion_sort, 'insertion_sort'))


def run_selection_sort_test():
    print(generate(list_of_numbers, sorting_algorithms.selection_sort, 'selection_sort'))


def run_bubble_sort_test():
    print(generate(list_of_numbers, sorting_algorithms.bubble_sort, 'bubble_sort'))


def run_quick_sort_test():
    print(generate(list_of_numbers, sorting_algorithms.quick_sort, 'quick_sort'))


def run_merge_sort_test():
    print(generate(list_of_numbers, sorting_algorithms.merge_sort, 'merge_sort'))


threads = [
    threading.Thread(target=run_insertion_sort_test, daemon=True),
    threading.Thread(target=run_selection_sort_test, daemon=True),
    threading.Thread(target=run_bubble_sort_test, daemon=True),
    threading.Thread(target=run_quick_sort_test, daemon=True),
    threading.Thread(target=run_merge_sort_test, daemon=True)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
