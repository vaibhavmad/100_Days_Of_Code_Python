import random
import hangman_art
import hangman_words
print(hangman_art.logo)
to_guess_word = random.choice(hangman_words.word_list)
to_guess_list = list(to_guess_word)
blank_list = []
function_list = []
for _ in to_guess_list:
    blank_list += "_"
print(" ".join(blank_list))
game_lives = 6
live_status = 0
game_status = True
while game_status == True:
    print()
    guess = input("Guess an alphabet: ").lower()
    for i in range(len(blank_list)):
        if guess == to_guess_list[i]:
            blank_list[i] = guess
    print(" ".join(blank_list))
    if guess not in to_guess_word:
        game_lives -= 1
        print(hangman_art.stages[game_lives])
        print(f"You have {game_lives} lives left.")
        if game_lives == 0:
            game_status = False
            print("You lose!")
    if "_" not in blank_list:
        game_status = False
        print("You win")