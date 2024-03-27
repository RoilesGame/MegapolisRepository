import random


def sorting(array):
    """
    Ключевой аргуент:
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


with open("scientist.txt", encoding="utf-8") as file:
    data = [line.split('#') for line in file.read().splitlines()][1:]
    sorted_data = sorting(data)

    for line in sorted_data[:5]:
        print(f'{line[0]}: {line[1]}')
