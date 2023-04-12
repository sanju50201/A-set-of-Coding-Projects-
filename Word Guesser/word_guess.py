import random
import sys
import pyfiglet


def print_title():
    ascii_banner = pyfiglet.figlet_format("Word Guesser")
    print(ascii_banner)


def load_words():
    with open("/media/sanju/Programming/Python Projects/Word Guesser/words.txt", "r") as f:
        words = f.read().splitlines()
    return words


def get_words():
    words = load_words()
    word = random.choice(words)
    return word


def prompt_guess():
    guess = str(input("Guess a Character: "))
    if guess == "quit":
        sys.exit()
    return guess


def play_game(word):
    guesses = set()
    turns = 10

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("You win")
            print(f"The word is {word}")
            return

        print(f"\n\nYou have {turns} more guesses")
        guess = prompt_guess()

        try:
            if guess in guesses:
                raise ValueError("You already guessed that character")
            elif len(guess) > 1:
                raise ValueError("You can only guess one character at a time")
            else:
                guesses.add(guess)
        except ValueError as error:
            print(error)
            continue

        if guess not in word:
            turns -= 1
            print("Wrong guess")

    print(f"You loose.\n The word was {word}")


if __name__ == "__main__":
    print_title()
    name = input("Enter your name: ")
    print(f"Hello {name}, Welcome to Word Guesser")
    word = get_words()
    play_game(word)


