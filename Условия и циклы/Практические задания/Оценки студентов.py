# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]
for x in students:
    if x["grade"] > 3:
        print(f'{x["name"]}. Оценка: {x["grade"]}')
# TODO Распечатать имена студентов с оценками выше тройки