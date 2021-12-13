import pandas as pd

# Note:
# [] == List
# {} == Set or Dictionary
# Series is like a column, a DataFrame is the whole table.

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(data)
print(myvar)
print(myvar.to_string)
my = myvar.loc[0]
print(my)
my1 = myvar.loc[[0, 1]]
print(my1)
myvar1 = pd.DataFrame(data=data, index={"day0", "day1", "day2"})
print(myvar1.loc["day2"])
print("///////////////////////////")
print(pd.options.display.max_rows)
print(myvar.info())
