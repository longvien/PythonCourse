class Calculation:
    def __init__(self, first_num, second_num):
        self.first = first_num
        self.second = second_num
class Addition(Calculation):
    def calculate(self):
        return self.first + self.second
class Subtraction(Calculation):
    def calculate(self):
        return self.first - self.second
class Multiplication(Calculation):
    def calculate(self):
        return self.first * self.second
class Division(Calculation):
    def __init__(self, first_num, second_num):
        super().__init__(first_num, second_num)
        if second_num == 0:
            raise ZeroDivisionError("Can't be divided by zero")
    def calculate(self):
        return self.first / self.second

cal_symbols = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division
}

symbol = input('Pls choose a calculate symbol: + - * / \n')
if symbol in cal_symbols:
    first_num = int(float(input('Pls enter the first number:\n')))
    second_num = int(float(input('Pls enter the second number:\n')))
    calculate = cal_symbols[symbol](first_num, second_num)
    print('The result of', first_num, symbol , second_num, 'is', float(calculate.calculate()))
else:
    print("The option you chose doesn't exist. Pls try again!")