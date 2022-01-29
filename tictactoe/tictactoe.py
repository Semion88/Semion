vert_coord = ("a", "b","c")


def get_igrok_char():
    igrok_char = input("Select char (x,0): ").strip(" ").lower()
    while igrok_char not in ("x","0"):
        print("Oshibka")
        igrok_char = input("Select char (x,0): ").strip(" ").lower()
        return igrok_char


pole = [["_" for x in range(3)] for y in range(3)]

def show_pole(pole):
    print(" ","1","2","3")
    for y, v in enumerate(vert_coord):
        print(v, pole[y])


igrok_char = get_igrok_char()
pc_char = "0" if igrok_char == "x" else "x"


while True:
    show_pole(pole)
    input('igrat dalshe?')
