Решение тестового задания: скрипт для парсинга диалогов из файла test_data.csv

Скрипт разработан на базе: pandas, pymorphy2, nltk

Установка и запуск:

Склонировать репозитарий с Github
https://github.com/alex281172/project_csv.git

Скопировать в директорую файл test_data.csv. По условиям теста его не должно быть на Github.

Перейти в директорую проекта

Создать виртуальное окружение

python -m venv venvдля - для Windows
python3 -m venv venv - для Linux

Активировать окружение
.\\scripts\activate
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux

Установить зависимости
pip install -r requirements.txt

Запуск
pasr_csv.py

NB: во время первого запуска необходимо дополнительно загрузить библиотеки nltk!

Далее можно отключить - #nltk.download() в pasr_txt.py
