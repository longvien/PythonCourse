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
     