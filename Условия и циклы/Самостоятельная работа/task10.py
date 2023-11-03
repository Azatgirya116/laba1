list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]
chet = 0  # количество четных чисел
nechet = 0  # количество нечетных чисел

for x in list_:  # перебираем все числа
    if x % 2 == 0:
        chet += 1
    else:
        nechet += 1

if chet > nechet:
    print('Четных чисел больше')
elif chet < nechet:
    print('Нечетных чисел больше')
else:
    print('Четных и нечетных одинаковое количество')


