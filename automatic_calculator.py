calculation = input('Please choose a calculation symbol - + : * ex: choose - if u need minus, + when u need plus!\n')
if calculation == '+':
    def a(a, c):
        return a + c
    first_num = float(input('Please enter the first number:\n'))
    if not isinstance(first_num, (int, float)):
        print('Invalid input! Please enter numbers only')
    second_num = float(input('Please enter the second number:\n'))
    result = a(first_num, second_num)
    print('The result of', first_num, calculation, second_num, 'is', result)      
elif calculation == '-':
    def a(a, b):
        return a - b
    first_num = float(input('Please enter the first number:\n'))
    second_num = float(input('Please enter the second number:\n'))
    result = a(first_num, second_num)
    print('The result of', first_num, calculation, second_num, 'is', result)
elif calculation == '*':
    def a(a, b):
        return a * b
    first_num = float(input('Please enter the first number:\n'))
    second_num = float(input('Please enter the second number:\n'))
    result = a(first_num, second_num)
    print('The result of', first_num, calculation, second_num, 'is', result)
elif calculation == ':':
    def a(a, b):
        return a/b
    first_num = int(float(input('Please enter the first number:\n')))
    second_num = int(float(input('Please enter the second number:\n')))
    result = a(first_num, second_num)
    print('The result of', first_num, calculation, second_num, 'is', result)
else:
    print('Invalid calculation symbol!')