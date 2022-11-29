"""
Скрипт формирует ссылки для парсинга.
К заданному шаблону добавляет номерацию страниц по возрастанию.
Проводится проверка url на статус.
"""
import csv
import requests
import re
from bs4 import BeautifulSoup

# Задаём шаблон url:

url_collection = set()

urls_file='links.txt'
with open(urls_file) as file:
    url_collection = [row.strip() for row in file]

url_collection = url_collection[1:]

print(url_collection)
urls = [] # urls - массив ссылок

for link in url_collection:
    url = link

    for i in range(2000):
        url_new = url+str(i+1) # Присоединяем номер страницы к url
        if requests.get(url_new).status_code == 200: # Проверка стр на доступность
            print(url_new)  # не обязательный шаг
            urls.append(url_new) # Добавляем существующий url в массив
        else:
            break

#print(urls) # вывод массива на экран
k = url.rfind('?')
#out_file = (url[18:k] + '.txt').replace('/','-')
out_file = 'links_for_scan.txt'
print(out_file)

with open(out_file, "w") as file: # Создаём файл для хранения ссылок
    for i in range(len(urls)): # Число шагов = количеству элементов массива
        print(urls[i], file=file, sep="\n") # запись элементов массива в файл по-строчно
print('Done')
