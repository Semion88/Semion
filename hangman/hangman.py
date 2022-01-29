import random


def guess(word_letters_array, guess_word):
    print(word_letters_array)
    print(guess_word)
    k = 8
    list_letter = []
    find_letter = False

    while k != 0:
        input_letter = input("Input a letter: ")
        list_letter += [input_letter]

        for index, letter in enumerate(guess_word):
            if input_letter == letter:
                 word_letters_array[index] = letter
                 find_letter = True

        if not find_letter:
            k -= 1
            print("No such letter in the word. Left ", k, "attempt")
            if k == 0:
                print('You lose')

        print("".join(word_letters_array))
        if "".join(word_letters_array) == guess_word:
            print("You win!")
            break


def random_word():
    word_list = ["python", "java", "kotlin", "javascript"]
    return random.choice(word_list)


def main():
    print("H A N G  M  A N")

    guess_word = random_word()
    ready_word = list("-" * len(guess_word))
    guess(ready_word, guess_word)

    while input("Play Hangman? (Yes/NO) ").upper() == "YES":
        print("Game started")
        guess_word = random_word()
        ready_word = list("-" * len(guess_word))
        guess(ready_word, guess_word)


main()
