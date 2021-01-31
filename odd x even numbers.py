def mergeList(list1, list2):
    print("First List {}".format(list1))
    print("Second List {}".format(list2))
    our_list = []

    for num in list1:
        if (num % 2 != 0):
            our_list.append(num)
    for num in list2:
        if (num % 2 == 0):
            our_list.append(num)
    return our_list


list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print("result List is {}".format(mergeList(list1, list2)))