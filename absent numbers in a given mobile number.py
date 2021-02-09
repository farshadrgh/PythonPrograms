def absent_digits(n):
  all_numbers = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_numbers)
  n = sorted(n)
  return n
print(absent_digits([0,9,3,8,6,9,0,0,6,9,6]))