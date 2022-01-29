import random


def guess(word_array, g_word):
    print(word_array)
    print(g_word)
    k = 8
    list_letter = []
    find_letter = False
    try_wrong = []
    while k != 0:
        input_letter = input("Input a letter: ")
        if len(input_letter) == 1:
            if input_letter.islower():

                if input_letter in list_letter:
                    print("That letter doesn't appear in the word")
                else:
                    list_letter += [input_letter]
                    # if input_letter not in guess_word:
                    #     try_wrong.append(list_letter)
                    #     print("That letter doesn't appear in the word")
                    for index, letter in enumerate(g_word):
                        if input_letter == letter:
                            word_array[index] = letter
                            find_letter = True

                    if not find_letter:
                        k -= 1
                        print("No such letter in the word. Left ", k, "attempt")
                        if k == 0:
                            print('You lose')

                    print("".join(word_array))
                    if "".join(word_array) == g_word:
                        print("You win!")
                        break
                    find_letter = False
            else:
                print("Not lower letter")
        else:
            print('Not single letter')


def random_word():
    w_list = ["python", "java", "kotlin", "javascript"]
    return random.choice(w_list)


def main():
    print("H A N G  M  A N")

    guess_word = random_word()
    r_word = list("-" * len(guess_word))
    guess(r_word, guess_word)

    while input("Play Hangman? (Yes/NO) ").upper() == "YES":
        print("Game started")
        g_word = r_word()
        r_word = list("-" * len(g_word))
        guess(r_word, g_word)


main()
