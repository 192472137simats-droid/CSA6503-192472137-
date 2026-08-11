import pandas as pd

df = pd.DataFrame({'Dept': ['CS', 'CS', 'EEE', 'EEE'],
                    'Marks': [80, 90, 70, 60]})
print(df.groupby('Dept')['Marks'].mean())
