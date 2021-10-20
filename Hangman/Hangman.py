import random
from word_list import word_list


def announce():
    print("HANGAMAN")
    # print("The game will avalible soon")


announce()


def word_selection():
    word = random.choice(word_list)
    return word.lower()


def game(word):
    guessed_word = input("Guess the word:>").lower()
    if guessed_word == word:
        print("You guess the word,", guessed_word, "\n You survived")
    else:
        print("You lose, try again")

def main():
    word = word_selection()
    game(word)


main()
