import csv
from datetime import datetime

from matplotlib import pyplot as plt 

# Get dates, highs, and low temperatures from file
dv = 'death_valley_2018_full.csv'
s = 'sitka_weather_2018_full.csv'

def comparison(filename, date_format, data_row):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs = [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], date_format)
                high = int(row[data_row])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
    return dates, highs

dv_dates, dv_highs = comparison(dv, "%Y-%m-%d", 6)
s_dates, s_highs = comparison(s, "%m/%d/%y", 8)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dv_dates, dv_highs, c='red', alpha= 0.5)

# Plot data.
plt.plot(s_dates, s_highs, c='blue', alpha= 0.5)

# Format plot.
title = "Daily high temperatures, 2018\nDeath Valley and Sitka"
plt.title(title, fontsize= 20)
plt.xlabel('', fontsize= 16)
fig.autofmt_xdate()
plt.ylabel("Temperate (F)", fontsize= 16)
plt.tick_params(axis= 'both', which= 'major', labelsize= 8)

plt.show()







