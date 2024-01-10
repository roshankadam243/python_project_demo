'''import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(df.head())'''

import pandas as pd

df = pd.read_csv("sample.csv",
                 sep='[:,|_]',
                 engine = 'python')

df1 = pd.read_csv("sample.csv")

print(df1)

print()

print(df)
