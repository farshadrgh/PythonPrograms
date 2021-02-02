def string_reverse(our_str):

    str1 = ''
    index = len(our_str)
    while index > 0:
        str1 += our_str[ index - 1 ]
        index = index - 1
    return str1
print(string_reverse('1234abcd'))
