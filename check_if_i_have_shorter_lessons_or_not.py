temperature = input("Is the temperature higher or reach 25 Celcius today?\n")
if temperature == 'yes' or temperature == 'YES' or temperature == 'Yes' or temperature == 'Y' or temperature == 'y':
    time = int(input("When does it reach 25 Celcius? ex: 12 o'clock = 12 \n"))
    if time <= 12:
        print('You have shorter lessons today!')
    else:
        print("You don't have shorter lessons today!")
else:
    print("You don't have shorter lessons today!")