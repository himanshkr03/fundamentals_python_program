january=1
febuary=2
march=3
april=4
may=5
june=6
july=7
august=8
september=9
october=10
november=11
december=12
from datetime import date
def days_count(date1,date2):
    return(date2 - date1).days
d1=int(input("Enter the starting day:"))
m1=eval(input("Enter the starting month:"))
y1=int(input("Enter the starting year:"))
date1=date(y1,m1,d1)
print("---------------------------------------------------------")
d2=int(input("Enter the ending day:"))
m2=eval(input("Enter the ending month:"))
y2=int(input("Enter the ending year:"))
date2=date(y2,m2,d2)
print(days_count(date1,date2)," days")
    
