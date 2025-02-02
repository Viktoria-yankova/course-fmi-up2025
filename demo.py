list_of_number = [100,200,3,4,5,6,7,8,9,10]

for index in range(len(list_of_number)):


    if (index+1)>=len(list_of_number):
        break
    current_number = list_of_number[index]
    next_number = list_of_number[index+1]
    sum_of_numbers = current_number + next_number
    print(sum_of_numbers)
