Numbers = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(Numbers)
OddNumbers = len(list(filter(lambda x: (x%2 != 0) , Numbers)))
EvenNumbers = len(list(filter(lambda x: (x%2 == 0) , Numbers)))
print("\nNumber of even numbers in the above array:\n", OddNumbers)
print("\nNumber of odd numbers in the above array:\n", EvenNumbers)
