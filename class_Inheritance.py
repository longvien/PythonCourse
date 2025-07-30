    #class Inheritance
# class Robot:
#     def __init__(self, name):
#         self.name = name
#         self.position = [0, 0] # Position Starting at origin (0, 0)
#         print('Hi, I am ' + self.name)
#     def walk(self, m):
#         self.position[0] = self.position[0] + m
#         print('New position' + str(self.position))
# class Dog(Robot):
#     def bark(self):
#         print('Woof! Woof!')

# my_dog = Dog('Robodog')
# my_dog.walk(8)
# my_dog.bark()





      #class Inheritance + Overriding
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0] # Position | Starting at origin (0, 0)
        print('Hi, I am ' + self.name)
    def walk(self, m):
        self.position[0] = self.position[0] + m
        print('New position' + str(self.position))
    def eat(self):
        print("I'm hungry!")
class Dog(Robot):
    def bark(self):
        print('Woof! Woof!')
        super().eat() # Call the eat method from the Robot class. If not used, it will call the Dog class's eat method
    # Overriding the eat method from Robot class
    def eat(self): # Programm will run this method instead of the one in Robot class
        print("I love dog food! Buy me some and be quick, i'm starving!")
class Cat(Robot):
    def make_sound(self):
        print('Meow! Meow!')
    def eat(self):
        print("I love cat food! Buy me some and be quick, i'm starving!")
my_dog = Dog('Robodog')
my_dog.walk(8)
my_dog.bark()
my_dog.eat()

my_cat = Cat('Robocat')
my_cat.walk(5)
my_cat.make_sound()
my_cat.eat()