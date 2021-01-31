def reverseCheck(number):
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False

print("The original and reverse number is the same: {}".format(reverseCheck(121)))