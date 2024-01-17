class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# emp_1 is passed automatically to Employee('john','saw',50000) as first argument.
emp_1 = Employee('john', 'saw', 50000)  #
emp_2 = Employee('Test', 'user', 60000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'peter'

print(emp_1.first)
print(emp_1.email) #email doesn't get the peter first name
print(emp_1.fullname())

#using @property and @x.setter we can set email correctly  without making changes to the cilent code