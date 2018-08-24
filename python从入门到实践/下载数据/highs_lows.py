import csv
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.ticker as mticker

filename = 'death_valley_2014.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=1)
#fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='both', labelsize=16)
# myLocator = mticker.MultipleLocator(3)
# ax = fig.add_subplot(1, 1, 1)
# ax.xaxis.set_major_locator(myLocator)
plt.show()
