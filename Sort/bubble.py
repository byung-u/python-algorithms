#!/usr/bin/env python3
'''
https://en.wikipedia.org/wiki/Bubble_sort

Data structure: Array

Performance
    Worst-case  : O(n^2)
    Best-case   : O(n)
    Average     : O(n^2)

    Worst-case space complexity: O(1)
'''


def bubble_sort(arr_list):
    for i in range(len(arr_list) - 1):
        for j in range(i + 1, len(arr_list)):
            if arr_list[i] > arr_list[j]:
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]


arr_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(arr_list)
print(arr_list)
