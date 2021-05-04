def ListCount (Nums):
    YourNumber=int(input("Which number do you want?\n"))
    Count = 0
    for Num in Nums:
        if Num == YourNumber:
            Count = Count + 1

    return Count

print(ListCount([1, 3, 4, 5, 6, 7, 4]))
