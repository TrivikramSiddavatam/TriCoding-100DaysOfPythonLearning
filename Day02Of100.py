#Data Types and Type Checking
## String
# print("Hello"[0])
# print("Hello"[1])
# print("Hello"[2])
# print("Hello"[3])
# print("Hello"[4])

# print(type("123"+"456"))

##Integer
# print(type(123+456))

##Float
# print(type(3.14159))

##Boolean
# print(type(True))
# print(type(False))

#Type Error and Type Conversion
# num_char = len(input("What is your Name?"))
# new_num_char = str(num_char)
# print("Your name contains "+new_num_char+" Characters")

# Program 02/01
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number_sum = first_digit + second_digitigit_number_str[1]))
#two_digit_number_sumsecond_digitfirst_digit

#Mathematical Operations in Python
# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

# Program 02/02
# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. The BMI is a measure of some's weight taking into account their height.
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# BMI = float(weight) / (float(height) ** 2)
# print(int(BMI))

#Number Manipulation and F Strings in Python

# print(round(8/3))
# print(8//3)

# score = 0

#user scores a point
# score += 1
# score -= 1
# score *= 1
# score /= 1

#f-string
# height = 1.8
# isWinning = True

# print(f"Your score is {score}  Height is {height}, you are winning is {isWinning}")

# Your Life in Weeks
# Program 2-3: Instructions
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# age = int(age)
# Remaining_Age = 90 - age
# Remaining_days = Remaining_Age * 365
# Remaining_weeks = Remaining_Age * 52
# Remaining_months = Remaining_Age * 12

# print(f"You have {Remaining_days} days, {Remaining_weeks} weeks, and {Remaining_months} months left.")

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the Tip calculator")
totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage of tip you would like to give? 10, 12, or 15? "))
SplitCount = int(input("How many people o split the bill? "))
FinalBill = round(((totalBill / SplitCount) * (1+(tipPercent/ 100))),2)

print(f"Each person should pay: ${FinalBill}")
