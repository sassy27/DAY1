

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

# single = means assigining too, == means comparisons
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

# int_string = 6
# print(int(int_string))

# Palindrome
# s = "radar"
# if s == s [::-1]:
#     print(s + " is a palindrome")
# else:
#     print(s + "is not a palindrome")

#collections - 4 types --- lists,tuples,dictionary, sets and frozen sets.


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
# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[-2::-1])

# list = [10,111,24,56,78,75,65,80]
# listOdd =[]
# listEven = []
# for num in list:
#     if num%2 == 0:
#         listEven.append(num)
#     else:
#         listOdd.append(num)
# print(list)
# print(listOdd)
# print(listEven)

# #Tuples
# # tuples is a collection is ordered and unchanable and allows duiplicates
# essentials = ("bread", "eggs", "milk") #unchangeable
# print(essentials)
# print(essentials.count("bread")) #counding number of iteams


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

# list_Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# New_list =[]
# for num in list_Data:
#     if num>5:
#         New_list.append(num)
#     else:
#         continue
#
# print(New_list)

#Dictionaries
# is a collection which is ordered, chanageable, and indexed
#we use curly brackets and dictionaries have keys and values

# student_1 = {
#    "names": "susan",    #names = keys values = susan
#    "stream": "teach",
#    "completed_lessons":4,
#    "completed_lessons_names": ["variables", "data_types", "set_up"] #index [0],[1],[2]-is setup
# }
# print(student_1)
# print(student_1["stream"])
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
# student_1["completed_lessons_names"].remove("data_types")
# print(student_1)

# #SETS
# #is a collection which is un ordered and un indexed
# #sets are written in curley brackets
#
# car_parts = {"wheels","doors","exchaust"} # it will not print in this order (unindexed)
# print(car_parts)
# car_parts.add("windows")
# car_parts.discard("doors")
# print(car_parts)

# #Frozen sets
# # are immuatable versions of the set similar to tuple
# x = frozenset([1, 2, 3, 4]) #to remain constant throughout e.g D.O.B/ POSTCODE
# print(type(x))

# #Contol flow -------------------------how to use else or elif
# # if statements and while loop
# age = 14
# if (age<=19):
#     print ("you are too young")
# else:
#     print("you are good to go")

# if there is more than 2 conditions you can have to end with else. so elif,elif,elif THEN else....
#=============================================================================
# film_rating = input("What is the film rating? ")
# if film_rating.lower() == "universal":
#     print("All age groups can watch this film.")
# elif film_rating.lower() == "pg":
#     print("General viewing, but some scenes mau be unsutable for young children.")
# elif film_rating.lower() == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contained material that is not generally suitable for "
#           "children aged under 12. No one younger than 12 may see a 12A"
#           " film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#     print("No one younger than 18 may see an 18 film in a cinema")
# else:
#     print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
#
# print(film_rating)
#==================================================================================
#Exercise fizzbuzz
#if the number is divisible by 3 print fizz, if it is divisible by 5 print buzz
#if divisible by both print fizz buzz
#you can get input as number or range

# number = int(input("enter your number"))
# if (number % 3) == 0 and (number % 5) == 0:
#     print("fizzbuzz")
# elif (number % 3) == 0:
#     print(number)

# #For loop
# fruits = ["apples","banana","cherry"]
# for x in "banana":
#     print(x)
#     if x == "banana":
#         break
# for x in range(6):
#     print(x)
#     else print("finally finished")

# adj = ["red,","big","tasty"]
# fruit = ["apples", "banana", "cherry"]
# for x in adj:
#   for y in fruit:
#    print(x,y)

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4, 5, 6]] #list of list inside list
#
# for data in embedded_lists:
#     print(data)
#     for num in data:
# #         print(num)
#
# dict_data = {1: {"name":} "Branson", "money": "$0.05"}, 2:{"name": "Masha", "money": "$3.66" },
#            3: {"name": "Roscoe", "Money": "$1.14"}



# #while loop
# x = 0 #any value
# while x<10:
#     print (f"its working --> {x}")
#     x = x + 1
#
# x = 0 #any value

