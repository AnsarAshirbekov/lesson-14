# а) Создайте json файл в операционной системе, заполните его данными с сайта https://jsonplaceholder.typicode.com/todos/

# Здесь воспользуемся модулем requests, который предоставляет простой способ взаимодействия с веб-серверами и отправки
# HTTP-запросов и является важным инструментом для взаимодействия с сетевыми ресурсами
import requests

# Так как нам нужно получить данные с сайта, это означает что нам нужно отправить HTTP-запрос методом GET, получить 
# данные с сервера по указанному URL и сохранить в какой-нибудь переменной.
# Здесь как раз таки у модуля requests есть метод .get(), который примает URL адрес
response = requests.get("https://jsonplaceholder.typicode.com/todos/")

# Мы можем вывести полученный результат в виде текста в консоль, воспользовавшись методом .text, который просто возвращает
# ответ сервера в виде строки
print(response.text)

# А также можем создать новый JSON-файл, записав в него полученный ответ с сервера. Здесь предпочтительней уже использовать
# метод .json(), потому что он преобразует ответ сервера в объект Python, что делает его более удобным. Также он 
# автоматически обрабатывает JSON-синтаксис и гарантирует, что сохраненные данные будут правильно сформатированы 
# в соответствии с JSON-стандартом.
# Но записать таким образом как file.write(response.json) не выйдет, потому что это не строка, как было с .text
# Нужно сначала полученный объект Python сохранить в переменную
data = response.json()

# Так как теперь мы будем работать с файлами JSON, нам нужно импортировать модуль json, который предоставляет инструменты
# для работы с такими файлами. 
import json

# Один из таких инструментов это метод .dump(), который принимает объект Python, словарь, список а также объект файла для
# для записи данных и создает отдельный JSON-файл
# print(json.dump(data, 'data.json')), такая запись не пойдет, потому что этот метод можно использоваться только тогда, 
# когда мы создаем, открываем какой-нибудь файл, то есть только при работе с файлами
with open('data.json', 'w') as file:
    json.dump(data, file)


# б) Прочитайте этот файл в массив python-словарей.

# Чтобы это сделать существует еще один инструмент модуля json - метод .load(), который проделывает операцию, обратную 
# методу .dump(), то есть принимает объект JSON или какой-нибудь другой объект, содержащий JSON-данные, и преобразует их
# в объекты Python, такие как словари или списки.

with open('data.json', 'r') as file:
    list_of_dicts = json.load(file)

print(list_of_dicts)


# в) Запишите каждый из этих словарей в отдельный json-файл.

# Проходим по каждому словарю в списке
for i, item in enumerate(list_of_dicts, start=1):
    # Формируем имя выходного JSON-файла, например, file1.json, file2.json и т.д.
    filename = f'file{i}.json'
    # Записываем текущий словарь в отдельный JSON-файл
    with open(filename, 'w') as file:
        json.dump(item, file)  # Запись текущего словаря в файл