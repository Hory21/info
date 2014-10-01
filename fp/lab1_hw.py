import sys
year = int(input("year:"))
nr = int(input("day number:"))
if nr > 366 or (nr > 365 and year % 4 != 0):
	print('Invalid day number')
	sys.exit()
month = 0;
if year % 4:
	daysInMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
else:
	daysInMonth = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)	
i = 0
aux = daysInMonth[0]
for i in range(12):
	if aux >= nr:
		month = i + 1
		day = daysInMonth[i] - (abs(aux - nr))
		break
	aux += daysInMonth[i + 1]
print("data:", year, '.', month, '.', day, sep = '')
