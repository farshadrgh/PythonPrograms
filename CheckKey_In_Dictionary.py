d = {1: 0, 2: 2, 3: 30, 4: 45, 5: 567, 6: 6.6}

def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
      
is_key_present(5)
is_key_present(9)
