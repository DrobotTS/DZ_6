# 1. Необходимо написать функцию, которая считает эти данные из файла и возвращала содержимое файла в той же структкру, что и в файле.
# Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text".
# Отсортировать данные из файла с помощью данных функций.
import json
import re


def open_json_file(filename):
    with open("data.json", "r", encoding="utf-8") as filename:
        data_json_file = json.load(filename)
    return data_json_file
print(open_json_file(filename="data.json"))

def sorted_surnames(filename):
    data_name = [item["name"] for item in open_json_file(filename)]
    surnames = [surname.split()[-1] for surname in data_name]
    return surnames
print (sorted_surnames(filename="data.json"))

def sorted_death(filename):
    year = [item["years"] for item in open_json_file(filename)]
    years = [years.split('–')[1] for years in year]
    data_years = [re.sub('\D', '', year) for year in years]
    sort_year = [int(data_years[0 + year]) for year in range(len(data_years))]
    return sorted(sort_year)
print(sorted_death(filename="data.json"))

# def key_for_count(filename):
#     data_text = [item["text"] for item in open_json_file(filename)]
#     words = [count_words.count(" ") for count_words in data_text]
#     return sorted(words)
# print(key_for_count(filename="data.json"))

def count_words_text(filename):
    data_text = [item["text"] for item in open_json_file(filename)]
    sort_text = sorted(data_text, key=len)
    return sort_text
print(count_words_text(filename="data.json"))
