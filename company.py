from employe import Employe
class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):