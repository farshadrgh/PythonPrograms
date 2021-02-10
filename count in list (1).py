def count_number_4(nums):
  count = 0  
  for x in nums:
    if x == 4:
      count += 1

  return count

print(count_number_4([1 ,4 ,6 ,4 ,7 ,4]))
print(count_number_4([1 ,4 ,6 ,7 ,4]))