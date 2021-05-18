def dayOfProgrammer(year):
    is_leap_year = lambda x: x % 400 == 0 or x % 4 == 0 and x % 100 != 0
    if year > 1918:
        if is_leap_year(year):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year < 1918:
        if year % 4 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    else:
        return "26.09.1918"