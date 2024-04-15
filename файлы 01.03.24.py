# Задание 1
# S:\Группы\ИБС125\Купряшкин\купряшкин

file = open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\new file.txt", "w")
file.write('Как называется гроб двух негров? - Твикс')
file.close()

# Задание 2
file1 = open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\input.txt", "w")
file1.write("Несколько строк")
file1.close()

file2 = open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\output.txt", "w")
file2.close()

with open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\input.txt", "r") as file1:
    content = file1.read()

with open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\output.txt", "w") as file2:
    file2.write(content + " <copy>")

# Задание 3
file = open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\log note.txt ","w" )
file.write("26.02.2024")




from datetime import datetime
def add_entry(text):
    with open ("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\log note.txt ","w" ) as file :
            file.write(f"Дата и время создания: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{text}")
            add_entry ("запись 1")
            add_entry ("запись 2")
file.close()

# Задание 4
file = open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\data.txt", 'r' )
with open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\data.txt ", 'r') as file:
    c = file.read()

count = 0
lines = c.split("\n")

for line in lines:
    if 'John' in line:
        count += 1
print("Количество человек с именем John:", count)


# Задание 5
e_dict = {'б':'а', 'в':'б', 'г':'в', 'д':'г', 'е':'д', 'ё':'е', 'ж':'ё', 'з':'ж', 'и':'з', 'й':'и', 'к':'й', 'л':'к', 'м':'л', 'н':'м', 'о':'н', 'п':'о', 'р':'п', 'с':'р', 'т':'с', 'у':'т', 'ф':'у', 'х':'ф', 'ц':'х', 'ч':'ц', 'ш':'ч', 'щ':'ш', 'ъ':'щ', 'ы':'ъ', 'ь':'ы', 'э':'ь', 'ю':'э', 'я':'ю', 'а':'я', 'О':'1', 'Д':'2', 'Т':'3', 'Ч':'4', 'П':'5', 'Ш':'6', 'С':'7', 'В':'8', 'Е':'9', 'Я':'0', '/':'.', '_':'!', ',':' ', ' ':',', '^':':', '*':'\n'}
with open("S:\\Группы\\ИБС125\\Купряшкин\\купряшкин\\encrypt_mess.txt", 'r') as file:
    e_message = file.read()
d_message = ""
for char in e_message:
    if char in e_dict:
        d_message += e_dict[char]
    else:
        d_message += char
print(d_message)

