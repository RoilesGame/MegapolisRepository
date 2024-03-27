import string
import csv
import random


def create_login(s: str):
    return f"{s.split()[0]}_{s.split()[1][0]}{s.split()[-1][0]}"


def create_password():
    symbols = string.ascii_letters + string.digits

    digits, low, up = 0, 0, 0

    password = ''.join(random.choice(symbols) for _ in range(10))

    while not (digits and low and up):

        password = ''.join(random.choice(symbols) for _ in range(10))

        for char in password:
            if char in string.ascii_lowercase:
                low += 1
            elif char in string.ascii_uppercase:
                up += 1
            else:
                digits += 1

    return password


new_data = []
with open("scientist.txt", encoding="utf-8") as file:
    data = [line.split('#') for line in file.read().splitlines()][1:]

    for line in data[1:]:
        line.extend([create_login(line[0]), create_password()])
        new_data.append(line)


with open("scientist_password.csv", 'w', encoding="utf-8", newline='') as to_file:
    print("ScientistName,preparation,date,components,login,password", file=to_file)
    write = csv.writer(to_file)
    write.writerows(new_data)
