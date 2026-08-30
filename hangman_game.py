# Task 1: Hangman Game
# A simple text based hangman game

import random

# list of predefined words
words = ["python", "hangman", "laptop", "coding", "internship"]

def play():
    word = random.choice(words)   # pick a random word from list
    guessed = []                  # letters guessed so far
    wrong = 0                     # count of wrong guesses
    max_wrong = 6

    print("Welcome to Hangman Game!")
    print("Word length is:", len(word))

    while wrong < max_wrong:
        # display the word with blanks
        display = ""
        for letter in word:
            if letter in guessed:
                display = display + letter + " "
            else:
                display = display + "_ "
        print("\nWord: " + display)
        print("Wrong guesses:", wrong, "/", max_wrong)

        guess = input("Enter a letter: ")
        guess = guess.lower()

        if guess in guessed:
            print("You already guessed that letter.")
        elif guess in word:
            guessed.append(guess)
            print("Correct guess!")
        else:
            guessed.append(guess)
            wrong = wrong + 1
            print("Wrong guess!")

        # check if all letters guessed
        found = True
        for letter in word:
            if letter not in guessed:
                found = False

        if found:
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame Over! The correct word was:", word)


play()