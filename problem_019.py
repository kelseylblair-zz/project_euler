months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
weekday = 2
month = 1
year = 1901
count = 0

while year <= 2000:
    if year % 4 == 0 and year != 1900:
	months[1] = 29
    else:
	months[1] = 28
    while month <= 12:
	while day <= months[month-1]:
	    if weekday == 7:
		if day == 1:
		    count += 1
		weekday = 1
	    else: 
		weekday += 1
	    day += 1
	day = 1
	month += 1
    month = 1
    year +=1
print count
