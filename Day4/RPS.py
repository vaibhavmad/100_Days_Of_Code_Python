import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
rps_list = ["Rock", "Paper", "Scissors"]
comp_input = random.randint(0, 2)
print(f"Computer chose: {rps_list[comp_input]}")

if user_input >= 3 or user_input < 0:
     print("That's an invalid response, please try again")
else:
    if (user_input == 0 and comp_input == 2) or (user_input == 2 and comp_input == 1) or (user_input == 1 and comp_input == 0):
         print("You win")
    elif user_input == comp_input:
        print("It's a draw")
    else:
         print("You lose")