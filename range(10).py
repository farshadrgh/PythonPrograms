def sum(num):
    previous_number = 0
    for i in range(num):
        sum = previous_number + i
        print("Current Number", i, "Previous Number ", previous_number," Sum: ", sum)
        previous_number = i

print("Printing current and previous number sum in a given range(10)")
print(sum(100))
