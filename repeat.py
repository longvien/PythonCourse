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
    def add_workes(self, new_worker):
        self.workers.append(new_worker)
    def print_workers(self):
        print('Current Workers: ')
