# task_1
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

import numpy as np


def print_arr(a):
    return np.array(a)


l = [5, 3, 6, 8, 7]


# task_2
# Write a NumPy program to create a NumPy array with values ranging from 2 to 10.

def array_range(a, b):
    return np.arange(a, b)


# task_3
# Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
def update(a, b):
    arr2 = np.zeros(a)
    arr2[5:8] = b
    return arr2


# task_4
# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

arr3 = np.array([[1, 3, 6, 7, 8], [3, 2, 5, 7, 8]])
l1 = arr3[0]
l2 = arr3[1]


def main():
    print(print_arr(l))
    print(array_range(2, 10))
    print(update(10, 11))
    np.in1d(l1, l2)


main()
