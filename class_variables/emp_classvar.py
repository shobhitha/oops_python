#class name convention : start with caps and use camelcase . Do not use underscore

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
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)

emp_1 = Employee('John', 'Saw', 50000)
emp_2 = Employee('Test', 'User', 6000)
print('number of employees {}'.format(Employee.num_emp))

# all three print 1.04. interpreter looks if emp_1 has increment variable.
# If no, then it looks at class variables.So all 3 print 1.04
print(Employee.increment)
print(emp_1.increment)
print(emp_2.increment)

#print the attributes in namespace
print(Employee.__dict__)
print(emp_1.__dict__)

# increment is created in emp_1 namespace
emp_1.increment = 1.05
print(Employee.__dict__)
print(emp_1.__dict__)

print(Employee.increment) #1.04
print(emp_1.increment) # 1.05
print(emp_2.increment) # 1.04




