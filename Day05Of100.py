#Using the for loop with Python Lists

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")

#Exercise 05/01 Instructions

# You are going to write a program that calculates the average student height from a List of heights.

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# Total_Height = 0
# Total_students = 0
# for height in student_heights:
#   Total_Height += height
#   Total_students += 1

# print(round(Total_Height/Total_students))

#Exercise 05/02 - Instructions
# You are going to write a program that calculates the highest score from a List of scores.

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# max_score = 0
# for score in student_scores:
#   if max_score < score:
#     max_score = score

# print(f"The highest score in the class is: {max_score}")

#for loops and the range() function
# total = 0
# for number in range(1,101):
#   total += number

# print(total)

#Exercise - 05/03 - Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

#Ex01
# total = 0
# for number in range(0,101,2):
#   total += number
# print(total) 

#Ex02
# total = 0
# for number in range(1,101):
#   if number % 2 == 0:
#     total += number    
# print(total) 

# Exercise - 05/04 Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for number in range(1,101):
#   if (number % 3 == 0) and (number % 5 == 0):
#     print(f"FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# Exercise 05/05 - Password Generator App
#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for letter in range(1, nr_letters+1):
#       password += random.choice(letters)

# for symbol in range(1, nr_symbols+1):
#       password += random.choice(symbols)

# for number in range(1, nr_numbers+1):
#       password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password_list = []
# for letter in range(1, nr_letters+1):
#       password_list.append(random.choice(letters))

# for symbol in range(1, nr_symbols+1):
#       password_list.append(random.choice(symbols))

# for number in range(1, nr_numbers+1):
#       password_list.append(random.choice(numbers))

# random.shuffle(password_list)
# for char in password_list:
#   password += char

# print(f"Your Generated Password is: {password}")
