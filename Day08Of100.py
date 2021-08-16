#Functions with Inputs
#simple Function:
# def greet():
#   print("Hello")
#   print("from")
#   print("Greet")

# greet()

# Function that allows for input
# def greet(name):
#   print(f"Hello, {name}")
#   print(f"How do you do {name}")

# greet("Trivikram")
# greet("Siddavatam")

#Positional vs. Keyword Arguments
# funtion with more than one input

# def greet(name, location):
#   print(f"Hello, {name}")
#   print(f"Are you from {location}, what is it like there?")

# greet("Trivikram", "India")
# greet(location="london", name="Alex")

#Exercise - 08/01 Instructions
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# import math
# def paint_calc(height, width, cover):
#   Total_cans = 0
#   Total_cans = math.ceil((height*width)/cover)

#   print(f"You'll need {Total_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Exercise - 08/02 - # Instructions

# Prime Checker: Prime numbers are numbers that can only be cleanly divided by itself and 1. 

# def prime_checker(number):
#   isPrime = True

#   if number > 1:
#     for num in range(2, int(number/2) + 1):
#       if (number % num == 0):
#         isPrime = False
#   else:
#     isPrime = False

#   if isPrime:
#     print(f"{number} is a Prime")
#   else:
#     print(f"{number} is not a Prime")

# n = int(input("Check this number: "))
# prime_checker(number=n)

#Cipher Encoder Program 
#main.py
# import art
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(message, shift_amount, mode):
#   Coded_text = ""
#   if mode == "decode":
#     shift_amount *= -1
#   for char in message:
#     if char in alphabet:
#       original_index = alphabet.index(char)
#       shifted_index = original_index+shift_amount
#       Coded_text += alphabet[shifted_index]
#     else:
#       Coded_text += char

#   print(f"The {mode}d text is {Coded_text}")

# print(art.logo)
# willRepeat = "yes"
# while willRepeat == "yes":
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   if shift > 26:
#     shift %= 26
    
#   caesar(message = text, shift_amount = shift, mode = direction)
#   willRepeat = str(input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")).lower()

# print("GOOD BYE!!")

#art.py
# logo = """           
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88           
# """
