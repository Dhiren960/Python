import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_dir = Path("data")
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

files = list(data_dir.glob("*.csv"))

all_data = []

for file in files:
    df = pd.read_csv(file)
    df.columns = [c.lower() for c in df.columns]
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
    df["building"] = file.stem
    all_data.append(df[["datetime", "building", "kwh"]])

df = pd.concat(all_data, ignore_index=True)
df = df.sort_values("datetime")

df.to_csv(output_dir / "cleaned_energy_data.csv", index=False)

daily = df.set_index("datetime").groupby("building").resample("D")["kwh"].sum().reset_index()
weekly = df.set_index("datetime").groupby("building").resample("W")["kwh"].sum().reset_index()

summary = df.groupby("building")["kwh"].agg(["min", "max", "mean", "sum"]).reset_index()
summary.columns = ["Building", "Min", "Max", "Average", "Total"]
summary.to_csv(output_dir / "building_summary.csv", index=False)

trend = daily.pivot(index="datetime", columns="building", values="kwh")

plt.figure()
trend.plot()
plt.savefig(output_dir / "dashboard.png")
plt.close()

total_consumption = df["kwh"].sum()
highest_building = summary.sort_values("Total", ascending=False).iloc[0]["Building"]

df["hour"] = df["datetime"].dt.hour
peak_hour = df.groupby("hour")["kwh"].sum().idxmax()

report = f"""
Total Campus Consumption: {total_consumption} kWh
Highest Consuming Building: {highest_building}
Peak Load Hour: {peak_hour}
"""

with open(output_dir / "summary.txt", "w") as f:
    f.write(report)

print(report)
