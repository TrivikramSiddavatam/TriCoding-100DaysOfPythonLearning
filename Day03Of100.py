#Control Flow with if / else and Conditional Operators
# if condition:
#   do this
# else:
#   do this

# Pass_Score = 35
# if Pass_Score > 35:
#   print("Pass")
# else:
#   print("Fail")

#Program#01
# print("welcome to the rollercoster!")
# height = int(input("what is you height in CMs?"))

# if height >= 120:
#   print("You can Ride")
# else:
#   print("Sorry!, you have to grow taller before you can ride")

# Instructions - exercise 03/01
# Write a program that works out whether if a given number is an odd or even number. 

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

#Nested if statements and elif statements
#Program#02
# print("welcome to the rollercoster! v2.0")
# height = int(input("what is you height in CMs?"))

# if height >= 120:
#   print("You can Ride")
#   age = int(input("what is your Age? "))
#   if age < 12:
#     print("You pay $5")
#   elif age <=18:
#     print("You pay $7")
#   else:
#     print("You pay $12")
# else:
#   print("Sorry!, you have to grow taller before you can ride")

## BMI Calculator 2.0
# Instructions - Exercise : 03/02
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.
# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = round(weight / height ** 2)
# if BMI < 18.5:
#   print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#   print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#   print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#   print(f"Your BMI is {BMI}, you are obese.")
# else:
#   print(f"Your BMI is {BMI}, you are clinically obese.")

#Leap Year
# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print(" Leap Year")
#     else:
#       print("Not Leap Year")
#   else:
#     print("Leap Year")
# else:
#   print("Not Leap Year")

#Multiple If Statements in Succession
#Example #Program#03
# print("welcome to the rollercoster! v3.0")
# height = int(input("what is you height in CMs?"))

# ticket = 0
# if height >= 120:
#   print("You can Ride")
#   age = int(input("what is your Age? "))
#   if age < 12:
#     print("Child Ticket $5")
#     ticket = 5
#   elif age <=18:
#     print("Youth Ticket $7")
#     ticket = 7
#   else:
#     print("Adult Ticket $12")
#     ticket = 12
  
#   wants_Photo = input("Do you want a photo taken? Y or N ")
#   if wants_Photo == "Y":
#     ticket += 3
  
#   print(f"final ticket you pay ${ticket}")
# else:
#   print("Sorry!, you have to grow taller before you can ride")


#Exercise - 03/03 - Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Small Pizza: $15
# Medium Pizza: $20
# Medium Pizza: $20
# Large Pizza: $25
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# Bill = 0
# if size == "S":
#   Bill += 15
# elif size == "M":
#   Bill += 20
# else:
#   Bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     Bill += 2
#   else:
#     Bill += 3

# if extra_cheese == "Y":
#   Bill += 1

# print(f"Your final bill is: ${Bill}")

#Logical Operators
#Example #Program#03
# print("welcome to the rollercoster! v4.0")
# height = int(input("what is you height in CMs?"))

# ticket = 0
# if height >= 120:
#   print("You can Ride")
#   age = int(input("what is your Age? "))
#   if age < 12:
#     print("Child Ticket $5")
#     ticket = 5
#   elif age <=18:
#     print("Youth Ticket $7")
#     ticket = 7
#   elif age >= 45 and age <= 55:
#     print("Have a Free ride")
#   else:
#     print("Adult Ticket $12")
#     ticket = 12
  
#   wants_Photo = input("Do you want a photo taken? Y or N ")
#   if wants_Photo == "Y":
#     ticket += 3
  
#   print(f"final ticket you pay ${ticket}")
# else:
#   print("Sorry!, you have to grow taller before you can ride")

#Exercise - 03/04 # Instructions
# You are going to write a program that tests the compatibility between two people.  

# To work out the love score between two people:
# > Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 

# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 

# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name = name1+name2
# name = name.lower()

# T_Count = name.count("t")
# R_Count = name.count("r")
# U_Count = name.count("u")
# E_Count = name.count("e")
# TRUE_count = T_Count+ R_Count+ U_Count+ E_Count

# L_Count = name.count("l")
# O_Count = name.count("o")
# V_Count = name.count("v")
# E_Count = name.count("e")
# LOVE_count = L_Count+ O_Count+ V_Count+ E_Count

# LOVE_Score = int(str(TRUE_count)+str(LOVE_count))

# if ((LOVE_Score < 10) or (LOVE_Score > 90)):
#   print(f"Your score is {LOVE_Score}, you go together like coke and mentos.")
# elif ((LOVE_Score >= 40) and (LOVE_Score <=50)):
#   print(f"Your score is {LOVE_Score}, you are alright together.")
# else:
#   print(f"Your score is {LOVE_Score}")

#Exercise - 03/05
# Tell a Story of treasure Hunt
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

Action = input("You came across a Crossing!, Which way do you want to go? left or right? \n")
print(Action)
if Action.upper() == "LEFT":
  Action = input("You Encountered a River! Do you want to wait for a Boat or swim across? type 'wait' or 'swim' \n")
  if Action.upper() == "WAIT":
    Action = input("Entered the Treasure castle, Founs 3 doors. Read, Yellow and Blue! Which one you want to choose \n")
    if Action.upper() == "RED":
      print("Burnt by Fire!, GAME OVER!!")
    elif Action.upper() == "BLUE":
      print("Eaten by Beast!, GAME OVER!!")
    elif Action.upper() == "YELLOW":
      print("YOU WIN")
    else:
      print("GAME OVER")
  else:
    print("Attacked by trout!, GAME OVER !!")
else:
  print("Fallen into a hole! GAME OVER !!")
