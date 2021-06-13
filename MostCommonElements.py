from collections import Counter

s = 'lkseropewdssafsdfafkpwekjnvkasbvkjasdssdfkkk'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))
