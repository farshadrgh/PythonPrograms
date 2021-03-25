def test_distinct(OurData):
  
  if len(OurData) == len(set(OurData)):
    return True
  else:
    return False;
  
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))
