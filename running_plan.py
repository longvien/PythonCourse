choice = input('Please enter a day that you want to know the plan!\n')
found = False
with open('running_plan.txt') as file:
    for line in file:
        if choice in line:
            print(line)
            found = True
    if not found:
        print('Invalid choice!!!')