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

def main():
    choice = input('In which direction would u like to convert? °F to °C or conversely?\n')

    if choice == '°F to °C' or choice == 'F to C':
        number_1 = float(input('Please type in a number that you want to convert to celcius.\n'))
        fahrenheit_to_celcius = convert_F_C(number_1)
        print(number_1, 'is equal to', fahrenheit_to_celcius, '°C')
    elif choice == '°C to °F' or choice == 'C to F':
        number_2 = float(input('Please type in a number that you want to convert to fahrenheit.\n'))
        celcius_to_fahrenheit = convert_C_F(number_2)
        print(number_2, 'is equal to', celcius_to_fahrenheit, '°F')
main()