import csv
import random

def create_login(fio):
    surname, name, patronymic = fio.split()
    return f'{surname}_{name[0]}{patronymic[0]}'

def get_password():
    chis = '0123456789'
    lowwercase = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    comma = '!?().'
    simvols = chis + lowwercase + uppercase + comma
    k = 0
    while k == 0:
        x = ''.join(random.choices(simvols, k=10))
        iscoma = any(coma in x for coma in comma)
        islow = any(low in x for low in lowwercase)
        isup = any(up in x for up in uppercase)
        ischis = any(ch in x for ch in chis)
        if iscoma + islow + isup + ischis > 1:
            k = 1
            return x

with open('grants.csv', encoding='CP1251') as file:
    reader = csv.reader(file, delimiter=';')
    student_list = list(reader)[1:]

    for student in student_list:
        student.append(create_login(student[1]))
        student.append(get_password())

with open('grants_auths.csv', 'w', newline='', encoding='CP1251') as new_file:
    writer = csv.writer(new_file, delimiter=';')
    writer.writerow(['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize', 'login', 'password'])
    writer.writerows(student_list)