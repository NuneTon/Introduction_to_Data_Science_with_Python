#Task 1
# Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.

def div(a, b):
    if a % b:
        return True
    return False


a = div(5, 15)
print(a)

#Task 2
# Write a Python function, which gets a number, and return True if that number is palindrome, otherwise False

def palindrome(a):
    b = str(a)
    if b == b[::-1]:
        return True
    return False
p = palindrome(505)
print(p)

#Task 3
#Write a Python function, which gets a number, and return True if that number is prime, otherwise False.
def prime(n):
    if n==1:
        return False
    for i in range(2, n): # sa shut lucel ei, gitei
        if n % i:
            return True
        return False


a = prime(1)
print(a)

#Task 4
#Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.

def proper(a):
    l = []
    for j in range(1, a):
        if a % j == 0:
            l.append(j)
    if sum(l) == a:
        return True
    return False


x = proper(77)
print(x)


#Task 5
#Write a function, which gets 2 numbers, and return their Great common divisor
def great_common_divisor(a, b):
    l = []
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            l.append(i)
    return max(l)


w = great_common_divisor(15, 75)
print(w)
