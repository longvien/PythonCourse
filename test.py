class ROBO:
    def __init__(self, name):
        self.name = name
    def display(self):
          print('HI, I am ' + self.name)
    
class ROBO_DOG(ROBO):
    def food(self):
        print('I am HUNGRY')
class ROBO_CAT(ROBO):
    def food(self):
        print('FISH PLEASE')

my_cat = ROBO_CAT('MEOW')
my_cat.food()
my_cat.display()

my_dog = ROBO_DOG('WOOF')
my_dog.food()
my_dog.display()