#  Find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9
print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())

print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))
