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
