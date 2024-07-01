import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=["sepal length", "sepal width", "petal length", "petal width", "species"])

# 	First 3 rows
print("Print First 3 rows")
print(data.head(3))

# Last 5 rows
print("Print Last 5 rows")
print(data.tail(5))
# Number of rows and columns
print("Number of rows and columns:")
print(data.shape)
# Add and drop any column
data["sepal length + width"] = data["sepal length"] + data["sepal length"]
print("Add and drop any column")
print(data.head())

# Drop column
data = data.drop(columns=["sepal length + width"])
print("Data with column dropped:")
print(data.head())