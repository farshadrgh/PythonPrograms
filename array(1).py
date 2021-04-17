def Array1(a, b)
    list = []
    for x in range(a,b+1):
        if x % 2 == 0 :
            "Divided into Twe"

        elif x % 3 == 0 :
            print("Divided into Three", end = " ")
            print("\t\n")
        else:
            print("not 2 , not 3 !!!", end = " ")
            print("\t\n")
print(Array1(0, 100))
