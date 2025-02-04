import re


def data_of_birth(data_n: str):
    data_n= data_n.replace(".", "")
    return (sum(data_n))


def sum(data_n: str)-> int:
    final_sum = 0

    for i in data_n:
        d= int(i)
        final_sum += d
    return final_sum


print("your personal year is:", sum)

if __name__ == "__main__":
    print(data_of_birth(input("Enter your birth data: ")))
