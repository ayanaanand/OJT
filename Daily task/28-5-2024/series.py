import pandas as pd

data = [10, 2, 3, 45, 65]

series = pd.Series(data)
print(series)
print(series[3]) 

series_add = series + 10
print(series_add)


filtered_series = series[series > 20]
print(filtered_series)


mean = series.mean()
print(f"Mean value of the series: {mean}")
