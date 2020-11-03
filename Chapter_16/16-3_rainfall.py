import csv
from datetime import datetime

from matplotlib import pyplot as plt 

# Get dates, highs, and low temperatures from file
filename = 'Seattle_weather_2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    try:
        header_row = next(reader)
        header_header_row = next(reader)
    except Exception as e: 
        print(e)

    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = row[0]
            rainfall = int(row[16])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue', alpha= 0.5)

# Format plot.
title = "Daily rainfall, Jan 2020\nSeattle, WA"
plt.title(title, fontsize= 20)
plt.xlabel('', fontsize= 16)
fig.autofmt_xdate()
plt.ylabel("Temperate (F)", fontsize= 16)
plt.tick_params(axis= 'both', which= 'major', labelsize= 8)

plt.show()





