import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    max_attempts = 6
    word = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)
            if guess not in word:
                attempts += 1
                print("Incorrect guess. Attempts left:", max_attempts - attempts)
                if attempts == max_attempts:
                    print("Sorry, you've run out of attempts. The word was:", word)
                    break
            print(display_word(word, guessed_letters))
            if all(letter in guessed_letters for letter in word):
                print("Congratulations, you've guessed the word!")
                break
        else:
            print("Please enter a valid single letter.")

hangman()
