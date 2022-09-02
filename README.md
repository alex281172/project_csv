Решение тестового задания: скрипт для парсинга диалогов из файла test_data.csv

Скрипт разработан на базе: pandas, pymorphy2, nltk

Установка и запуск:

1. Склонировать репозитарий с Github 
https://github.com/alex281172/project_csv.git 

2. Скопировать в директорую файл test_data.csv. По условиям теста его не должно быть на Github. 

3. Перейти в директорую проекта, 
   Создать виртуальное окружение 

python -m venv venvдля - для Windows
python3 -m venv venv - для Linux

4. Активировать окружение  

venv\scripts\activate.bat - для Windows  
source venv/bin/activate - для Linux  

5. Установить зависимости  
pip install -r requirements.txt 

Запуск 
pars_csv.py 
