def trapezoid_area ():
    height = float(input("Height of trapezoid: "))
    base1 = float(input('Base one value: '))
    base2 = float(input('Base two value: '))
    area = ((base1 + base2) / 2) * height
    print("Area is: {}".format(area))
print(trapezoid_area())