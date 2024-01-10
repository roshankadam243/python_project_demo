import pandas as pd
import numpy as np


#creating empty series
ser = pd.Series()
print(ser)
print(type(ser))

data = np.array(['a','r','w','d','s'])
ser = pd.Series(data)

print(ser)
