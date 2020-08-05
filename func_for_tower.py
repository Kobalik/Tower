def make_field (count_circle):
    field = []

    # Напонение колонок
    # Массив с колонкой на которой изначально располагаются кружки
    a = []
    # Вторая колонка
    b = []
    # Третья колонка
    c = []
    for i in range (0, count_circle+1):
        a.append(str(i))
        b.append('0')
        c.append('0')

    # Переносим значение колонок в поле
    field.append(a)
    field.append(b)
    field.append(c)

    # Возвращаем поле
    return field

# Функция для отображения поля
def print_field(field):
    print('*' * 20)
    for i in range(0,len(field[0])):
        print(field[0][i], field[1][i], field[2][i])
    print()
    print('a b c')
    print('*' * 20)


# Функция получения номера
def take_number(ch):
    if ch == 'a':
        ch = 0
    elif ch == 'b':
        ch = 1
    else:
        ch = 2
    
    return ch

# Функция взятия верхнего диска, если его нет вернуть ноль
def take_disk(put, field):
    # Берём верхний диск
    for i in range(0, len(field[0])):
        # Берём первое не нулевое значение
        if field[put][i] != '0':
            disk = field[put][i]
            # print ('Take ', disk, 'from ', i, 'column')
            return disk, i
    # Если не нашло диск, возвращаем ноль
    return False

# Функция проверки правильности хода
def can_move(put, place, field):
    lim = len(field[0])
    # Нельзя передвинуть на колонку с который ты берешь диск
    if put == place:
        return False

    # Берём диск
    disk = take_disk(put, field)
    if disk:
        # Проверям, можем ли положить на данную колонку
        for i in range (lim-1, 0, -1):
            # Если там ноль, значит сюда можно закинуть
            if field[place][i] == '0':
                return True
            # Если снизу лежит мелкий диск значит туда положить нельзя
            if field[place][i] < disk[0]:
                return False

   
# Функция отвечающая за передвижение диска
def move (put, place, field):
    lim = len(field[0])

    # Берём диск
    disk, locate = take_disk(put, field)
    if disk:
        # Выбираем куда вставить диск
        for i in range (lim-1, 0, -1):
            # Если там ноль, значит сюда можно закинуть
            if field[place][i] == '0':
                # Заменям ноль на диск
                field[place][i] = disk
                # Убираем диск, заменив его положение на ноль
                field[put][locate] = '0'
                return True
    return False