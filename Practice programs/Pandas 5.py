import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print("Before:\n", df)
print("After:\n", df.fillna(0))
