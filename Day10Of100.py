#Functions with Outputs
# def format_name(f_name, l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()

#   return f"{formated_f_name} {formated_l_name}"

# print(format_name("TriVIKRAM", "sidDAVAtam"))

#multiple Return values
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You Din't provide valid inputs."

#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()

#   return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("what is your First Name "), input("What is your Last name ")))

#Exercise 10/01 
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(Check_year, check_month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and check_month == 2:
#     return 29
#   return month_days[check_month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

#Exrecise: 10/02 - calculator Program
#main.py
# import art

# #Add
# def add(n1, n2):
#   return n1+n2

# #Substract
# def substract(n1, n2):
#   return n1-n2

# #Multiply
# def multiply(n1, n2):
#   return n1*n2

# #Divide
# def divide(n1, n2):
#   return n1/n2

# operations = {
#   "+" : add,
#   "-" : substract,
#   "*" : multiply,
#   "/" : divide
# }

# def calculator():
#   print(art.logo)
#   repeat = "y"
#   num1 = float(input("What's the first number? "))

#   while repeat == "y":
#     for oprand in operations:
#       print(oprand)
#     choosen_oprand = input("Pick an operation from the list above: ")

#     num2 = float(input("What's the next number? "))

#     calculation = operations[choosen_oprand]
#     result = calculation(num1, num2)

#     print(f"{num1} {choosen_oprand} {num2} = {result}")
#     repeat = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'exit' to close the calculator: "))
#     if repeat == "y":
#       num1 = result
#     elif repeat == "n":
#       calculator()
#     else:
#       return

# calculator()

#art.py
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
# |_____________________|
# """

