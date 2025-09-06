def find_acronym():
    look_up = input('Which acronym would you like to find out the meaning?\n')
    found = False
    with open('input.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
        if not found:
            print("Acronym doesn't exist! Pls try again!")
def append_acronym():
    acronym = input('Pls enter the acronym!\n')
    definition = input('Pls enter the definition\n')
    with open('input.txt', 'a') as file:
        file.write(acronym + ' - ' + definition)
def main():
    user_choice = input('Do u want to find(F) or add(A) an acronym?\n')
    if user_choice == 'A':
        append_acronym()
    elif user_choice == 'F':
        find_acronym()
    else:
        print('Invalid choice!')
        exit()
main()