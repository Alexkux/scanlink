"""
Скрипт формирует ссылки для парсинга.
К заданному шаблону добавляет номерацию страниц по возрастанию.
Проводится проверка url на статус.
"""

import requests
# Задаём шаблон url:
#url = 'https://tachka.ru/kreplenie-dlya-velosipeda?page='
#url = 'https://tachka.ru/farkop?page='
url = 'https://tachka.ru/zashita-kartera?page='
#url = 'https://tachka.ru/bagazhnik?page='
#url='https://tachka.ru/bagazhnik/na-reilingi?page='

# urls - массив ссылок
urls = []

for i in range(1000):
    url_new = url+str(i+1) # Присоединяем номер страницы к url
    if requests.get(url_new).status_code == 200: # Проверка стр на доступность
        print(url_new)  # не обязательный шаг
        urls.append(url_new) # Добавляем существующий url в массив
    else:
        break

#print(urls) # вывод массива на экран
k = url.rfind('?')
out_file = (url[18:k] + '.txt').replace('/','-')
print(out_file)

with open(out_file, "w") as file: # Создаём файл для хранения ссылок
    for i in range(len(urls)): # Число шагов = количеству элементов массива
        print(urls[i], file=file, sep="\n") # запись элементов массива в файл по-строчно
print('Done')
