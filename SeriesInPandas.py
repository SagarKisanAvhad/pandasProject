import pandas as pd

# Note:
# [] == List
# {} == Set or Dictionary
# Series is like a column, a DataFrame is the whole table.
a = [1, 2, 3]
myvar = pd.Series(a)  # by default, index is the label
print(a)
print(a[0])
b = [1, 2, 3]
myvar = pd.Series(data=a, index=["x", "y", "z"])  # we can change label
print(myvar["x"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print(myvar["day1"])  # key becomes label

myvar1 = pd.Series(calories, index=["day1", "day2"])
print(myvar1)
