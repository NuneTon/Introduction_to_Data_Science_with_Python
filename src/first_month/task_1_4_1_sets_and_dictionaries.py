#Task 1
#Write a python program which returns a given list without duplicates.

l=[4,5,8,9,6,3,5,5,7,8,4,5,2]
s=set(l)
w=list(s)
print(w)

def no_dublicates(l):
    s = set(l)
    w = list(s)
    print(w)
no_dublicates(l)


#Task 2
#Write a python program which returns common elements of 2 lists.

a=[4,5,8,7,9,6,5,5,3]
b=[5,5,8,4,3,0,12,56,8,4]
d=set(a)& set(b)
print(d)

def common(a,b):
    d = set(a) & set(b)
    print(d)
common(a,b)


#Task 3
#Write a python program which return elements which are in first list but not in second

a=[5,5,8,4,3,0,12,56,8,4]
b=[4,5,8,7,9,6,5,5,3]
d=set(a)-set(b)
print(d)

def difference(a,b):
    d = set(a) - set(b)
    print(d)
difference(a,b)


#Task 4
#Write a python program which return elements are or in first list, either in second, but not in both

a=[5,5,8,4,3,0,12,56,8,4]
b=[4,5,8,7,9,6,5,5,3]
d=set(a)^ set(b)
print(d)

def symmetric_diff(a,b):
    d = set(a) ^ set(b)
    print(d)
symmetric_diff(a,b)


#Task 5
#Write a python program which return elements which are or in first, either in second, or in both

a=[5,5,8,4,3,0,12,56,8,4]
b=[4,5,8,7,9,6,5,5,3]
d=set(a) | set(b)
print(d)

def union(a,b):
    d = set(a) | set(b)
    print(d)
union(a,b)

#Task 6
#Write  python function which get set and element value, and remove from set element with given value if exist

a= {4,1,2,3,5,7,8,9}
b=5
if b in a:
    print(a-{b})
a.remove(b)
print(a)
def remove(a,b):
    if b in a:
        print(a - {b})
    a.remove(b)
    print(a)
remove(a,b)

#Task 7
#Write a python python program, which return list from given set, where each element of list, is equal to cub of set element

a={5,4,3,9,8,7,4}
l=[]
for i in a:
    l.append(i**3)
print(l)

def cube(a):
    l = []
    for i in a:
        l.append(i ** 3)
    print(l)
cube(a)
