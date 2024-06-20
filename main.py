import pandas as pd

pm_data_path = 'pm_data.csv'
data = pd.read_csv(pm_data_path)

print(data.head())
