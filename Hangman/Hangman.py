def announce():
    print("HANGAMAN")
    # print("The game will avalible soon")


announce()


def main():
    word = input("Guess the word:>")
    if word == "Python":
        print("You guess the word,", word, "\n You survived")
    else:
        print("You lose, try again")


main()
