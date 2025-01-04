import calendar

month, day, year = input().split()
day == day[-1] if day in ['0'+str(i) for i in range(1, 10)] else day
month == month[-1] if month in ['0'+str(i) for i in range(1, 10)] else month
    
days = {1:'MONDAY', 2:'TUESDAY', 3:'WEDNESDAY', 4:'THURSDAY', 5:'FRIDAY', 6:'SATURADAY', 7:'SUNDAY'}

counter = 0
for val in calendar.TextCalendar(firstweekday=7).monthdatescalendar(int(year), int(month)):
    for value in val:
        counter += 1
        value = str(value)
        if value[5:7] == month and value[-2:] == day:
            print(days[counter%7])
            
import calendar

month, day, year = input().split()
day == day[-1] if day in ['0'+str(i) for i in range(1, 10)] else day
month == month[-1] if month in ['0'+str(i) for i in range(1, 10)] else month
    
days = {1:'MONDAY', 2:'TUESDAY', 3:'WEDNESDAY', 4:'THURSDAY', 5:'FRIDAY', 6:'SATURDAY', 7:'SUNDAY'}

print(days[calendar.weekday(int(year), int(month), int(day))+1])