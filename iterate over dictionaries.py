def iterate(a):
    for dict_key, dict_value in a.items():
        print(dict_key, '->', dict_value)

print(iterate({'x': 100, 'y': 200, 'z': 300}))
