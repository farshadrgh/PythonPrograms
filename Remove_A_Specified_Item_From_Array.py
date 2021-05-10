from array import *

# Build your array and print it
ArrayNums = array('i', [1, 3, 5, 7, 9])
print("Original array: " + str(ArrayNums))

# For example, we pop third item
print("Remove the third item form the array:")
ArrayNums.pop(2)
print("New array: "+str(ArrayNums))