import random

CharList = ['a', 'b', 'c', 'd', 'e', 'f']
random.shuffle(CharList)
OurString = ''.join(CharList)
print(OurString)
