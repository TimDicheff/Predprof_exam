import csv

sum_future_project = 0
count_future_project = 0
sum_innovation_leaders = 0
count_innovation_leaders = 0
sum_reality_changers = 0
count_reality_changers = 0
sum_mol_newer = 0
count_mol_newer = 0
sum_engine_of_progress = 0
count_engine_of_progres = 0

with open('grants.csv', encoding='CP1251') as file:
    reader = csv.reader(file, delimiter=';')
    student_list = list(reader)[1:]
    for id, Full_Name, Project_id, Nomination, Prize in student_list:
        if 'Агафья Артемовна Ершова' in Full_Name:
            print(f'Вы получили {Prize} рублей в конкурсе {Nomination} с номером заявки {Project_id}.')
            break
    for student in student_list:
        if student[-1] != 'NULL':
            if student[-2] == 'Меняющие реальность':
                sum_reality_changers += int(student[-1])
                count_reality_changers += 1
            elif student[-2] == 'Проект будущего':
                sum_future_project += int(student[-1])
                count_future_project += 1
            elif student[-2] == 'Двигатель прогресса':
                sum_engine_of_progress += int(student[-1])
                count_engine_of_progres += 1
            elif student[-2] == 'Лидеры инноваций':
                sum_innovation_leaders += int(student[-1])
                count_innovation_leaders += 1
            elif student[-2] == 'Молодой новатор':
                sum_mol_newer += int(student[-1])
                count_mol_newer += 1
        else:
            continue
    for student in student_list:
        if student[-1] == 'NULL':
            if student[-2] == 'Меняющие реальность':
                student[-1] = (sum_reality_changers / count_reality_changers // 1000 * 1000)
            elif student[-2] == 'Проект будущего':
                student[-1] = (sum_future_project / count_future_project // 1000 * 1000)
            elif student[-2] == 'Двигатель прогресса':
                 student[-1] = (sum_engine_of_progress / count_engine_of_progres // 1000 * 1000)
            elif student[-2] == 'Лидеры инноваций':
                 student[-1] = (sum_innovation_leaders / count_innovation_leaders // 1000 * 1000)
            elif student[-2] == 'Молодой новатор':
                 student[-1] = (sum_mol_newer / count_mol_newer // 1000 * 1000)
        else:
            continue

with open('grants_new.csv', 'w', newline='', encoding='CP1251') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writerows(student_list)