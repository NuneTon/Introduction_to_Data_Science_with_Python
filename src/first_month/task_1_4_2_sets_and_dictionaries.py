#Task 1
# Write a python program, which adds a new value with the given key in dict.

a={1: "second_month", 2: "bbb", 3: "ccc"}
a[1]="ddd"
print(a)

#Task 2
# Write a python program which concat 2 dicts

a={1: "second_month", 2: "bbb", 3: "ccc"}
b={4: "ddd", 5: "eee", 6: "fff"}
a.update(b)
print(a)

#Task 3
# Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers

N = 3
a = {}
for i in range(1, N + 1):
    a[i] = i ** 3
print(a)

#Task 4
#Write a python program which create dict from 2 lists with the same length

a = [1, 5, 6, 3, 7, 8]
b = ["a", "b", "c", "d", "e", "f"]
n = len(a)
d = {}
for i in range(n):
    d[a[i]] = b[i]
print(d)

#Task 5
#Write a python program which gets the maximum and minimum values of a dictionary.
a = {"a": 2, "b": 5, "c": 8, "d": 7, "e": 6}
l = list(a.values())
l.sort()
print("Max value is ", l[-1], ", Min value is ", l[0])

#Task 6
#Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.

a = {1: "second_month", 2: "bbb", 3: "ccc"}
b = {4: "ddd", 2: "eee", 6: "fff"}
l1 = list(a.keys())
l2 = list(b.keys())
for i in l2:
    if i in l1:
        a[i] = a[i] + b[i]
    else:
        a[i] = b[i]
print(a)

#Task7
#Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string

s = "aaabcdeefddddd"
a = {}
for x in s:
    a[x] = s.count(x)
print(a)
