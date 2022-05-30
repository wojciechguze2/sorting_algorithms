# naive sorting algorithms
from random import randint


def selection_sort(list_of_numbers: list) -> list:
    # iterating over unsorted part of list to find min value and put it to the end of sorted part
    list_of_numbers_len = len(list_of_numbers)

    for i in range(list_of_numbers_len):
        minimum_value_j_index = i

        for j in range(i + 1, list_of_numbers_len):
            if list_of_numbers[j] < list_of_numbers[minimum_value_j_index]:
                minimum_value_j_index = j

        swap(list_of_numbers, i, minimum_value_j_index)

    return list_of_numbers


def insertion_sort(list_of_numbers: list, n=None) -> list:
    # comparing n and n + 1 and swapping, calling self recursively n times (n - length of list)
    list_of_numbers_len = len(list_of_numbers)

    if n is None:
        n = list_of_numbers_len - 1

    if n > 0:
        insertion_sort(list_of_numbers, n - 1)

    for i in range(list_of_numbers_len - 1):
        if list_of_numbers[i] > list_of_numbers[i + 1]:
            swap(list_of_numbers, i, i + 1)

    return list_of_numbers


def bubble_sort(list_of_numbers: list) -> list:
    # comparing n and n + 1 until list is not sorted
    list_of_numbers_len = len(list_of_numbers)

    for i in range(list_of_numbers_len):
        for j in range(list_of_numbers_len - i - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                swap(list_of_numbers, j, j + 1)

    return list_of_numbers


# divide and conquer sorting algorithms


def quick_sort(list_of_numbers: list) -> list:
    return []


def merge_sort(list_of_numbers: list) -> list:
    return []


def heap_sort(list_of_numbers: list) -> list:
    return []


# helping algorithms

def swap(list_of_numbers: list, index_1: int, index_2: int):
    list_of_numbers[index_1], list_of_numbers[index_2] = list_of_numbers[index_2], list_of_numbers[index_1]


test_lists = [
    [
        randint(1, 10)
        for i in range(10)
    ]
    for j in range(6)
]

print(selection_sort(test_lists[0]))
print(insertion_sort(test_lists[1]))
print(bubble_sort(test_lists[2]))
