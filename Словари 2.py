# Задание 1
test_dict = {1: 'element 1', 2: 'element 2', 3: 'element 3', 4: 'element 4', 5: 'element 5'}
print("Пары (ключ, значение):")
print(test_dict.items())

# Задание 2
test_dict = {'key 1': 'value 1', 'keyyy': 'vlaueee', '123': 123, 'random?': 'yes', 1: 'two'}
value_keyy = test_dict.get('keyy')
value_1 = test_dict.get(1)
print("Значение для ключа 'keyy':", value_keyy)
print("Значение для ключа 1:", value_1)

# Задание 3
pc = {'info:': 'PC devices', 1: 'Video card', 2: 'Processor', 3: 'Monitor', 4: 'Strawberry', 5: 'Speakers'}
del pc['info:']

pc[6] = 'Hard Disk'
pc[7] = 'RAM'
pc[8] = 'System block'
print(pc)

# Задание 4
double_sy = {1: '10111011', 2: '010101', 3: '11111101', 4: '110010', 5: '011010', 6: '100011001'}
for key in double_sy:
    if key % 2 !=0:
        num = double_sy.get(key)
        decimal_value = int(num, 2)
        print(f"Для ключа {key} десятичное значение: {decimal_value}")

# Задание 5
books_and_authors = {}
while True:
    book_title = input("Введите название книги: ")
    if book_title.lower() == "всё" or book_title.lower() == "Все":
        break

    author_name = input("Введите имя автора: ")
    books_and_authors[book_title] = author_name
print(books_and_authors)
