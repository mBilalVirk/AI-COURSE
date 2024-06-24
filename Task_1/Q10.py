# Q10:Apply slicing [:],[5:],[:5], [:-2], [-7:-2] on the given list  L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] and show the result.
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# Apply slicing operations
slice1 = L[:]
slice2 = L[5:]
slice3 = L[:5]
slice4 = L[:-2]
slice5 = L[-7:-2]
# showing the result
print("L[:]: {}".format(slice1))
print("L[5:]: {}".format(slice2))
print("L[:5]: {}".format(slice3))
print("L[:-2]: {}".format(slice4))
print("L[-7:-2]: {}".format(slice5))