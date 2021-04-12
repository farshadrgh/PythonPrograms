# Your lists
Nums1 = [10, 10, 10]
Nums2 = [20, 20, 20]
Nums3 = [30, 30, 30]
# Show the list in output
print("Original list: ")
print(Nums1)
print(Nums2)
print(Nums3)
# Multiply elements in their columns elements
result = map(lambda x, y, z: x * y * z, Nums1, Nums2, Nums3)
print("\nNew list is:")
print(list(result))
