def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower()

qw = []
qword = []
qword_dict = {}
qword_dict_percent = {}
for i in main_str:
    qw.append(i)
for i in range(len(qw)):
    err = qw[i].isalpha()
    if err == True:
        qword.append(qw[i])

for i in range(len(qword)):
    if qword[i] in qword_dict:
        qword_dict[qword[i]] += 1
    else:
        qword_dict[qword[i]] = 1

print(qword_dict)

for i in range(len(qword)):
    if qword[i] in qword_dict_percent:
        qword_dict_percent[qword[i]] += 1/len(qword)*100
    else:
        qword_dict_percent[qword[i]] = 1/len(qword)*100

# print(qword_dict_percent) - не печатаю, чтобы в edutools был "correct" - выводит процентное содержание букв в предложении





