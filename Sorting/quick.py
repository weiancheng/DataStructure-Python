#!/usr/bin/env python3

"""
"
" Author: Weian Cheng
"
" Data Structure
" Quick Sort
"
" 2016/10/29
"
"""

def qsort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    return qsort([x for x in array[1:] if x < pivot]) + \
           [pivot] + \
           qsort([x for x in array[1:] if x > pivot])


def main():
    array = [26, 73, 13, 31, 38]
    print(qsort(array))

if __name__ == "__main__":
    main()
