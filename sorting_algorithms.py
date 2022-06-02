class Sort:
    """
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers
    """

    # naive sorting algorithms

    def selection_sort(self, list_of_numbers: list) -> list:
        # iterating over unsorted part of list to find min value and put it to the end of sorted part
        list_of_numbers_len = len(list_of_numbers)

        for i in range(list_of_numbers_len):
            minimum_value_j_index = i

            for j in range(i + 1, list_of_numbers_len):
                if list_of_numbers[j] < list_of_numbers[minimum_value_j_index]:
                    minimum_value_j_index = j

            self.swap(list_of_numbers, i, minimum_value_j_index)

        return list_of_numbers

    def insertion_sort(self, list_of_numbers: list, n=None) -> list:
        # comparing n and n + 1 and swapping, calling self recursively n times (n - length of list)
        list_of_numbers_len = len(list_of_numbers)

        if n is None:
            n = list_of_numbers_len - 1

        if n > 0:
            self.insertion_sort(list_of_numbers, n - 1)

        for i in range(list_of_numbers_len - 1):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                self.swap(list_of_numbers, i, i + 1)

        return list_of_numbers

    def bubble_sort(self, list_of_numbers: list) -> list:
        # comparing n and n + 1 until list is not sorted
        list_of_numbers_len = len(list_of_numbers)

        for i in range(list_of_numbers_len):
            for j in range(list_of_numbers_len - i - 1):
                if list_of_numbers[j] > list_of_numbers[j + 1]:
                    self.swap(list_of_numbers, j, j + 1)

        return list_of_numbers

    # divide and conquer sorting algorithms

    def quick_sort(self, list_of_numbers: list) -> list:
        # (recursively) sorting numbers on the left of pivot and right
        # removes duplicates todo: fix this
        list_of_numbers_len = len(list_of_numbers)

        if list_of_numbers_len <= 1:
            return list_of_numbers

        pivot = list_of_numbers[list_of_numbers_len // 2]

        left = [n for n in list_of_numbers if n < pivot]
        right = [n for n in list_of_numbers if n > pivot]

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def merge_sort(self, list_of_numbers: list) -> list:
        # split list into left and right half, do the same on each of them, sort, then merge into 1
        list_of_numbers_len = len(list_of_numbers)

        if list_of_numbers_len > 1:
            middle = list_of_numbers_len // 2

            left = list_of_numbers[0:middle]
            right = list_of_numbers[middle:]

            self.merge_sort(left)
            self.merge_sort(right)

            lc, rc, i = 0, 0, 0
            len_left, len_right = len(left), len(right)

            while lc < len_left and rc < len_right:
                if left[lc] < right[rc]:
                    list_of_numbers[i] = left[lc]
                    lc += 1
                else:
                    list_of_numbers[i] = right[rc]
                    rc += 1

                i += 1

            while lc < len_left:
                list_of_numbers[i] = left[lc]
                lc += 1
                i += 1

            while rc < len_right:
                list_of_numbers[i] = right[rc]
                rc += 1
                i += 1

            return list_of_numbers

    def heap_sort(self, list_of_numbers: list) -> list:
        return []

    # other sorting algorithms

    def count_sort(self, list_of_numbers: list) -> list:
        return []

    def shell_sort(self, list_of_numbers: list) -> list:
        return []

    # helping algorithms

    @staticmethod
    def swap(list_of_numbers: list, index_1: int, index_2: int):
        list_of_numbers[index_1], list_of_numbers[index_2] = list_of_numbers[index_2], list_of_numbers[index_1]