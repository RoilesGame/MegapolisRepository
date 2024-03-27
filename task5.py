import csv


def get_num_from_ascii(s):
    """Ключевой аргумент:
    s - символ
    """

    result = ''

    for char in ascii(s):
        if char in '0123456789':
            result += char

    return int(result)


def hashing(s: str):
    """Ключевой аргумент:
    s - ФИО человека
    """

    result = ''

    m = ''.join(s.split())

    hashes = []

    list_ = list(map(str, list(range(0, 1024))))
    table = ''.join(set(list_))

    for symbol in m:
        index = get_num_from_ascii(symbol) % 1024
        hashes.append(table[index])

    hashes = list(map(int, hashes))

    result += str(sum(hashes) % 2048)

    return result


new_data = []
with open("scientist.txt", encoding="utf-8") as file:
    data = [line.split('#') for line in file.read().splitlines()][1:]

    for line in data:
        line.insert(0, hashing(line[0]))

        new_data.append(line)


with open("scientist_with_hash.csv", 'w', encoding="utf-8", newline='') as to_file:
    print("hash,ScientistName,preparation,date,components,login,password", file=to_file)
    write = csv.writer(to_file)
    write.writerows(new_data)
