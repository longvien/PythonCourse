class Employe:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def calculate_paycheck(self):
        return self.salary/26 # salary divide to 52 because we need to 
    #- calculate the salary of the employee in 1 week    
    