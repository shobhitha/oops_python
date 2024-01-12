
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
class Developer(Employee):
    pass

dev_1 = Employee('Rachel','Green', 70000)
dev_2 = Employee('Chandler', 'Bing', 80000)

print(dev_1.email)
print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.fullname())

#Method Resolution order

dev_1 = Developer('Rachel','Green', 70000)
dev_2 = Developer('Chandler', 'Bing', 80000)

print("***Python following method resolution order***")
print(dev_1.email)
print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.fullname())

print(help(Developer))  #shows method resolution order and attributes inherited from parent class

