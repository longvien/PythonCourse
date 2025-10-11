# class Calculation:
#     def __init__(self, first_num, second_num):
#         self.first = first_num
#         self.second = second_num
#     def calculate(self, first_num, second_num):
#         return self.first + self.second
# first_num = int(float(input('Pls enter the first number:\n')))
# second_num = int(float(input('Pls enter the second number:\n')))
# calculate = Calculation(first_num, second_num)
# calculate.calculate(first_num, second_num) 

def addition(a, b):
    return a + b
num1 = int(float(input('Enter num 1:\n')))
num2 = int(float(input('Enter num 2:\n')))
result = addition(num1, num2)
print(result)