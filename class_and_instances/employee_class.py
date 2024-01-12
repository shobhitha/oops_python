#example of creating and instantiating class

class Employee:
    pass # python will skip this class if it has "pass" statement in it

# Both are employee instances but have unique data/attributes to each instance
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

#creating instance variables for emp_1
emp_1.first = 'John'
emp_1.last = 'saw'
emp_1.email = 'john.saw@company.com'
emp_1.salary = 50000

#creating instance variables for emp_2
emp_2.first = 'Test'
emp_2.last = 'user'
emp_2.email = 'test.user@company.com'
emp_2.salary = 50000

"""with no __init__ : instance variables creation is redundant and mistakes prone."""