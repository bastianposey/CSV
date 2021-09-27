import csv
import matplotlib.pyplot as plt
from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter =",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

#testing to convert date from string
mydate = datetime.strptime("2018-07-01",'%Y-%m-%d')
print(mydate)

lows = []
highs = []
dates = []
for row in csv_file:
    lows.append(int(row[6]))
    highs.append(int(row[5]))
    cur_date = datetime.strptime(str(row[2]),'%Y-%m-%d')
    dates.append(cur_date)

#print(highs)
#print(dates)
#print(lows)


fig = plt.figure()

plt.title("Daily high temperatures, 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

plt.plot(dates, highs,c="red", alpha=0.5)
plt.plot(dates, lows,c="blue", alpha=0.5)

plt.fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)

fig.autofmt_xdate()

plt.show()
