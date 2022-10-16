day, month, year = int(input()), int(input()), int(input())
CurrentDay, CurrentMonth, CurrentYear = int(input()), int(input()), int(input())
if (day > CurrentDay or month > CurrentMonth or year > CurrentYear) and year!=CurrentYear:
    print(CurrentYear - year - 1)
else:
    print(CurrentYear - year)
