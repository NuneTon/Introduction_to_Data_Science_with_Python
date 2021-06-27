#Task 1
# Write a Python function which returns factorial value of given number n.

def factorial(n): #recursion
    if n==1:
        return 1
    return factorial(n-1)*n
f=factorial(5)
print(f)

def factorial_1(m):
    i=1
    s=1
    while i<=m:
        s*=i
        i+=1
    return s
f_1=factorial_1(5)
print(f_1)

# Task 2
# Write a Python function which returns the n-th element of the fibonacci series.

def fibonacci(n): # 0 1 1 2 3 5 8 ...
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

f=fibonacci(5)
print(f)