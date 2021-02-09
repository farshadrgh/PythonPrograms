import random
n = int(input("give your number:\n "))
x = True
while x == True:
    if n == random.randint(1,6):
        print("Yes! woooow you did it !!! you rock")
        break
    else:
        int(input("give your number:\n "))