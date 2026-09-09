#import pandas as pd
#import matplotlib.pyplot as plt
#import glob

#files = sorted(glob.glob("ArduinoAverage*.csv"))

#if len(files) == 0:
#    raise Exception("No CSV files found")

#latest = files[-1]
#print(f"Analysing {latest}")

#df = pd.read_csv(latest, skiprows=4)

#plt.figure(figsize=(8,5))
#plt.plot(df["RECORD"])
#plt.title("Record Number")
#plt.xlabel("Sample")
#plt.ylabel("Record")
#plt.grid()
#plt.savefig("latest_plot.png")

#print("Plot saved")

import pandas as pd
import glob

files = sorted(glob.glob("ArduinoAverage*.csv"))

latest = files[-1]

df = pd.read_csv(latest)

print(df.columns)
