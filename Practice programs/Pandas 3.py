import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Marks': [85, 45, 78]})
passed = df[df['Marks'] >= 50]
print(passed)
