## Introduction to AI

Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions), and self-correction. AI can be categorized into narrow AI, which is designed to perform a narrow task (e.g., facial recognition or internet searches), and general AI, which can perform any intellectual task that a human can.

### Why Python for AI?

Python has become the de facto language for AI and machine learning (ML) for several reasons:

1. **Simplicity and Readability**: Python's syntax is clean and easy to learn, which makes it accessible for both beginners and experienced programmers. This simplicity allows developers to focus on solving AI problems rather than spending time on complex programming constructs.

2. **Extensive Libraries and Frameworks**: Python offers a vast array of libraries and frameworks that are specifically designed for AI and ML, such as TensorFlow, Keras, PyTorch, scikit-learn, and many others. These tools simplify the development process and enable rapid prototyping.

3. **Community Support**: Python has a large and active community, which means there is a wealth of resources, tutorials, and documentation available. This community support is invaluable when tackling complex AI problems.

4. **Integration**: Python integrates well with other languages and technologies. It can be used to call C/C++ libraries, integrate with Java through Jython, or with .NET through IronPython, making it a versatile tool for AI development.

## Basic Python Syntax vs. C++ Syntax

Python and C++ are both powerful programming languages, but they have some key differences in syntax and structure.

### Hello World

- **Python**:

  ```python
  print("Hello, World!")
  ```

- **C++**:

  ```cpp
  #include <iostream>

  int main() {
      std::cout << "Hello, World!" << std::endl;
      return 0;
  }
  ```

### Variables and Data Types

- **Python**:

  ```python
  x = 5
  y = "Hello"
  print(x, y)
  ```

- **C++**:
  ```cpp
  int x = 5;
  std::string y = "Hello";
  std::cout << x << " " << y << std::endl;
  ```

### Conditionals

- **Python**:

  ```python
  if x > 0:
      print("x is positive")
  elif x == 0:
      print("x is zero")
  else:
      print("x is negative")
  ```

- **C++**:
  ```cpp
  if (x > 0) {
      std::cout << "x is positive" << std::endl;
  } else if (x == 0) {
      std::cout << "x is zero" << std::endl;
  } else {
      std::cout << "x is negative" << std::endl;
  }
  ```

### Loops

- **Python**:

  ```python
  for i in range(5):
      print(i)

  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

- **C++**:

  ```cpp
  for (int i = 0; i < 5; i++) {
      std::cout << i << std::endl;
  }

  int i = 0;
  while (i < 5) {
      std::cout << i << std::endl;
      i++;
  }
  ```

### Functions

- **Python**:

  ```python
  def add(a, b):
      return a + b

  result = add(3, 5)
  print(result)
  ```

- **C++**:

  ```cpp
  int add(int a, int b) {
      return a + b;
  }

  int main() {
      int result = add(3, 5);
      std::cout << result << std::endl;
      return 0;
  }
  ```

Python has a set of reserved words, known as keywords, which have specific meanings and uses. These keywords are part of the Python language syntax and cannot be used as identifiers (variable names, function names, etc.). Here’s a breakdown of how to get and understand Python keywords using the `keyword` module:

### Code Explanation

First, import the `keyword` module, which contains a list of all Python keywords:

```python
import keyword as kw
```

To find out how many keywords there are in Python, use the `len` function on `kw.kwlist`:

```python
print("Total number of keywords:", len(kw.kwlist))
```

This will print the total number of keywords in the current version of Python.

Next, to display the list of all keywords, simply print `kw.kwlist`:

```python
print("Keywords are:", kw.kwlist)
```

### Output Explanation

When you run the above code, the output will look something like this (note that the exact number and list of keywords may vary depending on the Python version):

```
Total number of keywords: 36
Keywords are: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### Sample Explanation

Here are explanations and sample uses of a few Python keywords:

1. **`if`**: Used for conditional statements.

   ```python
   if x > 0:
       print("x is positive")
   ```

2. **`for`**: Used for looping over a sequence (such as a list, tuple, or string).

   ```python
   for i in range(5):
       print(i)
   ```

3. **`def`**: Used to define a function.

   ```python
   def my_function():
       print("Hello, World!")
   ```

4. **`import`**: Used to include a module into the current namespace.

   ```python
   import math
   print(math.sqrt(16))
   ```

5. **`try`**: Used for exception handling.

   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   ```

These keywords are fundamental building blocks of Python programming, and understanding them is essential for writing syntactically correct and functional code. Each keyword has a specific role, and misusing them can lead to syntax errors or unexpected behavior in the program.

### Explanation

There are two methods demonstrated here for formatting strings in Python: the `format` method and f-strings.

#### Using `format` Method

```python
a = 20
b = 10
print("The Variable a = {} and Variable b = {}".format(a, b))
```

- **`"The Variable a = {} and Variable b = {}".format(a, b)`**: This string contains placeholders `{}` that will be replaced by the values of `a` and `b`.
- **`.format(a, b)`**: The `format` method takes the values `a` and `b` and inserts them into the placeholders `{}` in the order they appear.

#### Using f-Strings

```python
a = 20
b = 10
print(f"The Variable a = {a} and Variable b = {b}")
```

- **`f"The Variable a = {a} and Variable b = {b}"`**: This is an f-string (formatted string literal). The `f` before the string tells Python to evaluate expressions inside `{}` and replace them with their values.
- **`{a}` and `{b}`**: These placeholders are replaced directly with the values of `a` and `b`.

### Differences Between `format` and f-Strings

1. **Syntax and Readability**:

   - **`format` Method**: Uses a more verbose syntax where the placeholders `{}` in the string are matched with arguments passed to the `format` method.
     ```python
     "The Variable a = {} and Variable b = {}".format(a, b)
     ```
   - **f-Strings**: Provide a more concise and readable syntax by allowing expressions to be directly embedded inside string literals.
     ```python
     f"The Variable a = {a} and Variable b = {b}"
     ```

2. **Performance**:

   - **f-Strings**: Generally faster than the `format` method because they are evaluated at runtime and are more efficient.
   - **`format` Method**: Slightly slower due to the overhead of the method call.

3. **Flexibility**:
   - **`format` Method**: More flexible for complex formatting tasks, especially when reordering or repeating variables.
     ```python
     "First: {1}, Second: {0}, Again First: {1}".format(a, b)
     ```
   - **f-Strings**: Best suited for simple and straightforward formatting tasks. They support expressions directly inside the braces.
     ```python
     f"The sum of a and b is {a + b}"
     ```

### Output

Both methods will produce the same output for the given examples:

```
The Variable a = 20 and Variable b = 10
The Variable a = 20 and Variable b = 10
```

Despite the different syntax and performance characteristics, both achieve the same result: dynamically inserting the values of `a` and `b` into the string.

Machine learning is a subset of artificial intelligence (AI) that involves the development of algorithms and statistical models that enable computers to perform specific tasks without explicit instructions. Instead, these models learn from and make predictions or decisions based on data. The primary goal of machine learning is to create systems that can adapt and improve their performance over time as they are exposed to more data.

There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.

### 1. Supervised Learning

Supervised learning is the most common type of machine learning. In supervised learning, the algorithm is trained on a labeled dataset, which means that each training example is paired with an output label. The goal is for the model to learn a mapping from inputs to outputs and make predictions on new, unseen data.

**Key concepts:**

- **Training Data:** Consists of input-output pairs.
- **Labels:** Known outputs used for training.
- **Goal:** Learn the mapping from input to output.

**Examples:**

- **Regression:** Predicting a continuous value, such as house prices.
- **Classification:** Predicting a discrete label, such as spam detection in emails.

**Example:**

- **Email Classification:** Training a model to classify emails as either "spam" or "not spam" based on features such as the email's content, sender, and subject line.

### 2. Unsupervised Learning

In unsupervised learning, the algorithm is trained on an unlabeled dataset, meaning the data has no corresponding output labels. The goal is to find hidden patterns or intrinsic structures in the input data.

**Key concepts:**

- **Training Data:** Consists of input data without labels.
- **Goal:** Discover underlying structure or distribution in the data.

**Examples:**

- **Clustering:** Grouping similar data points together, such as customer segmentation in marketing.
- **Dimensionality Reduction:** Reducing the number of features while retaining important information, such as Principal Component Analysis (PCA).

**Example:**

- **Customer Segmentation:** Analyzing customer data to group customers into segments with similar purchasing behaviors without prior knowledge of the categories.

### 3. Reinforcement Learning

Reinforcement learning involves training an agent to make a sequence of decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties and aims to maximize the cumulative reward over time.

**Key concepts:**

- **Agent:** The learner or decision-maker.
- **Environment:** The external system the agent interacts with.
- **Actions:** Choices made by the agent.
- **Rewards:** Feedback from the environment based on the agent's actions.
- **Goal:** Maximize cumulative reward.

**Examples:**

- **Game Playing:** Training an agent to play a game like chess or Go, where the agent learns strategies through trial and error.
- **Robotics:** Teaching robots to navigate environments and perform tasks like picking and placing objects.

**Example:**

- **Self-Driving Cars:** An autonomous vehicle learns to navigate and make driving decisions based on rewards and penalties for safe and unsafe driving behaviors.

### Summary

- **Supervised Learning:** Learn from labeled data to make predictions.
- **Unsupervised Learning:** Find patterns or structure in unlabeled data.
- **Reinforcement Learning:** Learn to make decisions through trial and error to maximize rewards.

Each type of machine learning has its own set of techniques and applications, and the choice of which to use depends on the specific problem and the nature of the data available.

### Lab Task 1

### Q1: Declare 10 identifiers, assign data of multiple types, and print them. Moreover, declare an identifier with the name of a keyword and show the result.

```python
# Declaring 10 identifiers with different data types
int_1 = 10
float_2 = 2.3
str_3 = "Hello World"
lst_4 = [3.3, 4, "Program", "Q1"]
complex_5 = 2 + 3j
bool_6 = True
bool_7 = False
str_8 = "This is a program"
lst_9 = [222, 332.22, "Hello", "Program", "Q1"]
list_10 = [1, 2, 3, 4, 5]

# Printing the identifiers
print("Integer:", int_1)
print("Float:", float_2)
print("String 1:", str_3)
print("List 1:", lst_4)
print("Complex number:", complex_5)
print("Boolean True:", bool_6)
print("Boolean False:", bool_7)
print("String 2:", str_8)
print("List 2:", lst_9)
print("List 3:", list_10)

# Attempting to declare an identifier with the name of a keyword (this will cause an error)
try:
    class = "This will show an error!"  # This line will cause a syntax error
    print(class)
except SyntaxError as e:
    print(f"Syntax error: {e}")
```

### Q2: Import and print all Python keywords.

```python
import keyword

# Printing the total number of keywords and the list of keywords
print("Total number of keywords:", len(keyword.kwlist))
print("Keywords are:", keyword.kwlist)
```

### Q4: Print 5 integer values using the format function. Print the statement “The Temperature in Islamabad today is 22.02 degrees outside!” using format.

```python
# Declaring 5 integer values
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5

# Using the format function to print the integers
print("First Number is {} Second Number is {} Third Number is {} Fourth number is {} Fifth number is {}".format(number1, number2, number3, number4, number5))

# Printing the statement with format function
city = "Islamabad"
temp = 22.02
print("The Temperature in {} today is {} degrees outside!".format(city, temp))
```

### Q5: Add a screenshot of adding single and multiple line comments in Python.

```python
# Following statement prints Hello World on the screen
print("Hello World")

"""
This is a
multi-line
comment
"""
```

### Q6: Assign one same value to 3 different identifiers and print their memory addresses.

```python
# Assigning the same value to 3 different identifiers
first = 40
second = 40
third = 40

# Printing their memory addresses
print(id(first))
print(id(second))
print(id(third))
```

### Q7: Declare 5 identifiers, assign values (int, float, string, Boolean, complex), and print their data types using the `type` function.

```python
# Declaring identifiers with different data types
intIden = 30
floatIden = 30.234
stringIden = "This is a String"
boolIden = True
complexIden = 3 + 3j

# Printing the data types of the identifiers
print(type(intIden))
print(type(floatIden))
print(type(stringIden))
print(type(boolIden))
print(type(complexIden))
```

### Q8: Use `isinstance` to check for float and complex values.

```python
# Checking if a value is a complex number
float_1 = 32.9
print(isinstance(float_1, complex))  # This will return False
```

### Q9: Declare a string “Python lab conduction” and print the address by location for each character in the string.

```python
# Declaring the string
pyLab = "Python lab conduction"

# Printing the memory address of each character in the string
for char in pyLab:
    print(f"Location of '{char}' is {id(char)}")
```

### Q10: Apply slicing on the given list and show the result.

```python
# Given list
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Applying slicing operations
slice1 = L[:]
slice2 = L[5:]
slice3 = L[:5]
slice4 = L[:-2]
slice5 = L[-7:-2]

# Showing the result
print("L[:]:", slice1)
print("L[5:]:", slice2)
print("L[:5]:", slice3)
print("L[:-2]:", slice4)
print("L[-7:-2]:", slice5)
```

### Standard Program to Perform Arithmetic Operations on Two Numbers in Python

```python
# Taking input from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else 'undefined (division by zero)'

# Printing the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
```

### Python Program for Various List Operations

```python
import statistics

# Given list
lst = [33, 83, 83, 34, 76, 97, 12, 9, 39]

# a. Interchange first and last elements in a list
print("Original list is:", lst)
lst[0], lst[-1] = lst[-1], lst[0]
print("Interchanged first and last elements in a list:", lst)

# b. To sum all elements in a list
sum_of_elements = sum(lst)
print("Sum of all elements in a list:", sum_of_elements)

# c. To calculate mean and median of a list
print("Mean:", statistics.mean(lst))
print("Median:", statistics.median(lst))
```
