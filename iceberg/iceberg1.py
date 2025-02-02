def print_iceberg(iceberg):
    for row in iceberg:
        print(''.join(row))

def melt_iceberg(iceberg):
    rows = len(iceberg)
    cols = len(iceberg)
    new_iceberg = [['0' for _ in range(cols)] for _ in range(rows)]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if iceberg[r][c] == '*':
                empty_neighbors = 0
                if iceberg[r - 1][c] == '0':
                    empty_neighbors += 1
                if iceberg[r + 1][c] == '0':
                    empty_neighbors += 1
                if iceberg[r][c - 1] == '0':
                    empty_neighbors += 1
                if iceberg[r][c + 1] == '0':
                    empty_neighbors += 1

                if empty_neighbors >= 2:
                    new_iceberg[r][c] = '0'
                else :
                    new_iceberg[r][c] = '*'
            else :
                new_iceberg[r][c] = '0'
    return new_iceberg
def fully_melted(iceberg):
    for row in iceberg:
        if '*' in row:
            return False
    return True
def main():
    with open('iceberg.txt', 'r') as file:
        lines = file.readlines()

    N = int(lines[0].strip())
    iceberg = [list(line.strip()) for line in lines[1: N+ 1]]
    hours = 0

    while not fully_melted(iceberg):
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
