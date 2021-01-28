def exponent(base, exp):
    number = exp
    result = 1
    while number > 0:
        result = result * base
        number -= 1
    print("{} raises to the power of {} is: {}".format(base ,exp ,result))

exponent(2 ,5)