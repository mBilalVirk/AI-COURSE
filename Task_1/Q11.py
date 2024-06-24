# Q: Write a standard program to perform arithmetic operations on two numbers in python.
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else 'undefined (division by zero)'
print("addition", addition)
print("subtraction", subtraction)
print("multiplication", multiplication)
print("division", division)