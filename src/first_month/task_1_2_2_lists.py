#Task 1
# Write a Python program to multiply all the items in a list.

# l = [4, 9, 8, 7, 6]
# m = 1
# i = 0
# while i < len(l):
#     m = m * l[i]
#     i += 1
# print(m)

# Task 2
# Write a Python program to get the largest number from a list.

# l = [45, 69, 87, 25, 1, 36, 98, 65, 47]
# l.sort()
# print(l[-1])

#Task 3
# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
# l = []
# i = 1
# while i < 31:
#     l.append(i * i)
#     i += 1
# print(l[5:])


#Task 4
# Write a Python program to remove duplicates from a list

l = [9, 4, 5, 6, 8, 7, 1, 2, 3, 5, 8, 9, 6, 4, 77, 77]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)


#Task 5
# Write a Python program to find the most appeared element in a list.

# l = [5, 5, 6, 9, 8, 5, 3, 2, 1, 4, 5]
# i = 0
# c = 0
# often_item = 0
# while i < len(l):
#     max_count = l.count(l[i])
#     if max_count > c:
#         c = max_count
#         often_item = l[i]
#     i += 1
# print(often_item)
