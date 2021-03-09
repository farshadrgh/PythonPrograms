def longer_words(n, our_str):
    words = []
    our_text = our_str.split(" ")
    for x in our_text:
        if len(x) > n:
            words.append(x)
    return words
print(longer_words(5 ,"This is only a test for practice python programming"))