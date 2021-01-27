def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)

numList = [10, 20, 33, 46, 55]
findDivisible(numList)