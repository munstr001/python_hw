class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, sales, bonus_percent):
        super().__init__(name, salary)
        self.sales = sales
        self.bonus_percent = bonus_percent

    def calculate_salary(self):
        return super().calculate_salary() + self.sales * self.bonus_percent / 100


class Developer(Employee):
    def __init__(self, name, salary, overtime_hours, hourly_rate):
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return super().calculate_salary() + self.overtime_hours * self.hourly_rate


if __name__ == '__main__':
    employees = [
        Employee('Иван', 45000),
        Manager('Анна', 60000, 300000, 5),
        Developer('Денис', 90000, 12, 1000)
    ]
    for employee in employees:
        print(f'{employee.name}: {employee.calculate_salary():.2f} руб.')
