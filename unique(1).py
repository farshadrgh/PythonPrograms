list1 = [1,1,1,2,2,3,4,4,5,6,6,6]
our_unique_list = []
for num in list1:
    if num not in our_unique_list:
        our_unique_list.append(num)
print(our_unique_list)

