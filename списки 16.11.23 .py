# Задание 1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
print (m)
m.remove(15)
print (m)
m.remove('10')
print (m)

# Задание 2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)

# Задание 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)

# Задание 4
m = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4]
m.remove(-6)
m.remove(-20)
m.remove(-6)
m.remove(-4)
print(m)
m.sort(reverse=False)
print(m)
m.sort(reverse=True)
print(m)
