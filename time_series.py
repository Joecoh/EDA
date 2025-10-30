import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2025-01-01', periods=7, freq='D'),
    'Temperature': [29, 30, 32, 31, 33, 34, 35]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
print("=== TIME SERIES DATA (Chennai Temperature) ===")
print(df, "\n")

# Line plot - visualize temperature trend
plt.plot(df.index, df['Temperature'], marker='o', color='orange')
plt.title("Daily Temperature Trend in Chennai (Time Series)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter plot - show daily temperature variation
plt.scatter(df.index, df['Temperature'], color='blue')
plt.title("Temperature Scatter Plot")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

# Bar chart - compare daily values
df['Temperature'].plot(kind='bar', color='green')
plt.title("Temperature by Day (Bar Chart)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()
