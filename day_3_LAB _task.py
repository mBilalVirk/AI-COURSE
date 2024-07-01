# sepal_length  sepal_width  petal_length  petal_width
import pandas as pd
import numpy as np
import seaborn as sns
ds = sns.load_dataset('iris')
ds = ds.drop('species' ,axis=1)
print(ds)
# feature01
sepal_length = ds['sepal_length']
feature01 = sepal_length.to_numpy()
# print(feature01)
feature01_ = feature01.mean()
# feature02
sepal_width = ds['sepal_width']
feature02 = sepal_width.to_numpy()
# print(feature02)
feature02_ = feature02.mean()
# feature03
petal_length = ds['petal_length']
feature03 = petal_length.to_numpy()
# print(feature03)
feature03_ = feature03.mean()
#  feature04
petal_width = ds['petal_width']
feature04 = petal_width.to_numpy()
# print(feature04)
feature04_ = feature04.mean()

# print(feature01_)
# print(feature02_)
# print(feature03_)
# print(feature04_)


mean_values = ds.mean()
print("Mean:\n", mean_values)

# median
# MeanFeature01=sepal_length.median()
# MeanFeature02=sepal_width.median()
# MeanFeature03=petal_length.median()
# MeanFeature04=petal_width.median()
# print("Median of the feature")
# print(MeanFeature01, MeanFeature02, MeanFeature03, MeanFeature04)
# print()
median_values = ds.median()
print("Median:\n", median_values)



# mode
# ModeFeature01=sepal_length.mode()
# ModeFeature02=sepal_width.mode()
# ModeFeature03=petal_length.mode()
# ModeFeature04=petal_width.mode()
# print("Mode of the feature")
# print(ModeFeature01, ModeFeature02, ModeFeature03, ModeFeature04)

mode_values = ds.mode()
print("Mode:\n", mode_values)
print("\n")

for column in ds.columns[:-1]:  # Exclude the 'species' column
    modes = ds[column].mode()
    if len(modes) > 1:
        print(f"{column} is multimodal: {modes.tolist()}")
    else:
        print(f"{column} is unimodal: {modes[0]}")
print()

# Range of the iris feature

# RangeFeature01 = sepal_length.max() - sepal_length.min()
# RangeFeature02 = sepal_width.max() - sepal_width.min()
# RangeFeature03 = petal_length.max() - petal_length.min()
# RangeFeature04 = petal_width.max() - petal_width.min()
# print("Range of Feature iris: ", RangeFeature01, RangeFeature02, RangeFeature03, RangeFeature04)
# Calculate range for each feature
range_values = ds.max() - ds.min()
print("Range:\n", range_values)
print("\n")
# print()

# VarianceFeature01 = sepal_length.var()
# VarianceFeature02 = sepal_width.var()
# VarianceFeature03 = petal_length.var()
# VarianceFeature04 = petal_width.var()
# print("Variance of the Feature iris: ", VarianceFeature01, VarianceFeature02,VarianceFeature03, VarianceFeature04)
# print()
# Calculate variance for each feature
variance_values = ds.var()
print("Variance:\n", variance_values)
print("\n")

# Calculate standard deviation for each feature
# sdFeature01 = sepal_length.std()
# sdFeature02 = sepal_width.std()
# sdFeature03 = petal_length.std()
# sdFeature04 = petal_width.std()
# print("Standard deviation is: ", sdFeature01, sdFeature02, sdFeature03, sdFeature04)
# print()
# Calculate standard deviation for each feature
std_dev_values = ds.std()
print("Standard Deviation:\n", std_dev_values)
print("\n")


# # Calculate the 25th, 50th, and 75th percentiles for each feature
# percentiles_sepal_length = sepal_length.quantile([0.25, 0.5, 0.75])
# percentiles_sepal_width = sepal_width.quantile([0.25, 0.5, 0.75])
# percentiles_petal_length = petal_length.quantile([0.25, 0.5, 0.75])
# percentiles_petal_width = petal_width.quantile([0.25, 0.5, 0.75])
# print("Percentiles:\n", percentiles_sepal_length, percentiles_sepal_width, percentiles_petal_length,percentiles_petal_width)
# Calculate the 25th, 50th, and 75th percentiles for each feature
percentiles = ds.quantile([0.25, 0.5, 0.75])
print("Percentiles:\n", percentiles)
print("\n")

Q1 = ds.quantile(0.25)
Q2 = ds.quantile(0.50)
Q3 = ds.quantile(0.75)

print("Q1 (25th percentile):\n", Q1)
print("Q2 (50th percentile, median):\n", Q2)
print("Q3 (75th percentile):\n", Q3)


# correlation_matrix = ds.corr()
# print("Correlation Matrix:\n", correlation_matrix)


# # Calculate covariance matrix
# covariance_matrix = ds.cov()
# print("Covariance Matrix:\n", covariance_matrix)
# Calculate correlation matrix
correlation_matrix = ds.corr()
print("Correlation Matrix:\n", correlation_matrix)

