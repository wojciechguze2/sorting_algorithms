# naive sorting algorithms
from random import randint


def selection_sort(unsorted_list: list) -> list:
    # iterating over unsorted part of list to find min value and put it to the end of sorted part

    unsorted_list_len = len(unsorted_list)

    for i in range(unsorted_list_len):
        minimum_value_j_index = i

        for j in range(i + 1, unsorted_list_len):
            if unsorted_list[j] < unsorted_list[minimum_value_j_index]:
                minimum_value_j_index = j

        swap(unsorted_list, i, minimum_value_j_index)

    return unsorted_list


def insertion_sort(unsorted_list: list, n=None) -> list:
    # comparing n and n + 1 and swapping, calling self recursively n times (n - length of list)
    unsorted_list_len = len(unsorted_list)

    if n is None:
        n = unsorted_list_len - 1

    if n > 0:
        insertion_sort(unsorted_list, n - 1)

    for i in range(unsorted_list_len - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            swap(unsorted_list, i, i + 1)

    return unsorted_list


def bubble_sort(unsorted_list: list) -> list:
    # comparing n and n + 1 until list is not sorted
    unsorted_list_len = len(unsorted_list)

    for i in range(unsorted_list_len):
        for j in range(unsorted_list_len - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                swap(unsorted_list, j, j + 1)

    return unsorted_list


# divide and conquer sorting algorithms


def quick_sort(unsorted_list: list) -> list:
    return []


def merge_sort(unsorted_list: list) -> list:
    return []


def kopiec(unsorted_list: list) -> list:
    return []


# helping algorithms

def swap(unsorted_list: list, index_1: int, index_2: int):
    unsorted_list[index_1], unsorted_list[index_2] = unsorted_list[index_2], unsorted_list[index_1]


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
