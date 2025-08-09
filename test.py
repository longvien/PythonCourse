class Gretting:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
    def gretting(self):
        print('Hi', self.f_name, self.l_name)
my_name = Gretting('Long', 'Vien')
my_name.gretting()