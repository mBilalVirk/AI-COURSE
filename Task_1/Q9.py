# Q9: Declare a string “Python lab conduction” and print the address by location for each of the character in the string.
pyLab = "Python lab conduction"
print("Location of P is ", id(pyLab[0]))
print("Location of y is ", id(pyLab[1]))
print("Location of t is ", id(pyLab[2]))
print("Location of h is ", id(pyLab[3]))
print("Location of o is ", id(pyLab[4]))
print("Location of n is ", id(pyLab[5]))
print("Location of space is ", id(pyLab[6]))
print("Location of l is ", id(pyLab[7]))
print("Location of a is ", id(pyLab[8]))
print("Location of b is ", id(pyLab[9]))
print("Location of space is ", id(pyLab[10]))
print("Location of c is ", id(pyLab[11]))
print("Location of o is ", id(pyLab[12]))
print("Location of n is ", id(pyLab[13]))
print("Location of d is ", id(pyLab[14]))
print("Location of u is ", id(pyLab[15]))
print("Location of c is ", id(pyLab[16]))
print("Location of t is ", id(pyLab[17]))
print("Location of i is ", id(pyLab[18]))
print("Location of o is ", id(pyLab[19]))
print("Location of n is ", id(pyLab[20]))
print("=================================")
for char in pyLab:
    print(f"Location of n is {char} {id(char)}")