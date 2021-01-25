string = 'salam. farshad is lucky because pythone is easy for him'

counter = dict()

for letter in string:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1


for this_one in list(counter.keys()):
    print('{} appeared {} times'.format (this_one, counter[this_one]))