mylist = [10, 20, 33, 46, 55]
def divisible_of_5():
    for i in mylist:
        if i % 5 == 0:
            print(i)
        else:
            pass
print( "Given list is  [10, 20, 33, 46, 55]" )
print( "Divisible of 5 in a list" )
print( divisible_of_5() )