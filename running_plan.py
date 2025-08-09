choice = input('Pls enter a day that u want to hnow the plan!\n')
found = False
with open('running_plan.txt') as file:
    for line in file:
        if choice in line:
            print(line)
            found = True
    if not found:
        print('Invalid choice!')




choice = input('Pls enter a day that u want to know the training paln for:\n')
found = False
with open('running_paln.txt') as file:
    for line in file:
        if choice in line:
            print(line)
            found = True
    if not found:
        print('Invalid Syntax')

