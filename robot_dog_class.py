class Robot_Dog: # To define a class, u type the 'class' keyword and then the class name.
    def __init__(self, name_val, breed_val): # The __init__() method let us initialize our Robot's Properties
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print('Woof Woof!')

dog = Robot_Dog('Tom', 'Daschund')
print(dog.name)
print(dog.breed)
dog.bark()

