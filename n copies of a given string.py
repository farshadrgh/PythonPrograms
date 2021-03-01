def larger_string(str, n):

   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('Farshad ', 2))
print(larger_string('Python ', 3))
