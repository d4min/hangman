# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- Created a remote github repository for this project to version control the software as well as practice the use of github.

- Connected the remote repository to a local clone using the command line.

```bash
git clone https://github.com/d4min/hangman.git
```

## Milestone 2

- Defined the variable 'word_list' which is a list of words that the python script will use as the word to be guessed during the Hangman game. 

- Imported the random library in python to allow the script to assign the variable 'word' a random word from the pre-defined list of words.
```python
import random
```

- Wrote the code necessary to allow the user to input a character as their first guess. Validated the input using an if statement to ensure it was a single alphabetical character. 

```python
guess = input("Please enter your first guess as a single character")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

