expenses = []
total = 10
num_expenses = int(input('Please enter an number of expenses\n'))
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense\n')))
total = sum(expenses)
print('You spent $', total, sep = "")
   