fio = input('ФИО: ')
ansfio = ''
anscnt = 0
for i in fio:
    if i.isupper():
        ansfio += i
    if i != ' ':
        anscnt += 1
print(f'Инициалы: {ansfio}')
print(f'Длина (символов): {anscnt + 2}')