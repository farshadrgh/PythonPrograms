def search_for_word(our_string):
    counter = 0
    for our_word in our_string:
        if our_word == "Emma":
            counter = counter + 1
    print('Emma appeared {} times'.format (counter))
our_string = "Emma is good developer. Emma is a writer"
print(search_for_word(our_string))