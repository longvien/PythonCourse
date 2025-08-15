acronym = input('Which acronym would u like to input?\n')
definition = input("What's the definition of the acronym?\n")
with open('input.txt', 'w') as file:
    file.write(acronym + ' - ' + definition + '\n')
