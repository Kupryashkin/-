# Задание 1
random_string = 'f1ix_ER8ROR_in_l1ine_&_an7d_B8UG._in_C61o0de!'
correct_string=''

for i in random_string:
    if i.isalpha() or i == '_':
        correct_string += i
        correct_string = correct_string.replace('_','')
        correct_string = correct_string.replace('', ' ')

print(correct_string)

# Задание 2
string = input('')
def count_letter(srting):
    letter = "АЕЁИОУЫЭЮЯауёиоуыэюя"
    count = 0
    for i in string:
        if i in letter:
            count += 1
    return count
result = count_letter(string)
print("Колличество гластных букв в строке:", result)

# Задание 3
random_elements = [3, 6, -9, '-5', 'str', list, 'elem', None, -1, 10, str]
n = 0
b = 0 
for i in random_elements:
    if isinstance(i, int):
        n = n + 0 
        if i < 0:
            b = i + b
print(n, b)

# Задание 5
while True:
    a = int(input(''))
    if b<50:
        b = a+b
        print (b)
    else:
        print(b)
        break

# while b < 50:
