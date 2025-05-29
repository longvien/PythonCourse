from employe import Employe
class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")