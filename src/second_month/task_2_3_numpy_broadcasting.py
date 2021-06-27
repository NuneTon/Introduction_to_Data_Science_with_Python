import numpy as np
from numpy import newaxis

# task1

arr = np.random.randn(4, 5)
print(arr)


def min_max_arr(arr):
    return "Min value of arr is ", np.min(arr), " and Max value of arr is ", np.max(arr)


# task2
def min_max_arr_for_second_column(arr):
    return "Min value for second column is ", np.min(arr, axis=0)[1], " and Max value for second column is ", np.max(arr, axis=0)[1]



# task3
def arr_median(arr):
    return np.median(arr)


# task4




def mul():
    a = np.random.randn(1,4)
    b = np.random.randn(2,4)
    b = b.reshape(4, 2)
    return a.dot(b)


def main():
    print(min_max_arr(arr))
    print(min_max_arr_for_second_column(arr))
    print("Median for arr is", arr_median(arr))
    print("A multiplicated by b is", mul())


main()
