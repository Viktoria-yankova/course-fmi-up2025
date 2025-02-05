def num(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count
start= int(input("Enter the start:"))
end= int (input("Enter the end:"))
