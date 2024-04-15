# Задание 1
all_keys = ['red key', 'blue key', 'golden key', 'red key', 'blue key', 'white key', 'golden key']
a = 0
i = 'golden key'
for i in all_keys:
    if i == 'golden key':
        a+=1
        print(True,a)
    else:
        print("False")
# Задание 2
message = '6_185+_7*/#4i/*(@n'
for i in message:
    if i== '7':
        i = 'П'
    elif i== '1':
        i = 'T'
    elif i== 'n':
        i = '!'
    elif i== '+':
        i = 'Я'
    elif i== 'i':
        i = 'И'
    elif i== '/':
        i = 'Л'
    elif i== '(':
        i = 'С'
    elif i== '5':
        i = 'Б'
    elif i== '6':
        i = 'у'
    elif i== '_':
        i = 'ПРОБЕЛ'
    elif i== '*':
        i = 'O'
    elif i== '8':
        i = 'E'
    elif i== '#':
        i = 'У'
    elif i== '4':
        i = 'Ч'
    elif i== '@':
        i = 'Ь'
    print(i)
