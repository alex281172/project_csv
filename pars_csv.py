import pymorphy2
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('names')
morph = pymorphy2.MorphAnalyzer()


prob_thresh = 0.4

list_hi = 'здравствуйте|добрый день'
list_manager = 'меня зовут|меня|мое имя'
list_name = 'меня зовут|меня|мое имя|это|звонит|говорит'
list_company = 'диджитал'
list_bye = 'свидания|всего доброго'
list_hi_bye = 'здравствуйте|добрый день|свидания|всего доброго'



csv_main = pd.read_csv("test_data.csv", delimiter=',')
csv_man = csv_main[csv_main.role.str.contains(pat='manager', case=False)]

def add_lines(f):
    def inner():
        print('*' * 50)
        result = f()
        return result
    return inner

@add_lines
def csv_hi():
    print("\033[32m" 'Задание a: Извлекать реплики с приветствием – где менеджер поздоровался.' "\033[0m")
    print(csv_man[csv_man.text.str.contains(pat=list_hi, case=False)])


@add_lines
def csv_manager():
    print("\033[32m" 'Задание b: Извлекать реплики, где менеджер представил себя.'"\033[0m")
    print(csv_man[csv_man.text.str.contains(pat=list_manager, case=False)])


@add_lines
def csv_mnager_name():
    print("\033[32m" 'Задание c: Извлекать имя менеджера.'"\033[0m")
    csv_man_hi = csv_man[csv_man.text.str.contains(pat=list_name, case=False)]
    for text in csv_man_hi.text:
        flag1 = csv_man_hi.dlg_id
        for word in nltk.word_tokenize(text):
            for p in morph.parse(word):
                if 'Name' in p.tag and p.score >= prob_thresh:
                    print(f'{word} {p.score} {p.tag}')
                    name_man = word
                    # print(csv_man[csv_man.text.str.contains(pat=name_man, case=False)])
                    print(text)


@add_lines
def csv_company():
    print("\033[32m" 'Задание d: Извлекать название компании.'"\033[0m")
    print(csv_man[csv_man.text.str.contains(pat=list_company, case=False)])


@add_lines
def csv_man_bye():
    print("\033[32m" 'Задание e: Извлекать реплики, где менеджер попрощался.'"\033[0m")
    print(csv_man[csv_man.text.str.contains(pat=list_bye, case=False)])


@add_lines
def csv_man_ok():
    print(
        "\033[32m" 'Задание f: Проверять требование к менеджеру: «В каждом диалоге обязательно необходимо поздороваться '
        'и попрощаться с клиентом».'"\033[0m")
    csv_privet = csv_man[csv_man.text.str.contains(pat='здравствуйте|добрый день|свидания|всего доброго', case=False)]
    flags = []
    for a, row in csv_privet.iterrows():
        flag1 = row.dlg_id
        flags.append(flag1)
    dup = {x for x in flags if flags.count(x) > 1}
    for counter in dup:
        print(f'Диалог {counter} соответствует требованиям')


csv_hi()
csv_manager()
csv_mnager_name()
csv_company()
csv_man_bye()
csv_man_ok()
