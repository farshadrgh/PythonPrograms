def square_value(Num1, Num2):
    OurDictionary = dict()

# Y+1 is easy to understand
    for x in range(Num1, Num2+1):
        OurDictionary[x] = x ** 2
    print(OurDictionary)

# you can write your numbers here and you do not need to Num2 + 1 anymore
square_value(1 ,20)
