import random

class TicTacToe:

    def __init__(self):
        self.pole = []

    def create_pole(self):
         for i in range(3):
             row = []
             for j in range(3):
                 row.append('-')
             self.pole.append(row)

    def get_random_first_gamer(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, gamer):
        self.pole[row][col] = gamer

    def gamer_win(self, gamer):
        win = False
        n = len(self.pole)
        # Выигрыш по горизонтали
        for row in range(n):
            if (self.pole[row][0] == self.pole[row][1] == self.pole[row][2] == gamer):
                win = True
        # Выигрыш по вертикали
        if (self.pole[0][0] == self.pole[1][0] == self.pole[2][0] == gamer):
            win = True
        if (self.pole[0][1] == self.pole[1][1] == self.pole[2][1] == gamer):
            win = True
        if (self.pole[0][2] == self.pole[1][2] == self.pole[2][2] == gamer):
            win = True
        # Выигрыш по диагонали 1
        if (self.pole[0][0] == self.pole[1][1] == self.pole[2][2] == gamer):
            win = True
        # Выигрыш по диагонали 2
        if (self.pole[0][2] == self.pole[1][1] == self.pole[2][0] == gamer):
            win = True

        return win

    def is_pole_full(self):
        filled = True
        for row in self.pole:
            for item in row:
                if item == '-':
                    filled = False

        return filled

    def is_filled(self, row, col):
        filled = False
        if (self.pole[row][col] != '-'):
                filled = True
        return filled


    def swap_gamer(self, gamer):
        return 'X' if gamer == 'O' else 'O'

    def show_pole(self):
        for row in self.pole:
            for item in row:
                print(item, end=" ")
            print()

    def begin(self):
        self.create_pole()
        count = 0
        gamer = 'O' if self.get_random_first_gamer() == 1 else 'X'
        self.show_pole()

        while True:
            print(f"igrok {gamer} turn")

            row, col = list(
                map(int, input("Enter cells: ").split()))
            print()

            if (not self.is_filled(row - 1, col - 1)):
                self.fix_spot(row - 1, col - 1, gamer)
                count += 1
                self.show_pole()
                if self.gamer_win(gamer):
                    print(f"Player {gamer} wins the game!")
                    break

                if self.is_pole_full():
                    print("Match Draw!")
                    break
                gamer = self.swap_gamer(gamer)
            else:
                print("That place is already filled.")
                continue

        print()

tic_tac_toe = TicTacToe()
tic_tac_toe.begin()
