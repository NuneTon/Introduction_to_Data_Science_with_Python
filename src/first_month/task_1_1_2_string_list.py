
# STRINGS

#Task 1
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

string = "bshbhdjd"
string_new = string[:2] + string[-2:]
print(string_new)


#Task 2
#Write a Python program to remove the nth index character from a nonempty string.

text = "hcwecu3cec3"
n = 3
text_new = text[:n] + text[n + 1:]
print(text_new)

# Task 3
#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

string = "chbchwvvee"
new_string = string[-1] + string[1:-1] + string[0]
print(new_string)


# Task 4
#Write a Python function to get a string made of 4 copies of the last two characters of a specified string

str = "asdfgk"
copies = str[-2:] * 4
print(copies)


#LISTS

#Task 1
#Write a Python program that make a list from given string
l = []
str = "aaaa"
l.extend(str)
print(l)

#Task 2
#Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.

list = [1, 2, 3, 4, 5, 6, 7]
new_list = list[1:4] + list[6:]
print(new_list)


#Task 3
#Write a Python program which add an element to the given list

a = [5, 6, 8, 9, 7]
b = a + [8]
print(b)


#Task 4
#Write a Python program which concat 2 lists.
c = [4, 5, 6, 9, 8]
d = [8, 8, 8, 5, 4]
e = c + d
print(e)
