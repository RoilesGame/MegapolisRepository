import random


def sorting(array):
    """Ключевой аргуент:
    array - список с данными
    """

    if len(array) <= 1:
        return array

    else:
        chosen_data_date = random.choice(array)
        low_data_date = []
        high_data_date = []
        this_data_date = []

        for line in array:
            if line[2] < chosen_data_date[2]:
                low_data_date.append(line)
            elif line[2] > chosen_data_date[2]:
                high_data_date.append(line)
            else:
                this_data_date.append(line)

        return sorting(low_data_date) + this_data_date + sorting(high_data_date)


def binary_search(array, length_array, search_value):
    """Ключевые аргументы:
    array - отсортированный список данных
    length_array - длина списка
    search_value - значение, которое нужно найти
    """

    low = 0
    high = length_array - 1
    search_index = 0

    while (low <= high) and search_index == 0:
        middle = (low + high) // 2

        if array[middle][2] == search_value:
            search_index = middle

        else:
            if array[middle][2] < search_value:
                low = middle + 1
            else:
                high = middle - 1

    return search_index


with open("scientist.txt", encoding="utf-8") as file:
    data = [line.split('#') for line in file.read().splitlines()][1:]
    sorted_data = sorting(data)

    user_date = input()

    while user_date != 'эксперимент':
        need_line = sorted_data[binary_search(sorted_data, len(sorted_data), user_date)]

        surname = need_line[0].split()[0]
        initials = f"{need_line[0].split()[1][0]}.{need_line[0].split()[-1][0]}."

        chemical = need_line[1]
        date = need_line[2]

        print(f"Ученый {surname} {initials} создал препарат: {chemical} - {date}")

        user_date = input()
