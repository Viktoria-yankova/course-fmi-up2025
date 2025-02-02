def print_iceberg(iceberg):
    for row in iceberg:
        print(''.join(row))
    print()


def melt_iceberg(iceberg):
    rows = len(iceberg)
    cols = len(iceberg[0]) if rows > 0 else 0
    new_iceberg = [['0' for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if iceberg[i][j] == '*':
                empty_neighbors = 0
                if iceberg[i - 1][j] == '0':
                    empty_neighbors += 1
                if iceberg[i + 1][j] == '0':
                    empty_neighbors += 1
                if iceberg[i][j - 1] == '0':
                    empty_neighbors += 1
                if iceberg[i][j + 1] == '0':
                    empty_neighbors += 1

                if empty_neighbors >= 2:
                    new_iceberg[i][j] = '0'
                else:
                    new_iceberg[i][j] = '*'
            else:
                new_iceberg[i][j] = '0'

    return new_iceberg


def is_fully_melted(iceberg):
    for row in iceberg:
        if '*' in row:
            return False
    return True


def main():
    with open('iceberg.txt', 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    iceberg = [list(line.strip()) for line in lines[1: + 1]]

    hours = 0

    while not is_fully_melted(iceberg):
        print(f"Hour {hours}:")
        print_iceberg(iceberg)
        input("Press ENTER to continue...")
        iceberg = melt_iceberg(iceberg)
        hours += 1

    print(f"Hour {hours}:")
    print_iceberg(iceberg)
    print(f"The iceberg fully melted in {hours} hours.")


if __name__ == "__main__":
    main()