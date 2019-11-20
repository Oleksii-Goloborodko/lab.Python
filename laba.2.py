import datetime

year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))

date1 = datetime.date(year, month, day)

print ("the first date: " + str(date1))

date2 = datetime.date.today()
print(date2)
if (date1 == date2):
   print("Date Time 1 is equal to Date Time 2")
else:
   print("Date times are unequal")
