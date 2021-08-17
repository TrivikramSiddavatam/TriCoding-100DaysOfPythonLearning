#The Python Dictionary: Deep Dive
# Mathamatics = {
#   "Add": "Addition eg a+b",
#   "Sub": "Substraction eg a-b",
#   "Mul": "Multiplication eg a*b",
#   "Div": "Division eg a/b"
# }

# Retriving the items
# print(Mathamatics["Add"])

# print(Mathamatics["Adf"])
  # Traceback (most recent call last):
  #   File "main.py", line 10, in <module>
  #     print(Mathamatics["Adf"])
  # KeyError: 'Adf'

# print(Mathamatics[Add])
#   Traceback (most recent call last):
#     File "main.py", line 17, in <module>
#       print(Mathamatics[Add])
#   NameError: name 'Add' is not defined

#Adding new Item to Dictionary
# Mathamatics["Mod"] = "Modulas eg a%b"
# print(Mathamatics)

#Creating Empty Dictionary
# Empty_dic = {}

#wiping existing Dictionary
# Mathamatics = {}
# print(Mathamatics)

#Edit an item
# Mathamatics["Mod"] = "Modulo Division eg a%b"
# print(Mathamatics)

#Loop thru Dictionary
# for key in Mathamatics:
#   print(key)
#   print(Mathamatics[key])


# Exercise 09/01 Instructions
#---------------------------------------------------------
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}
# for student in student_scores:
#   score = int(student_scores[student])
#   if score >= 91 and score <= 100:
#     Grade = "Outstanding"
#   elif score >= 81 and score <= 90:
#     Grade = "Exceeds Expectations"
#   elif score >= 71 and score <= 80:
#     Grade = "Acceptable"
#   else:
#     Grade = "Fail"

#   student_grades[student] = Grade    

# print(student_grades)

#Nesting Lists and Dictionaries
# Travel_log = {
#   "France" : {"Visited_Cities": ["Paris", "Lille", "Dijon"], "Total_Visited" : 5},
#   "Germany" : {"Visited_Cities": ["Berlin", "Hamburg", "Stuttaurt"], "Total_Visited" : 12}
# }

# print(Travel_log)

# Exercise - 09/02 - Instructions 
#-----------------------------------------
#You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(Visited_Country, Times_Visited, Visited_Cities):
#   add_country = {}
#   add_country["country"] = Visited_Country
#   add_country["visits"] = Times_Visited
#   add_country["cities"] = Visited_Cities

#   travel_log.append(add_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Exercise - 09/03 - Silent Bidding Program
#-----------------------------------------
#main.py
# from replit import clear
# from art import logo

# print(logo)
# Bid = {}

# def Bidding():
#   continue_bid = "Yes"
#   while continue_bid == "Yes":
#     Bidder_Name = str(input("What is your name? "))
#     Bidder_Amount = float(input("What is your Bidding Amount? $"))
#     Bid[Bidder_Name] = Bidder_Amount

#     continue_bid = str(input("Are there any other Bidders after you? type 'Yes' or 'No' "))
#     clear()

# def CheckForWinner(Bidding_Record):
#   Final_bid = 0.0
#   Winner = ""
#   for bidder in Bidding_Record:
#     if Bid[bidder] > Final_bid:
#       Final_bid = Bid[bidder]
#       Winner = bidder

#   print(f"Winner of this Bidding is {Winner} with an amount ${Final_bid}")

# Bidding()
# CheckForWinner(Bid)

#art.py
# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
