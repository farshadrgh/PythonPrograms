from random import shuffle

def ShuffleTheString(OurString):
    OutPut = OurString.split(" ")
    shuffle(OutPut)
    return OutPut

OurString = "The quick brown fox jumps over the lazy dog !"
print(ShuffleTheWords(OurString))
