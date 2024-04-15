# Задание 1
def upper(t):
    result =""
    for char in t:
        if char.isupper():
            result+= char +""
    print(result.strip())

upper('PriVeytrret')

# Задание 2
def punct(txt):
    count=0
    for char in txt:
        if char in '! ? . , ()':
            count+=1
    return count
print(punct('Как дела ?'))

# Задание 3
def create_cube (x,y):
    for i in range(y):
        print('*'*x)
create_cube(98, 16)

# Задание 4
def double(a):
    c=''
    for char in a:
        c+= char * 6666
    return c
print(double('qwertyuiop'))

# Задание 5
def constructor(detal_count, figure_count, car_count, tree_count):
    max_sets=min(detal_count//72, figure_count//4, car_count//2, tree_count//7)
    return max(0, max_sets)
resual1=constructor(144, 8, 4, 14)
print(resual1)
resual2=constructor(10000, 16, 6, 2)
print(resual2)

# Задание 6
def create_list(length, number=0):
    return [number] * length
print (create_list(5,3))
print(create_list (7))



# Задание 8
def c(x, y):
    n = " " + "_".join(str(i) for i in range(1, x+1)) + " "
    middle = "|" + "|".join(str(i) for i in range(1, x+1)) + "|"
    n = " " + "¯".join("¯" for i in range(x)) + " "
    print(n)
    for _ in range(y):
        print(middle)
    print(n)
c(3, 3)
