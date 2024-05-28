import pandas as pd

# Creating a DataFrame
data = {
    "name": ["ayana", "eva"],
    "age": [24, 2]
}

df = pd.DataFrame(data)
print(df)

# Accessing specific columns
print(df[["name", "age"]])

# Accessing a specific row by index
print(df.iloc[1])

# Filtering rows based on a condition
print(df[df["age"] > 23])

# Adding a new column
df["place"] = ["calicut", "kozhikode"]
print(df)

# Dropping a column
df = df.drop(columns=["age"])
print(df)

# Describing the DataFrame 
print(df.describe(include='all'))
