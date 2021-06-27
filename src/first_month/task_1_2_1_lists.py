# Task 1
# Write a Python program to get the largest number from a list.

l = [5, 8, 9, 6, 3, 2, 1, 7, 5, 3, 5]
l.sort(reverse=True)
print(l[0])


#Task 2
# Write a Python program to get the frequency of the given element in a list to.
l = [7, 8, 9, 5, 8, 7, 4, 2, 5, 8, 6, 3, 8, 8]
print(l.count(8))


#Task 3
# Write a Python program to remove the second element from a given list, if we know that the first elements index with that value is n.
l = [4, 5, 6, 9, 8, 7, 2, 3, 6, 5, 8, 4]
n = 1
z = l.index(5, n + 1, len(l))
l.pop(z)
print(l)
