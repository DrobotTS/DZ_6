# # 1. Необходимо написать функцию, которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле.
# # Параметр функции - имя файла.
# # 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# # Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# # Если фамилии нет, то использовать имя, например Euclid.
# # 3. Написать функцию сортировки по дате смерти из поля "years".
# # Обратите внимание на сокращение BC. - это означает до н.э.
# # 4. Написать функцию сортировки по количеству слов в поле "text".
# # Отсортировать данные из файла с помощью данных функций.

import json
import re

filename = "data.json"

def open_json_file(filename):
    with open("data.json", "r", encoding="utf-8") as file_json:
        data_json_file = json.load(file_json)
    return data_json_file

data_json = open_json_file(filename)
print(data_json)

def sort_surname(data_json_dict):
    return data_json_dict['name'].split()[-1]

sort_surname = sorted(data_json, key=sort_surname)
print(sort_surname)

def sort_death(data_json_dict):
    death = re.findall(r'[0-9]{1,4}', data_json_dict["years"])
    if "BC" in data_json_dict["years"]:
        return (-1) * int(death[-1])
    else:
        return int(death[-1])

sort_death_year = sorted(data_json, key=sort_death)
print(sort_death_year)

def sort_word(data_json_dict):
    word = data_json_dict["text"].split()
    return len(word)
sort_words = sorted(data_json, key=sort_word)
print(sort_words)
