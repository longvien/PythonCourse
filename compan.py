from employe import Employe

class Company:
    def __init__(self):
        self.employees = []
    def add_employees(self, new_employee):
        self.employees.append(new_employee)
    def employees_display(self):
        for i in self.employees:
            print(i.fname, i.lname)
            print('--------------------')
    def salary_a(self):
        for i in self.employees:
            print('$' + str(i.salary))
           
my_company = Company()
employee1 = Employe('Manuel', 'Neuer', 50000)
my_company.add_employees(employee1)
employee2 = Employe('Manuel', 'Neur', 500)
my_company.add_employees(employee2)
employee3 = Employe('Manuel', 'Neue', 5000)
my_company.add_employees(employee3)

my_company.employees_display()
my_company.salary_a()


