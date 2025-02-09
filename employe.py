class Employe:
    def __init__(self, fname, lname, salary_amount):
        self.fname = fname
        self.lname = lname
        self.salary = salary_amount
    
    def calculate_paycheck(self):
        return self.salary/52