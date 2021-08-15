#Random Module
# import random
# c = random.randint(1,10)
# print(c)

# c = random.random()
# print(c)

#Exercise 04/01 - Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# import random
# c = random.randint(0, 1)
# if c == 0:
#   print("Tails")
# elif c == 1:
#   print("Heads")
# else:
#   print("Error")

#Understanding the Offset and Appending Items to Lists
# sampleList = ["sample", "robot", "country", "Apple", "ball"]
# sampleList[1] = "Chopper"

# sampleList.extend(["Luffy","Zoro", "Ussap", "Nami"])
# print(sampleList)

#Exercise - 04/02 - Instructions
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# Head_Count = len(names) - 1
# pickerNumber = random.randint(0, Head_Count)
# print(f"{names[pickerNumber]} is going to buy the meal today!")

#IndexErrors and Working with Nested Lists
# sampleList = ["Chopper", "robot", "country", "Apple", "ball", "Luffy","Zoro", "Ussap", "Nami"]

# print(sampleList[15])
  # Traceback (most recent call last):
  # File "main.py", line 41, in <module>
  #   print(sampleList[15])
  # IndexError: list index out of range 

#Alphabets = ["a", "b", "c", "d", "A", "B", "C", "D"]
# Uppercase = ["A", "B", "C", "D"]
# Lowercase = ["a", "b", "c", "d"]
# Alphabets = [Uppercase, Lowercase]

# print(Alphabets[1][1])

# Exercise - 04/03 - Instructions
# You are going to write a program which will mark a spot with an X.
# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# This is to try and simulate the coordinates on a real map.

# row1 = ["⬜️","⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️","⬜️"]
# row4 = ["⬜️","⬜️","⬜️","⬜️"]

# map = [row1, row2, row3, row4]
# print(f"{row1}\n{row2}\n{row3}\n{row4}")
# position = input("Where do you want  to put the treasure? ")

# map[int(position[0])-1][int(position[1])-1] = "X"
# print(f"{row1}\n{row2}\n{row3}\n{row4}")

# Exercise - 04/04 - Instructions
# Write a Program for Rock, Paper and Scissors game
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# handsign = [rock, paper, scissors]
# User_choice = int(input("Please select your hand sign, type 0 for Rock, 1 for Paper or 2 for Scissors "))
# Computer_Choice = random.randint(0,2)

# if (User_choice >= 3 or User_choice < 0):
#   print("YOU LOSE!, Invalid Choice of Hand!  COMPUTER WIN")
# else:
#   print(f"You Choose \n{handsign[User_choice]} ")
#   print(f"Computer Choose \n{handsign[Computer_Choice]} ")

#   if User_choice == 0 and Computer_Choice == 2:
#     print("YOU WIN")
#   elif User_choice == 2 and Computer_Choice == 1:
#     print("YOU WIN")
#   elif User_choice == 1 and Computer_Choice == 0:
#     print("YOU WIN")
#   elif (User_choice == Computer_Choice):
#     print("GAME DRAW")
#   else:
#     print("YOU LOSE!, COMPUTER WIN")
