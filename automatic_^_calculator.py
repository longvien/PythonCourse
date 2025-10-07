class Calculation:
    def __init__(self, first_num, second_num):
        self.first = first_num
        self.second = second_num
    def calculate(self, first_num, second_num):
        return self.first + self.second
    def display(self):
        print(calculate)

first_num = int(float(input('Pls enter the first number:\n')))
second_num = int(float(input('Pls enter the second number:\n')))
calculate = Calculation(first_num, second_num)
calculate.calculate(first_num, second_num) # type: ignore


                