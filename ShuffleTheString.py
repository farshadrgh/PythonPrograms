from random import shuffle

def ShuffleTheWords(OurString):
    ListOfWords = []
    Our_txt = OurString.split(" ")

    for Word in Our_txt:
        ListOfWords.append(Word)
    return ListOfWords

    ShuffleList = shuffle(ListOfWords)
    print (ShuffleList)
OurString = "The quick brown fox jumps over the lazy dog !"
print(ShuffleTheWords(OurString))