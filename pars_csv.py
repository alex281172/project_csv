import pymorphy2
import pandas as pd
import nltk

nltk.download('punkt')
nltk.download('names')

prob_thresh = 0.4
morph = pymorphy2.MorphAnalyzer()

csv_main = pd.read_csv("test_data.csv", delimiter=',')
csv_man = csv_main[csv_main.role.str.contains(pat='manager', case=False)]

print('*' * 50)
print("\033[32m" 'Задание a: Извлекать реплики с приветствием – где менеджер поздоровался.' "\033[0m")
print(csv_man[csv_man.text.str.contains(pat='здравствуйте|добрый день', case=False)])
print('*' * 50)
print("\033[32m" 'Задание b: Извлекать реплики, где менеджер представил себя.'"\033[0m")
print(csv_man[csv_man.text.str.contains(pat='меня зовут|меня|мое имя', case=False)])
print('*' * 50)
print("\033[32m" 'Задание c: Извлекать имя менеджера.'"\033[0m")
csv_man_hi = csv_man[csv_man.text.str.contains(pat='меня зовут|меня|мое имя|это|звонит|говорит', case=False)]
for text in csv_man_hi.text:
    flag1 = csv_man_hi.dlg_id
    for word in nltk.word_tokenize(text):
        for p in morph.parse(word):
            if 'Name' in p.tag and p.score >= prob_thresh:
                print(f'{word}')
                name_man = word
                # print(csv_man[csv_man.text.str.contains(pat=name_man, case=False)])
                print(text)

print('*' * 50)
print("\033[32m" 'Задание d: Извлекать название компании.'"\033[0m")
print(csv_man[csv_man.text.str.contains(pat='диджитал', case=False)])
print('*' * 50)
print("\033[32m" 'Задание e: Извлекать реплики, где менеджер попрощался.'"\033[0m")
print(csv_man[csv_man.text.str.contains(pat='свидания|всего доброго', case=False)])

print('*' * 50)
print("\033[32m" 'Задание f: Проверять требование к менеджеру: «В каждом диалоге обязательно необходимо поздороваться '
      'и попрощаться с клиентом».'"\033[0m")

csv_privet = csv_man[csv_man.text.str.contains(pat='здравствуйте|добрый день|свидания|всего доброго', case=False)]

flags = []
for a, row in csv_privet.iterrows():
    flag1 = row.dlg_id
    flags.append(flag1)
    dup = {x for x in flags if flags.count(x) > 1}

dup = {x for x in flags if flags.count(x) > 1}

for counter in dup:
    print(f'Диалог {counter} соответствует требованиям')

