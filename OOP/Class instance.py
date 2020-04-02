class employees:

    raised_amount = 1.04
    num_emp = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

        employees.num_emp += 1 # prints number of employees by adding after each emp created

    def fullname(self):
       return "{} {}". format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raised_amount)


emp_1 = employees("sassy","siyan", 50000)
emp_2 = employees("santi","cazzorla",5050)

employees.raised_amount = 1.10 # can change the raised amount after

print(emp_1.__dict__)

print(emp_1.fullname())
print(emp_1.raised_amount)
print(emp_1.pay)
emp_1.apply_raise() # have to use apply raise to get new figure
print(emp_1.pay)
print(employees.num_emp)