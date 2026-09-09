import pandas as pd
import matplotlib.pyplot as plt
import glob

files = sorted(glob.glob("ArduinoAverage*.csv"))

if not files:
    raise Exception("No CSV files found")

latest = files[-1]
print(f"Analysing {latest}")
df = pd.read_csv(latest, skiprows=[0,2,3])

print(df.columns)

plt.figure(figsize=(8,5))
plt.plot(df["Batt_Volt_Avg"])
plt.title("Battery Voltage")
plt.xlabel("Sample")
plt.ylabel("Voltage (V)")
plt.grid()
plt.savefig("battery_voltage.png")

print("Plot saved")
