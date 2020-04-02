
#Inheritance allows us to define a class that inherits
#all the methods and properties from another class.
# only a sub class can inherit from a superclass





# class A :                              ### PARENT/SUPER CLASS####
#     def feature1(self):
#         print(" Feature 1 is working ")
#
#     def feature2(self):
#         print(" Feature 2 is working ")
#
# class B(A):                             #### CHILD/SUB CLASS###
#     def feature3(self):
#         print(" Feature 3 is working ")
#
#     def feature4(self):
#         print(" Feature 4 is working ")
#
# class C(B):  #### CHILD/SUB CLASS###
#         def feature5(self):
#             print(" Feature 5 is working ")
#
#
# a1 = A             # a only has 2 option as it is the parent class
# a1.feature1()
#
# B1 = B
# B1.feature1() # B1 can access function 1,2 as --class B (A)-- is inherited
#
# C1 = C
# C1.feature1()## although c is inheriting from b, it can all gain acessed to features in
# #class A, as it goes down in class (inherited like a family tree)# multilevel inhereitence

#
#
# class A ():
#
#     def __init__(self):
#         print(" In A init ")
#
#     def feature1(self):
#         print(" Feature 1 is working ")
#
#     def feature2(self):
#         print(" Feature 2 is working ")
#
# class B(A):
#
#     def __init__(self):
#         super().__init__() # calling init method from class A
#         print(" In B init ")
#
#     def feature3(self):
#         print(" Feature 3 is working ")
#
#     def feature4(self):
#         print(" Feature 4 is working ")
#
# class C(A,B):
#
#     def __init__(self):
#         super().__init__()
#         print(" In C init ")
#
# a1 = C()


# Inheritance: a mechanism in which one class acquires the property of another class
# it allows you to call methods of the superclass in your subclass
# primary use case of this is to extend the functionality of the inherited method

# from OOP import class_animal
# class Reptile(animal): #the reptile class (child) inheriting from the animal class (parent)
#     def __init__(self, name, age):
#         super().__init__(name, age) # this super command is a must for inheritance such that everything from the
#                                     # parent (animal) is brought to the child (reptile)
#                                     # let animal class to handle the arguments
#
#     def sleep(self):
#         return ("zzzz I am sleeping")
#     def running(self, speed):
#         return ("I am running in {} km/h".format(speed))
#
# Rept1 = Reptile("Lizzard", 5)
# Rept2 = Reptile("Mosy", 8)
# print(Rept1.eat())
# print(Rept1.running(10))
# print(Rept2.sleep())

# Exercise
# class Teacher:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def talk(self, number):
#         return ("There are {} students in my class.".format(number))
#
# Teacher1 = Teacher("John", "Smith")
# Teacher2 = Teacher("Jane", "Leung")
# print(Teacher1.talk(17))
#
# class Student(Teacher):
#     def __init__(self, first_name, last_name, prog_language):
#         super().__init__(first_name, last_name)
#         self.prog_language = prog_language
#
#     def enjoy(self):
#         return ("{} enjoys to learn {}".format(self.first_name, self.prog_language))
#
#     def chill(self, hobby):
#         return ("{} likes to {}".format(self.first_name, hobby))
#
# student1 = Student("Rachel", "Green", "Python")
# student2 = Student("Lily", "Collin", "Java")
# print(student1.talk(20))
# print(student1.enjoy())
# print(student2.chill("read"))