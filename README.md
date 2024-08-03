# Hangman-Game
This Python program implements a classic hangman game where two players can play. The first player thinks of a word, and the second player tries to guess the word by suggesting letters.

Features:
- Randomly selects a word from a predefined list
- Displays the word as a series of underscores (_)
- Asks the second player to guess a letter
- Checks if the guessed letter is in the word
- Updates the display with the correctly guessed letters
- Draws a hangman diagram for each incorrect guess
- Game ends when the word is fully guessed or the hangman diagram is complete

How it works:
1. The program randomly selects a word from the word_list.
2. It initializes the display list with underscores (_) representing each letter of the word.
3. The program asks the second player to guess a letter.
4. It checks if the guessed letter is in the word.
5. If the letter is correct, it updates the display list with the letter.
6. If the letter is incorrect, it decreases the number of lives and draws a part of the hangman diagram.
7. The game continues until the word is fully guessed or the hangman diagram is complete.
This code demonstrates basic Python concepts such as lists, loops, conditional statements, and random number generation. It also uses an external module stages to display the hangman diagram.
