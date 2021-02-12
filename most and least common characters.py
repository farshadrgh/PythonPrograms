from collections import Counter
def max_least_char(str1):
    temp = Counter(str1)
    max_char = max(temp, key = temp.get)
    min_char = min(temp, key = temp.get)
    return (max_char, min_char)

str1 = "hello world"
print ("Original string: ")
print(str1)
result = max_least_char(str1)
print("\nMost common character of the said string:",result[0])
print("Least common character of the said string:",result[1])
