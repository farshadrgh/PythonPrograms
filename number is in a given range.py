def test_range(n):
    if n in range(3 ,9):
        print( "{} is in the range".format(str(n)))
    else :
        print("The number is outside the given range.")
test_range(5)