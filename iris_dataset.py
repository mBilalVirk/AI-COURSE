import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=["sepal length", "sepal width", "petal length", "petal width", "species"])
print(data)