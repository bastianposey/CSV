import csv
import matplotlib.pyplot as plt
from datetime import datetime

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

fig = plt.figure()

plt.subplot(2,1,2)
plt.plot(dates_death, highs_death, c="red")
plt.plot(dates_death, lows_death, c="blue")
plt.fill_between(dates_death,highs_death,lows_death, facecolor="blue", alpha=0.1)
plt.title(chart_name[1])

plt.subplot(2,1,1)
plt.plot(dates_sitka, highs_sitka, c="red")
plt.plot(dates_sitka, lows_sitka, c="blue")
plt.fill_between(dates_sitka,highs_sitka,lows_sitka, facecolor="blue", alpha=0.1)
plt.title(chart_name2[1])

plt.suptitle("Temperature comparison between " + chart_name2[1] + " and " + chart_name[1])

fig.autofmt_xdate()

plt.show()
