#!/usr/bin/python
#In Sung Kwon

#Homework Number 1
for i in range(1,6):
	print " " * (5-i), "*" * i

#Homework Number 2
from datetime import date, datetime, timedelta

begin = raw_input("Insert Start Date: ")
end = raw_input("Insert End Date: ")

begin_year=int(start[:4])
begin_month=int(start[4:6])
begin_day=int(start[6:8])

begin_date= date(begin_year,begin_month,begin_day)

end_year=int(end[:4])
end_month=int(end[4:6])
end_day=int(end[6:8])

end_date= date(end_year,end_month,end_day)

print end_date - start_date

#Homework Number 3
num =""
for x in range(1,3001):
	num = num + str(x)
print num.count("2")	



