class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    @property
    def email(self):
        return '{}.{} @company.com'.format(self.first, self.last)

    @property
    #method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John', 'Smith', 70000)



print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'peter'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

#@property lets us to access email and fullname as attributes so we don't have to make changes to the client code