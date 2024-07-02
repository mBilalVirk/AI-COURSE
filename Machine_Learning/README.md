NAVTACC
Module: “Artificial Intelligence”

Machine Learning Libraries & Data Manipulation

Introduction to important libraries

1. Matplotlib
   Matplotlib is a low-level graph plotting library in python that serves as a visualization utility.
   Installation of Matplotlib
   If there is no pre-installed matplotlib in your python editor, then install it using this command:

Once Matplotlib is installed, import it in your applications by adding the import module statement as follows:

pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
Matplotlib Plotting
The plot() function is used to draw points (markers) in a diagram. By default, the plot() function draws a line from point to point. The function takes parameters for specifying points in the diagram. Parameter 1 is an array containing the points on the x-axis. Parameter 2 is an array containing the points on the y-axis.

2. Pandas
   Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"
   Installation of Pandas
   If there are no pre-installed pandas in your python editor, then install it using this command:

Once Pandas is installed, import it in your applications by adding the import keyword. The primary two components of pandas are the Series and DataFrame.

1. Panda Series:
   A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc. With the index argument, you can name your own labels. 2. Panda DataFrames
A Pandas DataFrame is a 2-dimensional data structure, like a 2-dimensional array, or a table with rows and columns.

Loading and reading data from CSVs

1. Create a new text file of extension .csv
   • Use the following data:
   sky,air temp,humidity,wind,water,forecast,enjoy sport
   sunny,warm,normal,strong,warm,same,yes
   sunny,warm,high,strong,warm,same,yes
   rainy,cold,high,strong,warm,change,no
   sunny,warm,high,strong,cool,change,yes

• Save it with lab2.csv name
• Create a new python3 file
• Read the data with the command and then display it
import pandas as pd
import numpy as np
data = pd.read_csv('lab2.csv')
data

2. Use the link to load the data: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

LAB TASK 01:
• From above given datasets, write a Pandas program to get the
o First 3 rows
o Last 5 rows
o Number of rows and columns
o Add and drop any column
LAB TASK 02:
Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
Sample Output:
Rows where scorre is missing:
attempts name qualify score
d 3 James no NaN
h 1 laura no Nan

LAB TASK 03:
Write a Pandas program to create a bar plot of the trading volume of Alphabet Inc. stock between two specific dates.
Click to download the dataset.
Sample Output:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

- **Imports**: This line imports the `pandas` library as `pd` for data manipulation and analysis, and the `matplotlib.pyplot` module as `plt` for plotting data.

```python
df = pd.read_csv("alphabet.csv")
```

- **Read CSV File**: This line reads the CSV file named `alphabet.csv` into a DataFrame `df` using the `pd.read_csv` function.

```python
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')
```

- **Define Date Range**: These lines define the start and end dates for the period you are interested in. The `pd.to_datetime` function converts the date strings to `datetime` objects.

```python
df['Date'] = pd.to_datetime(df['Date'])
```

- **Convert Date Column**: This line converts the `Date` column in the DataFrame to `datetime` format. This is necessary for date comparisons and filtering.

```python
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
```

- **Filter Date Range**: This line creates a boolean mask `new_df` where each row is `True` if the `Date` is within the specified range and `False` otherwise.

```python
df1 = df.loc[new_df]
```

- **Apply Filter**: This line uses the boolean mask to filter the DataFrame `df` and creates a new DataFrame `df1` containing only the rows where the `Date` is within the specified range.

```python
df2 = df1.set_index('Date')
```

- **Set Index**: This line sets the `Date` column as the index of the DataFrame `df1`, creating a new DataFrame `df2`. This is useful for time series plotting.

```python
plt.figure(figsize=(6,6))
```

- **Create Figure**: This line creates a new figure for plotting with a specified size of 6x6 inches.

```python
plt.suptitle('Trading Volume of Alphabet Inc. stock,\n01-04-2020 to 30-04-2020', fontsize=16, color='black')
```

- **Set Title**: This line sets the title of the plot with a font size of 16 and the color black. The `\n` is used to add a newline for better readability.

```python
plt.xlabel("Date", fontsize=12, color='black')
plt.ylabel("Trading Volume", fontsize=12, color='black')
```

- **Set Axis Labels**: These lines set the labels for the x-axis and y-axis with a font size of 12 and the color black.

```python
df2['Volume'].plot(kind='bar')
```

- **Plot Data**: This line creates a bar plot of the `Volume` column from `df2`. The `kind='bar'` argument specifies that the plot should be a bar chart.

```python
plt.show()
```

- **Show Plot**: This line displays the plot.

### Full Code with Comments

Here’s the complete code with added comments for clarity:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("alphabet.csv")

# Define the start and end dates for the period of interest
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a boolean mask for the date range
new_df = (df['Date'] >= start_date) & (df['Date'] <= end_date)

# Filter the DataFrame using the boolean mask
df1 = df.loc[new_df]

# Set the 'Date' column as the index of the DataFrame
df2 = df1.set_index('Date')

# Create a new figure for plotting
plt.figure(figsize=(6,6))

# Set the title of the plot
plt.suptitle('Trading Volume of Alphabet Inc. stock,\n01-04-2020 to 30-04-2020', fontsize=16, color='black')

# Set the labels for the x-axis and y-axis
plt.xlabel("Date", fontsize=12, color='black')
plt.ylabel("Trading Volume", fontsize=12, color='black')

# Plot the 'Volume' column as a bar plot
df2['Volume'].plot(kind='bar')

# Display the plot
plt.show()
```

This script filters the trading volume data for Alphabet Inc. stock to the specified date range and visualizes it as a bar plot.
