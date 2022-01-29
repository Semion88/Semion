print("Hangman")
print("The game will be available soon.")


def replace(guess_word):
    a = []
    for i in "guess_word":
        i = "-"
        a += i
        print("a")
        return a


def guess(guess_word, a):
    b = 8
    input_letter = input("Input a letter: ")
    typed = set()
    while b != 0:
        if input_letter in guess_word:
            typed.add(input_letter)
            print([a if a in typed else "_" for a in guess_word])
            print(a)
        else:
            print("No such letter in the word")
            b -= 1
            input_letter = input("Input a letter: ")
