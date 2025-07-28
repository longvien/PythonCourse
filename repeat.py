class Employee:
    def __init__(self, first_name, last_name, salary):
        self.fname = first_name
        self.lname = last_name
        self.income = salary
    def calculate_salary(self):
        return self.income/52
class Company:
    def __init__(self):
        self.workers = []
    def add_workers(self, new_worker):
        self.workers.append(new_worker)
    def print_workers(self):
        print('Current Workers: ')
        for i in self.workers:
            print(i.fname, i.lname)
            print('----------------------------------------')
    def workers_income(self):
        for i in self.workers:
            print('Weekly salary of', i.fname, i.lname, 'is', i.calculate_salary())
            print('----------------------------------------')
number = int(input("Enter a number of employees:\n")) 
my_company = Company()
for i in range(number):
    f_name = input('Enter employee first name:\n')
    l_name = input('Enter employee last name:\n')
    salary = float(input('Enter employee yearly salary:\n'))

    
    worker = Employee(f_name, l_name, salary)
    my_company.add_workers(worker)

my_company.print_workers()
my_company.workers_income()
