from datetime import date
def user_name(name):
    return  name


def calculate_Age(birthDate):
    days_in_year = 365
    age = int((date.today() - birthDate).days / days_in_year)
    return age


print(user_name("Farshad"), calculate_Age(date(2000, 1, 23)), "years old")