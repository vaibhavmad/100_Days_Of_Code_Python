# fizzbuzz game: say you have 5 friends, and all stand in a circle and each friend calls out a number starting 
# from 1. If a person comes across a number that is multiple of 3, say fizz, if someone comes across as number 
# that is a multiple of 5, then he/she should say buzz. if someone comes across a number that is a multiple 
# of both 3 and 5, then you should say fizzbizz. 

user_input_range = int(input("enter the range upto which you want the fizzbuzz to go on?: \n")) + 1

for i in range (1, user_input_range):
    if i % 15 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

