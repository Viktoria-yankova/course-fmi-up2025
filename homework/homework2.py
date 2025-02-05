numbers = [int(x) for x in input("Enter numbers: ").split()]
total = 0
for number in numbers:
    total += number

if total % 2 == 0:

    print("this sum is even")
else:
    print("this sum is odd")
if __name__ == "__main__":
    print()
