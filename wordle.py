# from random_word import RandomWords
# r = RandomWords()

# # Return a single random word
# word = r.get_random_word()
# print(word)

# word_list = ["crown", "build", "logic", "plane", "focus", "money", "plant", "plate", "pound", "other", "input", "horse", "green", "group", "beans", "guide", "layer", "mayor", "lunch", "limit", "model", "point", "scope", "score", "title", "total", "world"]

# if __name__ == "__main__":
#     loop = True
#     while loop:
#         print("Start a new game? (y/quit)")
#         command = input()
#         if command == "quit":
#             loop = False
#         elif command == "y":
#             print("Hello to Wordle")
#             print('''The Rules of the Game
# 1.Each time the code will randomly select a 5-letter word from the English Dictionary
# 2.You have six tries to guess the word correctly
# 3.If you guess the exact position of a letter in the word it will turn *
# 4.If you guess a letter that exists in the word of the day, but it is in the wrong position it turns !
# 5.If the letter does not exist, it will stay -''')
#             pass

# from random_word import RandomWords
# r = RandomWords()

# # Return a single random word
# print(r.get_random_word())

import random

# List of words for the game
word_list = ["apple", "chair", "beach", "baker", "table", "watch", "music", "house", "juice", "party"]

def play_game():
    # Select a random word from the word list
    secret_word = random.choice(word_list)

    # Initialize the number of attempts and guessed letters
    attempts = 6
    guessed_letters = []

    while attempts > 0:
        # Display the current status of the word
        display_word(secret_word, guessed_letters)

        # Prompt the user for a letter
        guess = input("Guess a word: ").lower()

        # if len(guess) != 1 or not guess.isalpha():
        #     print("Invalid input. Please enter a single letter.")
        #     continue

        # if guess in guessed_letters:
        #     print("You already guessed that letter. Try again.")
        #     continue
        for i in range(5):
            # Add the guessed letter to the list
            guessed_letters.append(guess[i])

        # if guess in secret_word:
        #     print("Correct guess!")
        # else:
        #     print("Wrong guess!")
        #     attempts -= 1


        # Check if the word has been completely guessed
        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word)
            return
        else:
            attempts-=1

    print("Game over. The word was:", secret_word)

def display_word(secret_word, guessed_letters):
    # Display the word with dashes for unguessed letters
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    print(displayed_word)

def is_word_guessed(secret_word, guessed_letters):
    # Check if all letters in the word have been guessed
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

# Start the game
play_game()
