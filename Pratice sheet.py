# x = 2
# y = 5.4
# z = "Hello"
# print(str(x)+str(y)+z)

# int_string = "6"
# print(type(int(int_string)))
#
# print(float(int_string))
# print(type(float(int_string)))
# x=2.4
# y=5.5
# z = 'hello'
# print(str(x)+str(y)+z)
#
# int_string = 6
# print(type(int_string))
# print(float(int_string))
# print(type(float(int_string)))

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])
# print(thislist[0:2])

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p4 = Person("John", 36)
#
# print(p4.name)
# print(p4.age)


# class User():
#     pass
# class User():
#     pass
#     user1 = User()
#     user1.firstname = "dave"
#     user1.lastname = "pool"
#     print(user1.firstname, user1.lastname)
#
# class User:
#      def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday
#
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#
# user = User ("Dave Bow", "19980127")   #indentation is important. Did NOT work when inline with def
# print(user.name)
# print(user.birthday)
# print(user.first_name)
# print(user.last_name)

### class pratice

# class User:
#     pass
# user1 = User() #user1 is an instance or object
# user1.first_name = "dave"
# user1.last_name = "pool"
# print(user1.first_name)
# print(user1.last_name)
# print(user1.first_name, user1.last_name)

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@company.com"
#
#
# emp_1 = Employee("sassy", "siyan", 5000)
#
# print(emp_1)
################# come back look at youtube

#inheritance is a mechinism in which one class accuires the property of another calss
#it allows you to call methods of the superclass in your subclass
#the primary use case of this is to extend the functionality of the inherited method.
#parent class = super class
#child class = subclass        know as inheritance

from animal import *
class reptile(Animal):
    def __init__(self, age,name):

