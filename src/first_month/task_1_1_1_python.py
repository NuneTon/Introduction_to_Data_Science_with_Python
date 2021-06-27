# Task 1
# Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.

a = 1
b = 2
s = a * b / 2
print("The area is ", s)


# Task 2
# Input a natural number n and output its last digit.

n = input("Input a natural number ")
print(str(n)[-1])


# Task 3

# Input a two-digit natural number and output the sum of its digits.
n = int(input("Input a two-digit natural number "))
print(n // 10 + n % 10)


# Task 4
# You are given the first and second number in an arithmetic progression and natural number  n. Find n-th element of arithmetic progression.

n1 = 2
n2 = 4
n = 7
n_th = n1 + (n - 1) * (n2 - n1)
print(n, "-th number is ", n_th)
