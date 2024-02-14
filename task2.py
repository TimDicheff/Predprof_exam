import csv

def quick_sort(array, start, stop):
    if start >= stop: return
    left = start
    right = stop
    x = array[(left+right) // 2]
    while left <= right:
        while array[left] > x: left += 1
        while array[right] < x: right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    quick_sort(array, start, right)
    quick_sort(array, left, stop)

with open('grants.csv', encoding='CP1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    prize_future_project = []
    for stat in data:
        if stat['Nomination'] == 'Проект будущего':
            prize_future_project.append[stat['Prize']]
        sorted_prize_feature_project = quick_sort(stat['Prize'], )
'''В пизду'''