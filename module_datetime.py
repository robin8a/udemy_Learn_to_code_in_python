# references: https://www.programiz.com/python-programming/datetime/strftime
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

# 22-02-2020
date_time_opencv = now.strftime("%d-%m-%Y")
print("date and time opencv:", date_time_opencv)