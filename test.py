class Employee:
    def __init__(self, f_name, l_name,):
        self.f_name = f_name
        self.l_name = l_name
class SalaryEmployee(Employee):
    def __init__(self, f_name, l_name, salary):
        super().__init__(f_name, l_name)
        self.salary = salary
    def calculate_salary(self):
        return self.salary/52
class HourlyEmployee(Employee):
    def __init__(self, f_name, l_name, hourly_income, hour_worked):
        super().__init__(f_name, l_name)
        self.hourly_income = hourly_income
        self.hour_worked = hour_worked
    def calculate_salary(self):
        return self.hourly_income * self.hour_worked
class Commission_Employee(SalaryEmployee):
    def __init__(self, f_name, l_name, commision_rate, commision_completed, salary):
        super().__init__(f_name, l_name, salary)
        self.c_rate = commision_rate
        self.c_c = commision_completed
    def calculate_salary(self):
        regular = super().calculate_salary()
        commission = self.c_rate * self.c_c
        return regular + commission
    
class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employee(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.f_name, i.l_name)
        print('----------------------------------------')
    def paycheck_salary(self):
        for i in self.employees:
            print('The paycheck of employee: ' + i.f_name + ' ' + i.l_name + ' is ' + str(i.calculate_salary()))
        print('----------------------------------------')

try: 
    number = input('Please enter a number of new Employees!\n')
except:
    print('Pls enter a valid number')

my_company = Company()
for i in range(number): 
    fname = input('Enter employee first name.\n')
    lname = input('Enter employee last name.\n')
    salary_type = input('Pls enter the paycheck type: Monthly, Hourly, or Commision?\n')
type = {'Monthly': SalaryEmployee, 
        'Hourly': HourlyEmployee,
        'Commision': Commission_Employee}

employee1 = SalaryEmployee('Va', 'Schulze', 1000)
my_company.add_employee(employee1)
employee2 = HourlyEmployee('Elon', 'Musk', 800, 250)
my_company.add_employee(employee2)
my_company.display_employee()
my_company.paycheck_salary()
