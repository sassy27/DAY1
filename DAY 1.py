

'''X = 1
b = 2
hi = "Hello world "
print (hi)
'''

# ''' print("what is your name")
# name = input()
# print("hi")
# print(name)
# '''


# print(" Hello, What is your Full name?")
# name = input()
# print ("Hi", name,",what is your D.O.B?")
# age = input()
# print("what is your address?")
# address = input()
# print("my adresses is", address)
#
# name = input("what is your name")

# a=24
# b=16
# print(a+b)
# print(4* "me")
# print(8%3) #remainder

# FloatNum = 1.356
# IntNum = 4
# print(FloatNum + IntNum)
# Name = "xyz"
# print(str(IntNum)+Name) # add a string str() to add to a num
#
# Example_text ="YIN IS TOP SCORER"
# print(Example_text.lower())
# print(Example_text.capitalize())
# print(Example_text.replace("YIN ", "Sassy "))
#
# concatination
# a="here "
# b="more "
# c="much more"
# d=10
#
# print(a+b+c, d)

# x = 2
# y = 5.4
# z = "Hello"
# print(str(x)+str(y)+z)

# int_string = "6"
# print(type(int(int_string)))
#
# print(float(int_string))
# print(type(float(int_string)))


# booleans
# a = True
# b = False
# print(a==b)
# print(a != b) #not equal
# print(a >= b)
# print(b <= a)

# booleans with strings

# hi = "hello world"
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("h"))
# print(hi.startswith("h"))

# Boolean valuses and numbers
# x = -1
# # y = 2
# # print(bool(x))
# # print(bool(y))
# # print(bool(None))

# Palindrome
# s = "radar"
# if s == s [::-1]:
#     print(s + " is a palindrome")
# else:
#     print(s + "is not a palindrome")

#list is a collection which is ordered and changeable. Allows dulpilcate members

# shopping_list = ["eggs", "bread","Bananas", "biscuits", "milk"]
# # # print(type(shopping_list))
# # # print(shopping_list[0])
# # # print(shopping_list[-1])
# # # shopping_list [1] = "roti"
# # # print(shopping_list)

# shopping_list = ["eggs", "bread","Bananas", "biscuits", "milk"]
# shopping_list.pop(-2) # removes an item
# print(shopping_list)
# shopping_list.append("ice cream") # adds to list
# print(shopping_list)
# print(len(shopping_list)) # how many iteams
#
# mixture = [1,2,3,"one","two","three"]
# print(mixture)

# a = 10
# b = 20
# if (a>b):
#     print("{} a is bigger than {}".format(a,b)) #. format brings in the values into {}
# else:
#     print("{} a is bigger than {}".format(b, a))
#
# a = input("ENTER A NUMBER ")
# b = input("ENTER A NUMBER ")
# c = input("ENTER A NUMBER ")
#
# if (a>b and a>c):
#      print("{} is bigger than {} and {}".format(a,b,c)) #. format brings in the values into {}
# elif (b>a and b>c):
#      print("{} is bigger than {} and {}".format(b,a,c))
# else:
#      print("{} is bigger than {} and {}".format(c,a,b))
#
# list_data = [1, 2, 3, 4,5] # m can be anything, so m * everything
# for m in list_data:
#     print (m * 2)

#declear a list of 10 numbers
#have a check condition like if a<15
#if the condition is satisfied write it to another list and print the list

list_Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
New_list =[]
for num in list_Data:
    if num>5:
        New_list.append(num)
    else:
        continue

print(New_list)

