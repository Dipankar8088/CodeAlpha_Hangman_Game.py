import random

def choose_word():
    # List of words for the game
    words = ['python', 'javascript', 'hangman', 'programming', 'developer', 'algorithm', 'function']
    return random.choice(words)

def display_board(word, guessed_letters):
    # Create a list to represent the current state of the word
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def hangman():
    word = choose_word()  # Random word selection
    guessed_letters = []  # List to track guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Maximum incorrect guesses before losing

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_board(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has been guessed before
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        # Add the guess to the guessed_letters list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        # Display the current state of the word
        print(display_board(word, guessed_letters))

        # Check if the player has guessed the word correctly
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}' correctly.")
            break
    else:
        # The player has used all their incorrect guesses
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
