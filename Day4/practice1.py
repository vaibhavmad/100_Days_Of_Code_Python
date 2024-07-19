# Randomness
# Python List
# Final Project: Rock Paper & Scissors, play with computer

# ************RANDOMIZATION***************
# ************RANDOMIZATION***************
# ************RANDOMIZATION***************
# ************RANDOMIZATION***************
# To produce random input from a give list of data
from asyncio import Task
import random
# import newmodule
# import mymodule
# randint produces a random number from the given list, random.randint(1, 10): 
# inclusive in nature and shall show a number between 1 and 10 including 1 and 10
# random_integer = random.randint(1, 4)
# print(random_integer)

# random is a python module. A module is like a section of code with a specific 
# set of funtionality. Random module is created by the python team. In this 
# directory only, I have created a new file by the name of mymodule.py in this 
# file, we have declared the value of pi - 3.148978 now in order to use this 
# value in our program, we shall simply type import mymodule at the top and use 
# the value as shown below
# print(mymodule.pi)

# random_float = random.random()
# random(), gives a non inclusive float between (0.0 and 1.0)
# unlike the above (rand_int), this is not inclusive
# print(random_float)

# print(random_float * random_integer)

# ********Heads or Tail******************
# print("Welcome to the virtual coin toss program:")
# toss = input("enter your choice(heads or tails): ")
# toss_list = ["heads", "tails"]
# toss_result = random.choice(toss_list)
# print(toss_result)
# if toss == toss_result:
#     print("You win")
# else:
#     print("You lose")

# ******other method***********
# random_int = random.randint(0, 1)
# toss_result = " "
# if random_int == 0:
#     toss_result = "heads"
# else:
#     toss_result = "tails"

# print(f"Toss Result: {toss_result}")
# if toss == toss_result:
#     print("Congratulations, You win")
# else:
#     print("You lose, better luck next time")




# ************Lists***************
# ************Lists***************
# ************Lists***************
# ************Lists***************
# ************Lists***************

# Lists is a type of Python Data Structure (organised way of saving grouped data), 
# such as all names of the states of a country in an orderly manner
# example
# fruits = ["Banana", "Orange", "Apple", "Grapes"]
# print(fruits)
# result: ['Banana', 'Orange', 'Apple', 'Grapes']
# print(fruits[1])
# result: Orange
# print(fruits[-1])
# result: last item - Grapes
# fruits[0] = "Pineapple"
# print(fruits[0])
# result: Pineapple

# add a single item at the end of the list:
# fruits.append("new Fruit")
# print(fruits)
# result: ['Pineapple', 'Orange', 'Apple', 'Grapes', 'new Fruit']

# add multiple items at the end, use: extend
# fruits.extend(["New Fruit1", "NewFruit2"])
# print(fruits)
# result: ['Pineapple', 'Orange', 'Apple', 'Grapes', 'new Fruit', 'New Fruit1', 'NewFruit2']

# Do not memorise all these functions, since there's a lot of information. Use search to find
# this information using documentation. Just understand the possibilities. As per Angela, 
# Programming is like an open book exam

# create a program to get the input of names from a user, then pick a random name to
# pay the bill

# name_list = []
# friend_count = int(input("What is the count of friends?\n"))

# for i in range (friend_count):
#     print(i)
#     name_list.append(input(f"Enter the name of friend {i + 1}\n"))

# friend_num = random.randint(0, (friend_count-1))
# print(friend_num)
# print(f"{name_list[friend_num]}, must pay the bill today")
# print(friend_count)
# # this is a git test

# another method
# names = ["hello", "Second", "Third", "Fourth"]
# name_count = len(names)

# random_num = random.randint(0, name_count-1)
# print(random_num)

# print(f"{names[random_num]}, must pay the bill today")




# pirate Task

# take input from user and place the object at in a given row and given cell. 
# structure: three lists, further nested into one list

list_1 = ["#", "#", "#"]
list_2 = ["#", "#", "#"]
list_3 = ["#", "#", "#"]

map = [list_1, list_2, list_3]
print("Here's the map: ")
print(f"{list_1} \n{list_2} \n{list_3}")
treasure_location = input("Where do you want to put the treaure?: ")

cols = ["a", "b", "c"]
col_num = cols.index(treasure_location[0])
row_num = int(treasure_location[1])
map[col_num][row_num] = "X"

print("Your treasure is now secure in vault")
print(f"{list_1} \n{list_2} \n{list_3}")












