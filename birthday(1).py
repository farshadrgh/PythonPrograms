import datetime
birth_date = datetime.date(2000, 1, 23)
end_date = datetime.date(2021, 2, 10)
time_difference = end_date - birth_date
age = time_difference.days
print(age)
