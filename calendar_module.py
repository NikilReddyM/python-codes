import calendar
d=list(map(int,input().split()))
print(list(calendar.day_name)[calendar.weekday(d[2],d[0],d[1])].upper())