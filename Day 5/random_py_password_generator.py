import random

symbol_list = ["=", "+", "-", "_", ")", "(", "*", "&", "^", "%", \
               "$", "#", "@", "!", ".", ",", "/", "<", ">"]
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alpha_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", \
                        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"  \
                        "u", "v", "w", "x", "y", "z"]
alpha_large = [i.upper() for i in alpha_small]

password_list = [symbol_list, num_list, alpha_small, alpha_large]

print("Welcome to the Random Py Pasword generator!!")

letter_count = int(input("How many letter you want in the password: "))
num_count = int(input("How many numbers would you like?: "))
symbol_count = int(input("How many special characters would you like?: "))

pass_length_range = letter_count + num_count + symbol_count + 1

password_list = []
for i in range(0, symbol_count):
    password_list.append(random.choice(symbol_list))
    
for j in range(0, num_count):
    password_list.append(random.choice(num_list))
    
for h in range(0, letter_count):
    password_list.append(random.choice(alpha_large + alpha_small))
    
random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(password)
    
    
    


