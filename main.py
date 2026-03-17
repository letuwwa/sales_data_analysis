import numpy as np
import pandas as pd

# reading data
df = pd.read_csv(r'csv_files/Sales.csv')

# getting first 6 rows
print(df.head(n=6))

# looking for missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print(pct_missing)

# data frame types of
print(df.dtypes)