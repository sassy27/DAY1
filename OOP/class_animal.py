
# class Animal():
#     animal_kind = "Canine"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         return ("{} says I am eating Chicken".format(self.name))
#
# dog1 = Animal("sassy", 22)
# print(dog1.eat())


# abstraction
class Animal():
    def __init__(self, name, age): #mehod/variables inint function, inint give class attributes
        self.name = name
        self.age = age

    def bark(self):
        return "rrrrrr" #method

an1 = Animal("sassy", 22)
an2 = Animal ("sughs", 22)

print(an1.name,an1.age)
print(an1.bark())
