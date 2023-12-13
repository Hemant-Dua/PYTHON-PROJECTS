import random
import pandas as pd

def choose_word():
    df = pd.read_csv("Hangman\words.csv")
    words = df["WORDS"].tolist()
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_guess():
    return input("Guess a letter: ").lower()

def check_guess(guess, word):
    return guess in word

def update_guessed_letters(guess, guessed_letters):
    guessed_letters.append(guess)

def main():
    word = choose_word()
    guessed_letters = []
    max_attempts = 6

    while max_attempts > 0:
        current_display = display_word(word, guessed_letters)
        print(current_display)

        guess = get_guess()

        if check_guess(guess, word):
            print("Correct!")
        else:
            print("Incorrect!")
            max_attempts -= 1

        update_guessed_letters(guess, guessed_letters)

        if set(word).issubset(guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

    if max_attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

main()