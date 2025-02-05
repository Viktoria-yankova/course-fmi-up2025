numbers = input("enter numbers separated by space: ")
number = [int(num) for num in numbers.split(",")]
largest = max(number)
smallest = min(number)
print("the largest number is: ", largest)
print("the smallest number is:", smallest)
if __name__=="__main__":
    print()