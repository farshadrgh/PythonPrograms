import math

precision = int(input("How many spaces? "))

while precision > 50:
	print("Number to large")
	precision = int(raw_input("How many spaces? "))
else:
	print('{}....{}'.format (precision, math.pi))