list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min = 0
min_value = list_[min]

for i, x in enumerate(list_):
    if x <= min_value:
        min_value = x
        min = i

print("Минимальный элемент =", min_value, "находится по индексу", min)

