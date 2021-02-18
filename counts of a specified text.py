from collections import Counter
s = 'lkseropewdssafsdfafkpweokmboktgobkgkbtblvdf'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))
