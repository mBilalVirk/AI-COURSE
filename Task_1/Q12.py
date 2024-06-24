""""
Q: Write a Python program to 
a.	Interchange first and last elements in a list
b.	To sum all elements in a list
c.	To calculate mean and median of a list
"""
import statistics
list = [33, 83, 83, 34, 76, 97, 12, 9, 39]
# a.	Interchange first and last elements in a list
print("Original list is: ", list)
list[0], list[-1] = list[-1], list[0]
print("Interchange first and last elements in a list: ", list)

# b. To sum all elements in a list
sum = sum(list)
print("To sum all elements in a list", sum)

# c.	To calculate mean and median of a list
print("Mean: ", statistics.mean(list))
print("Median: ", statistics.median(list))