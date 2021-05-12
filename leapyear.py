year = int(input("Please enter a year: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print("{} is a leap year".format(year))
else:
  print("{} is not a leap year".format(year))  