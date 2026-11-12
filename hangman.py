import random
words = ["python", "computer", "apple", "coding", "student"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6
print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
