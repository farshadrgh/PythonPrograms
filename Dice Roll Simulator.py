import random
again = "yes"
while again == "yes" or again == "y":

    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(1, 6))
    print (random.randint(1, 6))

    again = input("Roll the dices again(y/n)?\n")
