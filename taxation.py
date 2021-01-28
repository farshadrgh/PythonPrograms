def tax_salary(salary):
    tax = 0
    if salary <= 10000:
        tax = 0

    elif salary <= 20000:
        tax = (salary - 10000) * 10 / 100

    else:
        tax = 0
        tax = 10000 * 10 / 100
        tax += (salary - 20000) * 20 / 100

    print("Given income {}".format(salary))
    print("Total tax to pay is {}".format(tax))

print(tax_salary(45000))