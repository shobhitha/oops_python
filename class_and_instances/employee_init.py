class Employee:

#_Each method in a class takes instances as first argument automatically.
# By convention we name the instance variable passsed to method as self
# first, last, pay and email are called attributes of class. emp_1, emp_2 are called instance variables or objects of class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#emp_1 is passed automatically to Employee('john','saw',50000) as first argument.
emp_1 = Employee('john','saw',50000) #
emp_2 = Employee('Test','user',60000)


print(emp_1.email)
print(emp_2.email)

#lines 25 and 26 are doing the same thing. line 25 gets converted to 26 when it is run
print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_2.fullname())

