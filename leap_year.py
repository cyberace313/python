def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    elif year < 0:
        return "Invalid Year"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(year)
    if is_leap_year and month == 2:
        return 29
    else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)