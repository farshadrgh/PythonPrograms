def calculations (num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

print("The result is {}".format(calculations( 20 ,30 )))