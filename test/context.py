import json
import csv
import random

'''Открытие json файла и сбор словаря, удовлетворяющего условиям (отбрасываются лишние лючи'''

with open('users-39204-8e2f95.json') as users:
    users_data = json.load(users)
    structured_users = {key: users_data[key] for key in range(len(users_data))}
    structured = {}
    for i in range(len(structured_users)):
        structured[i] = dict(
            (k, v) for (k, v) in structured_users[i].items() if k == 'name' or k == 'gender' or k == 'address')

'''Открытие csv файла и попытка сбора списка книг, с отсечением лишних ключей во вложенном словаре'''
with open('books-39204-271043.csv') as ex_books:
    reader = csv.DictReader(ex_books, delimiter=',')
    book_atr = []
    for row in reader:
        if len(row['Author']) > 0:
            book_atr.append({'tittle': row['Title'], 'author': row['Author'], 'height': row['Height']})
        else:
            book_atr.append({'tittle': row['Title'], 'author': '--Unknown--', 'height': row['Height']})

'''Функция random.choices производит рандомную выборку от 1 до 6 книг книг, и помещает ее в словарь'''
for i in range(len(structured)):
    rand_number = random.randint(1, 6)
    structured[i].update({'books': random.choices(book_atr, k=rand_number)})

'''Сохранение полученного словаря в json'''
with open('my_exapmple.json', 'w') as my_ex:
    json.dump(structured, my_ex, indent=2)
