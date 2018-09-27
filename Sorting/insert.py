"""
"
" Author: Weian Cheng
"
" Insertion Sort
"
" Sep 27th, 2018
"
"""

def insert(array):
    if len(array) == 0:
        return

    for i in range(1, len(array)):
        current = i
        for j in range(i-1, -1, -1):  # current
            if array[current] < array[j]:
                array[j], array[current] = array[current], array[j] # swap
                current = j


def main():
    array = [5, 2, 4, 6, 1, 3]
    print('before: ')
    print(array)
    insert(array)
    print('after: ')
    print(array)


if __name__ == '__main__':
    main()
