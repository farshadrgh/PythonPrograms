import collections
sentence = "As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality"

words = sentence.split()
word_counts = collections.Counter(words)

for word, count in sorted(word_counts.items()):
    print("{} is repeated {} time{}.".format(word, count, "s" if count > 1 else ""))
