import calendar

def calendar_month():
    year=int(input("Enter the year: "))
    month=int(input("Enter the month(1-12): "))
    cal=calendar.TextCalendar(calendar.SUNDAY)

    month_cal=cal.formatmonth(year, month)
    return month_cal


print(calendar_month())
