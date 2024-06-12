import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_excel('weather_data.xlsx')

# Perform data cleaning and preprocessing
# Check for and handle missing values
df = df.dropna()

# Convert the Date column to a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Use NumPy to calculate statistics for the temperature
temperature_mean = np.mean(df['Temperature'])
temperature_std = np.std(df['Temperature'])
temperature_max = np.max(df['Temperature'])
temperature_min = np.min(df['Temperature'])

# Print calculated statistics
print(f"Temperature Mean: {temperature_mean}")
print(f"Temperature Standard Deviation: {temperature_std}")
print(f"Temperature Maximum: {temperature_max}")
print(f"Temperature Minimum: {temperature_min}")

# Generate a time series plot to show the temperature trend over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'], label='Temperature', color='b')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trend Over Time')
plt.legend()
plt.show()

# Create a bar chart to show the average monthly precipitation
df['Month'] = df['Date'].dt.to_period('M')
monthly_precipitation = df.groupby('Month')['Precipitation'].mean()

plt.figure(figsize=(10, 5))
monthly_precipitation.plot(kind='bar', color='c')
plt.xlabel('Month')
plt.ylabel('Average Precipitation (mm)')
plt.title('Average Monthly Precipitation')
plt.xticks(rotation=45)
plt.show()

# Plot a scatter plot to examine the relationship between wind speed and temperature
plt.figure(figsize=(10, 5))
plt.scatter(df['WindSpeed'], df['Temperature'], color='g')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Temperature (°C)')
plt.title('Relationship Between Wind Speed and Temperature')
plt.show()