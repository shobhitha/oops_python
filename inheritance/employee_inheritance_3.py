
class Employee():

    increment = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)

#Developer class inherited all attributes and methods from Employee class
#using super()
class Developer(Employee):
    increment = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->' , emp.fullname())





dev_1 = Developer('Rachel','Green', 50000, 'Python')
dev_2 = Developer('Chandler', 'Bing', 60000, 'Java')

mgr_1 = Manager('Joey','Tribiaani',100000,[dev_1])

print(mgr_1.email)

mgr_1.add_employee(dev_2)
mgr_1.print_employees()
mgr_1.remove_employee(dev_2)
mgr_1.print_employees()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

