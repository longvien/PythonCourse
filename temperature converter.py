#def convert_F_C(number): # 1 f = -17,222 c 1c = 33,8 F
#    num = -17,222
#    convert = number * num
#    return convert

#def convert_C_F(number): # 1 f = -17,222 c  1c = 33,8 F
#    num = 33,8
#    convert = number * num
#    return convert

def convert_F_C(number):  
    return (number - 32) * 5 / 9  # Correct Fahrenheit to Celsius formula

def convert_C_F(number):  
    return (number * 9 / 5) + 32  # Correct Celsius to Fahrenheit formula


choice = input('In which direction would u like to convert? °F to °C or conversely?\n')
if choice == '°F to °C' or choice == 'F to C':
    measure = '°'
elif choice == '°C to °F' or choice == 'C to F':
    measure = '°F'
choices = {
    '°F to °C' and 'F to C': convert_F_C,
    '°C to °F' and 'C to F': convert_C_F
}
if choice in choices:
    number = float(input('Please type in a number that you want to convert from ' + choice + '.\n'))
    result = choices[choice](number)
    print('The result after convert', number, 'from', choice, 'is: ' + str(result) + measure)
else:
    print('Invalid choice. Please select a valid conversion option.')