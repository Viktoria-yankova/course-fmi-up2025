def grading_number(graded_number, grading_number):
    result = 1
    for someting in range (grading_number):
       result = result * graded_number
    return result


    list_of_number = [100, 200, 3, 4, 5, 6, 7, 8, 9, 10]

    for index in range(len(list_of_number)):

        if (index + 1) >= len(list_of_number):
            break
        current_number = list_of_number[index]
        next_number = list_of_number[index + 1]
        result2 = grading_number(current_number, next_number)
        print(result)