from reptile import *
class Snake(Reptile):

    def __init__(self,name,age):
        super().__init__(name,age)

        self.name = name
        self.age = age
    def seek_heat (self):
        return ("let me see some sunshine")
    def sleep(self):
        return ("let me sleeeep")
#
#


