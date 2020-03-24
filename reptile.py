

from animal import *
class Reptile (Animal):

    def __init__(self,name,age):
        super().__init__(name,age)

    def sleep(self):
        return ("zzzz i am sleeping")
    def running (self,speed):
        return ("i am running in {} speed".format(speed))

Rept1= Reptile("lizzard", 5)
Rept2 = Reptile("Mosy", 8)