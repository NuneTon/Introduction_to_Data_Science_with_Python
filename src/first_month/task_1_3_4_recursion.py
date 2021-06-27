#Task 1
#Write a Python function, which Implements the Euler function.
#Euler function is return a count of numbers not great than N, which are mutually simple with N.
#Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which returns a count of numbers mutually simple with given N.

def euler(n):
    s = 0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0 and n % j == 0:
                s += 1
    print(s)

    return n - s - 1


e = euler(36)
print(e)


#Task 2
#Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it's lucky or not.

def isLucky(n):
    s = str(n)
    l = list(s)
    j = int((len(l) / 2))
    for i in range(len(l)):
        l[i] = int(l[i])
    if sum(l[:j]) == sum(l[j:]):
        print(True)
    else:
        print(False)


isLucky(102201)

#Task 3
#The robot is standing on a rectangular grid and is currently located at the point (X0, Y0). The coordinates are integers. It receives N remote commands(list with n elements each of them is a command). Each command is one of : up, down, left, right. Upon receiving a correct command, the robot moves one unit in the given direction. If the robot receives an incorrect command, it simply ignores it. Where will the robot be located after following all the commands?

def command(*args):
    x = int(input("X is - "))
    y = int(input("Y is - "))
    for n in args:
        if n == "up":
            y += 1
        if n == "down":
            y -= 1
        if n == "right":
            x += 1
        if n == "left":
            x -= 1
    print("X - ", x, "\nY - ", y)


command("up", "up", "right", "left")

#Task 4
#Write a python function, which returns the sum of digits of given number N

def sum_digits(N):
    s = str(N)
    l = list(s)
    j = len(l)
    for i in range(j):
        l[i] = int(l[i])
    return sum(l)


print(sum_digits(45678))

#Task 5
#Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121

def next_palindrome(n):
    while True:
        m = str(n)
        if m == m[::-1]:
            print(m)
            break
        n += 1


next_palindrome(1550)
