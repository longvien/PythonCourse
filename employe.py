class Employe:
     def __init__(self, first_name, last_name, salary):
         self.fname = first_name
         self.lname = last_name
         self.salary = salary
     def calculate_paycheck(self):
         return self.salary/52 # salary divide to 52 because we need to 
     #- calculate the salary of the employee in 1 week    
