# CodeAlpha_Hangman_Game.py
Here's a simple Python implementation of a text-based Hangman game. The program selects a random word from a predefined list, and the player guesses one letter at a time. The player is allowed a limited number of incorrect guesses before losing the game.

How it works:

choose_word(): This function selects a random word from a predefined list of words.
display_board(): This function returns the current state of the word, showing guessed letters and underscores for letters that have not been guessed yet.
hangman(): This is the main function where the game logic is implemented:

#The game continues until either the player guesses the word correctly or exhausts the maximum number of incorrect guesses.
#After each guess, the program updates the displayed word, shows the number of remaining incorrect guesses, and checks if the player has won or lost.
#If the player makes an invalid guess (e.g., more than one letter or a non-alphabet character), they are prompted to try again.
Main execution: The game starts by calling hangman() in the if __name__ == "__main__": block, ensuring the game runs when the script is executed.

How to Play:

Run the script.
Guess one letter at a time.
You have 6 incorrect guesses allowed before the game ends.
The game will show the current state of the word after each guess.
