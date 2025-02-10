# with open("company.py", "r") as file:
#     lines = file.readlines()
# 
# with open("company.py", "w") as file:
#     for line in lines:
#         file.write("# " + line)
# 
# 
# 
# 
# 
# from employe import Employe
# class Company:
#     def __init__(self):
#         self.employees = []
#     def add_employee(self, new_employee):
#         self.employees.append(new_employee)
#     def display(self):
#         print('Current Employees:')
#         for i in self.employees:
#             print(i.fname, i.lname)
#         print('---------------------')
#     def pay_employees(self):
#         print('Paying Employees:')
#         for i in self.employees:
#             print('Paycheck for', i.fname, i.lname)
#             print(f'Amount: ${i.calculate_paycheck():,.2f}')
#             print('---------------------------------')
# def main():
#     my_company = Company()
#     employee1 = Employe('Sarah', 'Hees', 4000)
#     my_company.add_employee(employee1)
#     employee2 = Employe('Lee', 'Smith', 5000)
#     my_company.add_employee(employee2)
#     employee3 = Employe('Bob', 'Brown', 6000)
#     my_company.add_employee(employee3)
#     my_company.display()
#     my_company.pay_employees()
# main()