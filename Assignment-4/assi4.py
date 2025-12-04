import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("weather.csv")

data.iloc[:, 0] = pd.to_datetime(data.iloc[:, 0])
data.fillna(0, inplace=True)

temperature = data.iloc[:, 1]
rainfall = data.iloc[:, 2] if data.shape[1] > 2 else data.iloc[:, 1]
humidity = data.iloc[:, 3] if data.shape[1] > 3 else data.iloc[:, 1]

mean_temp = np.mean(temperature)
max_temp = np.max(temperature)
min_temp = np.min(temperature)
std_temp = np.std(temperature)

print("Mean Temperature:", mean_temp)
print("Max Temperature:", max_temp)
print("Min Temperature:", min_temp)
print("Standard Deviation:", std_temp)

plt.figure()
plt.plot(data.iloc[:, 0], temperature)
plt.title("Daily Temperature")
plt.savefig("daily_temperature.png")
plt.close()

monthly_rain = data.groupby(data.iloc[:, 0].dt.month)[rainfall.name].sum()
plt.figure()
monthly_rain.plot(kind='bar')
plt.title("Monthly Rainfall")
plt.savefig("monthly_rainfall.png")
plt.close()

plt.figure()
plt.scatter(temperature, humidity)
plt.title("Humidity vs Temperature")
plt.savefig("scatter_plot.png")
plt.close()

monthly_avg = data.resample('M', on=data.columns[0]).mean()
print(monthly_avg)

data.to_csv("clean_weather.csv", index=False)

report = open("report.txt", "w")
report.write("Weather Data Analysis Report\n")
report.write("Mean Temperature: " + str(mean_temp) + "\n")
report.write("Maximum Temperature: " + str(max_temp) + "\n")
report.write("Minimum Temperature: " + str(min_temp) + "\n")
report.write("Standard Deviation: " + str(std_temp) + "\n")
report.close()

print("All Tasks Completed Successfully")
