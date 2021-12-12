import pandas as pd
from pandas import DataFrame

mydatasets = {
    'cars': ["BMW", "Volvo", "Ford"],
    'colors': ["Black", "White", "Red"],
    'passings': [3, 7, 2]
}

myvar: DataFrame = pd.DataFrame(mydatasets)
print(myvar)
print(pd.__version__)
