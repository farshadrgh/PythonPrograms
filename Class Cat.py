class cat():
    def __init__(self ,breed ,name ,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
my_cat = cat(breed = 'Persian' ,name = 'Harith' ,spots = False)

print("My cat's breed is: {}".format(my_cat.breed))
print("My cat's name is: {}".format(my_cat.name))
print("My cat's spots is: {}".format(my_cat.spots))