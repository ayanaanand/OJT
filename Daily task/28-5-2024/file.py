import pandas as pd

df = pd.read_csv('Book1.csv',
                 dtype={'AGE': int,'SALARY':float},
                 usecols=["NAME","AGE","PLACE"])

print(df)