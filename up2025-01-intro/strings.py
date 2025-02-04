import random
sea=[
'00000000',
'00**0000',
'00**0**0',
'0******0',
'0*****00',
'0**0**00',
'00000000',
'00000000',
]


def print_sea(list_of_numbers):
    for line in list_of_number:
        print(line)


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print(f'Size: {n}')
    list_of_number= []
    for i in range(n):
        if 0 < i < n-1:
            s = '_'
            for j in range(1, n-1):
                s += '*' if random.random() >= 0.5 else '_'
            s += '_'
            list_of_number.append(s)
        else:
            list_of_number.append('_'* n)

    print_sea(list_of_number)

    print()

    print_sea(sea)
