list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_i = 0
for i in range(len(list_numbers)):
    max_numb = list_numbers[max_i]
    current_number = list_numbers[i]

    if current_number > max_numb:
        max_numb = current_number
        max_i = i

s1 = list_numbers[-1]

list_numbers[-1] = max_numb

list_numbers[max_i] = s1

print(list_numbers)

