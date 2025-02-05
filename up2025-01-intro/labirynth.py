from venv import create


def create_labyrinth(rows: int, cols: int) -> list[list[int]]:
    # line = [0] * cols
    # labyrinth = []
    # for i in range(rows):
    #   labyrinth.append(line.copy())
    # return labyrinth
    return [[0] * cols for row in range(rows)]


def print_labyrinth(labyrinrth: list[list[int]]):
    for row in labyrinrth:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()


if __name__ == "__main__":
    l = create_labyrinth(4, 5)
    l[1][3] = 6
    print_labyrinth(l)
