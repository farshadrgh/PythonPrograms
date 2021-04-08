# Create a tuple first
OurTuple = ((1, "a"), (2, "b"), (3, "c"))
print(dict((y, x) for x, y in OurTuple))
