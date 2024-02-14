import csv

with open('grants_new.csv', encoding='CP1251') as file:
    reader = csv.reader(file, delimiter=';')
    student_list = list(reader)[1:]

    zapros = input()
    while zapros != 'СТОП':
        zapros = int(zapros)
        for id, Full_Name, Project_id, Nomination, Prize in student_list:
            if int(Project_id) == zapros:
                print(f'Заявка № {Project_id} Автор: {Full_Name} Сумма – {Prize} тыс. руб.')
                break
        else:
            print('Такой заявки нет в реестре')
        zapros = input()