def even_num(start, last):
    total = 0
    for num in range(start, last+1):
        if num %2==0:
            total += num
    return total
start= int(input("Enter the start number: "))
last = int(input("Enter the last number: "))
result =even_num(start, last)
print(f"the sum of even numbers from {start} to {last} is {result}")