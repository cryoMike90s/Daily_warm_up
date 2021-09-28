import calendar

def give_me_month(date):
    data = calendar.TextCalendar()
    str = data.formatmonth(*date)
    return str

date = (2021, 7)

print(give_me_month(date))