d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print("First dictionary:\n", d1)
print("Second dictionary:\n", d2)
print("Our new dictionary is:\n", d)
