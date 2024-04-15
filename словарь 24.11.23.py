# Задание 1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
print(my_dict)
del my_dict[3]
print(my_dict)
my_dict[10]='0100101'
print(my_dict)

# Задание 2
sl = {'</>':13, 'script':1, '__init__':10, 'self':5, 'number_9':6, '#comment':100}
print(sl)
a = int(input())
b = int(input())
sl[a]=int(b)
print(sl)

# Задание 3
l={}
while len(l)<3:
    a=int(input())
    b=input()
    l[a]=b
print(l)
Задание  4
all_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}
del all_d[1]
del all_d [101]
del all_d [3]
print(all_d)

Y = int(input('Введите Y: '))
N = int(input('Введите N: '))


answer = X*Y*N

print("Answer", answer)
