set1 = {1 ,2 ,3}
set2 = {4 ,5 ,6}
set3 = {3}
print("Original sets:")
print(set1)
print(set2)
print(set3)
print("Check sn1 set has no elements in common with sn2 set:")
print(set1.isdisjoint(set2))
print("Check sn1 set has no elements in common with sn3 set:")
print(set1.isdisjoint(set3))
