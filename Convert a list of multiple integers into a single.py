def ConvertList(OurList):

    print("Original List: ",OurList)
    NewInteger = int("".join(map(str, OurList)))
    print("Single Integer: ",NewInteger)

MyList = [1400, 1, 2]
ConvertList(MyList)

