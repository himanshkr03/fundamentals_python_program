from datetime import date
def count_days(date1,date2):
    return (date2-date1).days
d1=int(input("enter the starting day:"))
m1=int(input("enter the starting month:"))
y1=int(input("enter the starting year:"))
date1=date(y1,m1,d1)
d2=int(input("enter the ending day:"))
m2=int(input("enter the ending month:"))
y2=int(input("enter the ending year:"))
date2=date(y2,m2,d2)
print(count_days(date1,date2),"remaining days")
print(count_days(date1,date2)//7,"number of weeks")
