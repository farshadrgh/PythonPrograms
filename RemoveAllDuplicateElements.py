import array as arr

def test(nums):
    return sorted(set(nums),key=nums.index)

array_num = arr.array('i', [1, 3, 5, 1, 3, 7, 9])
print("Original array:")
for i in range(len(array_num)):    
    print(array_num[i], end=' ')
print("\nAfter removing duplicate elements from the said array:")
result = arr.array('i', test(array_num))
for i in range(len(result)):    
    print(result[i], end=' ')
array_num = arr.array('i', [2, 4, 2, 6, 4, 8])
print("\nOriginal array:")
for i in range(len(array_num)):    
    print(array_num[i], end=' ')
print("\nAfter removing duplicate elements from the said array:")
result = arr.array('i', test(array_num))
for i in range(len(result)):    
    print(result[i], end=' ')
