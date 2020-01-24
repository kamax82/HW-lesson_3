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
    reader = list(csv.DictReader(ex_books))
    book_atr = {}
    book_atr_list = []
    titles = []
    authors = []
    heights = []
    for row in reader:
        if row['Title']:
            titles.append(row['Title'])

        if row['Author'] and (len(row['Author'])) > 0:
            authors.append(row['Author'])
        else:
            authors.append('--Unknown--')

        if row['Height']:
            heights.append(row['Height'])

    # Не получилось собрать списко словарей, в цикле идет перезапись, в тоге book_atr_list состоит из одинаковых словарей
    for i in range(len(titles)):
        book_atr['title'] = titles[i]
        book_atr['author'] = authors[i]
        book_atr['heights'] = heights[i]
        book_atr_list.append(book_atr)

    # Из-за ошибки book_atr_list функция random.choices производящая рандомную выборку, выбирает из одинаковых елементов
    for i in range(len(structured)):
        structured[i].update({'books': random.choices(book_atr_list, k=3)})

'''Сохранение полученного словаря в json'''
with open('my_exapmple.json', 'w') as my_ex:
    json.dump(structured, my_ex, indent=2)
