class Employee():
    num_emp = 0
    increment = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.increment = amount

    # classmethod as alternate constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    #static methods have logical relation with the class but doesn't depend on any instance or class variables
    # if a method is not using self or cls inside it then it most likely can be made a staticmethod
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('John', 'Saw', 50000)
emp_2 = Employee('Test', 'User', 6000)

Employee.set_raise_amt(1.05)

print(Employee.increment)
print(emp_1.increment)
print(emp_2.increment)


emp1_string = 'John-Saw-50000'
new_emp = Employee.from_string(emp1_string)
print(new_emp.email)
print(new_emp.pay)

import datetime

my_date = datetime.date(2023,7, 10)
print(Employee.is_workday(my_date))

my_date = datetime.date(2024,1, 13)
print(Employee.is_workday(my_date))