import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'apple',]

word = random.choice(words)

print("Guess the characters")


def guess_word():
    guesses = ''

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
            break

        print("\n")
        guess = input("guess a character:")
        guesses += guess

        if guess not in word:
            turns -= 1

            print("Wrong")
            print(f"You have {turns} more guesses")

            if turns == 0:
                print("You loose.\n")


if __name__ == '__main__':
    guess_word()


