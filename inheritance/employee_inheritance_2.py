
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
    increment = 1.10

dev_1 = Developer('Rachel','Green', 50000)
dev_2 = Developer('Chandler', 'Bing', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

#changing increment attribute in subclass doesn't have any affect on parent class attribute
dev_1 = Employee('Rachel','Green', 50000)
dev_2 = Developer('Chandler', 'Bing', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)