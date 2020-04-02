# Polymorphism: define methods in the child class that have the same name as the methods in the parent class
#               In inheritance, the child class inherits the methods from the parent class possible to modify
#                a method in a child class that it has inherited from the parent class (Method overriding)

import reptile


class Snake(reptile.Reptile):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def seek_heat(self):
        return ("Let me see some sunshine")

    def sleep(self): # the same snake method is in reptile but here the sleep method is modified and change the contact
        return ("Please leave me to sleep peacefully")

Sidney = Snake("DOO", 2)
print(Sidney.sleep())
