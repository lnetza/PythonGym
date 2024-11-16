
weekYear = 52
maxWeekYear = 4680

def life_in_weeks(age):
    leftWeek = maxWeekYear-(age * weekYear)

    return leftWeek


print("Te restan ",life_in_weeks(56), "semanas")