import csv

with open('./password database.txt') as f:
    password_database = list(csv.reader(f, delimiter=' '))

def is_valid_password_1(amount, character, password):
    amount = amount.split('-')
    min_amount = int(amount[0])
    max_amount = int(amount[1])

    character = character[0]

    count = password.count(character)
    if count >= min_amount and count <= max_amount:
        return True
    else:
        return False

count_valid_passwords_1 = 0
for i in password_database:
    if is_valid_password_1(*i):
        count_valid_passwords_1 += 1

print(count_valid_passwords_1)

def is_valid_password_2(indices, character, password):
    indices = indices.split('-')
    index_1 = int(indices[0])
    index_2 = int(indices[1])

    character = character[0]

    if password[index_1 - 1] == character and password[index_2 - 1] != character:
        return True
    elif password[index_1 - 1] != character and password[index_2 - 1] == character:
        return True
    else:
        return False

count_valid_passwords_2 = 0
for i in password_database:
    if is_valid_password_2(*i):
        count_valid_passwords_2 += 1

print(count_valid_passwords_2)