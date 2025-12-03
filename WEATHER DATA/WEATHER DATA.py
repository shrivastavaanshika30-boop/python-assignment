#TITTLE: WEATHER DATA
#NAME: ANSHIKA SHRIVASTAVA
#DESCRIPTION: A program that analyzes weather data from a CSV file to clean it, visualize trends, calculate statistics, and generate a summary report.





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    df = pd.read_csv("weather.csv")
except FileNotFoundError:
    print("weather.csv not found!")
    exit()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])


df = df.dropna()  

df['month'] = df['date'].dt.month
monthly_avg = df.groupby('month')['temperature'].mean()


plt.figure(figsize=(12, 8))


plt.subplot(3, 1, 1)
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Line Plot")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")


plt.subplot(3, 1, 2)
plt.bar(monthly_avg.index, monthly_avg.values)
plt.title("Average Monthly Temperature (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Avg Temp (°C)")


plt.subplot(3, 1, 3)
plt.scatter(df['temperature'], df['humidity'])
plt.title("Temperature vs Humidity (Scatter Plot)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.savefig("weather_plots.png")
plt.show()


temps = df['temperature'].values

mean_temp = np.mean(temps)
max_temp = np.max(temps)
min_temp = np.min(temps)
std_temp = np.std(temps)


report = f"""
# Weather Data Summary Report

### 📌 Temperature Statistics
- **Mean:** {mean_temp:.2f} °C  
- **Max:** {max_temp:.2f} °C  
- **Min:** {min_temp:.2f} °C  
- **Standard Deviation:** {std_temp:.2f}

### 📌 Included Visuals
- Line Plot  
- Bar Chart  
- Scatter Plot  
(All saved in: `weather_plots.png`)
"""

with open("weather_report.md", "w") as file:
    file.write(report)

print("Analysis complete! Plots saved as weather_plots.png and report saved as weather_report.md")
