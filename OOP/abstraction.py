# Abstraction : displaying only essential information to the user and hiding the details from the user


from class_animal import Animal # can use * as well which means fetch everything from animal.py
                                # this step hide all the class code from the users

Dog1 = Animal("Nyme", 10)
Dog2 = Animal("Mone", 5)
print(Dog2.name)