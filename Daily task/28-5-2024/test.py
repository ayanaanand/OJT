import pandas as pd

df = pd.read_csv('Book1.csv')
# print(df)

df_cleaned_row = df.dropna(how="all")
# print(df_cleaned_row)

df_cleaned_col = df_cleaned_row.dropna(axis=1,how="all")
print(df_cleaned_col)

df_filled_data = df.fillna(0)
print(df_filled_data)