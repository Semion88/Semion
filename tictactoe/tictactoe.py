from random import randint


vert_coord = ("a", "b","c")


def get_igrok_char():
    igrok_char = input("Select char (x,0): ").strip(" ").lower()
    while igrok_char not in ("x","0"):
        print("Oshibka")
        igrok_char = input("Select char (x,0): ").strip(" ").lower()
    return igrok_char


pole = [["_" for x in range(3)] for y in range(3)]

def show_pole(pole):
    print("_","1","2","3")
    for y, v in enumerate(vert_coord):
        print(v, pole[y])


def igrok_position(pole):
    real_x,real_y = 0,0
    while True:
        coord = input("Input coord: ").lower().strip("_")
        y , x  = tuple(coord)


        if  int(x) not in (1,2,3) or y not in vert_coord:
          print("Not valid")
        continue
        real_x , real_y = int(x) - 1 , vert_coord.index(y)
        if pole[y][x] == "_":
            break
        else:
            print("Position not empty")
        return real_x,real_y



igrok_char = get_igrok_char()
pc_char = (igrok_char)


def get_opponent_char(char):
    return "0" if char == "x" else "x"
def is_win(igrok_char, pole):
    opponent_char = get_opponent_char(igrok_char)
    for y in range(3):
        if opponent_char not in pole[y] and "_" not in pole[y]:
            return True
    for x in range (3):
        kolonka = [pole[0][x],pole[1][x],pole[2][x]]
        if opponent_char not in kolonka and "_" not in kolonka:
            return True
    diagonal = [pole[0][0],pole[1][1],pole[2][2]]
    if  opponent_char not in diagonal and "_" not in diagonal:
        diagonal = [pole[0][2], pole[1][1], pole[2][0]]
        if opponent_char not in diagonal and "_" not in diagonal:
            return True
        return False


def is_draw(pole):
    print("Draw")
    count = 0
    for y in range(3):
        count += 1 if "_" in pole[y] else 0
    return count == 0


def get_pc_position(pole):
    x,y = randint(0,2), randint(0,2)
    while pole[y][x] !="_":
        x,y = randint(0,2),randint(0,2)
    return x,y

while True:
    show_pole(pole)
    if is_draw(pole):
        print("is draw")
        break


        x,y = igrok_position(pole)
        pole[y][x] = igrok_position
        if is_win(igrok_position,pole):
            print("you win")
            break
        x, y = pc_position(pole)
        pole[y][x] = pc_position
        if is_win(pc_position, pole):
            print("you win")
            break

