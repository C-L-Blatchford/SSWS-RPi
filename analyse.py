import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Find all CSV files
csv_files = sorted(glob.glob("ArduinoAverage_*.csv"))

if not csv_files:
    raise Exception("No CSV files found")

# Analyse every CSV
for csv_file in csv_files:

    print(f"Analysing {csv_file}")

    try:
        # Skip the CR3000 header lines
        df = pd.read_csv(csv_file, skiprows=4)

        # Create plot
        plt.figure(figsize=(10, 6))

        plt.plot(df["RECORD"])

        plt.title(f"Record Number\n{csv_file}")
        plt.xlabel("Sample")
        plt.ylabel("Record")
        plt.grid(True)

        # Create matching PNG filename
        png_file = os.path.splitext(csv_file)[0] + ".png"

        plt.savefig(png_file)
        plt.close()

        print(f"Created {png_file}")

    except Exception as e:
        print(f"Failed to analyse {csv_file}: {e}")
