
def func(day, month, year):
    listbig = [1,3,5,7,8,10,12]
    listsmall = [4,6,9,11]
    day_now = 26
    month_now = 10
    year_now = 2021
    if (year > 0 and month > 0 and day > 0 and month < 13 and day < 32) and (year <= year_now):
        if (year < year_now) or (year == year_now and month < month_now) or (year == year_now and month == month_now and day <= day_now):
            if day < 31 and month in listsmall:
                return True
            elif day < 32 and month in listbig:
                return True
            elif month == 2:
                if (day == 29 and year%4 == 0) or day < 29:
                    return True
    return False

print(func(40, 10 ,2021))