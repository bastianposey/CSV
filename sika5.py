import csv
import matplotlib.pyplot as plt
from datetime import datetime

'''
For your 5th python script file - 

Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX
columns. Use the header row to determine the indexes for these values, so your program can work
for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
for your graph as well.

create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

Matplotlib's pyplot API has a convenience function called subplots() which acts as a
utility wrapper and helps in creating common layouts of subplots, including the
enclosing figure object, in a single call.
'''

open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter =",")
csv_file2 = csv.reader(open_file2, delimiter = ",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

chart_name = next(csv_file)
chart_name2 = next(csv_file2)

def find_index(header,key):
    for index in header:
        if index == key:
            return header.index(index)

lows_death = []
highs_death = []
dates_death = []
for row in csv_file:

    try:
        cur_date = datetime.strptime(str(row[find_index(header_row,"DATE")]),'%Y-%m-%d')
        high = int(row[int(find_index(header_row,"TMAX"))])
        low = int(row[int(find_index(header_row, "TMIN"))])
    except ValueError:
        print(f"Missing data for {cur_date}")
    else:
        lows_death.append(int(row[find_index(header_row,"TMAX")]))
        highs_death.append(int(row[find_index(header_row,"TMIN")]))
        dates_death.append(cur_date)

lows_sitka = []
highs_sitka = []
dates_sitka = []
for row in csv_file2:

    try:
        cur_date = datetime.strptime(str(row[find_index(header_row2,"DATE")]),'%Y-%m-%d')
        high = int(row[find_index(header_row2,"TMAX")])
        low = int(row[find_index(header_row2, "TMIN")])
    except ValueError:
        print(f"Missing data for {cur_date}")
    else:
        lows_sitka.append(int(row[find_index(header_row2,"TMAX")]))
        highs_sitka.append(int(row[find_index(header_row2,"TMIN")]))
        dates_sitka.append(cur_date)

plt.subplot(2,1,1)
plt.plot(dates_death, highs_death, c="red")
plt.title(chart_name[1])

plt.subplot(2,1,2)
plt.plot(dates_sitka, lows_sitka, c="blue")
plt.title(chart_name2[1])

plt.show()
