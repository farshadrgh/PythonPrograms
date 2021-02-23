from heapq import nlargest
my_dict = {'a':500, 'b': 6000, 'c': 5000,'d':400, 'e':4000, 'f': 0}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)
