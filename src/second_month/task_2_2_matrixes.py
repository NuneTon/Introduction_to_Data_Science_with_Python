import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

# task1
# Write a NumPy program to compute the multiplication of two given matrixes

def mul(a, b):
    return a.dot(b)


a = np.random.randn(2, 3)
b = np.random.randn(3, 2)


# task2
# Write a NumPy program to compute the determinant of an array

c = np.array([[1, 2], [3, 4]])


# task3
# Write a NumPy program to compute the sum of the diagonal element of a given array
# task4
# Write a NumPy program to compute the inverse of a given matrix
# task5
# Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.

#task 3,4,5 aren in main function


def main():
    print(mul(a,b))
    print(det(c))
    print(np.trace(c))
    print(c.dot(inv(c)))
    arr = np.random.rand(5, 5)
    np.save("Other/array_file", arr)
    d = np.load("Other/array_file.npy")
    print(d)

main()