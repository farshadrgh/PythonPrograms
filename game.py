string = 'salam. farshad is lucky because pythone is easy for him'

counter = dict()

for letter in string:




for this_one in list(counter.keys()):
    print('{} appeared {} times'.format (this_one, counter[this_one]))