#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Bubble sort
"
" 2016/10/27
"
"""


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]  # swap


def main():
    array = [5, 4, 3, 2, 1]
    bubble_sort(array)

if __name__ == "__main__":
    main()
