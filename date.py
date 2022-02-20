# # date time printer

from datetime import date, datetime

# new_date = datetime(2022,5,1)

# print(datetime.now())

# date time difference
starting = "2021-1-1"
ending = "2022-1-1"

starting_date = datetime.strptime(starting, "%Y-%m-%d")
ending_date = datetime.strptime(ending, "%Y-%m-%d") 

print (ending_date-starting_date)