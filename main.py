
# a= "Hello World" # a is a variable of a type of string
# print (a)
# #creation of variables, initiating the variables. printing types of the variables
# # name ="skill city"
# # print (type(name))
# # name =2025
# # print (type(name))
# # name = True
# # print (type(name))
# # name = 20.30
# # print (type(name))

# # print ("Hello world")
# # var = 10 #variable declaration and initialisation assignment statement

# print (5*2/3*2-5*5+5/2)
# print (2_22_222_000)

# a =bool(1) #1 is true, 0 is false
# print (a)


# firstname = 1 #string variable
# lastname = 2 #string variable

# #string concatenation
# print(firstname +lastname)

firstname = "Mayowa" #string variable
lastname = 'Adefemi' #string variable

# #string concatenation
# print(firstname.upper() + " " + lastname.lower())
# print(firstname[0:3]) # May
# print(firstname[::-1]) # reverse

#logical
#comparison == != > < >= <= TRUE / FALSE

# num1 =5
# num2 =7
# print(not(num1 < num2))

#logical operators AND(all conditions must be true to proceed)
# OR (only one condition needs to be true to proceed)
# NOT (reverse i.e true converts to false and vice versa)

# num1 =5
# num2 =7
# print(not(num1 <= num2))

#conditional statements
email ="abc@gmail.com"
password ="1234567"

#login
# if email =="abc@gmail.com" and password =="123456":
#    print("welcome you are logged in")
# else:
#     print("sorry your password and email are not correct")

# if email =="abc@gmail.com":
#     print("email is correct")
# elif password == "1234567":
#     print("password is correct")
# else:
#     print("sorry your password and email are not correct)")

# user_input = int(input("enter your number:"))
# if user_input % 2 ==0 :
#     print("even number")
# else:
#     print("odd number")
# if conditions:
#     statements
# elif conditions:
#     statements
# else:
#     statements

# user_salary =float(input("enter your salary: "))
# starting_year =int(input("enter your start date: "))
# user_years =(2025 - starting_year)
# if user_years >3 :
#      bonus = round (user_salary * 0.07)
#      print ("your bonus is ", bonus)
# else:
#       print ("your bonus is 0")

# user_salary =float(input("enter your salary: "))
# service_years =int(input("enter your start date: "))
# if service_years <2022 :
#      bonus = round (user_salary * 0.07)
#      print ("your bonus is ", bonus)
# else:
#       print ("your bonus is 0")




# 15/01/2025 - Data collection
# Built in Methods

#fruit = ["apple", "banana", "cherry", "Mango"]# list of strings ordered, changeable, duplicates
# print(fruit[3]) # indexing starts from 0 from apple
# print(len(fruit)) #length of variable = 4
# print(type (fruit))
# print("Before addition", fruit)
# fruit.append("banana")
# print("After addition", fruit)
# fruit.remove("banana")
# print("After removal", fruit)
# fruit.pop(len(fruit)-1)# pop removes last item (in this case, list length minus 1)
# print("after removal of last fruit", fruit)

# Tuples
# fruit = ("apple", "banana", "cherry", "Mango") # tuple of strings ordered, unchangeable, duplicates, indexed
# print(fruit) #fruit[0] = "orange" will give an error as 'tuple' does not support item assignment
# list(fruit)
# print(fruit)
# fruit[0]= "orange"
# tuple(fruit)
# print(fruit)


# # Sets (onoredered, unchangeable, not indexed, no duplicates)
# fruit = {"apple", "banana", "cherry", "cherry", "kiwi"} # removes duplicates from data

# print(fruit) # output is not ordered
# # print(fruit[0]) not possible as sets are not indexed

# fruit = {"apple", "banana", "cherry", "cherry", "kiwi"} # removes duplicates from data
# fruit.add("mango") #this should come first before print not together
# print(fruit)

# fruit.clear()
# print(fruit)


# Dictionaries - Phone dictionary- Key value pair - changeable, ordered, no duplicates
# phoneDictionary = { 
#      "John": 123456789,
#      "Jane": 987654321,
#      "Jim" : 14683579
# }

# print(phoneDictionary["Jane"])

# users = { 
#      "user1": {
#          "firstname": "Jane",
#          "lastname": "Doe",
#          "phoneNumber": "12345678",
#          "email" : "janedoe@gmail.com",
#          "address" : "123, lorem Ipsum"
#      },
#      "user2": {
#          "firstname": "John",
#          "lastname": "Doe",
#          "phoneNumber": "12345678",
#          "email" : "janedoe@gmail.com",
#          "address" : "123, lorem Ipsum"
#      }
# }

# print(users["user1"]["lastname"])

# #users["user1"]["address"] = "felhurst crescent" #assigning new value to user 1 address
# #print(users["user1"]["address"])

# summary
#[] = lists
#{} = sets
#() = tuple

# mydata = ("dummy value")
# print(type(mydata))
# mydata2 = ("dummy value",)
# print(type(mydata2))





#18/01/2025
# Write programs using for and while loops
# for loop (use when we know range/ how many times to run for)
# for i in range (1, 50):
#     print (i)

# #while loop (use when we don't know how many times to run for)
# i= 1
# while i< 50:
#     print (i)
#     i = i + 1 #increasing value of i by 1. without this program will run for infinity and crash
#     #i +=1 #increasing value of i by 1
#     #i -=1 #decreasing value of i by 1

# Factorial excercise
# number =1
# user_input = int(input("enter a number: "))
# for i in range (1, user_input+1): #+1 to find the factorial up to and include user_input
#     number*=i

# print(number) #print is outside the loop

# myFirstName = "Muhammed"
# for character in myFirstName:
#     print(character)
# myList = [1,2,3,4,5,6,7,8,9,10]
# for number in myList:
#     print(number)
# mySet = {1,2,3,4,5,6,7,8,9,10}
# for number in mySet:
#     print(number)
# myTuple = (1,2,3,4,5,6,7,8,9,10)
# for number in myTuple:
#     print(number)


#Activity 1
# country_list= ["Italy", "Portugal", "Spain", "China"]
# for country in country_list:
#     print (country)
# if country_list[2] == "Spain" :
#         print ("yaay spain is 3rd in your favourite countries")
# else:
#         print("Boo, I can't believe Spain isn't your 3rd favourite")

#Activity 2
# my_name= "Emmanuel"
# reverse_name = my_name[::-1] #reverse my name
# for character in reverse_name:
#     print (character) 

# name= "Emmanuel Adefemi"
# reversed_name = ""
# for character in name:
#     reversed_name = character + reversed_name
# print(reversed_name)


#save a target number
#guess the number
#if number is correct go forward
#if number is not correct keep trying
#unless the correct number is found
import random

targetNumber = 6
guess = random.randint(0, 750)
counter = 1
# Comparison Operator != means not equal to == means equal to
while guess != targetNumber:
    print("Sorry, that's not it.")
    counter += 1 # Increment the counter
    guess = random.randint(0, 750)
    print("Guess again as your guess was ",guess)
    
    
print("You got it after ",counter," tries!")

