list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию
maxch = 0
max_value = list_numbers[maxch]

for i, x in enumerate(list_numbers):
    if x >= max_value:
        max_value = x
        maxch = i


list_numbers[maxch], list_numbers[-1] = list_numbers[-1], list_numbers[maxch]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]


