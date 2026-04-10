year = int(input("Year:\n"))
month = int(input("Month:\n"))
day = int(input("Day:\n"))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < months <= 12:
    sum = months[month - 1]
else:
    print("Data error")

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ("It is the %dth day." % sum)