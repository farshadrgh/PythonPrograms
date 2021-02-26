def volume_and_area_of_a_cylinder():

    height = float(input("Height of cylinder: "))
    radian = float(input("Radius of cylinder: "))
    pi = 3.14

    volume = pi * radian * radian * height
    sur_area = ((2 * pi * radian) * height) + ((pi * radian ** 2) * 2)
    print("Volume is: {}".format(volume))
    print("Surface Area is: {}".format(sur_area))

print(volume_and_area_of_a_cylinder())