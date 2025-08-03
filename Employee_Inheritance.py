class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
class SalaryEmployee(Employee):
    def __init__(self, f_name, l_name, salary):
        super().__init__(f_name, l_name)
        self.salary = salary
    def calculate_salary(self):
        return self.salary/12   
class HourlyEmployee(Employee):
    def __init__(self, f_name, l_name, weekly_hours, hourly_rate):
        super().__init__(f_name, l_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.weekly_hours * self.hourly_rate
class CommissionEmployee(SalaryEmployee):
    def __init__(self, f_name, l_name, salary, sales_num, com_rate):
        super().__init__(f_name, l_name, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    def calculate_paycheck(self):
        regular_salary = super().calculate_salary()
        total_commission = self.sales_num * self.com_rate
        return regular_salary + total_commission
    
