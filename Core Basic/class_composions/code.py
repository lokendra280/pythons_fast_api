class Salary:
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.base_salary + self.bonus

class Employee:
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self.salary = Salary(base_salary, bonus)

    def display_employee_info(self):
        total_salary = self.salary.calculate_total_salary()
        print(f"Employee Name: {self.name}")
        print(f"Total Salary: {total_salary}")

emp = Employee("John Doe", 50000, 10000)
emp.display_employee_info()