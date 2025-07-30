from Employee_Inheritance import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    def add_employees(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):
        print('Current Employees: ')
        for i in self.employees:
            print(i.f_name, i.l_name)
        print('----------------------------------------')
    def salary_display(self):
        for i in self.employees:
            print('Paycheck/week for ' + i.f_name + ' ' + i.l_name + ' is ' + str(i.calculate_salary()) + ' $')
        print('----------------------------------------')
def main():
    my_company = Company()
    employee1 = SalaryEmployee('Long', 'Vien', 8000000)
    my_company.add_employees(employee1)
    employee2 = HourlyEmployee('Elon', 'Musk', 25, 50)
    my_company.add_employees(employee2)
    employee3 = CommissionEmployee('Christian', 'Klein', 15000, 5, 200)
    my_company.add_employees(employee3)
    my_company.display_employees()
    my_company.salary_display()
main()