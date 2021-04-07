# You can write your string here
string_words = '''
A new study shows that 86 per cent of the world's rivers have been damaged by human activity.
The study was conducted by researchers from a university in Toulouse, France.
They examined data on over 2,500 rivers around the world. They did not look at rivers in the polar regions of the Arctic and Antarctica or in deserts.
The scientists looked into changes to biodiversity over the past 200 years.
They discovered that biodiversity in over half of rivers has been seriously damaged by humans.
The researchers said there were many reasons for this damage.
A big reason is the introduction of new species of fish into rivers.
Other reasons include pollution, dams, overfishing, farming and climate change.
'''

word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {} \n".format(str(list(zip(word_list, word_freq)))))