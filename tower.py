# Занойские башни
# суть игры: 
# У вас есть n палок, на них расположеные m дисков
# разного радиуса. Необходимо перенести все диски
# с левой на правую палку

# Цифрой обозначается ширина диска
# 0 - пустая ячейка
# 1 - самый узкий кружок
# и чем больше цифра, тем он шире

import func_for_tower as f

while (True):
    # Спрашиваем желаемое количество дисков
    try:
        count_circle = int(input('Please type count circle: '))
        if (count_circle > 1):
            break
        print ('Write number biggest then 1!')
    except:
        print ('Write number biggest then 1!')


# Массив с игровым полем
field = f.make_field(count_circle)

# Печатаем поле для начала игры
f.print_field(field)

# Создаём переменную для подсчёта количества ходов
count = 0

# Цикл игры
while (field[2][1] != '1'):
    while (True):
        # Спрашиваем желаемое количество дисков
        try:
            # Запрашиваем с какой колонки снять кружок
            put = input('Which disk move? (a,b or c)\n')
            # Запрашиваем куда его поставить
            place = input('Where this disk should locate? (a,b or c)\n')
            if (put in ('a','b','c') and place in ('a','b','c')):
                break
            print ('Write correct letter (a,b or c)')
        except:
            print ('Write correct letter (a,b or c)')
    

    # Переводим буквенное обозначение в номер колонки
    place = f.take_number(place) 
    put = f.take_number(put) 

    # Проверяем правильность хода
    if f.can_move(put, place, field):
        # Двигаем если можно
        f.move(put, place, field)
        f.print_field(field)
    else:
        # Выводим ошибку если нельзя
        print('Invalid choise!')
        f.print_field(field)
    count += 1

# Выводим результаты игры
print ('You finished game for', count, 'moves. You wonderful!')