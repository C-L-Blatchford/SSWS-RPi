import pandas as pd
import matplotlib.pyplot as plt
import glob

# Find all average CSV files
csv_files = sorted(glob.glob("ArduinoAverage_*.csv"))

if not csv_files:
    raise Exception("No CSV files found")

frames = []

for csv_file in csv_files:
    print(f"Reading {csv_file}")
    
    try:
        df = pd.read_csv(csv_file, skiprows=[0, 2, 3])
        frames.append(df)
    except Exception as e:
        print(f"Skipping {csv_file}: {e}")

if not frames:
    raise Exception("No usable CSV data")

# Combine all CSVs
df = pd.concat(frames, ignore_index=True)

# Convert timestamps
df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"])

start_date = df["TIMESTAMP"].min().strftime("%Y-%m-%d")
end_date = df["TIMESTAMP"].max().strftime("%Y-%m-%d")

plt.figure(figsize=(12,6))
plt.plot(df["TIMESTAMP"], df["Batt_Volt_Avg"])

plt.title(
    f"Snowdon Weather Station Summary\n"
    f"{start_date} to {end_date}"
)

plt.xlabel("Time")
plt.ylabel("Battery Voltage (V)")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_summary.png")

print("Created daily_summary.png")
