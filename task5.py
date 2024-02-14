import csv

def create_hash(s):
    simvols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    simvols += simvols.upper()
    simvols += ' '
    p, m = 67, 10**9 + 9
    dictionary = {simvols[i]:i+1 for i in range(len(simvols))}
    hash = 0
    for i in range(0, len(s)):
        hash += (dictionary[s[i]] * (i+1)**2)
    hash *= (p**len(s) - 1)
    hash += p
    hash = hash % m
    return hash

with open('grants.csv', encoding='CP1251') as file:
    reader = csv.reader(file, delimiter=';')
    student_list = list(reader)[1:]

    for student in student_list:
        student[0] = create_hash(student[1])

with open('grants_hash.csv', 'w', encoding='CP1251') as new_file:
    writer = csv.writer(new_file, delimiter=';')
    writer.writerow(['Hash', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writerows(student_list)

