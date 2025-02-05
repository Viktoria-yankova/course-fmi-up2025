def calculate_product(start,end):
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
result = calculate_product(start,end)
print(f"the product of numbers from {start} to {end} is: {result}")
if __name__ == "__main__":
    print()