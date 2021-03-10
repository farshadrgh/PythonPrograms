def insertion_sort(our_list):
   for number in range(1,len(our_list)):
     value = our_list[number]
     position = number

     while position > 0 and our_list[position-1] > value:
         our_list[position] = our_list[position-1]
         position = position - 1

     our_list[position] = value

our_list = [10,617,45,73,51,3,45,1,500]
insertion_sort(our_list)
print(our_list)
